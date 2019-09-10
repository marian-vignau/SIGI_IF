"""
To merge two databases into one

First, create a new database & copy schema & data from master database
Cycle through tables, migrate first the ones without relationships dependents from others
After migrating this, continue with other dependent
Compute new primary keys (pk), necessary to avoid collision to first db pk
Create a transform list of lambda functions to compute new row values
Using this transform list, append new data coming from second database

Note:
    Added database schema must be a equal or a subset of Master database
    Tables must have the same fields
"""

import sqlite3
from pprint import pprint


class Verbose(object):
    """Log many thing. """
    def __init__(self, level = 0):
        self.level = level

    def verbose_print(self, *args, **kwargs):
        if self.level:
            print(*args, **kwargs)

    def verbose_pprint(self, *args, **kwargs):
        if self.level:
            pprint(*args, **kwargs)


class Row(object):
    def __init__(self, row, pks=[]):
        self.row = row
        self.primary_keys = pks
        self.keys = row.keys

    def apply_transform(self, transform):
        return [transform[k](self.row[k]) for k in self.row.keys()]

    def values(self):
        return [self.row[k] for k in self.row.keys()]

    def list_fields(self):
        return ', '.join(list(self.row.keys()))

    def question_marks(self):
        return ', '.join(["?" for k in self.row.keys()])

    @property
    def pk(self):
        return {field: self.row[field] for field in self.primary_keys}

    def __eq__(self, other):
        for k in self.row.keys():
            if not k in other.keys():
                return False
            elif self.row[k] != other[k]:
                return False
        return True

    def __getitem__(self, item):
        return self.row[item]

    def __str__(self):
        def minimize(s, length=10):
            if not isinstance(s, str):
                return s
            s = s.strip()
            for c in ["\n", "\t", "    ", "  ", "  ", "  "]:
                s = s.replace(c, " ")
            if length + 3 < len(s):
                s = s[:length] + " .."
            return "'%s'" % s
        pk = "; ".join([f"{k}:{minimize(self.row[k])}" for k in self.primary_keys])
        data = "; ".join([f"{k}:{minimize(self.row[k])}" for k in self.keys() if k not in self.primary_keys])
        return f"<{pk}> {data}"


class Table(object):
    def __init__(self, database, table_name):
        self.db = database
        self.name = table_name
        self.desc_tranform = []
        self.load_schema()

    def load_schema(self):
        """Load table's schema: foreiggn & primary keys"""
        q = self.db.pragma("foreign_key_list", self.name)
        self.fk = [{"table": row["table"],
                    "from": row["from"],
                    "to": row["to"]}
                   for row in q]

        q = self.db.pragma("table_info", self.name)
        self.pk = [row["name"] for row in q if row["pk"] != 0]
        self.transform = {row["name"]: (lambda n: n) for row in q}

    def evaluate_pk_transformation(self):
        """Creates a dict of functions to simple transform keys"""
        def new_id_number_function(max_id):
            return lambda n: max_id + n

        def new_id_string_function(suffix):
            return lambda n: f"{n}_{suffix:>03}"

        # pk includes an integer, it can be transformed by adding a base number
        q = self.db.pragma("table_info", self.name)
        for row in q:
            if row["pk"] != 0 and row["type"] == "INTEGER":
                q2 = self.db.execute(f"select max({row['name']}) from {self.name}").fetchone()
                max_id = q2[0] if q2 and q2[0] else 0
                self.transform[row['name']] = new_id_number_function(max_id)
                self.desc_tranform.append(f"fn: {self.name}_{row['name']} :=  new_id_number_function({max_id})")
                return self.transform

        # pk includes a string, test adding a suffix to the string
        for row in q:
            if row["pk"] != 0 and row["type"] == "TEXT":
                suffix = 0
                while True and suffix < 20:
                    q2 = self.db.execute(f"""select {row['name']} 
                        from {self.name}
                        where {row['name']} like '%_{suffix:>03}'""").fetchone()
                    if q2 is None:
                        break
                    suffix += 1
                self.transform[row['name']] = new_id_string_function(suffix)
                self.desc_tranform.append(f"fn: {self.name}_{row['name']} :=  new_id_string_function({suffix})")
                return self.transform
        return None

    def eval_transform(self):
        """Evaluate transformation to create the new row"""
        # is it is dependent on other pk in a master-detail relationship
        is_master_detail = False
        for rel in self.fk:
            self.transform[rel["from"]] = self.db[rel["table"]].transform[rel["to"]]
            self.desc_tranform.append(f"fn: {self.name}_{rel['from']} := fn({rel['table']}_{rel['to']})")

            if rel["from"] in self.pk:
                self.desc_tranform[-1] += "    master,detail"
                is_master_detail = True

        if not is_master_detail:
            self.evaluate_pk_transformation()
        return self.transform

    def __str__(self):
        """One line definition of table's schema"""
        pk = ", ".join(self.pk)
        fk = "), (".join([f"{r['from']} -> {r['table']}_{r['to']}" for r in self.fk])
        if fk:
            return f"{self.name} <{pk}>    ===> ({fk})"
        else:
            return f"{self.name} <{pk}>"

    def __repr__(self):
        """Dump all table known data"""
        s = [f"\n ==== {self.name} ===="]
        q = self.db.pragma("table_info", self.name)
        for row in q:
            s.append(f"         {row['name']}: {row['type']} pk:{row['pk']} ")
        s.extend([f"    -fk- {self.name}_{r['from']} -> {r['table']}_{r['to']}" for r in self.fk])
        s.extend(self.desc_tranform)
        return "\n".join(s)





class Database(object):
    """Extract information from a database, using schema or using pragma functions"""
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row
        self._tables = {}

    def __setitem__(self, key, value):
        """To use a database as a tables's dict"""
        self._tables[key] = value

    def __getitem__(self, item):
        """To use a database as a tables's dict"""
        return self._tables[item]

    def load_schema(self):
        """Load schema of all tables"""
        for table_name in self.list_all_tables():
            self[table_name] = Table(self, table_name)

    def pragma(self, prag_name, table_name):
        """Execute a pragma function"""
        return self.con.cursor().execute(f"PRAGMA {prag_name}('{table_name}')").fetchall()

    def select(self, table, condition=None):
        """Executes a select query, condition is a dictionary"""
        if condition is None:
            q = self.con.cursor().execute(f"select * from {table}")
        else:
            cond = " AND ".join([f"{k} = '{v}'" for k, v in condition.items()])
            q = self.con.cursor().execute(f"select * from {table} where {cond}")
        for row in q.fetchall():
            yield Row(row, self[table].pk)

    def execute(self, sql, variables=[]):
        """Convenience function to execute a query"""
        return self.con.cursor().execute(sql, variables)

    def list_create_statements(self):
        """List all tables definitions"""
        q = """
           SELECT name, type, sql
            FROM sqlite_master
                WHERE sql NOT NULL AND
                type == 'table'
            """
        cu = self.con.cursor()
        schema_res = cu.execute(q)
        for table_name, type, sql in schema_res.fetchall():
            if table_name == 'sqlite_sequence':
                yield('DELETE FROM sqlite_sequence;')
            elif table_name == 'sqlite_stat1':
                yield('ANALYZE sqlite_master;')
            elif table_name.startswith('sqlite_'):
                continue
            else:
                yield(table_name, sql)

    def list_all_tables(self):
        for table_name, sql in self.list_create_statements():
            yield table_name

    def walk_tables_dependencies(self):
        """Walk through tables, starting from masters, and
        going to detail dependent tables.
        """
        self.missing = list(self._tables.keys())
        while self.missing:
            cont = False
            for table_name in self.missing:
                missed = [r["table"] for r in self[table_name].fk if r["table"] in self.missing]
                if not missed or missed == [table_name]:
                    yield table_name
                    del self.missing[self.missing.index(table_name)]
                    cont = True
            if not cont:
                log("Missed", self.missing)
                break

    def __str__(self):
        return "\n".join([str(v) for v in self._tables.values()])


class AppendDatabase(object):
    """Append a sqlite database to another with the same schema
    """
    def __init__(self, db_master, db_added, db_new):
        self.master = Database(db_master)
        self.master.load_schema()
        self.added = Database(db_added)
        self.added._tables = self.master._tables
        self.new = Database(db_new)
        self.copy_master()

    def copy_master(self):
        """Copy first database into a new db"""
        for table_name, sql in self.master.list_create_statements():
            self.new.execute(sql)
            log(sql)
            sql = False
            for row in self.master.select(table_name):
                if not sql:
                    sql = f"""INSERT INTO {table_name} ({row.list_fields()})
                        VALUES ({row.question_marks()});
                        """
                self.new.execute(sql, row.values())
            self.new.con.commit()

    def migrate(self, table_name):
        """Migrate one table, adding the new rows"""
        transform = self.master[table_name].eval_transform()
        # log(repr(self.master[table_name]))
        sql = False
        for nro, row in enumerate(self.added.select(table_name)):
            log(":", row)
            if not sql:
                sql = f"""INSERT INTO {table_name} ({row.list_fields()})
                    VALUES ({row.question_marks()});
                    """
                log(sql)
            self.new.execute(sql, row.apply_transform(transform))
            if nro % 5:
                self.new.con.commit()
        self.new.con.commit()

    def append_db(self):
        """Append second datebase to new database"""
        for table_name in self.master.walk_tables_dependencies():
            self.migrate(table_name)



todict = lambda result: [{k: row[k] for k in row.keys()} for row in result]

v = Verbose(1)
log = v.verbose_print
pp = v.verbose_pprint

if __name__ == '__main__':
    master = r"\\NAS01\NAS01_Disco01\run\data\data_added.db"
    added = r"\\NAS01\NAS01_Disco01\run\data\database.db"
    new = r"\\NAS01\NAS01_Disco01\run\data\new_006.db"
    app = AppendDatabase(master, added, new)
    #log(app.master)
    app.append_db()

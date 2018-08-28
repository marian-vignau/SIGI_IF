
import wx


class Column(object):
    header = "header"
    field = "field"

    def __init__(self, header, field, **kargs):
        self.header = header
        self.field = field
        self.__dict__.update(kargs)

    def to_str(self, value):
        return str(value)

    def __str__(self):
        return '{:>15}={}'.format(
            self.field, self.header)

class ListViewObject(object):
    def __init__(self, widget, columns, itemkey):
        self.widget = widget
        self.columns = columns
        self.itemkey = self.itemdata = None
        for n, col in enumerate(columns):
            if col.field == itemkey:
                self.itemkey = n
        if self.itemkey is None:
            self.itemdata = itemkey
        self.item = None
        self._format_cols()

    def _format_cols(self):
        for num, col in enumerate(self.columns):
            self.widget.InsertColumn(num, col.header)

    def change_item_list(self, model):
        index = self.item
        for num, col in enumerate(self.columns):
            text = col.to_str(getattr(model, col.field))  #= m=model.field
            if num == 0:
                if self.item is None:
                    index = self.widget.InsertItem(
                        self.widget.GetItemCount(), text)
                else:
                    self.widget.SetItemText(self.item, text)
            else:
                self.widget.SetItem(index, num, text)
        if self.itemdata:
            self.widget.SetItemData(index, getattr(model, self.itemdata))
        return index

    def get_key(self, item=None):
        if not item is None:
            self.item = item
        else:
            self.item = self.widget.GetFirstSelected()
        if isinstance(self.itemkey, int):
            return self.widget.GetItem(self.item, self.itemkey).GetText()
        else:
            return self.widget.GetItemData(self.item)

    def show_selection(self, item=None):
        if not item is None:
            self.item = item
        if not self.item is None:
            self.widget.Select(self.item, on=True)

    def delete_item(self, item=None):
        if not item is None:
            self.item = item
        if not self.item is None:
            self.widget.DeleteItem(self.item)
        self.item = None

    def clear_item(self):
        self.item = None

    def __str__(self):
        s = [">> itemkey = %r" % self.itemkey, ">> item = %r" % self.item]
        s.extend([str(x) for x in self.columns])
        return "\n".join(s)




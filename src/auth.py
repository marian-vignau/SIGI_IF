__author__ = "María Andrea Vignau"

import configparser

import configparser
import ldap
import models

def init():
    cfg = configparser.ConfigParser()
    cfg.read("config.ini")
    cfg_ldap = cfg["LDAP"]

    client = ldap.initialize("ldap://" + cfg_ldap["server"])
    client.set_option(ldap.OPT_REFERRALS, 0)
    return client, cfg_ldap


def test_ldap(usr, pwd):
    client, cfg_ldap = init()
    try:
        client.simple_bind_s(f"{usr}@{cfg_ldap['domain']}", pwd)
        filter = f"{cfg_ldap['filter']}={usr}@{cfg_ldap['domain']}"
        try:
            member_of = client.search_s(cfg_ldap['base_dn'], ldap.SCOPE_SUBTREE, filter, ["memberof"])[0][1]['memberOf']
            return member_of
        except ldap.OPERATIONS_ERROR:
            return False
    except ldap.INVALID_CREDENTIALS:
        return False


def test_db(usr):
    s1 = models.sessions()
    userlogin = (s1.query(models.TableUsuario)
                 .filter(models.TableUsuario.id == usr)
                 .first()
    )
    if userlogin:
        return usr
    else:
        return False


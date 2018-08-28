

import wx


def set_cur_data(object, target):
    for x in range(object.GetCount()):
        if object.GetClientData(x) == target:
            object.SetSelection(x)
            break


def get_cur_data(object):
    return object.GetClientData(object.GetCurrentSelection())

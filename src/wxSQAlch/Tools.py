"""
Some functions used many times
"""


def replace_widget(frame, old_widget, new_widget):
    itemsizer = frame.GetSizer().GetItem(old_widget, recursive=True)
    itemsizer.AssignWindow(new_widget)
    old_widget.Destroy()


def changeFont(object, diff):
    if hasattr(object, "GetFont"):
        f = object.GetFont()
        f.SetPointSize(f.GetPointSize() + diff)
        object.SetFont(f)
        setattr(object, "_font_normal", f)
    for x in object.GetChildren():
        changeFont(x, diff)
        # if hasattr(x, "GetFont"):
        #     f = x.GetFont()
        #     f.SetPointSize(f.GetPointSize() + diff)
        #     x.SetFont(f)

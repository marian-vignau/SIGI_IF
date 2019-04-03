"""
Some functions used many times
"""


def replace_widget(frame, old_widget, new_widget):
    itemsizer = frame.GetSizer().GetItem(old_widget, recursive=True)
    itemsizer.AssignWindow(new_widget)
    old_widget.Destroy()


def changeFont(object, diff):
    for x in object.GetChildren():
        if hasattr(x, "GetFont"):
            f = x.GetFont()
            f.SetPointSize(f.GetPointSize() + diff)
            x.SetFont(f)

"""
Some functions used many times
"""

def replace_widget(frame, old_widget, new_widget):
    itemsizer = frame.GetSizer().GetItem(old_widget, recursive=True)
    itemsizer.AssignWindow(new_widget)
    old_widget.Destroy()

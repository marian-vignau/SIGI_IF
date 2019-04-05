import wx


class Column(object):
    header = "header"
    field = "field"
    size = 1

    def __init__(self, header, field, **kargs):
        self.header = header
        self.field = field
        self.__dict__.update(kargs)

    def to_str(self, value):
        return str(value)

    def __str__(self):
        return "{:>15}={}".format(self.field, self.header)


class ListViewObject(object):
    """To provide a unified API and way on all wx.ListCtrl used in my project."""

    styles = {
        "normal": {
            "font-weight": "normal",
            "font-color": wx.BLACK,
            "background": wx.WHITE,
        },
        "enhanced": {
            "font-weight": "bold",
            "font-color": wx.BLUE,
            "background": wx.WHITE,
        },
        "faded": {
            "font-weight": "normal",
            "font-color": wx.LIGHT_GREY,
            "background": wx.WHITE,
        },
        "blue": {
            "font-weight": "normal",
            "font-color": wx.WHITE,
            "background": wx.BLUE,
        },
        "red": {"font-weight": "normal", "font-color": wx.WHITE, "background": wx.RED},
    }

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

        self.font_normal = self.widget.GetFont()
        self.font_bold = self.font_normal.Bold()

    def apply_style_all(self, style="", reset=False):
        for idx in range(self.widget.GetItemCount()):
            self.apply_style(idx, style, reset)

    def apply_style(self, item=None, style="", reset=False):
        if item is None:
            self.item = self.widget.GetFirstSelected()
        else:
            self.item = item
        if not style or reset:
            style = "normal"
        use = self.styles["normal"].copy()
        use.update(self.styles[style])
        if use["font-weight"] == "normal":
            self.widget.SetItemFont(self.item, self.font_normal)
        if use["font-weight"] == "bold":
            self.widget.SetItemFont(self.item, self.font_bold)
        self.widget.SetItemTextColour(self.item, use["font-color"])
        self.widget.SetItemBackgroundColour(self.item, use["background"])

    def _format_cols(self):
        """
        To use the size attribute, it is a fraction of total client width.
        """
        sum_of_units = 0
        for col in self.columns:
            sum_of_units += col.size

        total_width, _ = self.widget.GetClientSize()
        measure_unit = total_width / sum_of_units

        for num, col in enumerate(self.columns):
            self.widget.InsertColumn(num, col.header)
            self.widget.SetColumnWidth(num, col.size * measure_unit)


    def change_item_list(self, model, add=False):
        index = self.item
        for num, col in enumerate(self.columns):
            text = col.to_str(getattr(model, col.field))
            if num == 0:
                if add or index is None:
                    index = self.widget.InsertItem(self.widget.GetItemCount(), text)
                else:
                    self.widget.SetItemText(self.item, text)
            else:
                self.widget.SetItem(index, num, text)
        if self.itemdata:
            self.widget.SetItemData(index, getattr(model, self.itemdata))
        return index

    def get_key(self, item=None):
        """Return an item key, if arg item is None, inform current item"""
        if not item is None:
            self.item = item
        else:
            self.item = self.widget.GetFirstSelected()

        if self.item < 0:   # if nothing is selected
            return None
        if isinstance(self.itemkey, int):
            return self.widget.GetItem(self.item, self.itemkey).GetText()
        else:
            return self.widget.GetItemData(self.item)

    def get_text(self, item=None):
        if not item is None:
            self.item = item
        else:
            self.item = self.widget.GetFirstSelected()
        if self.item < 0:  # if nothing is selected
            return None
        return self.widget.GetItemText(self.item)

    def show_selection(self, item=None):
        """Select an item, if arg item is None"""
        if not item is None:
            self.item = item
        if not self.item is None:
            self.widget.Select(self.item, on=True)

    def delete_item(self, item=None):
        """Delete an item, if arg item is None, delete current item"""
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

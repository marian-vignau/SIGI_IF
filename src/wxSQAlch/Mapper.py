import wx
import datetime


class MapObj(object):
    def __init__(self, widget, field):
        self.field = field
        self.widget = widget
        if widget.__class__.__name__ == "DatePickerCtrl":
            self.SetValue = self.SetDateValue
            self.GetValue = self.GetDateValue
        elif widget.__class__.__name__ == "DirPickerCtrl":
            self.SetValue = widget.SetPath
            self.GetValue = widget.GetPath
        else:
            # no uso parentesis xq quiero el puntero a la funcion
            if hasattr(widget, "SetValue"):
                self.SetValue = widget.SetValue
            elif hasattr(widget, "SetLabel"):
                self.SetValue = widget.SetLabel
            if hasattr(widget, "GetValue"):
                self.GetValue = widget.GetValue
            elif hasattr(widget, "GetLabel"):
                self.GetValue = widget.GetLabel

        if hasattr(widget, "SetFocus"):
            self.SetFocus = widget.SetFocus
        if hasattr(widget, "Enable"):
            self.Enable = widget.Enable
        if hasattr(widget, "Clear"):
            self.Clear = widget.Clear
        if hasattr(widget, "HasFocus"):
            self.HasFocus = widget.HasFocus

    def GetDateValue(self):
        """Special getter for"""
        w = self.widget.GetValue()
        if w.IsValid():
            d = datetime.date(w.year, w.month, w.day)
            return d
        else:
            return None

    def SetDateValue(self, value):
        w = wx.DateTime()
        if not value is None:
            w.Set(value.day, value.month, value.year)
        self.widget.SetValue(w)

    def GetValue(self):
        return None

    def SetValue(self, value):
        pass

    def SetFocus(self):
        pass

    def Enable(self, value):
        pass

    def Clear(self):
        pass

    def HasFocus(self):
        return None

    def __str__(self):
        return "{:>15}={!r:<30},{}".format(
            self.field, self.GetValue(), self.widget.__class__.__name__
        )


class MapList(MapObj):
    """El objeto debe ser wx.ListBox, wx.Choice, etc
    """

    def __init__(self, widget, field, lista=None):
        super().__init__(widget, field)
        self.Clear = self.ClearList
        self.GetValue = self.GetValueList
        self.SetValue = self.SetValueList
        if lista and len(lista) > 0:
            for desc, ub in lista:
                self.widget.Append(desc, ub)
            self.widget.SetSelection(0)

    def reload(self, lista):
        self.widget.Clear()
        if lista and len(lista) > 0:
            for desc, ub in lista:
                self.widget.Append(desc, ub)
            self.widget.SetSelection(0)

    def ClearList(self):
        self.widget.SetSelection(0)

    def GetValueList(self):
        try:
            selec = self.widget.GetSelection()
            return self.widget.GetClientData(selec)
        except Exception as e:
            print(">>>> Error en %s", e)
            return 0

    def SetValueList(self, value):
        if self.widget.GetCount() > 0:
            anterior = self.widget.GetSelection()
            Dirty = False
            if value != self.GetValue():
                for i in range(self.widget.GetCount()):
                    n = self.widget.GetClientData(i)
                    if n == value and i != anterior:
                        self.widget.SetSelection(i)
                        Dirty = True
            return Dirty
        return False


class MapNumeric(MapObj):
    """el objeto debe ser un TextCtrl o StaticText
    """

    def __init__(self, widget, field, formato=None):
        super().__init__(widget, field)
        self.widget = widget
        if formato:
            self.formato = formato
        else:
            self.formato = "%.2f"
        if hasattr(widget, "GetValue"):
            self._get = widget.GetValue
        elif hasattr(widget, "GetLabel"):
            self._get = widget.GetLabel
        if hasattr(widget, "SetValue"):
            self._set = widget.SetValue
        elif hasattr(widget, "SetLabel"):
            self._set = widget.SetLabel
        self.widget.Bind(wx.EVT_CHAR, self.NumericOnChar)

    def NumericOnChar(self, event):
        # Para que solo puedan ingresarse numeros flotantes
        if (
            event.IsKeyInCategory(wx.WXK_CATEGORY_CUT)
            or event.IsKeyInCategory(wx.WXK_CATEGORY_NAVIGATION)
            or event.IsKeyInCategory(wx.WXK_CATEGORY_JUMP)
        ):
            event.Skip()
        else:
            c = chr(event._getKeyCode())
            if c in "0123456789":
                event.Skip()
            elif c == "." and not "." in event._getEventObject()._getValue():
                event.Skip()

    def GetValue(self):
        w = self._get().strip()
        if w == "":
            return 0
        else:
            try:
                f = float(w)
                return f
            except ValueError:
                return 0

    def SetValue(self, value):
        try:
            f = float(value)
            self._set(self.formato % f)
        except ValueError:
            self._set("")


class Mapper(object):
    """Toma los campos del modelo, y se fija si existen widgets con igual nombre
    en el frame, en ése caso usa las funciones SetValue y GetValue para asignar
    datos desde el registro al widget, y viceversa
    """

    def __init__(self, *args, **kargs):
        """carga en el diccionario las funciones con nombre estándar,
        válido para textctrl-varchar y para spinCtrl-integer"""
        #        campos=[x for x in dir(model) if not (x=='metadata' or x.startswith('_'))]
        self.fields = args
        for obj in args:
            self.__setattr__(obj.field, obj)

    def from_model(self, model):
        """Set values on widgets from model."""
        for field in self.fields:
            try:
                value = getattr(model, field.field)
                field.SetValue(value)
            except Exception as inst:
                print("Error en %s, SetValue" % field)
                print(inst)

    def clear(self):
        """Clear all widgets."""
        for field in self.fields:
            try:
                field.Clear()
            except Exception as inst:
                pass
                print("Error en %s, Clear" % field)
                print(inst)

    def to_model(self, model):
        """Set values from widgets on model"""
        for field in self.fields:
            try:
                value = field.GetValue()
                setattr(model, field.field, value)
            except Exception as inst:
                pass
                print("Error en %s, GetValue" % field)
                print(inst)

    def enable(self, state):
        """Habilita o deshabilita widgets para edición"""
        for field in self.fields:
            try:
                field.Enable(state)
            except Exception as inst:
                print("Error en %s, Enable" % field)
                print(inst)

    def dirty(self, model):
        """usa getvalue para comparar cada campo con el valor del modelo"""
        for field in self.fields:
            on_widget = field.GetValue()  # = n=wid_get._getValue()
            on_model = getattr(model, field)  # = m=model.field
            if on_widget != on_model:
                return True
        return False

    def __repr__(self):
        return "\n".join([str(field) for field in self.fields])

    def __str__(self):
        s = "%d asignados:(%s)" % (
            len(self.fields),
            ",".join([x.field for x in self.fields]),
        )
        return s

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class VistaCausa
###########################################################################


class VistaCausa(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Causa",
            pos=wx.DefaultPosition,
            size=wx.Size(718, 463),
            style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.paCausa = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, -1), wx.TAB_TRAVERSAL
        )
        bSizer2.Add(self.paCausa, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        clEscritosChoices = []
        self.clEscritos = wx.CheckListBox(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, clEscritosChoices, 0
        )
        bSizer3.Add(self.clEscritos, 1, wx.EXPAND | wx.ALL, 5)

        self.trcObjetos = wx.TreeCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE
        )
        bSizer3.Add(self.trcObjetos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.paEscrito = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        bSizer4.Add(self.paEscrito, 1, wx.EXPAND | wx.ALL, 5)

        self.paObjeto = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        bSizer4.Add(self.paObjeto, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.clEscritos.Bind(wx.EVT_LISTBOX, self.clEscritosOnCheckListBox)
        self.trcObjetos.Bind(wx.EVT_TREE_SEL_CHANGED, self.trcObjetosOnTreeSelChanged)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def clEscritosOnCheckListBox(self, event):
        event.Skip()

    def trcObjetosOnTreeSelChanged(self, event):
        event.Skip()


###########################################################################
## Class PanelCausa
###########################################################################


class PanelCausa(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.Size(224, 514),
            style=wx.TAB_TRAVERSAL,
        )

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Expediente Judicial",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText3.Wrap(-1)

        bSizer5.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.tcExpteJud = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer5.Add(self.tcExpteJud, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText4 = wx.StaticText(
            self,
            wx.ID_ANY,
            u"Expediente Policial",
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.m_staticText4.Wrap(-1)

        bSizer5.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.tcExptePol = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer5.Add(self.tcExptePol, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"Expediente Otro", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText5.Wrap(-1)

        bSizer5.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.tcExpteOtro = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer5.Add(self.tcExpteOtro, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(
            self, wx.ID_ANY, u"Carátula", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText6.Wrap(-1)

        bSizer5.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.tcCaratula = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_MULTILINE,
        )
        bSizer5.Add(self.tcCaratula, 1, wx.ALL | wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(
            self, wx.ID_ANY, u"Estado", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText7.Wrap(-1)

        bSizer7.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.lblEstado = wx.StaticText(
            self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.lblEstado.Wrap(-1)

        bSizer7.Add(self.lblEstado, 0, wx.ALL, 5)

        bSizer5.Add(bSizer7, 0, wx.EXPAND, 5)

        chEstadoChoices = []
        self.chEstado = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chEstadoChoices, 0
        )
        self.chEstado.SetSelection(0)
        bSizer5.Add(self.chEstado, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(
            self, wx.ID_ANY, u"Observaciones", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText8.Wrap(-1)

        bSizer5.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.tcObservaciones = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_MULTILINE,
        )
        bSizer5.Add(self.tcObservaciones, 1, wx.ALL | wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText9 = wx.StaticText(
            self, wx.ID_ANY, u"Destinatario", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText9.Wrap(-1)

        bSizer8.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.lblDestinatario = wx.StaticText(
            self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.lblDestinatario.Wrap(-1)

        bSizer8.Add(self.lblDestinatario, 0, wx.ALL, 5)

        bSizer5.Add(bSizer8, 0, wx.EXPAND, 5)

        chDestinatarioChoices = []
        self.chDestinatario = wx.Choice(
            self,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            chDestinatarioChoices,
            0,
        )
        self.chDestinatario.SetSelection(0)
        bSizer5.Add(self.chDestinatario, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        # Connect Events
        self.lblEstado.Bind(wx.EVT_LEFT_DCLICK, self.lblEstadoOnLeftDClick)
        self.chEstado.Bind(wx.EVT_CHOICE, self.chEstadoOnChoice)
        self.lblDestinatario.Bind(wx.EVT_LEFT_DCLICK, self.lblDestinatarioOnLeftDClick)
        self.chDestinatario.Bind(wx.EVT_CHOICE, self.chDestinatarioOnChoice)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def lblEstadoOnLeftDClick(self, event):
        event.Skip()

    def chEstadoOnChoice(self, event):
        event.Skip()

    def lblDestinatarioOnLeftDClick(self, event):
        event.Skip()

    def chDestinatarioOnChoice(self, event):
        event.Skip()


###########################################################################
## Class OficinasJudiciales
###########################################################################


class OficinasJudiciales(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(777, 471),
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer25 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer26 = wx.BoxSizer(wx.VERTICAL)

        self.lsOficinas = wx.ListCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LC_REPORT | wx.LC_SORT_ASCENDING,
        )
        bSizer26.Add(self.lsOficinas, 1, wx.ALL | wx.EXPAND, 5)

        bSizer25.Add(bSizer26, 1, wx.EXPAND, 5)

        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        fgSizer5 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer5.AddGrowableCol(1)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText331 = wx.StaticText(
            self, wx.ID_ANY, u"Identificador", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText331.Wrap(-1)

        fgSizer5.Add(
            self.m_staticText331,
            0,
            wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.tcId = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer5.Add(self.tcId, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText26 = wx.StaticText(
            self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText26.Wrap(-1)

        fgSizer5.Add(
            self.m_staticText26,
            0,
            wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT,
            5,
        )

        self.tcNombre = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer5.Add(self.tcNombre, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText28 = wx.StaticText(
            self, wx.ID_ANY, u"Circunscripción", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText28.Wrap(-1)

        fgSizer5.Add(
            self.m_staticText28,
            0,
            wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT,
            5,
        )

        self.tcCircunscripcion = wx.SpinCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.SP_ARROW_KEYS,
            0,
            10,
            0,
        )
        fgSizer5.Add(self.tcCircunscripcion, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText29 = wx.StaticText(
            self, wx.ID_ANY, u"Autoridad", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText29.Wrap(-1)

        fgSizer5.Add(
            self.m_staticText29,
            0,
            wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.tcACargo = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer5.Add(self.tcACargo, 0, wx.ALL | wx.EXPAND, 5)

        bSizer34 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer34.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText31 = wx.StaticText(
            self, wx.ID_ANY, u"Tipo", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText31.Wrap(-1)

        bSizer34.Add(self.m_staticText31, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.AddTipoOficina = wx.StaticText(
            self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.AddTipoOficina.Wrap(-1)

        bSizer34.Add(self.AddTipoOficina, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer5.Add(bSizer34, 0, wx.EXPAND, 5)

        chIdTipoChoices = []
        self.chIdTipo = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chIdTipoChoices, 0
        )
        self.chIdTipo.SetSelection(0)
        fgSizer5.Add(self.chIdTipo, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText33 = wx.StaticText(
            self, wx.ID_ANY, u"EMail", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText33.Wrap(-1)

        fgSizer5.Add(
            self.m_staticText33,
            0,
            wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.tcCorreoElectronico = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer5.Add(self.tcCorreoElectronico, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText34 = wx.StaticText(
            self, wx.ID_ANY, u"Teléfono", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText34.Wrap(-1)

        fgSizer5.Add(
            self.m_staticText34,
            0,
            wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL,
            5,
        )

        self.tcTelefono = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer5.Add(self.tcTelefono, 0, wx.ALL | wx.EXPAND, 5)

        fgSizer5.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer23.Add((0, 0), 1, wx.EXPAND, 5)

        self.btAdd = wx.Button(
            self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(20, 20), 0
        )
        bSizer23.Add(self.btAdd, 0, wx.ALL, 5)

        self.btDelete = wx.Button(
            self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(20, 20), 0
        )
        bSizer23.Add(self.btDelete, 0, wx.ALL, 5)

        fgSizer5.Add(bSizer23, 0, wx.EXPAND, 5)

        bSizer31.Add(fgSizer5, 1, wx.EXPAND, 5)

        bSizer231 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer231.Add((0, 0), 1, wx.EXPAND, 5)

        self.btReestablecer = wx.Button(
            self, wx.ID_ANY, u"&Reestablecer", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer231.Add(self.btReestablecer, 0, wx.ALL, 5)

        self.btSalir = wx.Button(
            self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer231.Add(self.btSalir, 0, wx.ALL, 5)

        bSizer31.Add(bSizer231, 0, wx.EXPAND, 5)

        bSizer25.Add(bSizer31, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer25)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OficinasJudicialesOnClose)
        self.lsOficinas.Bind(
            wx.EVT_LIST_ITEM_SELECTED, self.lsOficinasOnListItemSelected
        )
        self.AddTipoOficina.Bind(wx.EVT_LEFT_DCLICK, self.AddTipoOficinaOnLeftDClick)
        self.btAdd.Bind(wx.EVT_BUTTON, self.btAddOnButtonClick)
        self.btDelete.Bind(wx.EVT_BUTTON, self.btDeleteOnButtonClick)
        self.btReestablecer.Bind(wx.EVT_BUTTON, self.btReestablecerOnButtonClick)
        self.btSalir.Bind(wx.EVT_BUTTON, self.btSalirOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OficinasJudicialesOnClose(self, event):
        event.Skip()

    def lsOficinasOnListItemSelected(self, event):
        event.Skip()

    def AddTipoOficinaOnLeftDClick(self, event):
        event.Skip()

    def btAddOnButtonClick(self, event):
        event.Skip()

    def btDeleteOnButtonClick(self, event):
        event.Skip()

    def btReestablecerOnButtonClick(self, event):
        event.Skip()

    def btSalirOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class PanelEscrito
###########################################################################


class PanelEscrito(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.Size(414, 308),
            style=wx.TAB_TRAVERSAL,
        )

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.AddGrowableRow(1)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText18 = wx.StaticText(
            self, wx.ID_ANY, u"Identificador", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText18.Wrap(-1)

        fgSizer2.Add(self.m_staticText18, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcIdEscrito = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer2.Add(self.tcIdEscrito, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText19 = wx.StaticText(
            self, wx.ID_ANY, u"Descripción", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText19.Wrap(-1)

        fgSizer2.Add(self.m_staticText19, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcDescripcion = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_MULTILINE,
        )
        fgSizer2.Add(self.tcDescripcion, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText20 = wx.StaticText(
            self, wx.ID_ANY, u"Ubicación Fisica", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText20.Wrap(-1)

        fgSizer2.Add(self.m_staticText20, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcUbicacionFisica = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer2.Add(self.tcUbicacionFisica, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText21 = wx.StaticText(
            self, wx.ID_ANY, u"Fotos", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText21.Wrap(-1)

        fgSizer2.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcFotos = wx.DirPickerCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            u"Elija un directorio",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL,
        )
        fgSizer2.Add(self.tcFotos, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText22 = wx.StaticText(
            self, wx.ID_ANY, u"Ingreso", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText22.Wrap(-1)

        fgSizer2.Add(self.m_staticText22, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dpIngreso = wx.adv.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN,
        )
        fgSizer2.Add(self.dpIngreso, 0, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(
            self, wx.ID_ANY, u"Salida", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText23.Wrap(-1)

        fgSizer2.Add(self.m_staticText23, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dpSalida = wx.adv.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.adv.DP_ALLOWNONE | wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN,
        )
        fgSizer2.Add(self.dpSalida, 0, wx.ALL, 5)

        self.SetSizer(fgSizer2)
        self.Layout()

    def __del__(self):
        pass


###########################################################################
## Class PanelObjeto
###########################################################################


class PanelObjeto(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.Size(414, 308),
            style=wx.TAB_TRAVERSAL,
        )

        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.AddGrowableCol(1)
        fgSizer2.AddGrowableRow(2)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText30 = wx.StaticText(
            self, wx.ID_ANY, u"Pertenece a:", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText30.Wrap(-1)

        fgSizer2.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.lblObjetoRelacionado = wx.StaticText(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.lblObjetoRelacionado.Wrap(-1)

        fgSizer2.Add(self.lblObjetoRelacionado, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText19 = wx.StaticText(
            self, wx.ID_ANY, u"Descripción", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText19.Wrap(-1)

        fgSizer2.Add(self.m_staticText19, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcDescripcion = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_MULTILINE,
        )
        fgSizer2.Add(self.tcDescripcion, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticText20 = wx.StaticText(
            self, wx.ID_ANY, u"Ubicación Fisica", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText20.Wrap(-1)

        fgSizer2.Add(self.m_staticText20, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcUbicacionFisica = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer2.Add(self.tcUbicacionFisica, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText21 = wx.StaticText(
            self, wx.ID_ANY, u"Fotos", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText21.Wrap(-1)

        fgSizer2.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.tcFotos = wx.DirPickerCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            u"Elija un directorio",
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL,
        )
        fgSizer2.Add(self.tcFotos, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText22 = wx.StaticText(
            self, wx.ID_ANY, u"Ingreso", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText22.Wrap(-1)

        fgSizer2.Add(self.m_staticText22, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dpIngreso = wx.adv.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN,
        )
        fgSizer2.Add(self.dpIngreso, 0, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(
            self, wx.ID_ANY, u"Salida", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText23.Wrap(-1)

        fgSizer2.Add(self.m_staticText23, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.dpSalida = wx.adv.DatePickerCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultDateTime,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN,
        )
        fgSizer2.Add(self.dpSalida, 0, wx.ALL, 5)

        self.SetSizer(fgSizer2)
        self.Layout()

    def __del__(self):
        pass


###########################################################################
## Class EdicionCausa
###########################################################################


class EdicionCausa(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Edición Causa",
            pos=wx.DefaultPosition,
            size=wx.Size(781, 540),
            style=wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.paCausa = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(150, -1), wx.TAB_TRAVERSAL
        )
        bSizer2.Add(self.paCausa, 1, wx.EXPAND | wx.ALL, 5)

        bSizer23 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer23.Add((0, 0), 1, wx.EXPAND, 5)

        self.btReestablecer = wx.Button(
            self, wx.ID_ANY, u"&Reestablecer", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer23.Add(self.btReestablecer, 0, wx.ALL, 5)

        self.btGuardar = wx.Button(
            self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer23.Add(self.btGuardar, 0, wx.ALL, 5)

        bSizer2.Add(bSizer23, 0, wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer25 = wx.BoxSizer(wx.HORIZONTAL)

        self.btAddEscrito = wx.Button(
            self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(20, 20), 0
        )
        bSizer25.Add(self.btAddEscrito, 0, wx.ALL, 5)

        self.btDeleteEscrito = wx.Button(
            self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(20, 20), 0
        )
        bSizer25.Add(self.btDeleteEscrito, 0, wx.ALL, 5)

        bSizer25.Add((0, 0), 1, wx.EXPAND, 5)

        self.btVincular = wx.Button(
            self, wx.ID_ANY, u"Vincular", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer25.Add(self.btVincular, 0, wx.ALL, 5)

        bSizer25.Add((0, 0), 1, wx.EXPAND, 5)

        self.btAddObjeto = wx.Button(
            self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(20, 20), 0
        )
        bSizer25.Add(self.btAddObjeto, 0, wx.ALL, 5)

        self.btDeleteObjeto = wx.Button(
            self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(20, 20), 0
        )
        bSizer25.Add(self.btDeleteObjeto, 0, wx.ALL, 5)

        bSizer3.Add(bSizer25, 0, wx.EXPAND, 5)

        bSizer35 = wx.BoxSizer(wx.HORIZONTAL)

        self.lsEscritos = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT
        )
        bSizer35.Add(self.lsEscritos, 1, wx.ALL | wx.EXPAND, 5)

        self.trcObjetos = wx.TreeCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_HAS_BUTTONS,
        )
        bSizer35.Add(self.trcObjetos, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(bSizer35, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btReestablecer.Bind(wx.EVT_BUTTON, self.btReestablecerOnButtonClick)
        self.btGuardar.Bind(wx.EVT_BUTTON, self.btGuardarOnButtonClick)
        self.btAddEscrito.Bind(wx.EVT_BUTTON, self.btAddEscritoOnButtonClick)
        self.btDeleteEscrito.Bind(wx.EVT_BUTTON, self.btDeleteEscritoOnButtonClick)
        self.btVincular.Bind(wx.EVT_BUTTON, self.btVincularOnButtonClick)
        self.btAddObjeto.Bind(wx.EVT_BUTTON, self.btAddObjetoOnButtonClick)
        self.btDeleteObjeto.Bind(wx.EVT_BUTTON, self.btDeleteObjetoOnButtonClick)
        self.lsEscritos.Bind(wx.EVT_LEFT_DCLICK, self.lsEscritosOnLeftDClick)
        self.lsEscritos.Bind(
            wx.EVT_LIST_ITEM_SELECTED, self.lsEscritosOnListItemSelected
        )
        self.trcObjetos.Bind(wx.EVT_LEFT_DCLICK, self.trcObjetosOnLeftDClick)
        self.trcObjetos.Bind(wx.EVT_LEFT_DOWN, self.trcObjetosOnLeftDown)
        self.trcObjetos.Bind(wx.EVT_TREE_SEL_CHANGED, self.trcObjetosOnTreeSelChanged)
        self.trcObjetos.Bind(wx.EVT_TREE_SEL_CHANGING, self.trcObjetosOnTreeSelChanging)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btReestablecerOnButtonClick(self, event):
        event.Skip()

    def btGuardarOnButtonClick(self, event):
        event.Skip()

    def btAddEscritoOnButtonClick(self, event):
        event.Skip()

    def btDeleteEscritoOnButtonClick(self, event):
        event.Skip()

    def btVincularOnButtonClick(self, event):
        event.Skip()

    def btAddObjetoOnButtonClick(self, event):
        event.Skip()

    def btDeleteObjetoOnButtonClick(self, event):
        event.Skip()

    def lsEscritosOnLeftDClick(self, event):
        event.Skip()

    def lsEscritosOnListItemSelected(self, event):
        event.Skip()

    def trcObjetosOnLeftDClick(self, event):
        event.Skip()

    def trcObjetosOnLeftDown(self, event):
        event.Skip()

    def trcObjetosOnTreeSelChanged(self, event):
        event.Skip()

    def trcObjetosOnTreeSelChanging(self, event):
        event.Skip()


###########################################################################
## Class EdicionObjeto
###########################################################################


class EdicionObjeto(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Edición Objeto",
            pos=wx.DefaultPosition,
            size=wx.Size(363, 346),
            style=wx.DEFAULT_DIALOG_STYLE,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.paObjeto = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        bSizer16.Add(self.paObjeto, 1, wx.EXPAND | wx.ALL, 5)

        bSizer231 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer231.Add((0, 0), 1, wx.EXPAND, 5)

        self.btReestablecer = wx.Button(
            self, wx.ID_ANY, u"&Reestablecer", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer231.Add(self.btReestablecer, 0, wx.ALL, 5)

        self.btGuardar = wx.Button(
            self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer231.Add(self.btGuardar, 0, wx.ALL, 5)

        bSizer16.Add(bSizer231, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer16)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btReestablecer.Bind(wx.EVT_BUTTON, self.btReestablecerOnButtonClick)
        self.btGuardar.Bind(wx.EVT_BUTTON, self.btGuardarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btReestablecerOnButtonClick(self, event):
        event.Skip()

    def btGuardarOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class EdicionEscrito
###########################################################################


class EdicionEscrito(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Edición Escrito",
            pos=wx.DefaultPosition,
            size=wx.Size(463, 493),
            style=wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.paEscrito = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL
        )
        bSizer16.Add(self.paEscrito, 1, wx.EXPAND | wx.ALL, 5)

        bSizer231 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer231.Add((0, 0), 1, wx.EXPAND, 5)

        self.btReestablecer = wx.Button(
            self, wx.ID_ANY, u"&Reestablecer", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer231.Add(self.btReestablecer, 0, wx.ALL, 5)

        self.btGuardar = wx.Button(
            self, wx.ID_ANY, u"&Guardar", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer231.Add(self.btGuardar, 0, wx.ALL, 5)

        bSizer16.Add(bSizer231, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer16)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btReestablecer.Bind(wx.EVT_BUTTON, self.btReestablecerOnButtonClick)
        self.btGuardar.Bind(wx.EVT_BUTTON, self.btGuardarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btReestablecerOnButtonClick(self, event):
        event.Skip()

    def btGuardarOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class Main
###########################################################################


class Main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"SIGI IF",
            pos=wx.DefaultPosition,
            size=wx.Size(756, 350),
            style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.TAB_TRAVERSAL,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.mnuCausaAgregar = wx.MenuItem(
            self.m_menu1, wx.ID_ANY, u"Agregar", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu1.Append(self.mnuCausaAgregar)

        self.menubar1.Append(self.m_menu1, u"&Causas")

        self.m_menu6 = wx.Menu()
        self.mnuInfomeDesignar = wx.MenuItem(
            self.m_menu6, wx.ID_ANY, u"Designar perito", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.m_menu6.Append(self.mnuInfomeDesignar)

        self.menubar1.Append(self.m_menu6, u"&Informe")

        self.SetMenuBar(self.menubar1)

        bSizer41 = wx.BoxSizer(wx.VERTICAL)

        bSizer42 = wx.BoxSizer(wx.HORIZONTAL)

        self.scBuscar = wx.SearchCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.scBuscar.ShowSearchButton(True)
        self.scBuscar.ShowCancelButton(False)
        bSizer42.Add(self.scBuscar, 0, wx.ALL, 5)

        chSelectorChoices = [u"Causa", u"Informe"]
        self.chSelector = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chSelectorChoices, 0
        )
        self.chSelector.SetSelection(0)
        bSizer42.Add(self.chSelector, 0, wx.ALL, 5)

        self.raTodos = wx.RadioButton(
            self, wx.ID_ANY, u"Todos", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.raTodos.SetValue(True)
        bSizer42.Add(self.raTodos, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.raExpJud = wx.RadioButton(
            self, wx.ID_ANY, u"ExpJud", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer42.Add(self.raExpJud, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.raExpPol = wx.RadioButton(
            self, wx.ID_ANY, u"ExpPol", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer42.Add(self.raExpPol, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.raExpOtros = wx.RadioButton(
            self, wx.ID_ANY, u"ExpOtros", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer42.Add(self.raExpOtros, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.raInforme = wx.RadioButton(
            self, wx.ID_ANY, u"Informe", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer42.Add(self.raInforme, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.raCaratula = wx.RadioButton(
            self, wx.ID_ANY, u"Caratula", wx.DefaultPosition, wx.DefaultSize, 0
        )
        bSizer42.Add(self.raCaratula, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer41.Add(bSizer42, 0, wx.EXPAND, 5)

        self.lsPrincipal = wx.ListCtrl(
            self,
            wx.ID_ANY,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.LC_REPORT | wx.LC_SORT_ASCENDING,
        )
        bSizer41.Add(self.lsPrincipal, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer41)
        self.Layout()
        self.mnuContext = wx.Menu()
        self.mnuVer = wx.MenuItem(
            self.mnuContext, wx.ID_ANY, u"Ver", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mnuContext.Append(self.mnuVer)

        self.mnuEditar = wx.MenuItem(
            self.mnuContext, wx.ID_ANY, u"Editar", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mnuContext.Append(self.mnuEditar)

        self.mnuBorrar = wx.MenuItem(
            self.mnuContext, wx.ID_ANY, u"Borrar", wx.EmptyString, wx.ITEM_NORMAL
        )
        self.mnuContext.Append(self.mnuBorrar)

        self.Bind(wx.EVT_RIGHT_DOWN, self.MainOnContextMenu)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.MainOnClose)
        self.Bind(
            wx.EVT_MENU,
            self.mnuCausaAgregarOnMenuSelection,
            id=self.mnuCausaAgregar.GetId(),
        )
        self.scBuscar.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.scBuscarOnSearchButton)
        self.lsPrincipal.Bind(wx.EVT_LEFT_DCLICK, self.lsPrincipalOnLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def MainOnClose(self, event):
        event.Skip()

    def mnuCausaAgregarOnMenuSelection(self, event):
        event.Skip()

    def scBuscarOnSearchButton(self, event):
        event.Skip()

    def lsPrincipalOnLeftDClick(self, event):
        event.Skip()

    def MainOnContextMenu(self, event):
        self.PopupMenu(self.mnuContext, event.GetPosition())


###########################################################################
## Class Login
###########################################################################


class Login(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=u"Login",
            pos=wx.DefaultPosition,
            size=wx.DefaultSize,
            style=wx.DEFAULT_DIALOG_STYLE,
        )

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"USUARIO", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText1.Wrap(-1)

        fgSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.tcUsuario = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0
        )
        fgSizer1.Add(self.tcUsuario, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(
            self, wx.ID_ANY, u"CONTRASEÑA", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.m_staticText4.Wrap(-1)

        fgSizer1.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.tcPass = wx.TextCtrl(
            self,
            wx.ID_ANY,
            wx.EmptyString,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.TE_PASSWORD,
        )
        fgSizer1.Add(self.tcPass, 0, wx.ALL, 5)

        self.btCancelar = wx.Button(
            self, wx.ID_ANY, u"CANCELAR", wx.DefaultPosition, wx.DefaultSize, 0
        )
        self.btCancelar.SetBackgroundColour(wx.Colour(255, 183, 183))

        fgSizer1.Add(self.btCancelar, 0, wx.ALL, 5)

        self.btAceptar = wx.Button(
            self, wx.ID_ANY, u"ACEPTAR", wx.DefaultPosition, wx.DefaultSize, 0
        )

        self.btAceptar.SetDefault()
        self.btAceptar.SetBackgroundColour(wx.Colour(185, 255, 193))

        fgSizer1.Add(self.btAceptar, 0, wx.ALL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()
        fgSizer1.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.btCancelar.Bind(wx.EVT_BUTTON, self.btCancelarOnButtonClick)
        self.btAceptar.Bind(wx.EVT_BUTTON, self.btAceptarOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btCancelarOnButtonClick(self, event):
        event.Skip()

    def btAceptarOnButtonClick(self, event):
        event.Skip()

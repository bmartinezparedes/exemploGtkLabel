import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejercicio")

        notebook = Gtk.Notebook()
        self.add(notebook)

        cajaV1= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        notebook.append_page(cajaV1,Gtk.Label(label="MenuWidget1"))
        cajaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        notebook.append_page(cajaV2,Gtk.Label(label="MenuWidget2"))

        cajaH =Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boton = Gtk.Button(label="ToolbarButton")
        cajaH.add(boton)
        checkButon = Gtk.CheckButton(label="ToolbarCheckButton")
        cajaH.add(checkButon)
        cajaV1.add(cajaH)
        lblPanelCaption = Gtk.Label(label="Panel Caption")
        cajaV1.add(lblPanelCaption)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
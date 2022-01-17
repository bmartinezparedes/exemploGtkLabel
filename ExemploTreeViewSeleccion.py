import gi
import os
import GridConBotones

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView con Seleccion")
        self.set_border_width(5)
        self.set_default_size(400,200)

        programas = Gtk.ListStore(str, int, str)
        programas.append(["FireFox",1960, "C++"])
        programas.append(["Eclipse",1999, "Java"])
        programas.append(["AndroidEstudio",2000, "Kotling"])
        programas.append(["VirtualBox",2001, "Java"])
        programas.append(["VisualEstudio",2005, "PHP"])
        programas.append(["Chrome",2022, "C"])
        programas.append(["Netbeans",1998, "Java"])

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        trvVistaProgramas = Gtk.TreeView(model=programas)
        for i, tituloColumna in enumerate (["Software","Ano","Linguaxe de programación"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            trvVistaProgramas.append_column(columna)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 8, 10)
        scroll.add(trvVistaProgramas)

        seleccion = trvVistaProgramas.get_selection()
        seleccion.connect("changed", self.on_trvVistaProgramas_changed)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    def on_trvVistaProgramas_changed(self,selec):
        modelo, punteiro = selec.get_selected()
        if punteiro is not None:
            print("Seleccionaches ",modelo[punteiro][0])

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
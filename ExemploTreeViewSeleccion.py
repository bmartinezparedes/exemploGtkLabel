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

        seleccion = trvVistaProgramas.get_selection()
        seleccion.connect("changed", self.on_trvVistaProgramas_changed)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 8, 10)
        scroll.add(trvVistaProgramas)

        self.sofware = Gtk.Entry()
        self.ano = Gtk.Entry()
        self.linProgramacion = Gtk.Entry()
        self.modificar = Gtk.Button(label="Modificar")
        self.modificar.connect("clicked", self.on_modificar_clicked, seleccion)
        self.modificar.set_sensitive(False)

        grid.attach(self.sofware,0,10,2,1)
        grid.attach_next_to(self.ano,self.sofware,Gtk.PositionType.RIGHT,2,1)
        grid.attach_next_to(self.linProgramacion, self.ano, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(self.modificar,self.linProgramacion,Gtk.PositionType.RIGHT, 2, 1)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_trvVistaProgramas_changed(self,selec):
        modelo, punteiro = selec.get_selected()
        self.sofware.set_text(modelo[punteiro][0])
        self.ano.set_text(str(modelo[punteiro][1]))
        self.linProgramacion.set_text(modelo[punteiro][2])
        self.modificar.set_sensitive(True)

    def on_modificar_clicked(self,control,seleccion):
        modelo, fila = seleccion.get_selected()
        modelo[fila][0] = self.sofware.get_text()
        modelo[fila][1] = int(self.ano.get_text())
        modelo[fila][2] = self.linProgramacion.get_text()
        self.modificar.set_sensitive(False)

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
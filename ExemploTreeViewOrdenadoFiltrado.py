import gi
import os
import GridConBotones

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView con Ordenacion y Filtrado")
        self.set_border_width(5)
        self.set_default_size(400,200)

        self.filtro_actual_linguaxe = "None"

        programas = Gtk.ListStore(str, int, str)
        programas.append(["FireFox",1960, "C++"])
        programas.append(["Eclipse",1999, "Java"])
        programas.append(["AndroidEstudio",2000, "Kotling"])
        programas.append(["VirtualBox",2001, "Java"])
        programas.append(["VisualEstudio",2005, "PHP"])
        programas.append(["Chrome",2022, "C"])
        programas.append(["Netbeans",1998, "Java"])
        programas.append(["kernel Linux",1991,"C"])
        programas.append(["Sphinx",2003,"Python"])

        self.filtroLinguaxe = programas.filter_new()
        self.filtroLinguaxe.set_visible_func(self.filtro_linguaxe)


        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        trvVistaProgramas = Gtk.TreeView(model=self.filtroLinguaxe)
        for i, tituloColumna in enumerate (["Software","Ano","Linguaxe de programación"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            trvVistaProgramas.append_column(columna)

        scroll = Gtk.ScrolledWindow()
        scroll.set_vexpand(True)
        grid.attach(scroll, 0, 0, 8, 10)
        scroll.add(trvVistaProgramas)

        filtroJava= Gtk.Button (label="Java")
        filtroC = Gtk.Button(label="C")
        filtroCMaisMais = Gtk.Button(label="C++")
        filtroPython = Gtk.Button(label="Python")
        senFiltro = Gtk.Button(label="None")

        filtroJava.connect("clicked", self.on_botonSeleccion_clicked)
        filtroC.connect("clicked", self.on_botonSeleccion_clicked)
        filtroPython.connect("clicked", self.on_botonSeleccion_clicked)
        filtroCMaisMais.connect("clicked", self.on_botonSeleccion_clicked)
        senFiltro.connect("clicked", self.on_botonSeleccion_clicked)

        grid.attach_next_to(filtroJava,scroll,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(filtroC, filtroJava, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(filtroCMaisMais, filtroC, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(filtroPython, filtroCMaisMais, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(senFiltro, filtroPython, Gtk.PositionType.RIGHT, 1, 1)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    def on_botonSeleccion_clicked(self,boton):
        self.filtro_actual_linguaxe=boton.get_label()
        self.filtroLinguaxe.refilter()

    def filtro_linguaxe(self,modelo,fila,datos):
        if(self.filtro_actual_linguaxe=="None"):
            return True
        else:
            return modelo[fila][2]== self.filtro_actual_linguaxe


if __name__=="__main__":
    Aplicacion()
    Gtk.main()
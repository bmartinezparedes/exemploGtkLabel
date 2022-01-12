import gi
import os
import GridConBotones

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from gi.repository.GdkPixbuf import Pixbuf


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo TreeView con TreeStore")
        self.set_border_width(5)
        #Creo el modelo
        modelo = Gtk.TreeStore(str,int)
        for avo in range (5):
            punteiroAvo = modelo.append(None,['Avó', avo])
            for pai in range (4):
                punteiroPai = modelo.append(punteiroAvo, ['Pai', pai])
                for fillo in range(6):
                    punteiroFillo = modelo.append(punteiroPai, ['Fillo', fillo])

        trvArboreXeneraloxico = Gtk.TreeView(model=modelo)
        # Columna 1
        trvColumna = Gtk.TreeViewColumn('Parentesco')
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)
        #Columna 2
        trvColumna = Gtk.TreeViewColumn("Orde")
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)

        self.add(trvArboreXeneraloxico)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
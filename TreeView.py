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
        modelo = Gtk.TreeStore(str,int,str)
        for avo in range (5):
            punteiroAvo = modelo.append(None,['Avó', avo,"Sen datos"])
            for pai in range (4):
                punteiroPai = modelo.append(punteiroAvo, ['Pai', pai,"Lexítimo"])
                for fillo in range(6):
                    punteiroFillo = modelo.append(punteiroPai, ['Fillo', fillo,"Lexítimo"])

        trvArboreXeneraloxico = Gtk.TreeView(model=modelo)
        # Columna 1
        trvColumna = Gtk.TreeViewColumn('Parentesco')
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        celda.set_property("editable",True)
        celda.connect("edited", self.on_columna_edited, modelo)
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 0)
        #Columna 2
        trvColumna = Gtk.TreeViewColumn("Orde")
        trvArboreXeneraloxico.append_column(trvColumna)
        celda = Gtk.CellRendererText()
        trvColumna.pack_start(celda, True)
        trvColumna.add_attribute(celda, "text", 1)
        #Columna 3
        tipoParentesco = Gtk.ListStore(str)
        tipoParentesco.append(["Sen datos"])
        tipoParentesco.append(["Lexítimo"])
        tipoParentesco.append(["Bastardo"])

        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)
        celdaCombo.set_property("model", tipoParentesco)
        celdaCombo.set_property("text-column", 0)
        celdaCombo.set_property("has-entry", False)
        celdaCombo.connect("edited", self.on_combo_edited, modelo)
        trvColumnaCombo = Gtk.TreeViewColumn("Combo", celdaCombo, text=2)
        trvArboreXeneraloxico.append_column(trvColumnaCombo)

        self.add(trvArboreXeneraloxico)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    def on_combo_edited(self, control, fila, texto, modelo):
        modelo [fila][2] = texto
    def on_columna_edited(self, control, fila, texto, modelo):
        modelo [fila][0] = texto
        print("Te queremos kiskos")#By Patri y Britza :)
if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
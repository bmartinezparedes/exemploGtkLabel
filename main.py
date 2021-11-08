import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Aplicacion:
    def __init__(self):
        wndFiestra=Gtk.Window()
        wndFiestra.set_title("Exemplo de un Gtk.Label")

        caixaV= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        wndFiestra.connect("destroy",Gtk.main_quit)
        wndFiestra.show_all()
if __name__=="__main__":
    Aplicacion()
    Gtk.main()
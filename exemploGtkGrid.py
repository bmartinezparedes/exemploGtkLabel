import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de un Gtk.Grid")
        cuadricula=Gtk.Grid()
        self.add(cuadricula)

        btnBoton1 = Gtk.Button(label="Boton1")
        btnBoton2 = Gtk.Button(label="Boton2")
        btnBoton3 = Gtk.Button(label="Boton3")
        btnBoton4 = Gtk.Button(label="Boton4")
        btnBoton5 = Gtk.Button(label="Boton5")
        btnBoton6 = Gtk.Button(label="Boton6")

        cuadricula.add(btnBoton1)
        cuadricula.attach(btnBoton2,1,0,2,1)
        cuadricula.attach_next_to(btnBoton3,btnBoton1,Gtk.PositionType.BOTTOM,1,2)
        cuadricula.attach(btnBoton4,1,1,2,1)
        cuadricula.attach_next_to(btnBoton5,btnBoton4,Gtk.PositionType.BOTTOM,1,1)
        cuadricula.attach_next_to(btnBoton6,btnBoton5,Gtk.PositionType.RIGHT,1,1)

        self.connect("destroy",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
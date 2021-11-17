import gi
import GridConBotones

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso de Stack e StackSwicher")
        self.set_border_width(5)

        caixaV=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=5)
        self.add(caixaV)
        panel=Gtk.Stack()
        panel.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        panel.set_transition_duration(1000)

        pulsame=Gtk.CheckButton(label="Pulsame")
        panel.add_titled(pulsame, "Pulsame","Pulsameeeeeeeeeeeeeeeeeeeeee")

        etiqueta=Gtk.Label()
        etiqueta.set_markup("<big>Unha etiqueta presuntuosa</big>")
        panel.add_titled(etiqueta,"Etiqueta", "Unha etiqueta")

        botones=GridConBotones.CaixaDeBotons()
        panel.add_titled(botones, "Aqui van los botones", "Botones")

        selector_paneis=Gtk.StackSwitcher()
        selector_paneis.set_stack(panel)

        caixaV.pack_start(selector_paneis,True,True,0)
        caixaV.pack_start(panel,True,True,0)

        self.connect("destroy",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
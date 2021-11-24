import gi
import GridConBotones

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de FLowBox")
        self.set_border_width(5)
        self.set_default_size(300,250)

        cabeceira= Gtk.HeaderBar(title="FlowBox")
        cabeceira.set_subtitle("con cabeceira HeaderBar")
        cabeceira.props.show_close_button=True
        self.set_titlebar(cabeceira)

        boton=Gtk.Button()
        icon=Gio.ThemedIcon(name="mail-send-receive-symbolic")
        imaxe= Gtk.Image.new_from_gicon(icon,Gtk.IconSize.BUTTON)
        boton.add(imaxe)
        cabeceira.pack_end(boton)

        caixa=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(),"linked")

        boton2=Gtk.Button()
        boton2.add(
            Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT,shadow_type=Gtk.ShadowType.NONE)
        )
        caixa.add(boton2)

        boton3=Gtk.Button.new_from_icon_name("pan-end-symbolic",Gtk.IconSize.MENU)
        caixa.add(boton3)
        cabeceira.pack_start(caixa)

        flowbox= Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        for n in range(50):
            cuadro=GridConBotones.CaixaDeBotons()
            flowbox.add(cuadro)
        barras= Gtk.ScrolledWindow()
        barras.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.AUTOMATIC)
        barras.add(flowbox)
        self.add(barras)

        self.connect("destroy",Gtk.main_quit)
        self.show_all()

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
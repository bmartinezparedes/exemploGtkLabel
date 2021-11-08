import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de un Gtk.Label")
        self.set_size_request(200,150)

        self.baseTempo=None

        caixaV=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=8)
        self.add(caixaV)

        self.txtTexto=Gtk.Entry()
        self.txtTexto.set_width_chars(30)
        self.txtTexto.set_text("Benvidos")
        caixaV.pack_start(self.txtTexto,True,True,0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        caixaV.pack_start(caixaH, True, True, 0)

        self.chkEditable=Gtk.CheckButton(label="Editable")
        self.chkEditable.connect("toggled", self.on_chkEditable_toggled)
        self.chkEditable.set_active(True)

        caixaH.pack_start(self.chkEditable, True, True, 0)

        self.chkVisible = Gtk.CheckButton(label="Visible")
        self.chkVisible.connect("toggled", self.on_chkVisible_toggled)
        self.chkVisible.set_active(True)
        caixaH.pack_start(self.chkVisible, True, True, 0)

        self.connect("destroy",Gtk.main_quit)
        self.show_all()

    def on_chkEditable_toggled(self,control):
        estado=control.get_active()
        self.txtTexto.set_editable(estado)
    def on_chkVisible_toggled(self,control):
        estado=control.get_active()
        self.txtTexto.set_visible(estado)

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
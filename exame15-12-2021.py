import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 15-12-2021")
        self.set_border_width(10)

        cajaVprincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #Primera parte
        grid = Gtk.Grid()
        grid.set_margin_bottom(5)
        cajaVprincipal.pack_start(grid,True,True,0)

        lblNome = Gtk.Label(label = "Nome:")
        grid.attach(lblNome,0,0,1,1)
        lblApelido = Gtk.Label(label = "Apelido:")

        lblNomeUsuario= Gtk.Label (label = "Nome de Usuario:")

        lblFormato = Gtk.Label(label = "Formato:")
        grid.attach(lblFormato, 0, 2, 1, 1)
        lblTratamento = Gtk.Label(label = "Tratamento:")
        grid.attach(lblTratamento, 0, 1, 1, 1)

        txtNome= Gtk.Entry()
        grid.attach_next_to(txtNome,lblNome,Gtk.PositionType.RIGHT,2,1)
        txtApelido= Gtk.Entry()
        txtTratamento= Gtk.Entry()
        grid.attach_next_to(txtTratamento, lblTratamento,Gtk.PositionType.RIGHT, 2, 1)
        txtNomeUsuario= Gtk.Entry()

        cmbFormato=Gtk.ComboBoxText()
        cmbFormato.append_text("pdf")
        cmbFormato.append_text("docx")
        cmbFormato.append_text("odt")
        cmbFormato.append_text("texto")
        cmbFormato.connect("changed", self.cambio)


        grid.attach_next_to(cmbFormato, lblFormato, Gtk.PositionType.RIGHT, 5, 1)

        grid.attach_next_to(lblApelido,txtNome, Gtk.PositionType.RIGHT,1,1)
        grid.attach_next_to(lblNomeUsuario,txtTratamento, Gtk.PositionType.RIGHT,1,1)
        grid.attach_next_to(txtApelido,lblApelido, Gtk.PositionType.RIGHT,2,1)
        grid.attach_next_to(txtNomeUsuario,lblNomeUsuario,Gtk.PositionType.RIGHT,2,1)

        builder = Gtk.Builder()
        builder.add_from_file("cadroCorreoGlade.glade")

        box1 = builder.get_object("box1")
        cajaVprincipal.pack_start(box1,True,True,0)

        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        entryCorreo = builder.get_object("txtDireccionCorreo")
        btnEngadir = builder.get_object("btnEngadir")
        txvListaCorreos = builder.get_object("txvListaCorreos")
        self.bufer = txvListaCorreos.get_buffer()

        btnEngadir.connect("clicked",self.accion,entryCorreo,txvListaCorreos)
        self.btnAceptar=Gtk.Button(label = "Aceptar")
        cajaH.pack_end(self.btnAceptar,False,False,2)
        self.btnCancelar= Gtk.Button(label = "Cancelar")
        self.btnCancelar.connect("clicked",Gtk.main_quit)
        cajaH.pack_end(self.btnCancelar,False,False,2)

        cajaVprincipal.pack_start(cajaH,True,True,4)




        self.add(cajaVprincipal)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    def accion(self,boton,entryCorreo,txvListaCorreos):
        punteiro = self.bufer.get_end_iter()
        self.bufer.insert(punteiro,entryCorreo.get_text()+ "\n")
    def cambio(self,control):
        print(control.get_active_text())
if __name__=="__main__":
    Exame()
    Gtk.main()
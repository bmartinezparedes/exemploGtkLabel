import conexionBD
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer,Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Examen")
        self.set_border_width(5)
        self.set_default_size(400,200)

        caixaV = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        caixaH = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL)

        caixaV.pack_start(caixaH,False,False,0)

        lblNumeroAlbaran = Gtk.Label(label="Numero de albaran")
        caixaH.pack_start(lblNumeroAlbaran,False,False,2)


        modeloNumeroAlbaran = Gtk.ListStore(int)

        bd = conexionBD.ConexionBD("modelosClasicos.dat")
        bd.conectaBD()
        bd.creaCursor()
        numeroAlbaran = bd.consultaSenParametros("select numeroAlbaran from ventas")

        modeloNumeroAlbaran.append(0)
        for numero in numeroAlbaran:
            print(numero)
            modeloNumeroAlbaran.append(numero)

        modeloTreeView = Gtk.ListStore(int,str,int,float)

        self.filtroActual=0
        filtro = modeloTreeView.filter_new()
        filtro.set_visible_func(self.filtroNumeroAlbaran)

        twDetalles = Gtk.TreeView(model=filtro)
        detalles = bd.consultaSenParametros("select numeroAlbaran,codigoProducto,cantidade,prezoUnitario from detalleVentas")
        print(detalles)
        for datos in detalles:
            modeloTreeView.append(datos)
        for i, titulo in enumerate(["numeroAlbaran","codigoProducto","cantidade","prezoUnitario"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(titulo,celda,text=i)
            twDetalles.append_column(columna)
        caixaV.pack_start(twDetalles,True,True,0)
        comboNumeroAlbaran = Gtk.ComboBox.new_with_model(modeloNumeroAlbaran)
        comboNumeroAlbaran.connect("changed", self.changed_NumeroAlbaran, filtro, modeloTreeView)
        caixaH.pack_start(comboNumeroAlbaran, False, False, 0)
        celda = Gtk.CellRendererText()
        comboNumeroAlbaran.pack_start(celda, True)
        comboNumeroAlbaran.add_attribute(celda, "text", 0)

        btnCrearDocumento = Gtk.Button(label="Crear documento")
        btnCrearDocumento.connect("clicked",self.clicketButton,bd)
        caixaV.pack_start(btnCrearDocumento,False,True,0)
        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
    def filtroNumeroAlbaran(self,modelo,fila,datos):
        if(self.filtroActual==0 or None):
            return True
        else:
            return modelo[fila][0] == self.filtroActual

    def changed_NumeroAlbaran(self,combo,filtro,modelo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            numero = modelo[fila][0]
            self.filtroActual= int(numero)
        filtro.refilter()
    def clicketButton(self,boton,bd):
        doc = SimpleDocTemplate("examen.pdf")
        elemento = []
        estilos = getSampleStyleSheet()
        estilo = estilos["Heading2"]
        estilo2 = estilos["Heading1"]
        parrafo = Paragraph("Informe:",estilo2)
        elemento.append(parrafo)
        elemento.append(Spacer(0,10))
        cabeceras = bd.consultaSenParametros("select numeroAlbaran, dataAlbaran,numeroCliente from ventas")
        datos = bd.consultaSenParametros("select * from detalleVentas")
        print(datos)
        for cabecera in cabeceras:
            parrafo = Paragraph("Albaran: "+str(cabecera[0])+" Fecha: "+str(cabecera[1])+" Cliente: "+str(cabecera[2]),estilo)
            elemento.append(parrafo)
            elemento.append(Spacer(0,10))
            datTable = [["Cod Proucto", "Cantidad", "Prezo Unitario"]]
            for dato in datos:

                if(cabecera[0]==dato[0]):

                    datTable.append([dato[1],dato[2],dato[3]])
                    print(dato[0])
            table = Table(datTable)
            table.setStyle([("BACKGROUND",(0,0),(-1,0),colors.greenyellow),
                            ("BOX",(0,0),(-1,0),1,colors.black),
                            ("GRID",(0,1),(-1,-1),1,colors.lightgrey)])
            elemento.append(table)
            elemento.append(Spacer(0,10))

        doc.build(elemento)

if __name__=="__main__":
    Aplicacion()
    Gtk.main()
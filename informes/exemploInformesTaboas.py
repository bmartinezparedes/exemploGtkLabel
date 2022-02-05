from reportlab.platypus import SimpleDocTemplate, PageBreak, Table,TableStyle, Spacer, Paragraph,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import sqlite3 as dbapi

doc = SimpleDocTemplate("informes/exeploTaboas.pdf", pagesize=A4)

guion = []

taboa =Table([['','Ventas','Compras'],
              ['Xaneiro',123,456],
              ['Febreiro',2500,2555],
              ['Marzo',1400,990]],
             colWidths=80,rowHeights= 30)

taboa.setStyle([('TEXTCOLOR',(0,1),(0,-1),colors.blue),
                ('TEXTCOLOR',(1,1),(2,-1),colors.green),
                ('BACKGROUND',(1,1),(-1,-1),colors.beige),
                ('BOX',(1,1),(-1,-1),1.25,colors.yellowgreen),
                ('INNERGRID',(1,1),(-1,-1),1,colors.orangered),
                ('VALING',(0,0),(-1,-1),'MIDDLE')])

guion.append(taboa)
guion.append(Spacer(0,15))
p = Paragraph ("Este é un texto dun parragrafo\nCon varias liñas")
i = Image ('/home/oracle/Imaxes/Captura de pantalla de 2021-12-13 17-54-42.png',width = 50, height=100 )

datos=[['Arriba\nEsquerda', '', '02','03','04'],
       ['','','12',p,'14'],
       ['20',i,'22','Abaixo\nDereita'],
       ['30','31','32','','']]

estilo = [('GRID', (0,0), (-1,-1), 0.5, colors.grey),
          ('BACKGROUND', (0,0), (-1,-1), colors.palegreen),
          ('SPAN', (0,0), (1,1)),
          ('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
          ('SPAN', (-2,-2), (-1,-1))]
taboa2 = Table (data=datos,style=estilo)

guion.append(taboa2)
guion.append(Spacer(0,15))
try:
    bbdd = dbapi.connect("informes/modelosClasicos.dat")
    cursor = bbdd.cursor()
    usuarios =[]
    usuarios.append(("Nome","Apelidos", "Numero Cliente","Telefono"))
    cursor.execute("SELECT * FROM main.clientes")
    for rexistro in cursor.fetchall():
        print(rexistro[1],rexistro[0],rexistro[2])
        usuarios.append((rexistro[1],rexistro[0],rexistro[2], rexistro[4]))

except dbapi.DatabaseError as e:
    print("Erro na base de datos: " + str(e))

estilo = [('Box', (0,0), (1, -1), 1.0, colors.darkgray),
    ('Box', (1,0), (-1, -1), 1.0, colors.darkgray),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
    ('BACKGROUND', (0,0), (0,-1), colors.palegreen),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.brown),
    ('BACKGROUND',(1,0),(-1,-1), colors.grey),
    ('TEXTCOLOR',(1,0),(-1,-1),colors.brown),
    ('ALIGN',(0,0),(-1,-1),"CENTER")]
taboaUsuarios= Table(data=usuarios,style=estilo)
guion.append(taboaUsuarios)

doc.build(guion)
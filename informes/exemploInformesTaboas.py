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
    estilo = [('BOX', (0, 0), (-1, 0), 1.0, colors.darkgray),
              ('BOX', (0, 1), (-1, -1), 1.0, colors.darkgray),
              ('INNERGRID', (0, 0), (-1, -1), 0.4, colors.lightgrey),
              ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen)
              ]
    usuarios =[]
    usuarios.append(("Nome","Apelidos", "Numero Cliente","Telefono"))
    cursor.execute("SELECT nomeCliente, apelidosCliente, numeroCliente, telefono FROM main.clientes")
    for n, rexistro in enumerate(cursor.fetchall()):
        print(rexistro)
        usuarios.append((rexistro[1],rexistro[0],rexistro[2], rexistro[3]))
        if n%2 == 0:
            for c in range(len(rexistro)):
                if c % 2 == 0:
                    print(c,n)
                    estilo.append(('BACKGROUND', (c, n + 1), (c, n + 1), colors.HexColor('#f4f6f6')))
                else:
                    print(c,n)
                    estilo.append(('BACKGROUND', (c, n + 1), (c, n + 1), colors.HexColor('#e5e8e8')))
        else:
            estilo.append(('BACKGROUND', (0, n + 1), (0, n + 1), colors.HexColor('#d6dbdf')))
            estilo.append(('BACKGROUND', (1, n + 1), (1, n + 1), colors.HexColor('#d5d8dc')))
            estilo.append(('BACKGROUND', (2, n + 1), (2, n + 1), colors.HexColor('#d6dbdf')))
            estilo.append(('BACKGROUND', (3, n + 1), (3, n + 1), colors.HexColor('#d5d8dc')))

except dbapi.DatabaseError as e:
    print("Erro na base de datos: " + str(e))


taboaUsuarios= Table(data=usuarios,style=estilo)
guion.append(taboaUsuarios)

doc.build(guion)
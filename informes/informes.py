from reportlab.pdfgen import canvas

lenzo =canvas.Canvas("documento.pdf")
lenzo.drawString(0,0,"Posicion inicial (x,y)=(0,0)")
lenzo.drawString(50,100,"Posicion inicial (x,y)=(50,100)")
lenzo.drawString(200,50,"Posicion inicial (x,y)=(200,50)")

lenzo.drawImage("/home/oracle/Imaxes/Captura de pantalla de 2021-12-13 17-54-42.png",50,500,325,223)

lenzo.showPage()
lenzo.save()
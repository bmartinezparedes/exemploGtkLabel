from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

operacions = []

imaxe = Image(400,0,325,223, "/home/oracle/Imaxes/Captura de pantalla de 2021-12-13 17-54-42.png")

debuxo = Drawing (30,30)
debuxo.add(imaxe)
debuxo.translate(0,500)

operacions.append(debuxo)

debuxo = Drawing(30,30)
debuxo.add(imaxe)
debuxo.rotate(45)
debuxo.scale(1.5,0.5)
debuxo.translate(-30,200)
operacions.append(debuxo)

debuxo =Drawing(A4[0],A4[1])
for op in operacions:
    debuxo.add(op)

renderPDF.drawToFile(debuxo, "documento2.pdf")


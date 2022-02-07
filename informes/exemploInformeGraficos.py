from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []
d = Drawing(400,200)

datos = [(23,14,10,9,19,21,25,4),
       (2,7,9,16,14,19,20,24)]

bg = VerticalBarChart()
bg.data = datos
bg.x = 50
bg.y = 50
bg.height = 125
bg.width = 300
bg.strokeColor = colors.black
bg.valueAxis.valueMin = 0
bg.valueAxis.valueMax = 30
bg.valueAxis.valueStep = 10
bg.categoryAxis.labels.boxAnchor = 'ne' #North east
bg.categoryAxis.labels.dx = 8
bg.categoryAxis.labels.dy = -2
bg.categoryAxis.labels.angle = 30
bg.categoryAxis.categoryNames = ['Xan-21', 'Feb-21', 'Mar-21', 'Abr-21', 'Mai-21', 'Xun-21', 'Xul-21','Ago-21']
bg.groupSpacing = 10
bg.barSpacing = 2
d.add(bg)
guion.append(d)

doc = SimpleDocTemplate("informeGraficos.pdf", pagesize = A4)
doc.build(guion)
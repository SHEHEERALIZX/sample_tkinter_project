import tkinter as tk
root = tk.Tk()
from reportlab.pdfgen import canvas as screen

width=500
height=700


# report lab create canvas object
c=screen.Canvas("generated.pdf",pagesize=(width,height))




# export pdf fucntion logic works when button clicks
def exportAsPdf():
    xList = [0,100,200,300,400,500,600,700]
    yList = [0,100,200,300,400,500,600,700]
    c.grid(xList,yList)
    c.setFont("Helvetica",8)
    c.save()



# button instance
pdfButton = tk.Button(root,text="Export as PDF",fg="white",bg='red', width = 68, command=exportAsPdf)
pdfButton.pack()



# sampleData = [["sample1",]]


canvas = tk.Canvas(root, width=width, height=height, bg='white')
canvas.pack()
x1= 0
x2 =900
for k in range(0, 900, 100):
     y1 = k
     y2 = k
     canvas.create_rectangle(x1, y1, x2, y2,width=2)

   
     a=50
     b=50
     for j in range(1,8):
         a=50
         for i in range(1,6):
              canvas.create_text(a,b,text="food coupon")
              c.drawString(a-30,b,"food coupon")
              a=a+100
         b=b+100
y1 = 0
y2 = 900
for k in range(0, 900, 100):
     x1= k
     x2 =k
     canvas.create_rectangle(x1, y1, x2, y2,width=2)    

root.mainloop()
# import json
# with open(r"D:\英雄时刻\Scrapy\mspider\music.json","rb") as f:
# 	data=json.load(f)
# print(data)
# def f(n):
# 	for i in range(n):
# 		a=i*2
# 		yield a
		
# gen=f()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(f(4)))
# import scrapy
# import re
# class MspiderItem(scrapy.Item):
# 	title = scrapy.Field()#歌曲名
# 	artist = scrapy.Field()
# a="hello"
# t="world"
# item=MspiderItem()
# item["title"]=a
# item["artist"]=t
# c=item["title"]
# print(item)
import time
from graphics import*
from tkinter import*
#按钮响应
def processok():
	print("ok被点击")
def processcel():
	print("cancel被点击")
def main():
	tk=Tk()
	btnok=Button(tk,text="ok",fg="red",command=processok)
	btncle=Button(tk,text="cancel",bg="yellow",command=processcel)
	btnok.pack()
	btncle.pack()
	tk.mainloop()
#画布显示文字和图片
# def main():
# 	tk=Toplevel()
# 	canvas=Canvas(tk,width=200,height=200)
# 	canvas.pack()
# 	canvas.create_text(60,40,text="欢迎来到tk",fill="red",font=("Times",16))
# 	myImage=PhotoImage(file=r"D:\英雄时刻\aa.gif")
# 	canvas.create_image(10,70,anchor=NW,image=myImage)
# 	canvas.create_rectangle(10,70,190,13)
# 	tk.mainloop()
#上下左右控制图形移动
# def main():
# 	tk=Toplevel()
# 	canvas=Canvas(tk,width=200,height=200)
# 	# canvas.create_line(0,50,200,50,fill="red")
# 	canvas.pack()
# 	canvas.create_oval(40,20,160,80,fill="pink")	
# 	def moverectangle(event):
# 		if event.keysym=="Up":
# 			canvas.move(1,0,-5)
# 		elif event.keysym=="Down":
# 			canvas.move(1,0,5)
# 		elif event.keysym=="Left":
# 			canvas.move(1,-5,0)
# 		elif event.keysym=="Right":
# 			canvas.move(1,5,0)
# 	canvas.create_rectangle(60,80,120,140,fill="yellow")
# 	canvas.bind_all("<KeyPress-Up>",moverectangle)
# 	canvas.bind_all("<KeyPress-Down>",moverectangle)
# 	canvas.bind_all("<KeyPress-Left>",moverectangle)
# 	canvas.bind_all("<KeyPress-Right>",moverectangle)
# 	tk.mainloop()
# if __name__ == '__main__':
# 	main()

# def main():
# 	win=GraphWin("nice",400,300)
# 	win.setCoords(0.0,0.0,300.0,300.0)
# 	massage = Text(Point(150,20),"这很nice")
# 	massage.draw(win)
# 	p1=win.getMouse()
# 	p1.draw(win)
# 	p2=win.getMouse()
# 	p2.draw(win)
# 	p3=win.getMouse()
# 	p3.draw(win)
# 	p4=win.getMouse()
# 	p4.draw(win)
# 	p5=win.getMouse()
# 	p5.draw(win)
# 	polygon = Polygon(p1,p2,p3,p4,p5)
# 	polygon.setFill("peachpuff")
# 	polygon.setOutline("black")
# 	polygon.draw(win)
# 	massage.setText("下一步")
# 	win.getMouse()
# if __name__ == '__main__':
# 	main()
# p=turtle.Turtle()
# p.speed(3)
# p.pensize(5)
# p.forward(200)
# p.right(144)
# p.forward(200)

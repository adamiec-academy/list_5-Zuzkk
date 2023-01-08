from turtle import *

x0, y0 = -450, 350
data = []

for i in open("dots.txt"):
    data.append(i.strip().split(" "))
    
penup()
goto(int(data[0][0]) + x0, -int(data[0][1]) + y0)
pendown()

for x in range(len(data)):
    goto(int(data[x][0]) + x0, -int(data[x][1]) + y0)
    
update()
exitonclick()

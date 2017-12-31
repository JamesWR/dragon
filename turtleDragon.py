import turtle
from . import dragonColors as dc
def invert(list):
   newlist=[]
   for i in list:
      newlist.append(-i)
   newlist.reverse()
   return newlist


def dragon(level):
   d=[90]
   for i in range(level):
      d=d+[90]+invert(d)
   return(d)

   
def turtledragon1(level, t, size):
   d=dragon(level)
   for i in range(len(d)):
      t.forward(size)
      t.left(d[i])
      t.color(dc.bounce(float(i)/len(d)))
   t.forward(size)
   
def turtledragonc(level, t, size, color):
   d=dragon(level)
   for i in range(len(d)):
      t.forward(size)
      t.left(d[i])
      t.color(color(float(i)/len(d)))
   t.forward(size)

def turtledragon2(level, t, size): 
   d=invert(dragon(level))
   for i in range(len(d)):
      t.forward(size)
      t.left(d[i])
      t.color((0.5,float(i)/len(d),1-(float(i)/len(d))))
   t.forward(size)

def turtledragon(level, t, size):
	turtledragon1(level, t, size)
	t.left(90)
	turtledragon2(level, t, size)

def thing(level,t,size):
	turtledragon(level,t,size)
	t.right(90)
	turtledragon(level,t,size)
	t.left(90)
	turtledragon(level,t,size)
	t.right(90)
	turtledragon(level,t,size)
   
def setup():
   win = turtle.Screen()
   t = turtle.Turtle()
   t.speed(0)
   return (win, t)

(win, t) = setup()
# turtledragon(11, t, 2)

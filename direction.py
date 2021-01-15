#
# from turtle import Shape, Turtle, mainloop, Vec2D as Vec
#
# G = 8
#
# class GravSys(object):
#     def __init__(self):
#         self.planets = []
#         self.t = 0
#         self.dt = 0.01
#     def init(self):
#         for p in self.planets:
#             p.init()
#     def start(self):
#         for i in range(10000):
#             self.t += self.dt
#             for p in self.planets:
#                 p.step()
#
# class Star(Turtle):
#     def __init__(self, m, x, v, gravSys, shape):
#         Turtle.__init__(self, shape=shape)
#         self.penup()
#         self.m = m
#         self.setpos(x)
#         self.v = v
#         gravSys.planets.append(self)
#         self.gravSys = gravSys
#         self.resizemode("user")
#         self.pendown()
#     def init(self):
#         dt = self.gravSys.dt
#         self.a = self.acc()
#         self.v = self.v + 0.5*dt*self.a
#     def acc(self):
#         a = Vec(0,0)
#         for planet in self.gravSys.planets:
#             if planet != self:
#                 v = planet.pos()-self.pos()
#                 a += (G*planet.m/abs(v)**3)*v
#         return a
#     def step(self):
#         dt = self.gravSys.dt
#         self.setpos(self.pos() + dt*self.v)
#         if self.gravSys.planets.index(self) != 0:
#             self.setheading(self.towards(self.gravSys.planets[0]))
#         self.a = self.acc()
#         self.v = self.v + dt*self.a
#
# ## create compound yellow/blue turtleshape for planets
#
# def main():
#     s = Turtle()
#     s.reset()
#     s.getscreen().tracer(0,0)
#     s.ht()
#     s.pu()
#     s.fd(6)
#     s.lt(90)
#     s.begin_poly()
#     s.circle(6, 180)
#     s.end_poly()
#     m1 = s.get_poly()
#     s.begin_poly()
#     s.circle(6,180)
#     s.end_poly()
#     m2 = s.get_poly()
#
#     planetshape = Shape("compound")
#     planetshape.addcomponent(m1,"orange")
#     planetshape.addcomponent(m2,"blue")
#     s.getscreen().register_shape("planet", planetshape)
#     s.getscreen().tracer(1,0)
#
#     ## setup gravitational system
#     gs = GravSys()
#     sun = Star(1000000, Vec(0,0), Vec(0,-2.5), gs, "circle")
#     sun.color("yellow")
#     sun.shapesize(1.8)
#     sun.pu()
#     earth = Star(12500, Vec(210,0), Vec(0,195), gs, "planet")
#     earth.pencolor("green")
#     earth.shapesize(0.8)
#     # moon = Star(1, Vec(220,0), Vec(0,295), gs, "planet")
#     # moon.pencolor("blue")
#     # moon.shapesize(0.5)
#     gs.init()
#     gs.start()
#     return "Done!"
#
# if __name__ == '__main__':
#     main()
#     mainloop()
#
#

'''

# -*- coding:utf-8 -*-
#! python3
import numpy as np
import matplotlib.pyplot as plt
# ==========================================
# 圆的基本信息
# 1.圆半径
r = 2.0
# 2.圆心坐标
a, b = (0., 0.)
# ==========================================
# 方法一：参数方程
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(x, y)
axes.axis('equal')
plt.title('radius '+ str(r) +' circle')

0
# ==========================================
plt.show()
'''

''' 4th '''
'''import turtle as tt
import asyncio

tt.speed(100)

tt.circle(150)
tt.penup()
tt.speed(5)


async def paint(angle):
    await tt.circle(150, eval(angle))


async def main():
    print("enter angle:")
    angle = input()
    task_list = [
        asyncio.create_task(paint(angle))
    ]

    done, pending = await asyncio.wait(task_list)
    print(done)
    print('----------------------')
    print(pending)

#tt.pendown()
asyncio.run(main())
tt.done()'''

''' 3rd '''
# import turtle
#
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
#
# t1.speed(10)
# t2.speed(10)
# for i in range(180):
#   t1.forward(10)
#   t1.left(10)
#   t2.forward(10)
#   t2.right(10)


import threading
import turtle as tt

previousangle = 0
def init():
    tt.speed(0)
    tt.circle(150)
    tt.speed(10)
    tt.up()
    tt.circle(150,90)
    tt.done()
    #tt.bye()
    print("What's that you add threading: %s" % threading.current_thread())

def paint():
    global previousangle
    while 1:
        print("please enter angle: ")
        angle_str = input()
        angle_dec = eval(angle_str)

        angle = angle_dec - previousangle

        previousangle = angle_dec

        tt.circle(150, angle)
        #tt.done

def main():
    add_thread1 = threading.Thread(target=init, name= 'Init')
    add_thread1.start()
    add_thread2 = threading.Thread(target=paint, name= 'Paint')
    add_thread2.start()

    print(threading.active_count())
    print(threading.enumerate()) #查看激活的threading
    print(threading.current_thread())#当前线程
    pass

if __name__ == '__main__':
    main()


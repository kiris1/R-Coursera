# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 16:58:57 2017

@author: e543865
"""

import math
import turtle

class Point:
    '''Represents point on a 2-D plane
    
    attributes: x, y
    '''
    
class Circle:
    """Represents a cirscle on a 2-D plane
    
    attributes: center, radius
    """
    
class Rectangle:
    """Represents a rectngle
    
    attributes: corner, width, height
    """
    
def rectangle_instance(cent_x, cent_y, width, height):
    """Instance of a Rectangle class
    returns: rectangle with given corner, width an height
    """
    rect = Rectangle()
    rect.width = width
    rect.height = height
    rect.corner = Point()
    rect.corner.x = cent_x
    rect.corner.y = cent_y
    return rect    

turt = turtle.Turtle()
rect = rectangle_instance(50, 30, 100, 150)

def draw_rectangle(turt, rect):
    """Draws a rectangle using a turtle object
    turt: Turtle object
    rect: Rectangle object
    """
    turt.pu()
    turt.fd(rect.corner.x)
    turt.lt(90)
    turt.fd(rect.corner.y)
    turt.rt(90)
    turt.pd()
    
    for i in range(2):
        turt.fd(rect.width)
        turt.lt(90)
        turt.fd(rect.height)
        turt.lt(90)

def draw_circle(turt, circ):
    """Draws a circle using the Turtle object
    turt: Turtle object
    circ: instance of Circle class
    """
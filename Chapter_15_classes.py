import math
import copy

class Point:
    '''Represents point on a 2-D plane
    
    attributes: x, y
    '''
    
def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
    
def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + ((p1.y - p2.y) ** 2))

class Rectangle:
    '''Represents rectlangle
    attributes: corner, width, height
    '''

def find_center(rect):
    """Finds the center of a rectangle
    
    rect: Rectangle
    
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p

def grow_rectangle(rect, dwidth, dheight):
    """Expands rectangle by given width and height
    
    rect: Rectangle
    dwidth: additional width to be added to rectangle (can be negative)
    dheight: additional height to be added to rectangle (can be negative)
    """
    
    rect.width = rect.width + dwidth
    rect.height = rect.height + dheight
    
def move_rectangle(rect, dx, dy):
    """Moves the rectangle by changing the corner's coordinates
    
    rect: Rectangle
    dx: amount on x axis to be added to original x variable of the corner
    dy: amount on y axis to be added to original y variable of the corner
    
    return: new Rectangle
    """
    
    import copy   #added in case the module is not imported yet
    rect2 = copy.deepcopy(rect)
    rect2.corner.x = rect.corner.x + dx
    rect2.corner.y = rect.corner.y + dy
    return rect2

def show_parameters(rect):
    print(rect.corner.x, rect.corner.y, rect.width, rect.height)
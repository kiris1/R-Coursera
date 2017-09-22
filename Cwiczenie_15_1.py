import math

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
    

def distance_between_points(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + ((p1.y - p2.y) ** 2))

def circle_instance(rad, cent_x, cent_y):
    """Instance of a Circle class
    returns: circle with given center and radius
    """
    c = Circle()
    c.radius = rad
    c.center = Point()
    c.center.x = cent_x
    c.center.y = cent_y
    return c

def point_instance(p_x, p_y):
    """Instance of a Point class
    returns: point
    """
    p = Point()
    p.x = p_x
    p.y = p_y
    return p

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

def rect_corners(rect, left_right, low_high):
    """Return coordinates' values for given rectangle and corner name
    rect: Rectangle
    left_right: string
    low_high: string
    
    return point
    """
    p = Point()
    if left_right == 'left':
        p.x = rect.corner.x
    elif left_right == 'right':
        p.x = rect.corner.x + rect.width
    else:
        print("Wrong name of the corner")
        return
        
        
    if low_high == 'low':
        p.y = rect.corner.y
    elif low_high == 'high':
        p.y = rect.corner.y + rect.height
    else:
        print("Wrong name of the corner")
        return        
    
    return p
        
    

def point_in_circle(circ, p):
    return distance_between_points(circ.center, p) <= circ.radius

#==============================================================================
# def rect_in_circle(circ, rect):
#     """Checks if a rectangle is in circle, by checking if all corners
#     are within
#     circ: instance of Circle class
#     rect: instance of Rectangle class
#     
#     return: Boolean
#     """
#     corners = []
#     flag = True
#     corners.append(rect_corners(rect, "left", "low"))
#     corners.append(rect_corners(rect, "left", "high"))
#     corners.append(rect_corners(rect, "right", "low"))
#     corners.append(rect_corners(rect, "right", "high"))
#     
#     for cor in corners:
#         if not point_in_circle(circ, cor):
#             flag = False
#     
#     return flag
#==============================================================================
    
def rect_in_circle(circ, rect):
    """Checks if a rectangle is in circle, by checking if all corners
    are within
    circ: instance of Circle class
    rect: instance of Rectangle class
    
    return: Boolean
    """

    flag = True
    ll = rect_corners(rect, 'left', 'low')
    lh = rect_corners(rect, 'left', 'high')
    rl = rect_corners(rect, 'right', 'low')
    rh = rect_corners(rect, 'right', 'high')
    
    if not (point_in_circle(circ, ll) and 
            point_in_circle(circ, lh) and
            point_in_circle(circ, rl) and
            point_in_circle(circ, rh)):
            flag = False
    print('ll:', ll.x, ll.y, 'lh:', lh.x, lh.y, 'rl:', rl.x, rl.y, 'rh:', rh.x, rh.y)
    print('c_x:', circ.center.x,'c_y:', circ.center.y, 'rad:',circ.radius)
    return flag

def rect_circle_overlap(circ, rect):
    """Checks if any corner of a rectangle overlaps with a circle
    circ: instance of class Circle
    rect: instance of class Rectangle
    
    return: Boolean
    """
    flag = False
    ll = rect_corners(rect, 'left', 'low')
    lh = rect_corners(rect, 'left', 'high')
    rl = rect_corners(rect, 'right', 'low')
    rh = rect_corners(rect, 'right', 'high')   

    if (point_in_circle(circ, ll) or
    point_in_circle(circ, lh) or
    point_in_circle(circ, rl) or
    point_in_circle(circ, rh)):
        flag = True
            
    return flag
 
circ = circle_instance(75, 150, 100)
rect = rectangle_instance(150, 100, 100, 50)

print(rect_in_circle(circ, rect))
print(rect_circle_overlap(circ, rect))
    

class Time:
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        """Metoda wywoływana przy inicjacji obiektu
        """
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        """Tworzy reprezentację łańcuchową obiektu
        """
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def __add__(self, other):
        """Tworzy metodę zastępującą znak +
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
        
    def __radd__(self, other):
        return self.__add__(other)
    
    

    def add_time(self, other):
        """Dodaje dwa momenty czasu i zwraca obiekt Time
        """
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
        
    
    
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))       
        
        
        
    def time_to_int(self):
        minutes = self.hour* 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    

    def int_to_time(int):
        time = Time()
        minutes, time.second = divmod(int, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time
    
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
        
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
    
    
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    
    def __str__(self):
        return 'x: %d, y: %d' % (self.x, self.y)
    
    
    def __add__(self, other):
        """Metoda obsługująca znak + dla obiektow lub obiektu i krotki
        """
        if isinstance(other, Point):
            return self.point_add(other)
        elif type(other) == tuple:
            return self.add_tuple(tup)

    
    def point_add(self, p2):
        p = Point()
        p.x = self.x + p2.x
        p.y = self.y + p2.y
        return p
    
    
    def add_tuple(self, tup):
        pn = Point()
        pn.x = self.x + tup[0]
        pn.y = self.y + tup[1]
        return pn
        
start = Time (9, 45)
duration = Time (1, 35)
print(start + duration)
print(start + 320)
print(1337 + start)

p1 = Point(2, 4)
p2 = Point(3, 4)
tup = (4, 7)
print(p1 + p2)
print(p1 + tup)

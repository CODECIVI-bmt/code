import copy
class Point:
    def __init__(self,*args):
        if len(args)==2:
            print(f'diem d1:({args[0]},{args[1]})')
        else:
          print(f'diem d1:({args[0]},{args[1]}')
          print(f'diem d2:({args[2]},{args[3]}')
class LineSegment:
        def __init__(self, *args):
         if len(args) == 0:
           self.__d1 = Point(8, 5)
           self.__d2 = Point(1, 0)
         elif len(args) == 2:
           if isinstance(args[0], Point):
             self.__d1 = args[0]
             self.__d2 = args[1]
         elif len(args) == 4:
             self.__d1 = Point(args[0], args[1])
             self.__d2 = Point(args[2], args[3])
        def COPY(self):
            seg1=self.__d1
            seg2=self.__d2
            seg3=copy.deepcopy(seg2)
            seg2=Point(8,9)
a=LineSegment(1,2,3,4)
a.COPY()
            
            

    
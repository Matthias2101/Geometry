#First scene containing a circle and two polygons
#November 02, 2021
#Matthias Müller
from manim import *
import math
sys.path.append("../geometry_classes")

from circle_polygon import CirclePoly

class CirclePolySc(Scene):
  
    def construct(self):
        print("in circlepoly ")
        circle_polygon = CirclePoly(no_corners=5, koord_center = [1,1,0], rad_circle =1)
        circle_polygon.add_into(self)
    
        

            
            
        

        

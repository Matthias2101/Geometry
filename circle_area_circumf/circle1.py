#First scene containing a circle and two polygons
#October 17, 2021
#Matthias Müller
from manim import *
import math

class CirclePoly(Scene):
  
    def construct(self, no_corners=6):
            
        rad_circle = 3 
        circle=Circle(radius = rad_circle)   #create a circle

        self.add(circle)
        inner_lines = []
        outer_lines = []
        radial_lines = []

        out_radius = rad_circle*1/math.cos(2*math.pi/(2*no_corners))
        p_center = Dot([0,0,0])
        
        for count in range(0, no_corners+1):
            angle= 2*count*math.pi /no_corners
            print("count", count, "angle", angle)
            corner_circle = Dot([rad_circle*math.cos(angle),rad_circle*math.sin(angle),0])
            corner_out = Dot([out_radius*math.cos(angle),out_radius*math.sin(angle),0])
            #self.add(corner_out)
            # corners_circle.add(corner_circle)
            # corners_out.add(corner_out)
            rad_line = Line(p_center.get_center(),corner_out.get_center())
            radial_lines.append(rad_line)
            #self.add(rad_line)
            
            if count > 0:
                inner_line = Line(corner_circle.get_center(), corner_circle_prev.get_center())
                inner_lines.append(inner_line)
                outer_line = Line(corner_out.get_center(),corner_out_prev.get_center())
                outer_lines.append(outer_line)

            corner_circle_prev = corner_circle
            corner_out_prev = corner_out

        for rali in radial_lines: self.add(rali)
        for inli in inner_lines: self.add(inli)
        for ouli in outer_lines: self.add(ouli)
        
    
        

            
            
        

        

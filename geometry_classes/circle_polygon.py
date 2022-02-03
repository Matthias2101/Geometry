#Circle with inner and outer polygon
#November 02, 2021
#Matthias Müller
from manim import *
import math


class CirclePoly():
    
    def __init__(self, rad_circle = 3, no_corners = 6, koord_center = [0,0,0]):
        #print("in Circle_Poly __init__")
        self.rad_circle = rad_circle
        self.no_corners = no_corners
        self.koord_center = koord_center
        self.circle=Circle(radius = rad_circle)   #create a circle
        self.circle.move_to(koord_center)
        self.inner_lines = []
        self.outer_lines = []
        self.radial_lines = []

        out_radius = rad_circle*1/math.cos(2*math.pi/(2*no_corners))
        self.p_center = Dot([koord_center])
        
        for count in range(0, no_corners+1):
            angle= 2*count*math.pi /no_corners
            #print("count", count, "angle", angle)
            corner_circle = Dot([rad_circle*math.cos(angle)+koord_center[0], rad_circle*math.sin(angle)+koord_center[1], 0 + koord_center[2] ])
            corner_out = Dot([out_radius*math.cos(angle) + koord_center[0] ,out_radius*math.sin(angle) + koord_center[1] ,0 + koord_center[2] ] )

            #self.add(corner_out)
            # corners_circle.add(corner_circle)
            # corners_out.add(corner_out)
            rad_line = Line(self.p_center.get_center(),corner_out.get_center())
            self.radial_lines.append(rad_line)
            
            if count > 0:
                inner_line = Line(corner_circle.get_center(), corner_circle_prev.get_center())
                self.inner_lines.append(inner_line)
                outer_line = Line(corner_out.get_center(),corner_out_prev.get_center())
                self.outer_lines.append(outer_line)

            corner_circle_prev = corner_circle
            corner_out_prev = corner_out

    def add_into(self, scene_into):
        scene_into.add(self.circle)
        for rali in self.radial_lines: scene_into.add(rali)
        for inli in self.inner_lines: scene_into.add(inli)
        for ouli in self.outer_lines: scene_into.add(ouli)
        
        #scene_into.add(circle)
    
        

            
            
        

        

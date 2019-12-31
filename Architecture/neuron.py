#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont

class neuron():

    def __init__(self, layer=None, diameter=20 , coordinates=(25,25)):
        self.x_coordinate = coordinates[0]
        self.y_coordinate = coordinates[1]
        self.radius = int(diameter*0.5)
        self.initialize()

    def initialize(self):
        x = self.x_coordinate
        y = self.y_coordinate
        r = self.radius
        self.circle = Image.new("RGB", (50,50), color="white")
        self.draw = ImageDraw.Draw(self.circle)
        left_upper_point = (x-r, y-r)
        right_lower_point = (x+r, y+r)
        point_list = [left_upper_point, right_lower_point]
        self.draw.ellipse(point_list, fill="white", outline="black")

    def get_neuron_coordinates(self):
        x = self.x_coordinate
        y = self.y_coordinate
        return x,y

    def visualize(self):
        # visualize
        self.circle.show()
#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from node import node
import numpy as np

# USAGE:
# 1. Initialize the Network
# network = Network()
# 2. Now you can add layers as much as you want.
#    The network grid ist getting longer
# network.add_layer()
# network.add_layer()
# 3. If you want to see your network call the visualization function.
# network.visualize()

class Network():

    def __init__(self):
        # initially creating the network grid layer
        self.image = Image.new("RGB", (300, 100), color="white")
        self.image_width, self.image_height = self.image.size

        # defining global variables for the add_node_.. function
        self.layer_x_counter = 1
        self.layer_y_counter = 0

    def add_layer_y(self):
        # adds a layer in the y achsis
        self.layer = Image.new("RGB", (self.image_width, self.image_height), color="white")
        dst = Image.new('RGB', (max(self.image.width, self.layer.width), self.image.height + self.layer.height), color="white")
        dst.paste(self.image, (0,0))
        dst.paste(self.layer, (0, self.image.height))
        self.image = dst
    
    def add_layer_x(self):
        # adds a layer in the x achsis
        self.layer = Image.new("RGB", (self.image_width, self.image_height), color="white")
        dst = Image.new('RGB', (self.image.width + self.layer.width, max(self.image.height , self.layer.height)), color="white")
        dst.paste(self.image, (0,0))
        dst.paste(self.layer, (self.image.width, 0))
        self.image = dst

    def add_node(self, layer, node):
        # automated grid layer addition
        pos_y = layer[0]
        pos_x = layer[1]
        if pos_y > self.layer_y_counter:
            self.add_layer_y()
            self.layer_y_counter+=1
        if pos_x > self.layer_x_counter:
            self.add_layer_x()
            self.layer_x_counter+=1

        node_in = node.rectangle
        self.node_rectangle_size_x, self.node_rectangle_size_y= node.get_size()

        # Defining the x and y coordinate of every node
        node_y, node_x = self.get_node_coordinates(pos_y, pos_x)

        print(node_x, node_y)
        self.image.paste(node_in, (node_x,node_y))   

    def get_node_coordinates(self, node_y_coord, node_x_coord):
        node_y = (node_y_coord-1) * self.image_height + int(self.image_height*0.5)
        node_x = int((self.image_width-240) * 0.5) + (node_x_coord-1)*self.image_width
        return node_y, node_x

    def connect(self, start, end):
        self.draw = ImageDraw.Draw(self.image)
        # calculate start point
        start_y , start_x = self.get_node_coordinates(start[0], start[1])
        start_x = start_x + int(self.node_rectangle_size_x*0.5)
        start_y = start_y + int(self.node_rectangle_size_y)
        # calculate end point
        end_y , end_x = self.get_node_coordinates(end[0], end[1])
        end_x = end_x + int(self.node_rectangle_size_x*0.5)
        end_y = end_y 
        self.draw.line((start_x,start_y,end_x,end_y), fill=128, width=2)
        #self.draw.line((end_x-5,end_y-5,end_x,end_y), fill=128, width=2)
        #self.draw.line((end_x+5,end_y-5,end_x,end_y), fill=128, width=2)       

    def visualize(self):
        self.image.show()


network = Network()
#network.add_layer_y()
#network.add_layer_y()
network.add_node(layer=(1,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
#network.get_node_coordinates(1,1)
network.add_node(layer=(1,2), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(2,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(2,2), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(2,3), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(3,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.connect((1,1),(2,1))
network.connect((1,1),(2,2))
network.connect((2,2),(3,1))
network.connect((2,1),(3,1))
#network.add_node(layer=(4,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))

network.visualize()

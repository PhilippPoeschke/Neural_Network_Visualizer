#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from node import node

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
        self.image = Image.new("RGB", (300, 100), color="white")
        self.image_width, self.image_height = self.image.size
    
    def add_layer(self):
        self.layer = Image.new("RGB", (self.image_width, self.image_height), color="white")
        dst = Image.new('RGB', (min(self.image.width, self.layer.width), self.image.height + self.layer.height))
        dst.paste(self.image, (0,0))
        dst.paste(self.layer, (0, self.image.height))
        self.image = dst

    def add_node(self, layer, node):
        self.add_layer()
        width , height = self.image.size
        pos_x = layer[0]
        pos_y = layer[1]
        node_in = node.rectangle
        node_width, node_height = node_in.size

        # Defining the x and y coordinate of every node
        node_y = int(((pos_x-1)*self.image_height*0.5)) + int((height-node_height) * 0.5)
        node_x = int((width-node_width) * 0.5)
        #self.add_layer()
        self.image.paste(node_in, (node_x,node_y))   

    def connect(self, start, end):
        ax = plt.axes()
        ax.arrow(start, end, length_includes_head=True ,head_width=0.05, head_length=0.05, fc='k', ec='k')

    def visualize(self):
        self.image.show()


network = Network()
network.add_node(layer=(1,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(2,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(3,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))
network.add_node(layer=(4,1), node=node(node_name="layer1", input_nodes="10", output_nodes="10"))

network.visualize()

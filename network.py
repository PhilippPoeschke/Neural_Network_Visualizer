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
        self.image = Image.new("RGB", (1000, 200), color="white")

    def add(self, im1, im2):
        dst = Image.new('RGB', (min(im1.width, im2.width), im1.height + im2.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst
    
    def add_layer(self):
        self.layer = Image.new("RGB", (1000, 200), color="white")
        dst = Image.new('RGB', (min(self.image.width, self.layer.width), self.image.height + self.layer.height))
        dst.paste(self.image, (0,0))
        dst.paste(self.layer, (0, self.image.height))
        self.image = dst

    def connect(self, start, end):
        ax = plt.axes()
        ax.arrow(start, end, length_includes_head=True ,head_width=0.05, head_length=0.05, fc='k', ec='k')

    def visualize(self):
        self.image.show()


'''
Network = Image.new("RGB", (1000, 200), color="white")
net = node(node_name="layer1", input_nodes="10", output_nodes="10")
draw = ImageDraw.Draw(Network)
Network.show()

'''
im1 = Network()
#im3 = Image.open('basic_shape.png')
im2 = node(node_name="layer1", input_nodes="10", output_nodes="10")
#im2.rectangle.show()
im1.image.paste(im2.rectangle, (0,0))
im1.image.show()

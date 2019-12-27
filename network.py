#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from node import node



class Network():

    def __init__(self):
        self.Image.new("RGB", (1000, 200), color="white")

    def add(self):
        self.node(node_name="layer1", input_nodes="10", output_nodes="10")

    def connect(self, start, end):
        ax = plt.axes()
        ax.arrow(start, end, length_includes_head=True ,head_width=0.05, head_length=0.05, fc='k', ec='k')
    
    
'''
Network = Image.new("RGB", (1000, 200), color="white")
net = node(node_name="layer1", input_nodes="10", output_nodes="10")
draw = ImageDraw.Draw(Network)
Network.ps
Network.show()
'''
im1 = Image.new("RGB", (1000, 200), color="white")
im3 = Image.open('basic_shape.png')
#im2 = node(node_name="layer1", input_nodes="10", output_nodes="10")

im1.paste(im3)
im1.show()
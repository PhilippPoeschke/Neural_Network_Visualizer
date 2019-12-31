#!/usr/bin/python3

from PIL import Image, ImageDraw
from neuron import neuron

class layer():

    def __init__(self):
        # initially creating the network grid layer
        self.image = Image.new("RGB", (100, 300), color="white")
        self.image_width, self.image_height = self.image.size

        # defining global variables for the add_node_.. function
        self.layer_x_counter = 1
        self.layer_y_counter = 0

    def add_layer(self):
        # adds a layer in the y achsis
        self.layer = Image.new("RGB", (self.image_width, self.image_height), color="white")
        dst = Image.new('RGB', (max(self.image.width, self.layer.width), self.image.height + self.layer.height), color="white")
        dst.paste(self.image, (0,0))
        dst.paste(self.layer, (0, self.image.height))
        self.image = dst
    
    def add_neuron(self, neuron=neuron(), x=0, y=0):
        neuron_in = neuron.circle
        xn,yn = neuron.get_neuron_coordinates()
                
        #x = int(self.image_width*0.5)
        #y = int(self.image_height*0.5)
        x_e = x
        y_e = y
        self.image.paste(neuron_in, (x_e,y_e))
        print("x_e:", x_e)

    def add_neurons(self, layer, count, neuron=neuron()):
        # Defining local variables for calculation
        border = 25
        height = self.image_height - (2 * border)
        width = self.image_width
        parts = height/(count+1)
        print("parts: ", parts)
        # Defining the x coordinate 
        # the neurons are centered in every layer
        xn, yn = neuron.get_neuron_coordinates()
        neurons_x_coordinate = int(int(self.image_width*0.5) - xn + (layer-1) * int(self.image_width*0.5))
        
        for number in range(count):
            # Let the count start at one
            number = number+1
            neurons_y_coordinate = int(border + number * parts) - yn
            self.add_neuron(x=neurons_x_coordinate, y=neurons_y_coordinate)
            print("neurons_y:", neurons_y_coordinate)
            print("neurons_x:", neurons_x_coordinate)

    def visualize(self):
        self.image.show()

neuralnet = layer()
neuralnet.add_neurons(layer=1,count=3)
neuralnet.visualize()
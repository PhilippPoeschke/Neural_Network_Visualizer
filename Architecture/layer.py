#!/usr/bin/python3

from PIL import Image, ImageDraw
from neuron import neuron

class layer():

    def __init__(self):
        # initially creating the network grid layer
        self.image = Image.new("RGB", (100, 800), color="white")
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

    def add_layer_x(self):
        # adds a layer in the x achsis
        self.layer = Image.new("RGB", (self.image_width, self.image_height), color="white")
        dst = Image.new('RGB', (self.image.width + self.layer.width, max(self.image.height , self.layer.height)), color="white")
        dst.paste(self.image, (0,0))
        dst.paste(self.layer, (self.image.width, 0))
        self.image = dst
    
    def add_neuron(self, neuron=neuron(), x=0, y=0):
        # add a neuron in the place of x and y coordinate
        neuron_in = neuron.circle      
        self.image.paste(neuron_in, (x,y))

    def add_neurons(self, layer, count, neuron=neuron()):
        # Defining local variables for calculation
        if count > 2:
            self.add_layer_x()
        border = 25
        height = self.image_height - (2 * border)
        width = self.image_width
        parts = height/(count+1)

        # Defining the x coordinate 
        # the neurons are centered in every layer
        xn, yn = neuron.get_neuron_coordinates()
        neurons_x_coordinate = int(int(self.image_width*0.5) - xn + (layer-1) * int(self.image_width))
        
        # adding a neuron for the number defined by count
        for number in range(count):
            # Let the count start at one
            number = number+1
            neurons_y_coordinate = int(border + number * parts) - yn
            self.add_neuron(x=neurons_x_coordinate, y=neurons_y_coordinate)
        
    def model(self, list=[1,1]):
        for layer_number, number_of_nodes in enumerate(list):
            layer_number = layer_number + 1
            self.add_neurons(layer=layer_number, count=number_of_nodes)
            print(layer_number+1, number_of_nodes)

    def visualize(self):
        self.image.show()

neuralnet = layer()


neuralnet.model([1,5,8,4,6,2])

neuralnet.visualize()
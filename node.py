#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont

class node():

    def __init__(self, node_name="dense_1", input_nodes="2", output_nodes="2"):
        self.initialize()
        self.set_font()
        self.add_block()
        self.add_text(block_name=node_name ,input_shape=input_nodes, output_shape=output_nodes)
    
    def initialize(self, x=600, y=100):
        # IMAGE SIZE
        self.rectangle = Image.new("RGB", (500, 100), color="white")
        self.draw = ImageDraw.Draw(self.rectangle)
        self.width, self.height = self.rectangle.size

        # width parts
        self.width_half = self.width*0.5
        self.width_three_quater = self.width*0.75
        self.width_full = self.width

        # height parts
        self.height_quater = self.height*0.25
        self.height_half = self.height*0.5
        self.height_three_quater = self.height*0.75
        self.height_full = self.height

        # border to rectangle
        self.border = 20

    def set_font(self, font_size=20, font_family="Courier_Prime.ttf"):
        # FONT
        self.font_family = font_family
        self.font_size = font_size
        self.font = ImageFont.truetype(self.font_family, self.font_size)

        # text parts
        self.text_size_half = self.font_size*0.5
        
    def add_block(self):
        #  ------------------------------------
        # |             |rect_two   |rect_four |
        # |  rect_one   |-----------|----------|
        # |             |rect_three |rect_five |
        #  ------------------------------------
        # create rectangles
        rect_one = self.draw.rectangle((0, 0, self.width_half, self.height-1), None, "black")
        rect_two = self.draw.rectangle((self.width_half, 0, self.width_three_quater, self.height_half), None, "black")
        rect_three = self.draw.rectangle((self.width_half, self.height_half, self.width_three_quater, self.height-1), None, "black")
        rect_four = self.draw.rectangle((self.width_three_quater, 0, self.width_full-1, self.height_half), None, "black")
        rect_five = self.draw.rectangle((self.width_three_quater, self.height_half, self.width_full-1, self.height_full-1), None, "black")

    def add_text(self, block_name="dense_1", input_shape="(None)", output_shape="(None)"):
        #  ------------------------------------
        # |             |text_two   |text_four |
        # |  text_one   |-----------|----------|
        # |             |text_three |text_five |
        #  ------------------------------------
        # create text
        text_one = self.draw.text((self.border, self.height_half-self.text_size_half), block_name, font=self.font, fill="black")
        text_two = self.draw.text((self.border+self.width_half, self.height_quater-self.text_size_half), "input:", font=self.font, fill="black")
        text_three = self.draw.text((self.border+self.width_half, self.height_three_quater-self.text_size_half), "output:", font=self.font, fill="black")
        text_four = self.draw.text((self.border+self.width_three_quater, self.height_quater-self.text_size_half), input_shape, font=self.font, fill="black")
        text_five = self.draw.text((self.border+self.width_three_quater, self.height_three_quater-self.text_size_half), output_shape, font=self.font, fill="black")

    def visualize(self):
        # visualize
        self.rectangle.show()

    def save(self):
        # save as png
        self.rectangle.save("basic_shape.png")

#net = node(node_name="layer1", input_nodes="10", output_nodes="10")
#net.visualize()
from PIL import Image, ImageDraw, ImageFont

# FONT
font_family = "Courier_Prime.ttf"
font_size = 20
font = ImageFont.truetype(font_family, font_size)

# IMAGE SIZE
rectangle = Image.new("RGB", (600, 100), color="white")
draw = ImageDraw.Draw(rectangle)
width, height = rectangle.size

# width parts
width_half = width*0.5
width_three_quater = width*0.75
width_full = width

# height parts
height_quater = height*0.25
height_half = height*0.5
height_three_quater = height*0.75
height_full = height

# text parts
text_size_half = font_size*0.5
border = 20

#  ------------------------------------
# |             |rect_two   |rect_four |
# |  rect_one   |-----------|----------|
# |             |rect_three |rect_five |
#  ------------------------------------

# create rectangles
rect_one = draw.rectangle((0, 0, width_half, height-1), None, "black")
rect_two = draw.rectangle((width_half, 0, width_three_quater, height_half), None, "black")
rect_three = draw.rectangle((width_half, height_half, width_three_quater, height-1), None, "black")
rect_four = draw.rectangle((width_three_quater, 0, width_full-1, height_half), None, "black")
rect_five = draw.rectangle((width_three_quater, height_half, width_full-1, height_full-1), None, "black")

#  ------------------------------------
# |             |text_two   |text_four |
# |  text_one   |-----------|----------|
# |             |text_three |text_five |
#  ------------------------------------

# create text
text_one = draw.text((border, height_half-text_size_half), "dense_1: Dense", font=font, fill="black")
text_two = draw.text((border+width_half, height_quater-text_size_half), "input:", font=font, fill="black")
text_three = draw.text((border+width_half, height_three_quater-text_size_half), "output:", font=font, fill="black")
text_four = draw.text((border+width_three_quater, height_quater-text_size_half), "(None, 10)", font=font, fill="black")
text_five = draw.text((border+width_three_quater,height_three_quater-text_size_half), "(None, 10)", font=font, fill="black")

# visualize
rectangle.show()
rectangle.save("basic_shape.png")
import time

import epaper
from PIL import Image, ImageDraw, ImageFont

epd = epaper.epaper('epd2in13b_V3').EPD()
epd.init()
epd.Clear()
time.sleep(1)

font = ImageFont.truetype('digital-7.ttf', 110)

# Set image buffer for drawing
image_black = Image.new('1', (250, 122), 255).transpose(Image.ROTATE_90)
image_red = Image.new('1', (250, 122), 255).transpose(Image.ROTATE_90)

# Create an image object
draw_black = ImageDraw.Draw(image_black)
draw_red = ImageDraw.Draw(image_red)

draw_red.text((10, 15), '0', font=font, fill=0)
draw_red.text((65, 15), '0', font=font, fill=0)
draw_black.text((115, 15), ':', font=font, fill=0)
draw_red.text((135, 15), '0', font=font, fill=0)
draw_red.text((190, 15), '0', font=font, fill=0)

epd.display(epd.getbuffer(image_black), epd.getbuffer(image_red))

epd.sleep()

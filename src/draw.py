# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def draw(word1, word2, word3):
    asset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'asset')
    font_path = os.path.join(asset_dir, 'BarcelonaITCStd-Medium.otf')
    heart_path = os.path.join(asset_dir, 'heart.png')

    heart = Image.open(heart_path)
    canvas_size = tuple(map(lambda x: x * 2, heart.size))
    canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))
    txt = Image.new("RGBA", canvas_size, (255, 255, 255, 0))
    
    font_color = '#212121'

    # Resize heart Image
    # heart = heart.resize((int(canvas_box[0]/2), int(canvas_box[0]/2)))

    # Put heart into canvas
    canvas.paste(heart, (heart.size[0] - 150, 10))
    # New txt draw
    draw = ImageDraw.Draw(txt)
    font = ImageFont.truetype(font_path, int(heart.size[1] * 1.33))

    # Draw text
    draw.text((heart.size[0] / 4 + 100, 50), word1, font=font, fill=font_color)
    draw.text((heart.size[0] / 4, heart.size[1] + 50), word2, font=font, fill=font_color)
    draw.text((heart.size[0] + 20, heart.size[1] + 50), word3, font=font, fill=font_color)

    # Combine layers
    out = trim(Image.alpha_composite(canvas, txt))
    out.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static', word1 + word2 + word3 + '.jpg'), format="JPEG")
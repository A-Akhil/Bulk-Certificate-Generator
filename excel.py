import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import os

# Locate your font
FONT_NAME = "/usr/share/fonts/TTF/times.ttf"
FONT_SIZE = 80
FONT_COLOR = "#000000"

def make_certificates(df, name_column, template_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    names = df[name_column].tolist()
    font = ImageFont.truetype(FONT_NAME, FONT_SIZE)

    for name in names:
        name = str(name).upper()  # Change all names to capital letters

        template = Image.open(template_file)
        width, height = template.size

        image_source = template.copy()
        draw = ImageDraw.Draw(image_source)

        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Adjust the vertical position of the text
        vertical_offset = -60  # Increase the offset to move the text higher up
        draw.text(((width - text_width) / 2, (height - text_height) / 2 + vertical_offset), name, fill=FONT_COLOR, font=font)

        output_file = os.path.join(output_dir, name + ".png")
        image_source.save(output_file)
        print('Saving Certificate for:', name)

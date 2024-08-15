import pandas as pd
from PIL import Image, ImageFont, ImageDraw
import os
import matplotlib.font_manager as fm  # For cross-platform font management

FONT_COLOR = "#000000"

def make_certificates(df, name_column, template_file, output_dir, vertical_offset, horizontal_offset, font_size, font_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    names = df[name_column].tolist()
    font = ImageFont.truetype(font_path, font_size)

    for name in names:
        name = str(name).upper()  # Change all names to capital letters

        template = Image.open(template_file)
        width, height = template.size

        image_source = template.copy()
        draw = ImageDraw.Draw(image_source)

        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Apply the user-defined vertical and horizontal offsets
        draw.text(((width - text_width) / 2 + horizontal_offset, (height - text_height) / 2 + vertical_offset), name,
                  fill=FONT_COLOR, font=font)

        output_file = os.path.join(output_dir, f"{name}.png")

        try:
            image_source.save(output_file)
            print('Saving Certificate for:', name)
        except Exception as e:
            print(f"Error saving {output_file}: {e}")

    # Delete the temporary file if it exists
    if os.path.exists(template_file):
        os.remove(template_file)
        print(f"Deleted temporary file: {template_file}")

def preview_certificate(template_file, name, vertical_offset, horizontal_offset, font_size, font_path):
    font = ImageFont.truetype(font_path, font_size)
    name = str(name).upper()

    template = Image.open(template_file)
    width, height = template.size

    image_source = template.copy()
    draw = ImageDraw.Draw(image_source)

    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Apply the user-defined vertical and horizontal offsets
    draw.text(((width - text_width) / 2 + horizontal_offset, (height - text_height) / 2 + vertical_offset), name,
              fill=FONT_COLOR, font=font)

    return image_source

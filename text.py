from PIL import Image, ImageFont, ImageDraw
import os

FONT_COLOR = "#000000"

def make_certificates_txt(file_path, template_file, output_dir, vertical_offset, horizontal_offset, font_size, font_path):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(template_file):
        print(f"Template file not found: {template_file}")
        return

    with open(file_path, "r") as file:
        names = file.read().splitlines()

    font = ImageFont.truetype(font_path, font_size)

    for name in names:
        name = str(name).strip().upper()  # Change all names to capital letters and remove extra spaces

        if not name:
            print("Skipped empty name")
            continue

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

        # Ensure the file extension is correct
        if not output_file.lower().endswith('.png'):
            output_file += '.png'

        try:
            image_source.save(output_file)
            print('Saving Certificate for:', name)
        except Exception as e:
            print(f"Error saving {output_file}: {e}")

    # Delete the template file after processing all names
    if os.path.exists(template_file):
        os.remove(template_file)
        print(f"Deleted template file: {template_file}")
    else:
        print(f"Template file already deleted or not found: {template_file}")

    # Delete the temp_file.txt after processing
    temp_file = "temp_file.txt"  # Ensure this matches the actual temp file path
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"Deleted temporary file: {temp_file}")
    else:
        print(f"Temporary file already deleted or not found: {temp_file}")

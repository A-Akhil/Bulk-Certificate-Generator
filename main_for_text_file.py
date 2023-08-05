from PIL import Image, ImageFont, ImageDraw

#make sure you have the right font
FONT_FILE = ImageFont.truetype(r'font/georgia.ttf', 180)
FONT_COLOR = "#000000"
TEMPLATE_FILE = "temp.png"
OUTPUT_DIR = "./out/"



def make_certificates(name):
    template = Image.open(TEMPLATE_FILE)
    width, height = template.size

    image_source = template.copy()
    draw = ImageDraw.Draw(image_source)

    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    draw.text(((width - name_width) / 2, (height - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    output_file = OUTPUT_DIR + name + ".png"
    image_source.save(output_file)
    print('Saving :', name)

if __name__ == "__main__":
    #make sure you change the file.txt with your file name
    with open("file.txt", "r") as file:
        names = file.read().splitlines()

    for name in names:
        make_certificates(name)

    print(len(names), "Finished generating certificates.")


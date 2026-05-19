from PIL import Image, ImageDraw, ImageFont

card = Image.open("dr.jpg")
draw = ImageDraw.Draw(card)

name = input("Введите имя того, кого хотите поздравить: ")
text_to_print = f"{name}, поздравляю!"

font = ImageFont.truetype("C:\\Windows\\Fonts\\Red October-Regular.ttf", 40)

width, height = card.size

x_position = width / 2

y_position = 700

draw.text(
    (x_position, y_position),
    text_to_print,
    fill=(230, 0, 0),
    font=font,
    anchor="mt"
)

card.save("final_congratulation.png", "PNG")

card.show()
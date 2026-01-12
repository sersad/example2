from PIL import Image, ImageDraw


name = "wolf.png"
color = input()
size = int(input())
# color = "#ABE1F7"
wolf_color = "#D1D1D1"
outline_color = "#595959"
wolf2_color = "#595959"
# size = 20
size_width = size // 20
width = 19 * size
height = 18 * size


im = Image.new("RGB", (width, height), color)
dw = ImageDraw.Draw(im)

dw.ellipse((1 * size, 4 * size, 3 * size, 6 * size), fill=wolf2_color, outline=outline_color,
           width=size_width)

dw.rectangle([(2 * size, 5 * size), (8 * size, 9 * size)], fill=wolf_color, outline=outline_color,
           width=size_width)

dw.ellipse((7 * size, 2 * size, 18 * size, 13 * size), fill=wolf_color, outline=outline_color,
           width=size_width)

dw.ellipse((9 * size, 6 * size, 11 * size, 8 * size), fill="white", outline=outline_color,
           width=size_width)
dw.ellipse((9 * size, 6.5 * size, 10 * size, 7.5 * size), fill="black", outline=outline_color,
           width=size_width)

im.save(name)

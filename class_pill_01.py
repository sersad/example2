from PIL import Image  # Обратите внимание, что не Pillow, а PIL

im = Image.open("image.jpg")  # Открываем картинку
pixels = im.load()  # Список с пикселями
x, y = im.size  # Ширина (x) и высота (y) изображения

sum_red = sum_green = sum_blue = 0

# Проходимся по всем пикселям картинки
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]  # Странная индексация O_o
        sum_red += r
        sum_green += g
        sum_blue += b

print(f"R: {sum_red}\nG: {sum_green}\nB: {sum_blue}")

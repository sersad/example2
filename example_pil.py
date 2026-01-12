from PIL import Image, ImageDraw

file_name = 'test.jpg'
width = height = 1000
sky_color = '#75BBFD'
asphalt_color = '#4E5452'
car_color = '#bF311A'
wheels_color = '#000000'
sun_color = '#FFDB00'

im = Image.new("RGB", (width, height))
drawer = ImageDraw.Draw(im)

# Небо
drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
# Земля
drawer.rectangle(((0, int(height * 0.8)), (width, height)),
                 asphalt_color)
# Солнце
# Можно смело рисовать целый круг; если что-то выходит за пределы картинки при рисовании — просто потеряется
drawer.ellipse((
    (int(0.8 * width), -int(0.2 * height)),
    (int(1.2 * width), int(0.2 * height))),
    sun_color)
# Машина
drawer.polygon(((int(0.2 * width), int(height * 0.85)),
                (int(0.2 * width), int(height * 0.7)),
                (int(0.3 * width), int(height * 0.6)),
                (int(0.55 * width), int(height * 0.6)),
                (int(0.65 * width), int(height * 0.7)),
                (int(0.8 * width), int(height * 0.7)),
                (int(0.8 * width), int(height * 0.85))),
               car_color)
# Колёса
for i in range(2):
    drawer.ellipse(((int(0.3 * width) + int(0.3 * width) * i,
                     int(0.8 * height)),
                    (int(0.4 * width) + int(0.3 * width) * i,
                     int(0.9 * height))),
                   wheels_color)
im.save(file_name)
# im.show()
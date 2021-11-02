from PIL import Image

TYPE = ".png"
PATH_IN = "../img/presale/"
PATH_OUT = "../img/presale-pixel/"
AMOUNT = 100
PIXEL_SIZE = [24, 24]
FULL_SIZE = [960, 960]

for n in range(1, AMOUNT+1):
    with Image.open(PATH_IN + str(n) + TYPE) as img:
        img = img.resize(PIXEL_SIZE)
        img = img.resize(FULL_SIZE,  Image.BOX)
        img.save(PATH_OUT + str(n) + TYPE)
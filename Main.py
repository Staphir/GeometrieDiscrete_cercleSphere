import cercle_brute_force
import cercle_analytique

from PIL import Image

img_width = 1000
img_height = 1000


def drawImage(list_coords_pixels):
    # création image

    WHITE = (255, 255, 255, 0)
    image = Image.new('RGBA', (img_width, img_height), WHITE)

    # parcours des coordonnées des pixels à dessiner
    for coord_pixel in list_coords_pixels:
        image.putpixel(coord_pixel, (0,0,0))

    # affichage image
    image.show()

if __name__ == "__main__":
    # affichage cercle brute force (rayon du cercle, img_width, img_height)
    drawImage(cercle_analytique.createCercle(200, img_width, img_height))

    # affichage cercle analytique
    # drawImage(cercle_analytique.createCercle())


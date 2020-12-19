import cercle_brute_force
import cercle_analytique
import hypersphere
import sphere_brute_force

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

rayon = 20
img_width = 50
img_height = 50
img_deep = 50

def draw3DImage(list_coords_pixels):
    voxels = [[[False for _ in range(img_deep)] for _ in range(img_height)] for _ in range(img_width)]

    for i in list_coords_pixels:
        voxels[i[1]][i[0]][i[2]] = True

    voxels = np.array(voxels) #numpy array de true et false

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors='yellow')

    plt.show()

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
    # drawImage(cercle_brute_force.createCercle(rayon, img_width, img_height))

    # affichage cercle analytique
    # drawImage(cercle_analytique.createCercle(rayon, img_width, img_height))

    # affichage sphere analytique
    # draw3DImage(hypersphere.createHypersphere(rayon, img_width, img_height, img_deep))

    # affichage sphere analytique
    draw3DImage(sphere_brute_force.createSphere(rayon, img_width, img_height, img_deep))


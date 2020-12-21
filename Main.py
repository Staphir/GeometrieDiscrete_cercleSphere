import cercle_brute_force
import cercle_analytique
import hypersphere
import sphere_brute_force

from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

radius = 12
img_size = 30
img_deep = 30

def draw3DImage(list_coords_pixels):
    # print(list_coords_pixels)
    voxels = [[[False for _ in range(img_deep)] for _ in range(img_size)] for _ in range(img_size)]

    for i in list_coords_pixels:
        voxels[i[0]][i[1]][i[2]] = True

    voxels = np.array(voxels) #numpy array de true et false

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors='yellow')

    plt.show()

def drawImage(list_coords_pixels):
    # création image

    WHITE = (255, 255, 255, 0)
    image = Image.new('RGBA', (img_size, img_size), WHITE)

    # parcours des coordonnées des pixels à dessiner
    for coord_pixel in list_coords_pixels:
        image.putpixel(coord_pixel, (0,0,0))

    # affichage image
    image.show()

if __name__ == "__main__":
    stroke_width = 1
    cmd = ''
    while(cmd != 'q'):
        cmd = input(
        "circle command :\n"
        "\tb: brute force\n"
        "\ta: analytique\n"
        "\ts: sphere\n"
        "q: quit application\n"
        "r: change radius\n"
        "c: change stroke width\n"
        "i: change image size\n"
        "d: change image deepness\n>> ")
        if(cmd == 'b'):
            # affichage cercle brute force (rayon du cercle, img_size, stroke_width)
            drawImage(cercle_brute_force.createCercle(radius, img_size, stroke_width))

        if(cmd == 'a'):
            # affichage cercle analytique
            drawImage(cercle_analytique.createCercle(radius, img_size, stroke_width))
    
        if(cmd == 's'):
            # affichage sphere analytique
            draw3DImage(sphere_brute_force.createSphere(radius, img_size, img_deep))

        if(cmd == 'c'):
            param = int(input("stroke width (>= 1): "))
            stroke_width = param if param and param >= 1 else 1

        if(cmd == 'r'):
            param = int(input("radius (> 10): "))
            radius = param if param and param > 10 else 12

        if(cmd == 'i'):
            param = int(input("size (>= 30): "))
            img_size = param if param and param >= 30 else 30
        
        if(cmd == 'd'):
            param = int(input("deepness (> 1): "))
            img_deep = param if param and param > 1 else 1

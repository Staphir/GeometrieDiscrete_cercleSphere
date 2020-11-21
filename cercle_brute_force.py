def getPixelsOctantEstSud(circle_ray, img_width, img_height):
    # position de départ (centre droite du cercle)
    x_c = (int)(img_width / 2 + 1/2)
    y_c = (int)(img_height / 2 + 1/2)
    circle_pixels = [(x_c + circle_ray, y_c)]

    return circle_pixels

def completeCircle(octant_est_sud, circle_ray):
    octant_sud_est = []
    octant_sud_est.append(octant_est_sud[0])

    for coord in octant_est_sud:
        new_coord = (coord[1], coord[0])
        octant_sud_est.append(new_coord)

    quart_sud_est = octant_est_sud + octant_sud_est

    # -----------------------------

    pos_center = (quart_sud_est[0][0] - circle_ray, quart_sud_est[0][1] - circle_ray)

    quart_sud_ouest = []

    for coord in quart_sud_est:
        new_coord = (coord[0] - (coord[0] - pos_center[0]) * 2, coord[1])
        quart_sud_ouest.append(new_coord)

    # -----------------------------

    quart_nord_est = []

    for coord in quart_sud_ouest:
        new_coord = (coord[1] , coord[0])
        quart_nord_est.append(new_coord)

    # -----------------------------

    quart_nord_ouest = []

    for coord in quart_nord_est:
        new_coord = (coord[0] - (coord[0] - pos_center[0]) * 2, coord[1])
        quart_nord_ouest.append(new_coord)

    # -----------------------------

    return  quart_sud_est + quart_sud_ouest + quart_nord_est + quart_nord_ouest


def createCercle(circle_ray, img_width, img_height):
    octant_est_sud = getPixelsOctantEstSud(circle_ray, img_width, img_height)

    list_coords_pixels = completeCircle(octant_est_sud, circle_ray)

    # return octant_est_sud
    return list_coords_pixels
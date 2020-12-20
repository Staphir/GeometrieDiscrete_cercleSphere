from math import sqrt


def getPixelsOctantEstSud(circle_ray, img_width, img_height, stroke_width):
    # position de départ (centre droite du cercle)
    x_c = (int)(img_width / 2 + 1/2)
    y_c = (int)(img_height / 2 + 1/2)

    all_points = []
    for i in range(stroke_width):
        circle_ray_i = circle_ray + i
        circle_pixels = [(x_c + circle_ray_i, y_c)]
        y = y_c
        while y != (int)(y_c + (int)((sqrt(2)/2)+1/2) * circle_ray_i + 1/2):

            c_x = (circle_pixels[-1][0] - x_c) * (circle_pixels[-1][0] - x_c)
            c_x_1 = (circle_pixels[-1][0] - 1 - x_c) * (circle_pixels[-1][0] - 1 - x_c)

            c_y = (y - y_c) * (y - y_c)
            c_y_1 = (y - y_c + 1) * (y - y_c + 1)

            r2 = (int)(circle_ray_i * circle_ray_i + 1/2)
            r2_1 = (int)((circle_ray_i + 1) * (circle_ray_i + 1) +1/2)

            var_x_1 = (int)(c_x_1 + c_y + 1/2)
            var_y_1 = (int)(c_x + c_y_1 + 1/2)

            if r2 <= var_y_1 and var_y_1 < r2_1 :
                circle_pixels.append((circle_pixels[-1][0], y + 1))
                y += 1
            elif r2 <= var_x_1 and var_x_1 < r2_1:
                circle_pixels.append((circle_pixels[-1][0] - 1, y))
            else :
                circle_pixels.append((circle_pixels[-1][0] - 1, y + 1))
                y += 1
        all_points = all_points + circle_pixels
    return all_points


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

def createCercle(circle_ray, img_width, img_height, stroke_width):
    octant_est_sud = getPixelsOctantEstSud(circle_ray, img_width, img_height, stroke_width)

    list_coords_pixels = completeCircle(octant_est_sud, circle_ray)

    # return octant_est_sud
    return list_coords_pixels
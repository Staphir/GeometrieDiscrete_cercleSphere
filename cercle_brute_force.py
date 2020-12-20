def createCercle(circle_ray, img_width, img_height, stroke_width):
    list_coords_pixels = list(tuple())

    x_c = (int)(img_width / 2 + 1/2)
    y_c = (int)(img_height / 2 + 1/2)
    r2 = (int)(circle_ray * circle_ray + 1 / 2)

    r2_1 = (int)((circle_ray + stroke_width) * (circle_ray + stroke_width) + 1 / 2)

    for x in range(img_width):
        for y in range(img_height):
            pos = (int)((x - x_c)*(x - x_c) + (y - y_c)*(y - y_c) + 1/2)
            if r2 <= pos and pos < r2_1:
                list_coords_pixels.append((x,y))

    return list_coords_pixels

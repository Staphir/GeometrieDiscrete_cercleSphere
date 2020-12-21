# renvoie les cordonnées des points compris entre le rayon et rayon + stroke width
# appartenant à la sphere en parcourant tous les points de l'image
def createSphere(sphere_ray, img_size, img_deep, stroke_width):
    list_coord_pixels_sphere = []

    sphere_ray_2 = sphere_ray * sphere_ray
    sphere_ray_2_1 = (sphere_ray+stroke_width) * (sphere_ray+stroke_width)

    x_c = int(img_size / 2 + 1 / 2)
    y_c = int(img_size / 2 + 1 / 2)
    z_c = int(img_deep / 2 + 1 / 2)

    for x in range(img_size):
        for y in range(img_size):
            for z in range(img_deep):

                pos = int((x - x_c) * (x - x_c) +
                          (y - y_c) * (y - y_c) +
                          (z - z_c) * (z - z_c) + 1 / 2)

                if sphere_ray_2 <= pos < sphere_ray_2_1:
                    list_coord_pixels_sphere.append((x,y,z))

    return list_coord_pixels_sphere
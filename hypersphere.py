import cercle_analytique

def newZ(z, ray_t, hyper_sphere_ray, img_width, img_deep):
    r2 = (int) (hyper_sphere_ray * hyper_sphere_ray +1/2)
    r2_1 = (int) ((hyper_sphere_ray+1) * (hyper_sphere_ray+1) +1/2)

    c_x = ray_t*ray_t
    c_x_1 = (ray_t + 1) * (ray_t + 1)

    c_z = z*z
    c_z_1 = (z + 1) * (z + 1)

    var_x_1 = (int)(c_z + c_x_1 + 1/2)
    var_z_1 = (int)(c_x + c_z_1 + 1/2)

    if r2 <= var_z_1 and var_z_1 < r2_1:
        return 1
    elif r2 <= var_x_1 and var_x_1 < r2_1:
        return 0
    else:
        return 1

def coords2DTo3D(z, pixels_cercle_2D):
    pixels_cercle_3D = []

    for coord in pixels_cercle_2D:
        coord_3D = (coord[0],coord[1],z)
        pixels_cercle_3D.append(coord_3D)

    return pixels_cercle_3D

def createHypersphere(hyper_sphere_ray, img_width, img_height, img_deep):
    list_coord_pixels_sphere = []

    z = 0
    ray_t = hyper_sphere_ray

    while ray_t != - 1:
        list_coord_pixels_cercle = cercle_analytique.createCercle(ray_t, img_width, img_height)
        list_coord_pixels_sphere += coords2DTo3D(hyper_sphere_ray - z, list_coord_pixels_cercle)

        list_coord_pixels_cercle = cercle_analytique.createCercle(ray_t, img_width, img_height)
        list_coord_pixels_sphere += coords2DTo3D(hyper_sphere_ray + z, list_coord_pixels_cercle)

        ray_t -= newZ(z, ray_t, hyper_sphere_ray, img_width, img_deep)
        z += 1

    return list_coord_pixels_sphere
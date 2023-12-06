def grid_to_pixel(grid_pos, zone_width, zone_height):
    pixel_x = grid_pos[0] * zone_width
    pixel_y = grid_pos[1] * zone_height
    return pixel_x, pixel_y

def pixel_to_grid(pixel_pos, zone_width, zone_height):
    grid_x = pixel_pos[0] // zone_width
    grid_y = pixel_pos[1] // zone_height
    return grid_x, grid_y
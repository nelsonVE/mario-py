from PIL import Image
from io import BytesIO
import constants

def get_tile(tile_set_number, tile_x, tile_y, tilesize_x=None, tilesize_y=None):
    tile_set = Image.open(f"./tiles/{tile_set_number}.png")
    width, height = tile_set.size
    tilesize_x = tilesize_x if tilesize_x else constants.TILE_SIZE
    tilesize_y = tilesize_y if tilesize_y else constants.TILE_SIZE
    x_initial = ((tile_x - 1) * tilesize_x)
    x_final = tile_x * tilesize_x
    y_initial = ((tile_y - 1) * tilesize_y)
    y_final = tile_y * tilesize_y
    bytes = BytesIO()
    print((x_initial, y_initial, x_final, y_final))
    tile_image = tile_set.crop((x_initial, y_initial, x_final, y_final))

    return (tile_image.tobytes(), tile_image.size, tile_image.mode)
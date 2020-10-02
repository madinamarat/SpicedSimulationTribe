from PIL import Image
import cv2
import numpy as np
import random

img = Image.open('./img/tiles.png')
market = np.array(img)


def rgba_to_rgb(img):
    img_array = np.array(img)
    img_array_new = img_array[:, :, :3]
    return Image.fromarray(img_array_new)


def bgr_to_rgb(img):
    img_array = np.array(img)
    new_arr = img_array.copy()
    new_arr[:, :, 0] = img_array[:, :, 2]
    new_arr[:, :, 2] = img_array[:, :, 0]
    return Image.fromarray(new_arr)

# fish1 = Image.fromarray(market[4 * 32:4 * 32+32, 15 * 32:15 * 32+32])
# fish2 = Image.fromarray(market[5 * 32:5 * 32+32, 15 * 32:15 * 32+32])
# fish3 = Image.fromarray(market[6 * 32:6 * 32+32, 15 * 32:15 * 32+32])
# fish4 = Image.fromarray(market[7 * 32:7 * 32+32, 15 * 32:15 * 32+32])


ghost = Image.fromarray(market[7 * 32:7 * 32+32, 0 * 32:0 * 32+32])

pc = Image.open('./img/pm2.png')
pc_array = np.array(pc)
pc_array_new = pc_array[:, :, :3]
pc_new = bgr_to_rgb(Image.fromarray(pc_array_new))


ghost1 = bgr_to_rgb(rgba_to_rgb(Image.open('./img/ghost4.png')))
ghost2 = bgr_to_rgb(rgba_to_rgb(Image.open('./img/ghost6.png')))
ghost3 = bgr_to_rgb(rgba_to_rgb(Image.open('./img/ghost7.png')))


pac_right = pc_new
pac_left = Image.fromarray(np.fliplr(pc_new))
pac_down = pc_new.rotate(270)
pac_up = pc_new.rotate(90)


pacmans = [pac_right, pac_left, pac_down, pac_up]
# ghosts = [Image.fromarray(np.array(img)[:, :, :3])
#           for img in [ghost1, ghost2, ghost3]]

ghosts = [ghost1, ghost2, ghost3]


imgs_use = pacmans + ghosts
# imgs_rgb = []


def get_random_ghost():
    return random.choice(ghosts)


def get_random_image():
    icon = random.choice(['ghost', 'pacman'])
    if icon == 'ghost':
        return {'type': 'ghost',
                'icon': get_random_ghost()}
    else:
        return {'type': 'pacman',
                'icon': pac_up}

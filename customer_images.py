from PIL import Image
import numpy as np
import random

img = Image.open('./img/tiles.png')
market = np.array(img)

fish1 = Image.fromarray(market[4 * 32:4 * 32+32, 15 * 32:15 * 32+32])
fish2 = Image.fromarray(market[5 * 32:5 * 32+32, 15 * 32:15 * 32+32])
fish3 = Image.fromarray(market[6 * 32:6 * 32+32, 15 * 32:15 * 32+32])
fish4 = Image.fromarray(market[7 * 32:7 * 32+32, 15 * 32:15 * 32+32])

pacman1 = Image.fromarray(market[3 * 32:3 * 32+32, 0 * 32:0 * 32+32])
pacman2 = Image.fromarray(market[4 * 32:4 * 32+32, 0 * 32:0 * 32+32])
pacman3 = Image.fromarray(market[5 * 32:5 * 32+32, 0 * 32:0 * 32+32])
pacman4 = Image.fromarray(market[6 * 32:6 * 32+32, 0 * 32:0 * 32+32])
pacman5 = Image.fromarray(market[3 * 32:3 * 32+32, 1 * 32:1 * 32+32])
pacman6 = Image.fromarray(market[4 * 32:4 * 32+32, 1 * 32:1 * 32+32])
pacman7 = Image.fromarray(market[5 * 32:5 * 32+32, 1 * 32:1 * 32+32])
pacman8 = Image.fromarray(market[6 * 32:6 * 32+32, 1 * 32:1 * 32+32])
pacman9 = Image.fromarray(market[3 * 32:3 * 32+32, 2 * 32:2 * 32+32])
pacman10 = Image.fromarray(market[4 * 32:4 * 32+32, 2 * 32:2 * 32+32])
pacman11 = Image.fromarray(market[5 * 32:5 * 32+32, 2 * 32:2 * 32+32])
pacman12 = Image.fromarray(market[6 * 32:6 * 32+32, 2 * 32:2 * 32+32])
ghost = Image.fromarray(market[7 * 32:7 * 32+32, 0 * 32:0 * 32+32])
pc=Image.open('./img/pm2.png')
pc_array= np.array(pc)
pc_array_new=pc_array[:,:,:3]
pc_new=Image.fromarray(pc_array_new)

imgs = [fish1, fish2, fish3, fish4, pacman1,
        pacman2, pacman3, pacman4, pacman5, pacman6, pacman7, pacman8, pacman9, pacman10, pacman11, pacman12, ghost, ghost, ghost, ghost, ghost, ghost]


def get_random_image():
    return random.choice(imgs)

from PIL import Image
import numpy as np

img = Image.open('./img/tiles.png')
market = np.array(img)

fish1=Image.fromarray(market[4 * 32:4 * 32+32, 15 * 32:15 * 32+32])
fish2=Image.fromarray(market[5 * 32:5 * 32+32, 15 * 32:15 * 32+32])
fish3=Image.fromarray(market[6 * 32:6 * 32+32, 15 * 32:15 * 32+32])
fish4=Image.fromarray(market[7 * 32:7 * 32+32, 15 * 32:15 * 32+32])

pacman1=Image.fromarray(market[3 * 32:3 * 32+32, 0 * 32:0 * 32+32])
pacman2=Image.fromarray(market[4 * 32:4 * 32+32, 0 * 32:0 * 32+32])
pacman3=Image.fromarray(market[5 * 32:5 * 32+32, 0 * 32:0 * 32+32])
pacman4=Image.fromarray(market[6 * 32:6 * 32+32, 0 * 32:0 * 32+32])
pacman5=Image.fromarray(market[3 * 32:3 * 32+32, 1 * 32:1 * 32+32])
pacman6=Image.fromarray(market[4 * 32:4 * 32+32, 1 * 32:1 * 32+32])
pacman7=Image.fromarray(market[5 * 32:5 * 32+32, 1 * 32:1 * 32+32])
pacman8=Image.fromarray(market[6 * 32:6 * 32+32, 1 * 32:1 * 32+32])
pacman9=Image.fromarray(market[3 * 32:3 * 32+32, 2 * 32:2 * 32+32])
pacman10=Image.fromarray(market[4 * 32:4 * 32+32, 2 * 32:2 * 32+32])
pacman11=Image.fromarray(market[5 * 32:5 * 32+32, 2 * 32:2 * 32+32])
pacman12=Image.fromarray(market[6 * 32:6 * 32+32, 2 * 32:2 * 32+32])
ghost=Image.fromarray(market[7 * 32:7 * 32+32, 0 * 32:0 * 32+32])

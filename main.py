import numpy as np
import cv2
import time

from supermarket import Supermarket

market_img = cv2.imread('./img/market.png')

customers = []

for x in range(10):  # number of customers we want
    # create customers
    ...

market = Supermarket(market_img, [])

while True:
    frame = market_img.copy()
    market.draw(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

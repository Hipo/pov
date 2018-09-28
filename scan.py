import sys
import math
import numpy as np
from PIL import Image

w, h = 500, 500
cx = int(w / 2)
cy = int(h / 2)


def main():
    filename = sys.argv[1]
    im = Image.open(filename)
    im = im.convert('RGBA')
    im = im.resize((w, h))
    angular_rate = 2
    num_leds = 15
    positions, leds = scan(im, num_leds, angular_rate)
    out = draw(positions, leds, angular_rate)
    out.save('output_%s.png' % filename.split('.')[0])
    for l in leds:
        s = ', '.join([' '.join(map(str, c)) for c in l])
        print(s)


def rotate(point, cx, cy, angle):
    px, py = point
    angle = math.radians(angle)
    s = math.sin(angle)
    c = math.cos(angle)
    # // translate point back to origin:
    px -= cx
    py -= cy

    # // rotate point
    xnew = px * c - py * s
    ynew = px * s + py * c

    # // translate point back:
    px = xnew + cx
    py = ynew + cy
    return px, py


def scan(im, num_leds, angular_rate):
    pixels = np.array(im)
    leds = np.zeros((num_leds, 360, 4))
    positions = [None] * len(leds)
    led_interval = int(250 / num_leds)
    x = 250
    for i, c in enumerate(leds):
        positions[i] = [x, cy]
        x += led_interval

    for angle in range(0, 360, angular_rate):
        for i, c in enumerate(leds):
            x, y = rotate(positions[i], cx, cy, angle)
            x, y = int(x), int(y)
            if x < w and y < h and x > 0 and y > 0:
                color = pixels[x-2:x+2, y-2:y+2].mean(1).mean(0)
                leds[i, angle, :] = color
    return positions, leds


def draw(positions, leds, angular_rate):
    pixels = np.zeros((w, h, 4))
    for angle in range(0, 360, angular_rate):
        for i, c in enumerate(leds):
            x, y = rotate(positions[i], cx, cy, angle)
            x, y = int(x), int(y)
            if x < w and y < h and x > 0 and y > 0:
                pixels[x-2:x+2, y-2:y+2, :] = leds[i][angle]
    return Image.fromarray(pixels.astype('uint8'), 'RGBA')


if __name__ == '__main__':
    main()

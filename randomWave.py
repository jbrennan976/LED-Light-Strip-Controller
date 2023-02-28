import neopixel
import board
import time
import threading

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.6, auto_write=False)

PIXEL_COUNT = 100

"""Sends a pulse to the LED strip
    :param position: the location of the crest of the wave
    :param strength: number of pixels back the wave will go from the crest
    :param speed: how fast the waves move
    :param red: red value
    :param green: green value
    :param blue: blue value
"""
def wave(position, strength, speed, red, green, blue):
    moving = True
    brightness_multiplier = 1.0 / strength
    red_step = red * brightness_multiplier
    green_step = green * brightness_multiplier
    blue_step = blue * brightness_multiplier

    count = 0

    while moving:
        if position + count < 100:
            pixels[position + count] = (red, green, blue)
            for i in range(1, strength + 1):
                if i <= strength:
                    pixels[position + count - i] = (int(red - (red_step * i)),
                                                    int(green - (green_step * i)),
                                                    int(blue - (blue_step * i)))

                # called on the last pixel of the wave that we wave to turn off
                else:
                    pixels[position + count - i] = (0, 0, 0)
            pixels.show()

            count += 1
            time.sleep(speed)

        else:
            for i in range(strength):
                pixels[99 - i] = (0,0,0)
            pixels.show()
            moving = False


t1 = threading.Thread(target=wave, args=[0, 10, .05, 150, 100, 100])
t2 = threading.Thread(target=wave, args=[0, 10, .01, 0, 200, 50])
t3 = threading.Thread(target=wave, args=[0, 10, .05, 200, 10, 150])

t1.start()
time.sleep(.5)
t2.start()
time.sleep(.5)
t3.start()

t1.join()
t2.join()
t3.join()






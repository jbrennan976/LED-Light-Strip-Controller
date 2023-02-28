import neopixel
import board
import time

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.2, auto_write=False)


def cycle(speed):
    PIXEL_COUNT = 100

    COLOR_STEP = 255 / PIXEL_COUNT

    playing = True

    counter = 0

    while playing:
        for i in range(PIXEL_COUNT):
            pixel_color_step = int(i * COLOR_STEP)
            # print(red)
            pixels[i] = ((255 - pixel_color_step - counter) % 255,
                         (pixel_color_step - counter) % 255,
                         (122 - pixel_color_step - counter) % 255)

        pixels.show()

        counter += 1
        time.sleep(speed)



cycle(.02)






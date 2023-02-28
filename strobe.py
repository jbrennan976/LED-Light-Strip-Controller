import neopixel
import board
import time

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.5, auto_write=False)


def strobe(speed, red, green, blue):
    PIXEL_COUNT = 100

    playing = True

    while playing:
        for i in range(PIXEL_COUNT):
            pixels[i] = (red, green, blue)
        pixels.show()

        time.sleep(speed / 2)

        for i in range(PIXEL_COUNT):
            pixels[i] = (0, 0, 0)
        pixels.show()

        time.sleep(speed / 2)




# strobe(.05, 100, 100, 100)






import neopixel
import board

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.6, auto_write=False)


def solid(red, blue, green):
    NUM_PIXELS = 100

    for i in range(NUM_PIXELS):
        pixels[i] = (red, blue, green)
    pixels.show()

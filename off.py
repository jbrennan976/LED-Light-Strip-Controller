import neopixel
import board

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.6, auto_write=False)

def off():
    NUM_PIXELS = 100

    for i in range(NUM_PIXELS):
        pixels[i] = (0,0,0)
    pixels.show()

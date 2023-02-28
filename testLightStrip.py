import neopixel
import board
import time

NUM_PIXELS = 100
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness=.5, auto_write=False)



def solid(red, blue, green):
    for i in range(NUM_PIXELS):
        pixels[i] = (red, blue, green)
    pixels.show()


def off():
    for i in range(NUM_PIXELS):
        pixels[i] = (0,0,0)
    pixels.show()


solid(50, 50, 50)
time.sleep(.5)
off()
time.sleep(.2)

solid(100, 100, 100)
time.sleep(.5)
off()
time.sleep(.2)

solid(150, 150, 150)
time.sleep(.5)
off()
time.sleep(.2)

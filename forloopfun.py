import neopixel
import board
import time
pixels = neopixel.NeoPixel(board.D18,900, brightness=.6)

for i in range(100):
    time.sleep(.001)
    pixels[i+1] = (0,0,255)
    pixels[i] = (0,0,0)
    pixels[i+10] = (0,255,0)
    pixels[i + 9] = (0, 0, 0)
import neopixel
import board
import time
pixels = neopixel.NeoPixel(board.D18,900, brightness = .6)

time.sleep(.005)
pixels[i] = (100,200,101)
pixels[i] = (0,0,0)
time.sleep(.005)
pixels[i] = (200,100,101)
pixels[i] = (0,0,0)
time.sleep(.005)
pixels[i] = (100,100,200)
pixels[i] = (0,0,0)



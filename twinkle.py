import neopixel
import board
import time

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.6, auto_write=False)


def twinkle(speed, red, green, blue):
    PIXEL_COUNT = 100

    evenPixels = []
    oddPixels = []

    for i in range(PIXEL_COUNT):
        if i % 2 == 0:
            evenPixels.append(i)
        else:
            oddPixels.append(i)

    playing = True

    while playing:
        for i in oddPixels:
            pixels[i] = (0, 0, 0)
        for i in evenPixels:
            pixels[i] = (red, green, blue)
        pixels.show()
        time.sleep(speed / 2)
        for i in evenPixels:
            pixels[i] = (0, 0, 0)
        for i in oddPixels:
            pixels[i] = (red, green, blue)
        pixels.show()
        time.sleep(speed / 2)

        # if time.perf_counter() - start >= duration:
        #     for i in oddPixels:
        #         pixels[i] = (0, 0, 0)
        #     pixels.show()
        #     playing = False


#twinkle(5, .5, 100, 50, 200)


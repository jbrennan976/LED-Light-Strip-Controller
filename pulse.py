import neopixel
import board
import time

pixels = neopixel.NeoPixel(board.D18, 100, brightness=.6, auto_write=False)

"""Sends a pulse to the LED strip
    :param count: the number of pulses
    :param strength: how far out from the origin the led will go. Maximum value is 6
    :param speed: delay between iterations of the pulse
    :param red: red value
    :param green: green value
    :param blue: blue value
"""
def pulse(count, strength, red, green, blue):
    global exit_event
    PIXEL_COUNT = 100
    activePixels = []
    speed = .1
    looping = True

    placement = int(PIXEL_COUNT / (count + 1))

    while looping:
        for glow in range(strength + 1):
            for pulseCount in range(count):
                # for repeat in range(glow):
                center = placement * (pulseCount + 1)

                if glow == 1:
                    pixels[center] = (red, green, blue)
                    activePixels.append(center)
                    #print(str(center))
                elif glow == 2:
                    pixels[center - 1] = (red, green, blue)
                    pixels[center + 1] = (red, green, blue)
                    activePixels.append(center - 1)
                    activePixels.append(center + 1)
                    #print(str(center - 1) + " and " + str(center + 1))

                elif glow == 3:
                    pixels[center - 2] = (red, green, blue)
                    pixels[center + 2] = (red, green, blue)
                    activePixels.append(center - 2)
                    activePixels.append(center + 2)
                    #print(str(center - 2) + " and " + str(center + 2))

                elif glow == 4:
                    pixels[center - 3] = (red, green, blue)
                    pixels[center + 3] = (red, green, blue)
                    activePixels.append(center - 3)
                    activePixels.append(center + 3)
                    #print(str(center - 3) + " and " + str(center + 3))

                elif glow == 5:
                    pixels[center - 4] = (red, green, blue)
                    pixels[center + 4] = (red, green, blue)
                    activePixels.append(center - 4)
                    activePixels.append(center + 4)
                    #print(str(center - 4) + " and " + str(center + 4))

                elif glow >= 6:
                    pixels[center - 5] = (red, green, blue)
                    pixels[center + 5] = (red, green, blue)
                    activePixels.append(center - 5)
                    activePixels.append(center + 5)
                    #print(str(center - 5) + " and " + str(center + 5))
            pixels.show()
            time.sleep(speed)
        for i in activePixels:
            pixels[i] = (0, 0, 0)
        pixels.show()
        time.sleep(speed)
        if exit_event.wait(.01):
            break


# for i in range(10):
#     pulse(4, 10, .01, 150, 100, 100)
#     # time.sleep(.3)


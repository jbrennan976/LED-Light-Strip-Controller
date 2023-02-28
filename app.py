import neopixel
import board
import threading
import signal
import time
from flask import Flask, render_template
from off import off
from solid import solid
import random
import alsaaudio
import audioop

# from wave import wave
# from twinkle import twinkle
# from pulse import pulse
# from strobe import strobe


NUM_PIXELS = 100
app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = .5, auto_write=False)

light_thread = threading.Thread()
global exit_event
exit_event = threading.Event()
global moving
moving = True


def signal_handler(signum, frame):
    exit_event.set()


@app.route("/solid/<int:red>/<int:green>/<int:blue>", methods=["POST"])
def solid_called(red, green, blue):
    create_light_thread(solid, [red, blue, green])
    light_thread.join()
    print("Solid On")
    return "ok"


@app.route("/wave/<int:strength>/<int:speed>/<int:red>/<int:green>/<int:blue>", methods= ["POST"])
def wave_called(strength, speed, red, green, blue):
    global moving
    create_light_thread(wave, [True, 0, strength, .1/speed, red, blue, green])
    print("Wave On")
    return "ok"


@app.route("/twinkle/<int:speed>/<int:red>/<int:green>/<int:blue>", methods= ["POST"])
def twinkle_called(speed, red, green, blue):
    create_light_thread(twinkle, [.3/speed, red, blue, green])
    print("Twinkle On")
    return "ok"


@app.route("/strobe/<int:speed>/<int:red>/<int:green>/<int:blue>", methods= ["POST"])
def strobe_called(speed, red, green, blue):
    create_light_thread(strobe, [.2/speed, red, blue, green])
    print("Strobe On")
    return "ok"


@app.route("/cycle/<int:speed>", methods= ["POST"])
def cycle_called(speed):
    create_light_thread(cycle, [.1/speed])
    print("Cycle On")
    return "ok"

@app.route("/pulse/<int:count>/<int:strength>/<int:red>/<int:green>/<int:blue>", methods= ["POST"])
def pulse_called(count, strength, red, green, blue):
    create_light_thread(pulse, [count, strength, red, blue, green])
    print("Pulse On")
    return "ok"

@app.route("/microphone", methods= ["POST"])
def microphone_called():
    create_light_thread(microphone)
    print("Microphone On")
    return "ok"


@app.route("/led_off", methods=["POST"])
def led_off():
    create_light_thread(off)
    print("LED off")
    return "ok"


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.php")


@app.route("/#", methods=["GET", "POST"])
def second_home():
    return render_template("index.php")


"""Each submission on the form causes the light thread to be purposed for faster execution of that light function
    :param function: the function to be executed by the thread
    :param args: arguments to be sent to the function
"""
def create_light_thread(function, args=None):
    if args is None: # no args passed for off and cycle
        args = []

    global light_thread
    global exit_event

    exit_event.set()
    if light_thread.isAlive():
        light_thread.join()
    exit_event.clear()
    for i in range(100):
        pixels[i] = (0, 0, 0)
    pixels.show()
    light_thread = threading.Thread(target=function, args=args)
    light_thread.start()


def wave(loop, position, strength, speed, red, green, blue):
    global moving
    global exit_event
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
                pixels[99 - i] = (0, 0, 0)
            pixels.show()

            if loop:
                count = 0

            else:
                moving = False
        if exit_event.wait(.01):
            break


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
        if exit_event.wait(.001):
            break


def twinkle(speed, red, green, blue):
    global exit_event
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
        if exit_event.wait(.001):
            break


def strobe(speed, red, green, blue):
    global exit_event
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
        if exit_event.wait(.001):
            break


def cycle(speed):
    global exit_event
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
        if exit_event.wait(.001):
            break

def microphone():
    global exit_event
    called = False
    print(alsaaudio.PCM_CAPTURE)
    print(alsaaudio.PCM_NONBLOCK)
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

    # Set attributes: Mono, 8000 Hz, 16 bit little endian samples
    inp.setchannels(1)
    inp.setrate(8000)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

    inp.setperiodsize(320)

    while True:
        # Read data from device
        l, data = inp.read()
        if l:
            # Return the maximum of the absolute value of all samples in a fragment.
            print (audioop.max(data, 2))
            if (audioop.max(data, 2) > 100 and audioop.max(data, 2) < 1000):
                print ("Joe is a poopoo head")
                called = True

        if called == True:
            red = random.randint(0, 200)
            green = random.randint(0, 200)
            blue = random.randint(0, 200)
            wave(False, 0, 7, .1, red, green, blue)
            called = False


        if exit_event.wait(.001):
            break

        time.sleep(.3)

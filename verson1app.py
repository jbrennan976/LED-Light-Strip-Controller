import neopixel
import board
import pulse
from flask import Flask, render_template
import threading
import os

NUM_PIXELS = 100
app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS, brightness = .6, auto_write=False)


# @app.route("/solidOn", methods=["POST"])
# def solid_on(red, green, blue):
#     pixels[NUM_PIXELS] = (red, green, blue)
#     print("LED on")
#     return "ok"
#
# @app.route("/solidOff", methods=["POST"])
# def solid_off():
#     pixels[NUM_PIXELS] = (0, 0, 0)
#     print("LED off")
#     return "ok"
#
# @app.route("/pulseOn", methods=["POST"])
# def pulse_on(count,strength, speed, red, green, blue):
#     pulse.pulse(count, strength, speed, red, green, blue)
#     print("LED on")
#     return "ok"
#
# @app.route("/pulseOff", methods=["POST"])
# def pulse_on():
#     pixels[NUM_PIXELS] = (0, 0, 0)
#     print("LED off")
#     return "ok"

@app.route("/", methods=["GET"])
def home():
    # pulse()
    return render_template("test.php")


@app.route("/submit", methods=["POST"])
def submit():
    print("submitted")
    return "submit button clicked"

# def pulse():
#     os.system("echo hello")

# def main():
#     threading.Thread(target=lambda: app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()    t2 = threading.Thread(target=pulse)
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# main()

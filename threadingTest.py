import threading
import time

# method = "wave"

def light_up_led(method):
    print(method + " started")
    time.sleep(1)
    print(method + " finished")

def main_thread():
    while True:
        print("hosting site")
        time.sleep(.5)

def main():
    t1 = threading.Thread(target=light_up_led, args=["wave"])
    # t2 = threading.Thread(target=light_up_led, args=["solid"])

    t1.start()
    main_thread()




    t1.join()



main()
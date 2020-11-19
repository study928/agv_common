import Jetson.GPIO as GPIO
import time
GPIO.setwarnings(False)
#gpio0
led_pin0 = 25 
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(led_pin0, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            time.sleep(1)
            # Toggle the output every second
            print("Outputting {} to pin {}".format(curr_value, led_pin0))
            GPIO.output(led_pin0, curr_value)
            curr_value ^= GPIO.HIGH
    finally:
        GPIO.cleanup()
        print(curr_value)

if __name__ == '__main__':
    main()
import RPi.GPIO as GPIO
from time import sleep

# Setup
servo_pin = 18  # GPIO pin where the signal wire is connected
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize PWM on the pin with a 50Hz frequency (standard for servos)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def move_servo(direction, duration):
    """
    Moves the continuous rotation servo in small steps.
    - direction: "forward" or "backward"
    - duration: time the servo is active (default 0.2 sec)
    - speed: duty cycle (default slightly above neutral)
    """
    if direction == "forward":
        duty_cycle = 9.05  # above 7.05% to move forward
    elif direction == "backward":
        duty_cycle =5.05  # below 7.05% to move backward
    else:
        return

    print(f"Moving {direction} for {duration} seconds at {duty_cycle}% duty cycle")
    pwm.ChangeDutyCycle(duty_cycle)
    sleep(duration)  # stop for set duration
    pwm.ChangeDutyCycle(7.05)  # neutral duty cycle
    sleep(0.5)  # Small pause

try:
    for i in range(10):
        print("Moving small step forward...")
        move_servo("forward", duration=0.2)  # Move forward
        sleep(0.25)

        print("Moving small step backward...")
        move_servo("backward", duration=0.2)  # Move backward
        sleep(0.25)

finally:
    pwm.stop()
    GPIO.cleanup()

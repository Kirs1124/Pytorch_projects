import RPi.GPIO as GPIO
import time


class Move():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.Motor1A = 11
        self.Motor1B = 12
        self.Motor1E = 35  # 使能通道A

        self.Motor2A = 13
        self.Motor2B = 15
        self.Motor2E = 37  # 使能通道B

        self.speed = 70  # 速度

        # print("Setting up GPIO pins")
        GPIO.setup(self.Motor1A, GPIO.OUT)
        GPIO.setup(self.Motor1B, GPIO.OUT)
        GPIO.setup(self.Motor1E, GPIO.OUT)
        GPIO.setup(self.Motor2A, GPIO.OUT)
        GPIO.setup(self.Motor2B, GPIO.OUT)
        GPIO.setup(self.Motor2E, GPIO.OUT)

        # print("Warming up engines")
        self.motorR = GPIO.PWM(self.Motor1E, 100)
        self.motorL = GPIO.PWM(self.Motor2E, 100)
        # print("Starting motors")

    def initStart(self):
        self.motorR.start(0)
        self.motorL.start(0)

    def checkSpeed(self, speed):
        print("Checking the speed")
        if speed < 25:
            speed = 25
        if speed > 100:
            speed = 100
        print("Speed is: " + str(speed))
        return speed

    def goStraight(self, speed = 70):
        speed = self.checkSpeed(speed)
        GPIO.output(self.Motor1A, GPIO.LOW)
        GPIO.output(self.Motor1B, GPIO.HIGH)
        GPIO.output(self.Motor2A, GPIO.HIGH)
        GPIO.output(self.Motor2B, GPIO.LOW)
        self.motorR.ChangeDutyCycle(speed)
        self.motorL.ChangeDutyCycle(speed)
        print("Going straigh with speed: " + str(speed))

    def stop(self):
        print("Stoping")
        GPIO.output(self.Motor1A, False)
        GPIO.output(self.Motor1B, False)
        GPIO.output(self.Motor2A, False)
        GPIO.output(self.Motor2B, False)
        self.motorR.ChangeDutyCycle(0)
        self.motorL.ChangeDutyCycle(0)

    def exitAndClean(self):
        print("Exiting")
        self.motorR.stop()
        self.motorL.stop()
        GPIO.cleanup()
        exit()

    def cleanNoExit(self):
        print("Exiting")
        self.motorR.stop()
        self.motorL.stop()
        GPIO.cleanup()

    def goBack(self, speed):
        speed = self.checkSpeed(speed)
        print("Going back with speed: " + str(speed))
        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor2A, GPIO.LOW)
        GPIO.output(self.Motor2B, GPIO.HIGH)
        self.motorR.ChangeDutyCycle(speed)
        self.motorL.ChangeDutyCycle(speed)

    def turnRight(self, speed):
        speed = self.checkSpeed(speed)
        print("Turning right with speed: " + str(speed))
        GPIO.output(self.Motor1A, GPIO.LOW)
        GPIO.output(self.Motor1B, GPIO.HIGH)
        GPIO.output(self.Motor2A, False)
        GPIO.output(self.Motor2B, False)
        self.motorR.ChangeDutyCycle(80)
        self.motorL.ChangeDutyCycle(80)

    def turnLeft(self, speed):
        speed = self.checkSpeed(speed)
        print("Turning left with speed: " + str(speed))
        GPIO.output(self.Motor1A, False)
        GPIO.output(self.Motor1B, False)
        GPIO.output(self.Motor2A, GPIO.HIGH)
        GPIO.output(self.Motor2B, GPIO.LOW)
        self.motorR.ChangeDutyCycle(80)
        self.motorL.ChangeDutyCycle(80)


if __name__ == "__main__":
    a = Move()
    a.initStart()
    a.goStraight(70)
    time.sleep(1)
    a.turnRight(50)
    time.sleep(1)
    a.turnLeft(50)
    time.sleep(1)
    a.goStraight(70)
    time.sleep(2)
    a.stop()
    a.exitAndClean()
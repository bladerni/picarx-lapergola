from picarx import Picarx
from time import sleep
from robot_hat import Servo, Motor

px = Picarx()

# Set the motor speed (0-100)
left_speed = 50
right_speed = 50

# Set the motor direction (forward or backward)
#left_direction = px.forward
#right_direction = px.backward

#px.left_rear_dir_pin(1)
#px.right_rear_dir_pin(0)


#print(px.right_rear_pwm_pin.channel)
#print(px.right_rear_dir_pin)
#print(px.right_rear_pwm_pin.freq)

#px.set_motor_speed(px.left, left_speed)
#px.set_motor_speed(px.right, right_speed)

#px.set_motor_direction(px.left, left_direction)
#px.set_motor_direction(px.right, right_direction)

#time.sleep(10)  # Run the motors for 2 seconds

#px.stop()

servos_pin = 'M1'
Motor.speed = 20
sleep(1)
sleep(1)
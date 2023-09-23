import RPi.GPIO as GPIO
from time import sleep

# Configura el modo BCM (Broadcom SOC channel) para los pines GPIO
GPIO.setmode(GPIO.BCM)

# Lista de pines GPIO disponibles en la Raspberry Pi 3
# Puedes ajustar esto según tu modelo de Raspberry Pi
# Consulta la documentación de tu modelo de Raspberry Pi para conocer los pines disponibles.
pines_disponibles = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

# Función para verificar si un pin tiene algo conectado
def verifica_pin(pin):
    GPIO.setup(pin, GPIO.IN)
    estado = GPIO.input(pin)
    return "conectado" if estado == GPIO.HIGH else "no conectado"

try:
    print("Verificando pines GPIO:")
    for pin in pines_disponibles:
        estado = verifica_pin(pin)
        if estado == "conectado":
            print(f"Pin GPIO {pin}: {estado}")
            pwm_frequency = 50
            GPIO.setup(pin, GPIO.OUT)
            pwm = GPIO.PWM(pin, pwm_frequency)
            pwm.start(7.5)  # Inicializa el servo en posición media
            sleep(1)
            pwm.ChangeDutyCycle(2.5)  # Mueve el servo a 0 grados
            sleep(1)
            pwm.ChangeDutyCycle(12.5)  # Mueve el servo a 180 grados
            sleep(1)
            pwm.stop()  # Detiene el PWM
            
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

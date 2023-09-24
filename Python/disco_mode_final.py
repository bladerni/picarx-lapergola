from picarx import Picarx
from time import sleep
from robot_hat import TTS
import readchar
import pygame
import threading

px = Picarx()

# Variable para controlar si la función move() debe seguir ejecutándose
move_thread_running = True

def play_song():
    audio_file = "disco_mode_song.mp3"

    pygame.init()
    pygame.mixer.init()

    # Establecer el volumen al máximo (1.0)
    pygame.mixer.music.set_volume(1.0)

    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.quit()

def move_car():
    global move_thread_running

    speed = 90
    sleep_time = 1

    while move_thread_running:
        px.set_dir_servo_angle(0)
        px.forward(speed)
        sleep(sleep_time)
        px.forward(0)
        sleep(sleep_time)

        px.backward(speed)
        sleep(sleep_time)
        px.backward(0)
        sleep(sleep_time)
        px.set_dir_servo_angle(-30)
        px.forward(speed)
        sleep(sleep_time)
        px.forward(0)
        sleep(sleep_time)

        px.backward(speed)
        sleep(sleep_time)
        px.backward(0)
        sleep(sleep_time)
        px.set_dir_servo_angle(0)
        px.forward(speed)
        sleep(sleep_time)
        px.forward(0)
        sleep(sleep_time)

        px.backward(speed)
        sleep(sleep_time)
        px.backward(0)
        sleep(sleep_time)
        px.set_dir_servo_angle(30)
        px.forward(speed)
        sleep(sleep_time)
        px.forward(0)
        sleep(sleep_time)

def move_camera():
    global move_thread_running
    
    sleep_time = 1
    
    while move_thread_running:
        px.set_camera_tilt_angle(0)
        px.set_cam_pan_angle(0)
        sleep(sleep_time)
            
        px.set_camera_tilt_angle(-50)
        sleep(sleep_time)
        
        px.set_camera_tilt_angle(0)
        sleep(sleep_time)
        
        px.set_cam_pan_angle(-50)
        sleep(sleep_time)
        
        px.set_cam_pan_angle(0)
        sleep(sleep_time)
        
        px.set_camera_tilt_angle(50)
        sleep(sleep_time)
        
        px.set_camera_tilt_angle(0)
        sleep(sleep_time)
        
        px.set_cam_pan_angle(50)
        sleep(sleep_time)
        
        px.set_cam_pan_angle(0)
        sleep(sleep_time)
        
def introduction():
    speech1 = "Hello my name is BRASCADA"
    speech2 = "and i am the new host of ERNI Valencia office"
    tts_robot = TTS()
    tts_robot.say(speech1)
    tts_robot.say(speech2)

def main():
    global move_thread_running
    
    introduction()
    
    song_thread = threading.Thread(target=play_song)
    move_car_thread = threading.Thread(target=move_car)
    move_camera_thread = threading.Thread(target=move_camera)

    song_thread.start()
    move_car_thread.start()
    move_camera_thread.start()

    while True:
        # readkey
        key = readchar.readkey().lower()
        # operation
        if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            print('\nquit ...')
            move_thread_running = False  # Detener el bucle de move()
            px.stop()
            break

        sleep(0.1)

    song_thread.join()  # Esperar a que termine el hilo de la canción
    move_car_thread.join()  # Esperar a que termine el hilo de movimiento
    move_camera_thread.join()  # Esperar a que termine el hilo de movimiento

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("error:%s" % e)
        move_thread_running = False  # Detener el bucle de move()
        px.stop()
    finally:
        move_thread_running = False
        px.stop()

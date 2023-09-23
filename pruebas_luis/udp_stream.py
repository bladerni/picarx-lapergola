from time import sleep
from vilib import Vilib
import readchar
import socket

manual = '''
Press keys on the keyboard to control recording:
    Q: record/pause/continue
    E: stop video and stream
    ESC: Quit and stop streaming
'''

video_path = "/home/pi/Videos/video_test.avi"

# Función para transmitir video por UDP
def udp_stream():
    UDP_IP = "10.142.90.136"  # Dirección IP del receptor UDP
    UDP_PORT = 4212  # Puerto UDP del receptor

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    with open(video_path, 'rb') as video_file:
        while True:
            data = video_file.read(1024)
            if not data:
                break
            sock.sendto(data, (UDP_IP, UDP_PORT))

    sock.close()
    print("Video sent successfully.")

def main():
    rec_flag = 'stop'  # start, pause, stop
    vname = None
    Vilib.rec_video_set["path"] = "/home/pi/Videos/"  # Establece la ruta

    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.display(local=True, web=True)
    sleep(0.8)  # Espera al inicio

    print(manual)
    while True:
        # Lee el teclado
        key = readchar.readkey().lower()
        # Iniciar, pausar
        if key == 'q':
            key = None
            if rec_flag == 'stop':
                rec_flag = 'start'
                # Establece el nombre
                Vilib.rec_video_set["name"] = "video_test"
                # Iniciar grabación
                Vilib.rec_video_run()
                Vilib.rec_video_start()
                print('Recording started...')
                print('Stream starting (10 sec)...')
                sleep(10)
                # Iniciar la transmisión por UDP
                udp_stream()

            elif rec_flag == 'start':
                rec_flag = 'pause'
                Vilib.rec_video_pause()
                print('Paused')
            elif rec_flag == 'pause':
                rec_flag = 'start'
                Vilib.rec_video_start()
                print('Resumed')
        # Detener
        elif key == 'e' and rec_flag != 'stop':
            key = None
            rec_flag = 'stop'
            Vilib.rec_video_stop()
            print("The video saved as %s%s.avi" % (Vilib.rec_video_set["path"], vname))
        # Salir
        elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            Vilib.camera_close()
            print('Quit')
            break

        sleep(0.1)

if __name__ == "__main__":
    main()

from time import sleep
from vilib import Vilib
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import streamlink
import readchar

manual = '''
Press keys on keyboard to control recording:
    Q: record/pause/continue
    E: stop video and stream
    ESC: Quit and stop stream
'''

video_path ="/home/pi/Videos/video_test.avi"
youtube_url = ""

def print_overwrite(msg,  end='', flush=True):
    print('\r\033[2K', end='',flush=True)
    print(msg, end=end, flush=True)
    
# Función para detener la transmisión en vivo de YouTube
def stop_youtube_stream():
    session = streamlink.Streamlink()
    streams = session.streams(youtube_url)
    stream = streams['best']

    # Cierra la transmisión en vivo
    stream.close()
    
# Función para transmitir video local a la transmisión en vivo de YouTube
def stream_local_video_to_youtube():
    session = streamlink.Streamlink()
    streams = session.streams(youtube_url)
    stream = streams['best']

    with open(video_path, 'rb') as video_file:
        while True:
            frame = video_file.read(1024)  # Lee un bloque del video local
            if not frame:
                break

            # Envía el bloque de video a la transmisión en vivo de YouTube
            stream.send_frame(frame)
    
def init_video_stream():   
    # Configura las credenciales OAuth 2.0
    credentials_path = 'client_secret_yt.json'
    api_service_name = 'youtube'
    api_version = 'v3'

    # Crea una instancia de autenticación
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, ['https://www.googleapis.com/auth/youtube.force-ssl'])
    credentials = flow.run_console()

    # Crea una instancia de YouTube Data API
    youtube = build(api_service_name, api_version, credentials=credentials)

    # Configura la transmisión en vivo
    stream_name = 'erni_hackaton_valencia_stream'
    stream_description = 'This is the robot streaming'
    broadcast_title = 'HELLO YOUTUBE'

    # Crea una transmisión en vivo
    live_broadcast = youtube.liveBroadcasts().insert(
        part='snippet,status',
        body={
            'snippet': {
                'title': broadcast_title,
                'description': stream_description,
                'scheduledStartTime': '2023-09-23T12:00:00Z',  # Configura la hora de inicio
            },
            'status': {
                'privacyStatus': 'public',  # Puedes cambiar esto a 'private' si lo deseas
            },
        }
    ).execute()

    # Configura la transmisión en vivo
    stream = youtube.liveStreams().insert(
        part='snippet',
        body={
            'snippet': {
                'title': stream_name,
            },
        }
    ).execute()

    # Asocia la transmisión con la transmisión en vivo
    youtube.liveBroadcasts().bind(
        part='id,contentDetails',
        id=live_broadcast['id'],
        streamId=stream['id']
    ).execute()

    # URL de la transmisión en vivo
    youtube_url = f"https://www.youtube.com/watch?v={live_broadcast['id']}"

    print(f"La transmisión en vivo está disponible en: {youtube_url}")
     

def main():
    rec_flag = 'stop' # start,pause,stop
    vname = None
    Vilib.rec_video_set["path"] = "/home/pi/Videos/" # set path

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    sleep(0.8)  # wait for startup
    
    init_video_stream()

    print(manual)
    while True:
        # read keyboard
        key = readchar.readkey().lower()
        # start,pause
        if key == 'q':
            key = None
            if rec_flag == 'stop':
                rec_flag = 'start'
                # set name
                # vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                Vilib.rec_video_set["name"] = "video_test"
                # start record
                Vilib.rec_video_run()
                Vilib.rec_video_start()
                print_overwrite('rec start ...')
                # stream start
                stream_local_video_to_youtube()
                
            elif rec_flag == 'start':
                rec_flag = 'pause'
                Vilib.rec_video_pause()
                print_overwrite('pause')
            elif rec_flag == 'pause':
                rec_flag = 'start'
                Vilib.rec_video_start()
                print_overwrite('continue')
        # stop
        elif key == 'e' and rec_flag != 'stop':
            key = None
            rec_flag = 'stop'
            Vilib.rec_video_stop()
            print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')
            # Stop the YouTube stream
            stop_youtube_stream()
        # quit
        elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
            Vilib.camera_close()
            stop_youtube_stream()
            print('\nquit')
            break

        sleep(0.1)

if __name__ == "__main__":
    main()
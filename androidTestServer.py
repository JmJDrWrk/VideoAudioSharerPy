import socket
import pyaudio
import configparser
import threading

p = pyaudio.PyAudio()
# print('\t handshake')

SERVER_IP = '0.0.0.0'
SERVER_REGISTRATION_PORT = 54424
CLIENT_PORT = 5005
FORMAT = pyaudio.paInt16

def load_config(filename='config.ini'):
    config = configparser.ConfigParser()
    config.read(filename)
    audio_config = config['audio_sharing']
    return {
        'audioServerIp': audio_config.get('audioServerIp'),
        'audioServerPort': int(audio_config.get('audioServerPort')),
        'channels': int(audio_config.get('channels')),
        'rate': int(audio_config.get('rate')),
        'chunk': int(audio_config.get('chunk')),
        'deviceIndex': int(audio_config.get('deviceIndex'))
    }

config = load_config()
stream = p.open(
    format=FORMAT,
    channels=config['channels'],
    rate=config['rate'],
    input=True,
    input_device_index=config['deviceIndex'],
    frames_per_buffer=config['chunk']
)

CHUNK = config['chunk']

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print(f"\tstreaming system audio to {client_ip}:{CLIENT_PORT}...")
    try:
        while True:
            data = stream.read(CHUNK)
            sock.sendto(data, (client_ip, CLIENT_PORT))
    except KeyboardInterrupt:
        print("\tstreaming stopped.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
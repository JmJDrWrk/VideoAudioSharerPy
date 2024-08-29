from jnius import autoclass
import socket
import threading

# Import the Android classes for audio
AudioTrack = autoclass('android.media.AudioTrack')
AudioFormat = autoclass('android.media.AudioFormat')
AudioManager = autoclass('android.media.AudioManager')

# Set up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 12345))  # Replace with your server port

# Audio Configuration
sample_rate = 44100
channel_config = AudioFormat.CHANNEL_OUT_STEREO
audio_format = AudioFormat.ENCODING_PCM_16BIT
buffer_size = 2 * 1024

# Create AudioTrack for playback
audio_track = AudioTrack(AudioManager.STREAM_MUSIC, sample_rate, channel_config,
                         audio_format, buffer_size, AudioTrack.MODE_STREAM)
audio_track.play()

def receive_audio():
    while True:
        try:
            data, _ = sock.recvfrom(2048)
            audio_track.write(data, 0, len(data))
        except Exception as e:
            print("Error receiving audio:", e)
            break

# Start a new thread for audio receiving
thread = threading.Thread(target=receive_audio)
thread.start()

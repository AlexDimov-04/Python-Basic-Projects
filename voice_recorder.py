# import modules
import sounddevice
from scipy.io.wavfile import write

# default audio frequency
fps = 44100
# record duration time
duration = 10

# Record our audio volume
print("Recording...")
recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
sounddevice.wait()
print("Done!")

# output audio name
write("output_audio.wav", fps, recording)

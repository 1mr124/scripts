import numpy as np
import sounddevice as sd

# Set the sample rate and duration of the white noise
sample_rate = 4100  # 4.1 kHz
duration = 30  # 30 seconds

# Generate white noise
white_noise = np.random.normal(0, 1, int(duration * sample_rate))
# Play the white noise using the sounddevice module
sd.play(white_noise, sample_rate)
# Wait for the audio to finish playing
sd.wait()

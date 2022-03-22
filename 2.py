import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.fft import fft

fn_wav = '1.wav'
y1, fs1 = sf.read(fn_wav)

Ny = len(y1)

tiv = 1 / fs1

t = np.arange(0, ((Ny - 1) * tiv), tiv)

ff1 = fft(y1,fs1)


plt.plot(np.abs(ff1(np.arange(1,401))))

plt.title('spectral density')

plt.xlabel('Hz')
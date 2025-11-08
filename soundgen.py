import os, wave, math, random, struct

SR = 44100

def _env(n,attack = 0.01, release = 0.05, sr = SR):
    a = int(attack * sr)
    r = int(release * sr)
    out = [1.0] * n
    for i in range(min(a,n)):
        out[i] = i / max(1,a-1)
    for i in range(r):
        j = n - 1 - i
        if j >= 0:
            out[j] = min(out[j], i / max(1,r))
    return out

def _sine(i,f,sr):
    return math.sin(2 * math.pi * f * i / sr)

def _square(i,f,sr):
    return 1.0 if (i * f / sr) % 1 < 0.5 else -1.0

def _saw(i,f,sr):
    return 2.0 * ((i * f / sr) % 1) - 1.0

def _triangle(i,f,sr):
    x = (i * f / sr) % 1
    return 4.0 * x - 1.0 if x < 0.5 else -4.0 * x + 3.0

def _noise(i,f,sr):
    return random.uniform(-1,1)


WAVES = [_sine, _square, _saw, _triangle, _noise]

def synth_to_wav(path,freq=440.0,duration=0.6,volume=0.6,wave_fn=None.sr=SR):
    n = int(duration * sr)
    env = _env(n, 0.01, 0.05, sr)
    if wave_fn is None:
        wave_fn = random.choice(WAVES)
    with wave.open(path,'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        for i in range(n):
            s = wave_fn(i,freq,sr) * env[i] * volume
            wf.writeframes(struct.pack('<h',max(-32768, min(32767, int(s * 32767)))))



    
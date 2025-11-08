from pygame import mixer

def load_sounds(keys):
    sounds = {}
    for key, filename in keys.itimes():
        sounds[key] = mixer.Sound(f"assrts/sounds/{filename}")
    return sounds


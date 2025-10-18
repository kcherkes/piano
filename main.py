from pygame import*
from settings import*
from sounds import load_sounds
from keys import draw_keys, create_key_rects
#from buttons import Button


init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano game")

sounds = load_sounds(KEYS)
key_rect = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
temp_font = font.SysFont("arial",24)
pressed_keys = set()
import pygame
class Slider:
    def __init__(self,x,y,width,min_val,max_val,step=1,initial=None, label='',value_to_text = None):
        self.track_rect = pygame.Rect(x,y,width, 6 )
        self.handle_radius = 10
        self.min = float(min_val)
        self.max = float(max_val)
        self.step = float(step)
        if initial is not None:
            self.value = float(initial)
        else:
            self.value = self.min
        self.label = label
        self.value_to_text = value_to_text
        self.dragging = False
        self._hit_rect = pygame.Rect(0, 0, self.handle_radius*2+8, self.handle_radius*2+8)

    def set_on_change(self, callback):
        self.on_change = callback

    def _clamp(self, val: float):
        val = max(self.min, min(self.max, val))
        if self.step > 0:
            val = round(val / self.step) * self.step
        return max(self.min, min(self.max, val))
    
    def _pos_to_value(self, px:float):
        ratio = (px - self.track_rect.left) / self.track_rect.width
        return self._clamp(self.min + ratio * (self.max - self.min))
    
    def _value_to_pos(self):
        if self.max == self.min:
            return self.track_rect.left
        ratio = (self.value - self.min) / (self.max - self.min)
        return int(self.track_rect.left + ratio * self.track_rect.width)
    

    def draw(self, surface, font = None):
        pygame.draw.rect(surface, (200,200,200), self.track_rect, border_radius=3)
        pygame.draw.rect(surface,(100,100,100), self.track_rect, 1, border_radius=3)
from pygame import Rect, draw, mouse, transform, image,MOUSEBUTTONDOWN,draw

class Button:
    def __init__(
            self, x, y, width, height,
            text:str="", action=None,
            img_idle=None, ing_hover=None,
            center: bool=False):
        
        self.text = text
        self.action = action
        self.img_idle = img_idle
        self.img_hover = ing_hover
        self.use_image = img_idle is not None

        self.color_idle = (200,200,200)
        self.color_hover = (180,180,180)
        self.color_border = (0,0,0)
        self.text_color = (0,0,0)

        if self.use_image and (width is None or height is None):
            img_width, img_height = self.img_idle.get_size()
            width = width or img_width
            height = height or img_height

        if center:
            self.rect = Rect(0,0,width,height)
            self.rect.center = (x,y)
        else:
            self.rect = Rect(x,y,width,height)

    def draw(self,surface,font):
        mouse_pos = mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)

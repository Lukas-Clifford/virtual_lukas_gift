import pygame,os,random
from data.img_loading import img_loading
from configuracion import config_loading as config
porcentajes = config.porcentajes

class Entity:
    def __init__(self,iden,img):
        self.images = img_loading.images[iden]
        self.selected = img
        self.img = self.images[self.selected]["0"]
        self.scale = self.images[self.selected]["0"]
        self.escala = config.scale
        
        self.w = self.scale.get_width()*self.escala
        self.h = self.scale.get_width()*self.escala
        self.x = 0
        self.y = 0
        
        self.rect = pygame.Rect([self.x,self.y],[self.w,self.h])

        self.velx = 0
        self.vely = 0
        self.gravity = 3
        self.dragging = False

    def set_pos(self,x,y):
        self.x = x
        self.y = y
    def set_scale(self,scale):
        self.escala = scale
    def set_gravity(self,grav):
        self.gravity = grav
    
    def render(self,h,w,win):
        self.rect.x = self.x
        self.rect.y = self.y
        self.x += self.velx
        self.y += self.vely
        
        self.rect.w = self.w
        self.rect.h = self.h
        self.w = self.scale.get_width()*self.escala
        self.h = self.scale.get_width()*self.escala

        if self.dragging:
            self.vely = 0
            self.velx = 0
            self.moving = False
        elif self.rect.bottom > h:
            self.vely = 0
            self.y = h-self.h +1 
        else:
            self.vely += self.gravity
        
        
        self.img = pygame.transform.scale(self.img,[self.w,self.h])
        win.blit(self.img,(self.x,self.y))
#DRAWINGS----------------------------------------------------------------
class Drawing(Entity):
    def __init__(self):
        self.images = img_loading.images["Drawings"]
        self.selected = random.choice(os.listdir("data/img_loading/images/Drawings"))
        self.img = self.images[self.selected]["0"]
        self.scale = self.images[self.selected]["0"]
        self.escala = config.scale
        
        self.w = self.scale.get_width()*self.escala
        self.h = self.scale.get_width()*self.escala
        self.x = 0
        self.y = 0
        
        self.rect = pygame.Rect([self.x,self.y],[self.w,self.h])

        self.velx = 0
        self.vely = 0
        self.gravity = 0
        self.dragging = False
        self.selected = False
    def random_img(self):
        self.selected = random.choice(os.listdir("data/img_loading/images/Drawings"))
        self.img = self.images[self.selected]["0"]
        self.selected = True    
    
class Icon(Entity):
    def __init__(self,icon):
        self.images = img_loading.images["iconos"]
        self.selected = icon
        self.img = self.images[self.selected]["0"]
        self.scale = self.images[self.selected]["0"]
        self.escala = config.scale
        
        self.w = self.scale.get_width()*self.escala
        self.h = self.scale.get_width()*self.escala
        self.x = 0
        self.y = 0
        
        self.rect = pygame.Rect([self.x,self.y],[self.w,self.h])

        self.velx = 0
        self.vely = 0
        self.gravity = 0
        self.dragging = False
        self.selected = False
    
#LUKAS-------------------------------------------------------------------
class Lukas(Entity):
    def __init__(self):
        self.images = img_loading.images["Lukas"]
        self.selected = "sitting"
        self.img = self.images[self.selected]["0"]
        self.scale = self.images[self.selected]["0"]
        self.escala = config.scale
        
        self.w = self.scale.get_width()*self.escala
        self.h = self.scale.get_width()*self.escala
        self.x = 0
        self.y = 0
        
        self.rect = pygame.Rect([self.x,self.y],[self.w,self.h])

        self.velx = 0
        self.vely = 0
        self.gravity = 3
        self.dragging = False
        self.timer = 0

        self.animation = False
        self.right = True
        self.left = False
        self.moving = False
        self.drawing = False
        self.dragging = False
        self.showing = False
    
    def animate(self,h,w,win):
        if self.moving:
            if self.right:
                self.velx = 7
                self.selected = "walk_right_1"
                if self.x >= w-self.w:
                    self.left = True
                    self.right = False
                    self.moving = False
            elif self.left:
                self.velx = -7
                self.selected = "walk_left_1"
                if self.x < 0:
                    self.left = False
                    self.right = True
        elif self.drawing:
            if self.timer == 0:
                self.showing = True
                self.moving = False
                self.drawing = False
            else:
                self.selected = "drawing"
        elif self.showing:
            self.selected = "standing"
        else:
            self.velx = 0
            if not self.animation:
                choice = random.choice(porcentajes)
                if choice == "walk":
                    self.moving = True
                elif choice == "drawing":
                    self.drawing = True
                else:
                    self.selected = choice
                    self.animation = True

        if self.timer <= len(self.images[self.selected])-1:
            self.timer += 0.20
        else:
            self.animation = False
            self.timer = 0
        self.img = self.images[self.selected][str(round(self.timer))]
        self.scale = self.images[self.selected][str(round(self.timer))]


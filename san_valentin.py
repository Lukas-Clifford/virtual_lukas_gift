import win32api, win32con, win32gui, pygame,sys,os,random
from pygame import *
from data.entity import Lukas
from data.entity import Entity
from data.entity import Drawing
from data.entity import Icon

#window stuff----------------
pygame.init()
clock = pygame.time.Clock()
w = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
h = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
win = pygame.display.set_mode((w,h),pygame.NOFRAME)
pygame.mouse.set_cursor(pygame.cursors.broken_x)
icono = pygame.image.load("data/micara.ico")
pygame.display.set_icon(icono)
pygame.display.set_caption("Virtual_lukitas")

hwnd = pygame.display.get_wm_info()["window"]

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
    hwnd, win32con.GWL_EXSTYLE)|win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255,0,128),0,
                                    win32con.LWA_COLORKEY)

win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,win32con.SWP_NOSIZE,
                      win32con.SWP_NOMOVE,w,h,0)

#variables ----------------
mpos = (0,0)
        
lukas = Lukas()
lukas.set_pos(w-300,h-300)

dibujo = Drawing()
dibujo.set_pos(w/2-dibujo.w/2,h/2-dibujo.h/2)

cross = Icon("cross")
cross.set_pos(dibujo.x,dibujo.y-cross.h)

entities = [lukas,dibujo]

#Main loop-----------------------
while True:
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for e in entities:
                    if e.rect.collidepoint(event.pos):
                        e.dragging = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                for e in entities:
                    if e.rect.collidepoint(event.pos):
                        e.dragging = False
                if cross.rect.collidepoint(event.pos):
                    lukas.showing = False
                    dibujo.selected = False
        if event.type == pygame.MOUSEMOTION:
            for e in entities:
                if e.dragging:
                    mx,my = event.pos
                    e.x = mx - e.w/2
                    e.y = my - e.h/2
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    cross.set_pos(dibujo.x,dibujo.y-cross.h)
    #Drawing-----------
    win.fill((255,0,128))
    lukas.animate(h,w,win)
    if lukas.showing:
        lukas.set_pos(w-w/3,400)
        if dibujo.selected:
            dibujo.render(h,w,win)
            cross.render(h,w,win)
        else:
            dibujo.random_img()
    lukas.render(h,w,win)
    pygame.display.update()
    clock.tick(30)
    

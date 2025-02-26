import pygame,os
from os import listdir
path = "data/img_loading/"

images = {}
#imglist = listdir(path+"images/"+entity+"/"+action)

for entity in listdir(path+"images"):
    images[entity] = {}
    for action in listdir(path+"images/"+entity):
        images[entity][action] = {}
        imglist = listdir(path+"images/"+entity+"/"+action)
        for img in range(len(imglist)):
            images[entity][action][str(img)] = pygame.image.load(path+"images/"+entity+"/"+action+"/"+imglist[img])
            
   


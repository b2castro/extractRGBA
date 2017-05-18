import os
import sys
import pygame
from pygame.locals import *
import time
from mpi4py import MPI
from PIL import Image

pygame.init()
img = Image.open('dice.png')
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
running = 1

# set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
# get this display
os.environ['DISPLAY'] = ':0.0'

# init clock and display\
clock = pygame.time.Clock()
pygame.display.init()

# get the screen hight and width
disp_info = pygame.display.Info()
width = disp_info.current_w
height = disp_info.current_h

universe_size = (width*2, height*2)
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)

screen.fill((0,0,0))

img1 = img.crop((0,0,400,300)) 
img2 = img.crop((400,0,800,300))
img3 = img.crop((0,300,400,600))
img4 = img.crop((400,300,800,600))

mode = img1.mode
size = img1.size
data = img1.tobytes()

py_img1 = pygame.image.fromstring(data,size,mode)
py_img1 = pygame.transform.scale(py_img1,(width,height))


mode2 = img2.mode
size2 = img2.size
data2 = img2.tobytes()

py_img2 = pygame.image.fromstring(data2,size2,mode2)
py_img2 = pygame.transform.scale(py_img2,(width,height))



mode3 = img3.mode
size3 = img3.size
data3 = img3.tobytes()

py_img3 = pygame.image.fromstring(data3,size3,mode3)
py_img3 = pygame.transform.scale(py_img3,(width,height))


mode4 = img4.mode
size4 = img4.size
data4 = img4.tobytes()

py_img4 = pygame.image.fromstring(data4,size4,mode4)
py_img4 = pygame.transform.scale(py_img4,(width,height))

pygame.mouse.set_visible(0)

while running == 1:
	comm.Barrier()
	events = pygame.event.get()
	
	if rank == 0:
		screen.blit(py_img1,(0,0))
	
	if rank == 1:
		screen.blit(py_img2,(0,0))

	if rank == 2:
		screen.blit(py_img3, (0,0))
	if rank == 3:
		screen.blit(py_img4,(0,0))
	pygame.display.flip()
	time.sleep(5)
	running = 0
		
exit(0)

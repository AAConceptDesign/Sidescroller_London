import os, sys, pygame, random
pygame.init()

size = width, height = 1920, 1080
speed = [6, 3]
black = 200, 40, 20
num_of_cats = 20

screen = pygame.display.set_mode(size)

class girl():
    def __init__(self, image, rect, speed):
        self.image = image
        self.rect = rect
        self.speed = speed

#def ticky():
#    whiff_sound.play()
        
#pygame.time.set_timer(ticky, 3000)

girl_array = []

for i in range(num_of_cats):
    gal = pygame.image.load("girl.png")
    recta = gal.get_rect()
    recta.move_ip(random.randint(0, 900), random.randint(0, 900))
    girl_array.append(girl(gal, recta, [6, 3]))
bg = pygame.image.load("bg1.png")

def load_sound(name):
    fullname = os.path.join('data', name)
    sound = pygame.mixer.Sound(fullname)
    return sound

pygame.mixer.music.load('data/bgm1.mp3')
#pygame.mixer.music.play(loops = -1, start=0.0)

whiff_sound = load_sound('whiff.wav')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(bg, (0, 0))
    
    for i in range (num_of_cats):
        girl_array[i].rect = girl_array[i].rect.move(girl_array[i].speed)
        if girl_array[i].rect.left < 0 or girl_array[i].rect.right > width:
            girl_array[i].speed[0] = -girl_array[i].speed[0]
            whiff_sound.play()
        if girl_array[i].rect.top < 0 or girl_array[i].rect.bottom > height:
            girl_array[i].speed[1] = -girl_array[i].speed[1]
        for j in range (num_of_cats):
            if(i != j):
                if pygame.Rect.colliderect(girl_array[i].rect, girl_array[j].rect):
                    girl_array[i].speed[0] = -girl_array[i].speed[0]
                    girl_array[i].speed[1] = -girl_array[i].speed[1]
                    girl_array[j].speed[0] = -girl_array[j].speed[0]
                    girl_array[j].speed[1] = -girl_array[j].speed[1]
        screen.blit(girl_array[i].image, girl_array[i].rect)
    
    pygame.display.flip()
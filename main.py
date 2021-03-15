import math
import pygame

pygame.init()
scrn = pygame.display.set_mode([800, 600])
pygame.display.set_caption("illusioon")
scrn.fill([255, 255, 255])
pygame.draw.line(scrn, [0, 0, 0], [385, 300], [415, 300])  # loob risti ekraani keskele
pygame.draw.line(scrn, [0, 0, 0], [400, 285], [400, 315])
sx = 90  # loob ringi punktide leidmiseks x telje punkti(A1)
sy = 0  # loob ringi punktide leidmiseks y telje punkti(A2)
a = 0  # loob muutuja mis loeb kui palju tsukleid on tehtud
z = 13
running = True
while running:
    a += 1  # xtelje algus punkt(x=B1/y=B2)+sin(A1)*rad/sin(90)  x+sin(Ax)*rad/sin(taisnurk/90)
    x = 400 + int(math.sin(math.radians(sx)) * 150 / math.sin(math.radians(90)))
    y = 300 + int(math.sin(math.radians(sy)) * 150 / math.sin(math.radians(90)))
    pygame.draw.circle(scrn, [221, 148, 220], [x, y], 15)  # loob ringi leitud kordinaatidega
    sx += 30  # lisab 30 kraadi sest, 360/12=30
    sy += 30
    if a == z:  # kui tsuklite arv on 13 siis v�rvib 13-nda ringi valgeks
        pygame.draw.circle(scrn, [255, 255, 255], [x, y], 16)  # loob valge ringi
        pygame.time.delay(500)  # ootab 500ms
        a = 0  # taaskuivitab tsuklite lugemise tagasi 0-i
        pygame.display.flip()  # varskendab ekraani
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                z = 13
            if i.key == pygame.K_RIGHT:
                z = 11
pygame.quit()

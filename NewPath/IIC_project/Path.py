import pygame
pygame.init()
window = pygame.display.set_mode((713,409))
map = pygame.image.load('map.png')
car = pygame.image.load('car.png')
car = pygame.transform.scale(car,(30,50))
car = pygame.transform.rotate(car, -90)
car_x=40
car_y=329
cam_x_offset= 0
cam_y_offset= 0
focal_dis =20
direction = 'right'
drive =True
clock = pygame.time.Clock()

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive=False
    clock.tick(90)
    cam_x=car_x+35+cam_x_offset
    cam_y =car_y+15+cam_y_offset


    right_px = window.get_at((cam_x+focal_dis,cam_y))[0]
    up_px = window.get_at((cam_x , cam_y-focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis ))[0]

    print(right_px,up_px,down_px)

    #direction
    if direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        cam_y_offset=0
        cam_x_offset = -19
        car_x += 26
        car = pygame.transform.rotate(car,90)

    elif direction == 'up' and right_px == 255 and up_px != 255:
        direction = 'right'
        cam_y_offset=0
        cam_x_offset = 0
        car_x += 25
        car = pygame.transform.rotate(car,-90)
    elif direction == 'right' and down_px == 255 and right_px != 255:
        direction = 'down'
        cam_y_offset = 20
        cam_x_offset = -19
        car_x += 20
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        cam_y_offset = 0
        cam_x_offset = 12
        car_x += 35
        car_y +=24
        car = pygame.transform.rotate(car, 90)


    #drive
    if  direction == 'right' and right_px == 255:
        car_x = car_x + 2

    elif direction == 'up' and up_px == 255:
        car_y = car_y-2
    elif direction == 'down' and down_px == 255:
        car_y = car_y+2

    window.blit(map,(0,0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()
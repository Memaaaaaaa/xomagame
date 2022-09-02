import pygame as pg
pg.init()
scr = pg.display.set_mode((500, 500))
import time
#загрузка изображений
go1 = pg.image.load("mouse.png")
go2 = pg.image.load("mouse 2.png")
go3 = pg.image.load("mouse mirror.png")
go4 = pg.image.load("mouse mirror 2.png")
go5 = pg.image.load("mouse down.png")
go6 = pg.image.load("mouse down 2.png")
go7 = pg.image.load("mouse down mirror 2.png")
go8 = pg.image.load("mouse down mirror.png")
go9 = pg.image.load("mouse up.png")
go10 = pg.image.load("mouse up mirror.png")
go11 = pg.image.load("mouse mirror.png")
eat = pg.image.load("eat.png")
eat2 = pg.image.load("eat 2.png")
eat3 = pg.image.load("eat 3.png")
down1 = pg.image.load("down cloud.png")
down2 = pg.image.load("down cloud mirror.png")
up1 = pg.image.load("up crocodile.png")
up2 = pg.image.load("up crocodile mirror.png")
street = pg.image.load("street.jpg")
street1 = pg.image.load("street1.png")
street2 = pg.image.load("street2.png")
street3 = pg.image.load("street3.png")
street4 = pg.image.load("street4.png")


go1 = pg.transform.scale(go1.convert_alpha(), (120, 120))
go2 = pg.transform.scale(go2.convert_alpha(), (120, 120))
go3 = pg.transform.scale(go3.convert_alpha(), (120, 120))
go4 = pg.transform.scale(go4.convert_alpha(), (120, 120))
go9 = pg.transform.scale(go9.convert_alpha(), (120, 120))
go10 = pg.transform.scale(go10.convert_alpha(), (120, 120))
go5 = pg.transform.scale(go5.convert_alpha(), (120, 120))
go6 = pg.transform.scale(go6.convert_alpha(), (120, 120))
go7 = pg.transform.scale(go7.convert_alpha(), (120, 120))
go8 = pg.transform.scale(go8.convert_alpha(), (120, 120))
up1 = pg.transform.scale(up1.convert_alpha(), (160, 160))
up2 = pg.transform.scale(up2.convert_alpha(), (80, 80))
down1 = pg.transform.scale(down1.convert_alpha(), (300, 300))
down2 = pg.transform.scale(down2.convert_alpha(), (300, 300))

jump = False
rol = False

a = 1

loose = False

f = pg.font.SysFont('serif', 20) # шрифт и его размер
w = pg.font.SysFont('serif', 50) # шрифт и его размер

jump_break = False

x_player = 185
y_player = 360

mid = 185
left_x = 35
right_x = 335

go_left = False
go_right = False

eat_x_speed = -10
eat_y_speed = 10

crop_speed = 8

#еда
import random
z = random.randint(1, 3)
if z == 1:
    x_eat = 180
    y_eat = 205
    crop = 45
    eat_x_speed = -10
    eat_y_speed = 10
if z == 2:
    x_eat = 230
    y_eat = 205
    crop = 45
    eat_x_speed = -3
    eat_y_speed = 10
if z == 3:
    x_eat = 270
    y_eat = 205
    crop = 45
    eat_x_speed = 4
    eat_y_speed = 10
#крокодил
import random
q = random.randint(1, 3)
if q == 1:
        x_enemy = 185
        y_enemy = 200
        cropUp = 45
        up_x_speed = -11
        up_y_speed = 10
if q == 2:
        x_enemy = 220
        y_enemy = 200
        cropUp = 45
        up_x_speed = -4
        up_y_speed = 10
if q == 3:
        x_enemy = 240
        y_enemy = 200
        cropUp = 45
        up_x_speed = 4
        up_y_speed = 10
#подкат облако
import random
s = random.randint(1, 3)
if s == 1:
        x_cloud = 190
        y_cloud = 150
        cropDown = 45
        down_x_speed = -55
        down_y_speed = 2
if s == 2:
        x_cloud = 200
        y_cloud = 150
        cropDown = 45
        down_x_speed = -33
        down_y_speed = 2
if s == 3:
        x_cloud = 210
        y_cloud = 150
        cropDown = 45
        down_x_speed = -12
        down_y_speed = 2

score = 0

run = True
while run:
    #экран
    scr = pg.display.set_mode((500, 500))
    text_score = f.render(str(score), False, (0, 0, 0))  # создание надписи score
    text_score1 = f.render("THE END", False, (200, 0, 0))  # создание надписи score

    while loose:
        scr = pg.display.set_mode((500, 500))
        scr.fill((0, 0, 0))
        scr.blit(text_score1, (200, 250))
        pg.display.flip()
        for i in pg.event.get():
            # закрытие экрана
            if i.type == pg.QUIT:
                run = False
                loose = False
            if i.type == pg.KEYDOWN:
                jump = False
                rol = False
                a = 1
                loose = False
                jump_break = False
                x_player = 185
                y_player = 360
                mid = 185
                left_x = 35
                right_x = 335
                go_left = False
                go_right = False
                eat_x_speed = -10
                eat_y_speed = 10
                crop_speed = 8
                # еда
                import random
                z = random.randint(1, 3)
                if z == 1:
                    x_eat = 180
                    y_eat = 205
                    crop = 45
                    eat_x_speed = -10
                    eat_y_speed = 10
                if z == 2:
                    x_eat = 230
                    y_eat = 205
                    crop = 45
                    eat_x_speed = -3
                    eat_y_speed = 10
                if z == 3:
                    x_eat = 270
                    y_eat = 205
                    crop = 45
                    eat_x_speed = 4
                    eat_y_speed = 10
                # крокодил
                import random
                q = random.randint(1, 3)
                if q == 1:
                    x_enemy = 185
                    y_enemy = 200
                    cropUp = 45
                    up_x_speed = -11
                    up_y_speed = 10
                if q == 2:
                    x_enemy = 220
                    y_enemy = 200
                    cropUp = 45
                    up_x_speed = -4
                    up_y_speed = 10
                if q == 3:
                    x_enemy = 240
                    y_enemy = 200
                    cropUp = 45
                    up_x_speed = 4
                    up_y_speed = 10
                # подкат облако
                import random
                s = random.randint(1, 3)
                if s == 1:
                    x_cloud = 190
                    y_cloud = 200
                    cropDown = 45
                    down_x_speed = -55
                    down_y_speed = 2
                if s == 2:
                    x_cloud = 200
                    y_cloud = 200
                    cropDown = 45
                    down_x_speed = -33
                    down_y_speed = 2
                if s == 3:
                    x_cloud = 210
                    y_cloud = 200
                    cropDown = 45
                    down_x_speed = -12
                    down_y_speed = 2
                score = 0
                run = True

    #фон
    if a == 1:
        scr.blit(street1, (0,  0))
    if a == 2:
        scr.blit(street2, (0, 0))
    if a == 3:
        scr.blit(street3, (0, 0))
    if a == 4:
        scr.blit(street4, (0, 0))

    scr.blit(text_score, (10, 10))
    #еда
    if z == 1:
        crop_speed = 8
        cropEat = pg.transform.scale(eat.convert_alpha(), (crop, crop))
        cropEat2 = pg.transform.scale(eat2.convert_alpha(), (crop, crop))
        cropEat3 = pg.transform.scale(eat3.convert_alpha(), (crop, crop))
        eat_x_speed = -10
        eat_y_speed = 10
    if z == 2:
        crop_speed = 8
        cropEat = pg.transform.scale(eat.convert_alpha(), (crop, crop))
        cropEat2 = pg.transform.scale(eat2.convert_alpha(), (crop, crop))
        cropEat3 = pg.transform.scale(eat3.convert_alpha(), (crop, crop))
        eat_x_speed = -3
        eat_y_speed = 10
    if z == 3:
        crop_speed = 8
        cropEat = pg.transform.scale(eat.convert_alpha(), (crop, crop))
        cropEat2 = pg.transform.scale(eat2.convert_alpha(), (crop, crop))
        cropEat3 = pg.transform.scale(eat3.convert_alpha(), (crop, crop))
        eat_x_speed = 4
        eat_y_speed = 10

    if a == 1:    scr.blit(cropEat3, (x_eat, y_eat))
    if a == 2:    scr.blit(cropEat, (x_eat, y_eat))
    if a == 3:    scr.blit(cropEat2, (x_eat, y_eat))
    if a == 4:    scr.blit(cropEat, (x_eat, y_eat))

    if y_eat > 360:
        if x_player == left_x and z == 1:
            score = score + 1
        if x_player == right_x and z == 3:
            score = score + 1
        if x_player == mid and z == 2:
            score = score + 1
        z = random.randint(1, 3)
        crop = 45
        if z == 1:
            x_eat = 180
            y_eat = 205
            eat_x_speed = -10
            eat_y_speed = 10
        if z == 2:
            x_eat = 230
            y_eat = 205
            eat_x_speed = -3
            eat_y_speed = 10
        if z == 3:
            x_eat = 270
            y_eat = 205
            eat_x_speed = 4
            eat_y_speed = 10
    #крокодил

    if q == 1:
        cropUp_speed = 8
        cropEnemy = pg.transform.scale(up1.convert_alpha(), (cropUp, cropUp))
        up_x_speed = -11
        up_y_speed = 10
    if q == 2:
        cropUp_speed = 8
        cropEnemy = pg.transform.scale(up1.convert_alpha(), (cropUp, cropUp))
        up_x_speed = -4
        up_y_speed = 10
    if q == 3:
        cropUp_speed = 8
        cropEnemy = pg.transform.scale(up1.convert_alpha(), (cropUp, cropUp))
        up_x_speed = 4
        up_y_speed = 10

    scr.blit(cropEnemy, (x_enemy, y_enemy))

    if y_enemy > 370:
        q = random.randint(1, 3)
        if q == 1:
            x_enemy = 185
            y_enemy = 200
            cropUp = 45
            up_x_speed = -11
            up_y_speed = 10
        if q == 2:
            x_enemy = 220
            y_enemy = 200
            cropUp = 45
            up_x_speed = -4
            up_y_speed = 10
        if q == 3:
            x_enemy = 240
            y_enemy = 200
            cropUp = 45
            up_x_speed = 4
            up_y_speed = 10

    #облака

    if s == 1:
        cropDown_speed = 70
        cropCloud = pg.transform.scale(down1.convert_alpha(), (cropDown, cropDown))
        cropCloud2 = pg.transform.scale(down2.convert_alpha(), (cropDown, cropDown))
        down_x_speed = -55
        down_y_speed = 2
    if s == 2:
        cropDown_speed = 70
        cropCloud = pg.transform.scale(down1.convert_alpha(), (cropDown, cropDown))
        cropCloud2 = pg.transform.scale(down2.convert_alpha(), (cropDown, cropDown))
        down_x_speed = -33
        down_y_speed = 2
    if s == 3:
        cropDown_speed = 70
        cropCloud = pg.transform.scale(down1.convert_alpha(), (cropDown, cropDown))
        cropCloud2 = pg.transform.scale(down2.convert_alpha(), (cropDown, cropDown))
        down_x_speed = -12
        down_y_speed = 2

    if a % 2 == 0:    scr.blit(cropCloud, (x_cloud, y_cloud))
    if a % 2 == 1:    scr.blit(cropCloud2, (x_cloud, y_cloud))


    if y_cloud > 180:
        s = random.randint(1, 3)
        if s == 1:
            x_cloud = 190
            y_cloud = 150
            cropDown = 50
            down_x_speed = -55
            down_y_speed = 2
        if s == 2:
            x_cloud = 200
            y_cloud = 150
            cropDown = 50
            down_x_speed = -33
            down_y_speed = 2
        if s == 3:
            x_cloud = 210
            y_cloud = 150
            cropDown = 50
            down_x_speed = -12
            down_y_speed = 2


    #подкат
    if rol:
        if a == 1:
            rol = False
        elif a == 1:
            scr.blit(go5, (x_player, y_player))
        elif a == 2:
            scr.blit(go6, (x_player, y_player))
        elif a == 3:
            scr.blit(go7, (x_player, y_player))
        elif a == 4:
            scr.blit(go8, (x_player, y_player))
    #проигрыш крокодил
    if y_enemy > 330:
        if q == 1 and x_player == 35 and not jump:
            loose = True
        if q == 2 and x_player == 185 and not jump:
            loose = True
        if q == 3 and x_player == 335 and not jump:
            loose = True

    #проигрыш облако
    if y_cloud > 165:
        print("kjhgfdrsxdcfgvnj")
        if s == 1 and x_player == 35 and not rol:
            loose = True
        if s == 2 and x_player == 185 and not rol:
            loose = True
        if s == 3 and x_player == 335 and not rol:
            loose = True

    print(y_cloud)
    print(loose)

    # хомяк прорисовка бега
    if not jump and not rol:
        if a == 1:
            scr.blit(go1, (x_player, y_player))
        if a == 2:
            scr.blit(go2, (x_player, y_player))
        if a == 3:
            scr.blit(go3, (x_player, y_player))
        if a == 4:
            scr.blit(go4, (x_player, y_player))

    #хомк прыг
    if jump:
        if jump_break == True and a == 1:
            jump = False
        if a == 1 and not jump_break:
            scr.blit(go9, (x_player, y_player - 80))
            jump_break = True
        elif a % 2 == 0:
            scr.blit(go9, (x_player, y_player - 80))
        else:
            scr.blit(go10, (x_player, y_player - 80))

    #управление
    if go_left and x_player > left_breake:
        x_player = x_player - 50
    else:
        go_left = False

    if go_right and x_player < right_breake:
        x_player = x_player + 50
    else:
        go_right = False

    #закрытие экрана
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
    #управление
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_LEFT:
                if x_player == mid:
                    go_left = True
                    left_breake = left_x
                if x_player == right_x:
                    go_left = True
                    left_breake = mid
            if i.key == pg.K_RIGHT:
                if x_player == mid:
                    go_right = True
                    right_breake = right_x
                if x_player == left_x:
                    go_right = True
                    right_breake = mid
            if i.key == pg.K_UP and not rol:
                jump = True
                jump_break = False
                a = 1
            if i.key == pg.K_DOWN and not jump:
                rol = True
                a = 1

    x_eat = x_eat + eat_x_speed
    y_eat = y_eat + eat_y_speed
    crop = crop + crop_speed
    x_enemy = x_enemy + up_x_speed
    y_enemy = y_enemy + up_y_speed
    cropUp = cropUp + crop_speed
    x_cloud = x_cloud + down_x_speed
    y_cloud = y_cloud + down_y_speed
    cropDown = cropDown + cropDown_speed

    #счётчик кадров
    a = a + 1
    if a == 5:
        a = 1

    time.sleep(0.2)
    pg.display.flip()
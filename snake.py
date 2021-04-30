import pygame, time, random

pygame.init()
apple = pygame.image.load("apple.png")
apple_rect = apple.get_rect()
colours = {
    "white" : (255,255,255),
    "black" : (0,0,0),
    "red" : (255,0,0),
    "blue" : (0, 0, 255),
    "green" : (0, 179, 0),
    "yellow" : (255, 255, 179)
}
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Snake Dominika')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("comicsansms", 20)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Wynik: " + str(score), True, colours["black"])
    screen.blit(value, [0, 0])

def timer(start_time):
    now_time = int(time.time() - start_time)
    value = score_font.render("Czas: " + str(now_time), True, colours["black"])
    screen.blit(value, [200, 0])
    return now_time

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, colours["green"], [x[0], x[1], snake_block, snake_block])

def message(msg,color,position):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, position)

def food_placement():
    return round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
 
def gameLoop():
    game_over = False
    game_close = False
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = food_placement()
    foody = food_placement()
    foodx1 = food_placement()
    foody1 = food_placement()
    prev_time = None
    start_time = time.time()

    while not game_over:
        while game_close == True:
            message("Przegrana!", colours["red"],[screen_width//3, screen_height//3])
            message("Q - Wyjście", colours["red"],[screen_width//3, (screen_height//3)+50])
            message("C - Nowa gra", colours["red"],[screen_width//3, (screen_height//3)+100])
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        screen.fill(colours["yellow"])
        screen.blit(apple, (foodx, foody))
        screen.blit(apple, (foodx1, foody1))
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        now_time = timer(start_time)
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = food_placement()
            foody = food_placement()
            Length_of_snake += 1
        elif now_time % 3 == 0 and prev_time != now_time:
            foodx = food_placement()
            foody = food_placement()
            prev_time = now_time
            
        if x1 == foodx1 and y1 == foody1:
            foodx1 = food_placement()
            foody1 = food_placement()
            Length_of_snake += 1   
        elif now_time % 7 == 0 and prev_time != now_time:
            foodx1 = food_placement()
            foody1 = food_placement()
            prev_time = now_time
            
        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()
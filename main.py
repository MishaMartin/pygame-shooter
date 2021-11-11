import pygame
import os
#use os to import images from other folders

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

FPS = 60
# Hard coding a frames per second so that you can control the environment since not every computer will run as quickly as the one you're using. 60 is an industry standard for a game like this.

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    # You have to manually update once you add the drawing with the code in line 19.
    #Order of drawing matters! If we put the spaceship was infront of this, we wouldn't see it b/c this draws overtop of it after. But since it's first, it'll work.
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    #Use blit when drawing a surface onto the screen. Text and image is defined as a surface. 
    #pygame coordinate system: from top left, (0,0) so, depending on the height and width you have defined,define where you want your image.
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()
    
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    #defining, (x, y, width, height) These are creating rectangles to move your spaceships

    clock = pygame.time.Clock()
    # along with line 22, ensuring that it will never run over our defined FPS. Will only run up to this number.
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        
        draw_window(red, yellow)

    pygame.quit()



if __name__ == "__main__":
    main()
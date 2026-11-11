import pygame

def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color changing shapes")

    # Add this:
    font = pygame.font.SysFont("arial", 24)

    #Mapping of the colors names to RGB values
    colors = {
        "red": pygame.Color("Red"),
        "green": pygame.Color("Green"),
        "blue": pygame.Color("Blue"),
        "yellow": pygame.Color("Yellow"),
        "white": pygame.Color("White")
    }
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 100, 30

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        #Change color based on boundary contact
        if x == 0: current_color = colors['blue']
        elif x == screen_width - sprite_width: current_color = colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == screen_height - sprite_height:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))

        # Add this:
        text = font.render("My first game screen", True, (255, 255, 255))
        screen.blit(text, (120, 10))

        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()
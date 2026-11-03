# Example file showing a circle moving on screen
import pygame, random

# pygame setup
pygame.init()
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
random_pos_x = random.randint(0, 980)
random_pos_y = random.randint(0, 580)
pontos = 0
font = pygame.font.SysFont(None, 30)

print((pygame.time.get_ticks()) / 1000)

while running:
    random_pos = random_pos_x, random_pos_y
    texto_pontos = font.render(str(pontos), True, ("white"))
    tempo = pygame.time.get_ticks()

    if (tempo / 1000) > 30:
        pygame.time.delay(3000)
        break
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(font.render(f"Tempo: {(tempo / 1000):.0f}/30", True, "white"), (30, 10))
    screen.blit(font.render(f"Pontos:", True, "white"), (30, 30))
    screen.blit(texto_pontos, (30, 50))

    pygame.draw.circle(screen, "white", random_pos, 20)
    pygame.draw.circle(screen, "red", player_pos, 40)

    if (player_pos.x <= random_pos_x + 20 and player_pos.x >= random_pos_x - 20) and (player_pos.y <= random_pos_y + 20 and player_pos.y >= random_pos_y - 20):
        random_pos_x = random.randint(0, 980)
        random_pos_y = random.randint(0, 580)
        pontos += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if player_pos.y > height:
        player_pos.y = 0
    if player_pos.y < 0:
        player_pos.y = height
    if player_pos.x > width:
        player_pos.x = 0
    if player_pos.x < 0:
        player_pos.x = width


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

print(f"Tempo de execução: {(pygame.time.get_ticks()) / 1000}")
print(f"Total de pontos: {pontos}")
pygame.quit()

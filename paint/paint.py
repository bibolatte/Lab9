import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    points = []
    drawing = False
    eraser_mode = False

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:  # Draw circle
                    mode = 'circle'
                elif event.key == pygame.K_e:  # Eraser
                    eraser_mode = not eraser_mode
                elif event.key == pygame.K_t:  # Draw rectangle
                    mode = 'rectangle'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)
                if mode in ['rectangle', 'circle']:
                    drawing = True
                    start_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if mode in ['rectangle', 'circle']:
                    drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    end_pos = event.pos
                    if mode == 'rectangle':
                        pygame.draw.rect(screen, pygame.Color(mode), (start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 3)
                    elif mode == 'circle':
                        pygame.draw.circle(screen, pygame.Color(mode), start_pos, max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])), 3)
                elif eraser_mode and event.buttons[0]:  # Erase while left mouse button is held
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        screen.fill((255, 255, 255))

        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode in ['rectangle', 'circle']:
        color = pygame.Color(color_mode)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / max(1, iterations)
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if color_mode in ['rectangle', 'circle']:
            if color_mode == 'rectangle':
                pygame.draw.rect(screen, color, (start, (end[0] - start[0], end[1] - start[1])), 3)
            elif color_mode == 'circle':
                pygame.draw.circle(screen, color, start, max(abs(end[0] - start[0]), abs(end[1] - start[1])), 3)
        else:
            pygame.draw.circle(screen, color, (x, y), width)

main()

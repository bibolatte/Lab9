import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 5  # Reduced initial speed

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.score = 0
        self.level = 1
        self.speed = 10

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE

        # Check border collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True

        new_head = (x, y)

        # Check self-collision
        if new_head in self.body[1:]:
            return True

        self.body.insert(0, new_head)

        # Check food collision
        if new_head == food.position:
            self.score += 1
            if self.score % 3 == 0:  # Increase level every 3 foods
                self.level += 1
                self.speed += 5  # Increase speed on level up
            food.generate_position()
        else:
            self.body.pop()

        return False

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.generate_position()

    def generate_position(self):
        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)
            if (x, y) not in snake.body:
                self.position = (x, y)
                break

    def draw(self):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.position, CELL_SIZE, CELL_SIZE))

# Initialize game objects
snake = Snake()
food = Food()

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    # Move snake
    if snake.move():
        running = False  # Game over if border collision or self-collision

    # Draw objects
    snake.draw()
    food.draw()

    # Display score and level
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {snake.score} | Level: {snake.level}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(FPS)  # Adjusted FPS for reduced speed

pygame.quit()

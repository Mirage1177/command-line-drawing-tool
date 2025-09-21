import pygame
import threading

# Command registry setup
command_registry = {}
def command(name):
    def decorator(func):
        command_registry[name] = func
        return func
    return decorator

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill((255, 255, 255))
pygame.display.update()
color = (0, 0, 0)
size = 1

# Drawing commands
@command("change size")
def change_size(args):
    global size
    size = int(args[0])

@command("change color")
def change_color(args):
    global color
    color = (args[0], args[1], args[2])

@command("draw line")
def draw_line(args):
    pygame.draw.line(screen, color, (args[0], args[1]), (args[2], args[3]), size)

@command("draw circle")
def draw_circle(args):
    pygame.draw.circle(screen, color, (args[0], args[1]), args[2], size)

@command("draw polygon")
def draw_polygon(args):
    if len(args) % 2 != 0:
        print("Error: Polygon requires pairs of coordinates.")
        return
    points = [(args[i], args[i+1]) for i in range(0, len(args), 2)]
    pygame.draw.polygon(screen, color, points, size)

@command("end drawing")
def end_drawing(args=None):
    pygame.image.save(screen, 'draw.png')
    print("Drawing saved as draw.png")
    return True

# Command handler
def handle_command(prompt):
    parts = prompt.strip().split()
    possible_command = ' '.join(parts[:2]).lower()
    args = parts[2:]
    func = command_registry.get(possible_command)
    if not func:
        print(f"Unknown command: {possible_command}")
        return
    numeric_args = list(map(int, args))
    return func(numeric_args)

# Threaded input loop
def input_loop():
    while True:
        user_input = input("Enter command: ")
        close_signal = handle_command(user_input)
        pygame.display.update()
        if close_signal:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            break

# Start input thread
threading.Thread(target=input_loop, daemon=True).start()

# Main Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(50)

pygame.quit()

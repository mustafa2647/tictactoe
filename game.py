import pygame

turn = 'X'
grid = [['-' for i in range(3)] for j in range(3)]

print(grid)

pygame.init()

screen = pygame.display.set_mode((772, 772))

pygame.display.set_caption('Tic Tac Toe')
board = pygame.image.load('assets/Board.png')
x_img = pygame.image.load('assets/X.png')
o_img = pygame.image.load('assets/O.png')



running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(board, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)

    pygame.display.update()




# size = 257
# border = 10

# x = 702
# y = 420

# a =  x // size
# b =  y // size

# print(a, b)


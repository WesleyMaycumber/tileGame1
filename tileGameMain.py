
import pygame
import random
#import sys


screen_width = 1280
screen_height = 720


#Initialize the game:
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)


#Background Images --------------------------------------------------------------------------------------

filepath = 'C:/Users/wesle/OneDrive/Documents/Scripts - Python/Projects/tileGame1/Sprites/BG/'
#0 = water; 1 = grass:
#Tiles:
tile_images = {
    '0000' : pygame.image.load(f'{filepath}0000.PNG'), #Dirt Tile
    #'0001' : pygame.image.load(f'{filepath}0001.PNG'), #Water Tile
    #'0010' : pygame.image.load(f'{filepath}0010.PNG'), #Dirt Tile
    #'0100' : pygame.image.load(f'{filepath}0100.PNG'), #Water Tile
    #'1000' : pygame.image.load(f'{filepath}1000.PNG'), #Dirt Tile
    '0011' : pygame.image.load(f'{filepath}0011.PNG'), #Water Tile
    #'0101' : pygame.image.load(f'{filepath}0101.PNG'), #Dirt Tile
    '1001' : pygame.image.load(f'{filepath}1001.PNG'), #Water Tile
    '0110' : pygame.image.load(f'{filepath}0110.PNG'), #Dirt Tile
    #'1010' : pygame.image.load(f'{filepath}1010.PNG'), #Water Tile
    '1100' : pygame.image.load(f'{filepath}1100.PNG'), #Water Tile
    '0111' : pygame.image.load(f'{filepath}0111.PNG'), #Water Tile
    '1011' : pygame.image.load(f'{filepath}1011.PNG'), #Water Tile
    '1101' : pygame.image.load(f'{filepath}1101.PNG'), #Water Tile
    '1110' : pygame.image.load(f'{filepath}1110.PNG'), #Water Tile
    '1111' : pygame.image.load(f'{filepath}1111.PNG'), #Water Tile
    }

tile_height = tile_images['0000'].get_height()
tile_Width = tile_images['0000'].get_width()



#Generate Tileman
tilemap = [
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

#Add Borders to the tilemap:
def tilemap_Borders(tilemap):
    rows = len(tilemap)
    cols = len(tilemap[0])
    tilemap2 = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            # Get the surrounding tiles with proper bounds checking
            t1 = str(tilemap[i][j-1]) if j >= 1 else '0'  # Left
            t2 = str(tilemap[i-1][j]) if i >= 1 else '0'  # Top
            t3 = str(tilemap[i][j+1]) if j < cols - 1 else '0'  # Right
            t4 = str(tilemap[i+1][j]) if i < rows - 1 else '0'  # Bottom

            # Combine tiles into the string
            tile = f"{t1}{t2}{t3}{t4}"
            
            # Append to the current row
            row.append(tile)
        
        # Append the completed row to tilemap2
        tilemap2.append(row)
    
    return tilemap2


tilemap2 = tilemap_Borders(tilemap)
for row in tilemap2:
    print(row)





"""
#Draw the background:
for x in range(0, screen_width, tile_Width):
    for y in range(0, screen_height, tile_height):
        tile_image = random.choice(tiles)
        screen.blit(tile_image, (x, y))
"""
        

"""
#Characters: --I'm trying to see if I can declare a player outside of the event loop, assign it class RenderClear so it updates.
#ultimately I would like to be able to keep the background static and have sprites rendered on top of it.
player = pygame.draw.circle(screen, "red", player_pos, 15)
all_sprites = RenderClear

all_sprites.add(player)
"""

"""
#Main Loop:
while running:
    #poll for events
    #pygame.QUIT event means the user clicked the X to close out your window



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN():
            if event.key == pygame.K_ESCAPE:
                running = False
    
    #fill the screen with a color to whipe everything from the last frame:
    #screen.fill("black")

    #Render your game here



    pygame.draw.circle(screen, "red", player_pos, 15)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
"""
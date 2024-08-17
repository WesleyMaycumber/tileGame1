
import pygame
import random
"""
dungeonsize = (10,12)

#split first level
splitdims = ['x','y']

axis = random.randint(0,1)
print(f'selected axis: {splitdims[axis]}')

def splitDungeon(size, axis):
    split1 = tuple(random.randint(0,size[i]) if i == axis else size[i] for i in range(2))
    split2 = tuple(size[i]-split1[i] if i == axis else size[i] for i in range(2))
    return split1, split2


def recursiveSplit(size, splits):
    # Base case: If no more splits are needed, return the size as a single tuple in a list
    if splits == 0:
        return [size]

    # Choose a random axis to split (0 for x, 1 for y)
    axis = random.randint(0, 1)
    
    # Split the dungeon
    split1, split2 = splitDungeon(size, axis)
    
    # Recursively split the resulting dungeons
    return recursiveSplit(split1, splits - 1) + recursiveSplit(split2, splits - 1)



# Example usage
initial_size = ((1,100), (1,100))
splits = 3
final_dungeons = recursiveSplit(initial_size, splits)
print(final_dungeons)
"""




#attempt 2:

def XOrY(x,y):
    slice = random.randint(3, x + y - 9)
    if slice <= x-3:
        split = (0, slice)
    else:
        split = (1, slice - x + 3)
    return split



def splitDungeon(bounds, axis):
    # bounds: ((x_start, x_end), (y_start, y_end))
    x_start, x_end = bounds[0]
    y_start, y_end = bounds[1]

    if axis == 0:  # Split along the x-axis
        split_point = random.randint(x_start, x_end)
        split1 = ((x_start, split_point), (y_start, y_end))
        split2 = ((split_point, x_end), (y_start, y_end))
    else:  # Split along the y-axis
        split_point = random.randint(y_start, y_end)
        split1 = ((x_start, x_end), (y_start, split_point))
        split2 = ((x_start, x_end), (split_point, y_end))
    
    return split1, split2

def recursiveSplit(bounds, splits):
    # Base case: If no more splits are needed, return the current bounds as a single tuple in a list
    if splits == 0:
        return [bounds]

    # Choose a random axis to split (0 for x, 1 for y)
    axis = random.randint(0, 1)
    
    # Split the dungeon
    split1, split2 = splitDungeon(bounds, axis)
    
    # Recursively split the resulting dungeons
    return recursiveSplit(split1, splits - 1) + recursiveSplit(split2, splits - 1)

# Example usage
initial_bounds = ((0, 30), (0, 30))
splits = 3
final_dungeons = recursiveSplit(initial_bounds, splits)
for dungeon in final_dungeons:
    print(dungeon)

print(final_dungeons)



#Generate Tileman
tilemap = [
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
]

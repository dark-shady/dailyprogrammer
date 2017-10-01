#https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

def display_spiral(grid):
    print('\n'.join(''.join(c) for c in grid))
    print('\n')

a = int(input("Choose a number: "))
ccw = int(input("1 for clockwise, 2 for counter clockwise"))

grid = [['' for x in range(a)] for y in range(a)]

current_x = current_y = 0
direction_x = 0 if ccw == 2 else 1
direction_y = -1 if ccw == 2 else 0
justification = len(str(a**2)) + 1
for i in range(a**2):

    grid[current_y][current_x] = str(i + 1).ljust(justification)

    if (any((current_x + direction_x >= a, current_y - direction_y >=a,
            current_x + direction_x < 0))
        or grid[current_y - direction_y][current_x + direction_x]):

        direction_x, direction_y = -direction_y if ccw == 2 else direction_y, \
                                    direction_x if ccw == 2 else -direction_x

    current_x += direction_x
    current_y -= direction_y

display_spiral(grid)

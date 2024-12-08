from enum import Enum

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

def read_map():
    with open("input.txt", "r") as f:
        # Store obstructions positions into an array
        obs_pos = []
        start_guard = ()
        max_cols = 0
        lines = f.readlines()
        for i, line in enumerate(lines):
            max_cols = len(line)
            for j, car in enumerate(line):
                if car == "#":
                    obs_pos.append((i, j))
                if car == Direction.UP.value:
                    start_guard = [i, j]
                    
    f.close()
    return obs_pos, start_guard, len(lines), max_cols
    
        
def first_part(start_guard, obs_pos, max_i, max_j):
    num_of_positions = 0
    pos_done = []
    posGuard, dirGuard = start_guard, Direction.UP
    while(posGuard[0] < max_i and posGuard[0] > 0 and posGuard[1] < max_j and posGuard[1] > 0):

        if dirGuard == Direction.UP:
            if (posGuard[0] - 1, posGuard[1]) in obs_pos:
                dirGuard = Direction.RIGHT
            else:
                if posGuard in pos_done:
                    posGuard[0]-=1 
                else:
                    num_of_positions += 1
                    pos_done.append(posGuard.copy())
                    posGuard[0]-=1
                    
        elif dirGuard == Direction.RIGHT:
            if (posGuard[0], posGuard[1] + 1) in obs_pos:
                dirGuard = Direction.DOWN
            else:
                if posGuard in pos_done:
                    posGuard[1]+=1 
                else:
                    num_of_positions += 1
                    pos_done.append(posGuard.copy())
                    posGuard[1]+=1
                    
        elif dirGuard == Direction.DOWN:
            if (posGuard[0] + 1, posGuard[1]) in obs_pos:
                dirGuard = Direction.LEFT
            else:
                if posGuard in pos_done:
                    posGuard[0]+=1 
                else:
                    num_of_positions += 1
                    pos_done.append(posGuard.copy())
                    posGuard[0]+=1
        elif dirGuard == Direction.LEFT:
            if (posGuard[0], posGuard[1] - 1) in obs_pos:
                dirGuard = Direction.UP
            else:
                if posGuard in pos_done:
                    posGuard[1]-=1 
                else:
                    num_of_positions += 1
                    pos_done.append(posGuard.copy())
                    posGuard[1]-=1
    
    return num_of_positions
        

if __name__ == "__main__":
    obs_pos, start_guard, max_i, max_j = read_map()
    print(f"Number of positions (Part 1) : {first_part(start_guard, obs_pos, max_i, max_j)}")
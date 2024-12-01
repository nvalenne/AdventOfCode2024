# Open the input file as read mode
with open("input.txt", "r") as input:
    leftArr = []
    rightArr = []
    
    for line in input:
        # Split the two numbers on each line then store in the arrays
        col1, col2 = map(int, line.split())
        leftArr.append(col1)
        rightArr.append(col2)

# Close the file    
input.close()

def calculate_distance(array1, array2):    
    # Sort by asc
    array1.sort()
    array2.sort()
    
    # Compare between the two arrays to calculte the distance
    distTotal = 0
    for i in range(0, len(array1)):
        dist = 0
        left = array1[i]
        right = array2[i]
        
        # Convert into absolute value if the distance is negative
        dist = abs(left - right)
            
        # Add the dist to the sum    
        distTotal += dist
    return distTotal
    
distTotal = calculate_distance(leftArr, rightArr)
print(distTotal)


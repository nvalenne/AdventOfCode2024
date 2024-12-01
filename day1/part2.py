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

similiraty_score = 0
# To calculate the similarity score, we need to mulitply each number
for number in leftArr:
    # Get the occurences for the current number, multiplied by the number, then add to the result
    similiraty_score += number * rightArr.count(number)
    
print(similiraty_score)

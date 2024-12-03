import re

with open("input.txt", "r") as f:
    corrupted_mem = f.read()
    # RegEx pattern to find the good syntax into the text
    pattern = "mul[(][0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9][)]"
    mem_cleaned = re.findall(pattern, corrupted_mem)

    # Extract each multiplication and do the sum
    sum = 0
    for el in mem_cleaned:
        # Remove "mul" and convert string to tuple
        numbers = el.replace("mul", "")
        numbers = eval(numbers)

        # Do the multiplication and add to the result
        sum += numbers[0] * numbers[1]

    print(sum)
        

# Close the file
f.close()
    
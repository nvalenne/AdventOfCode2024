import re

with open("input.txt", "r") as f:
    corrupted_mem = f.read()
    # Same regex pattern + add 2 more patterns where do() and don't()
    pattern = "mul[(][0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9][)]|do[(][)]|don't[(][)]"
    mem_cleaned = re.findall(pattern, corrupted_mem)

    # Extract each multiplication and do the sum
    sum = 0
    mul_enabled = True
    for el in mem_cleaned:
        # Check if element is an instruction
        if el == "do()":
            mul_enabled = True
        elif el == "don't()":
            mul_enabled = False
        else:
            # Calculate only if instructions are enabled    
            if mul_enabled:
                # Remove "mul" and convert string to tuple
                numbers = el.replace("mul", "")
                numbers = eval(numbers)
                # Do the multiplication and add to the result
                sum += numbers[0] * numbers[1]

    print(sum)
        

# Close the file
f.close()
    
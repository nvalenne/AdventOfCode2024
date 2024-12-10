"""
Read the data and give an array of dictionnaries
Returns:
    equations: list[dict]
"""
def read_equations():
    with open("input.txt", "r") as f:
        equations = []
        for line in f.readlines():
            arr = line.split(":")

            # Convert strings to integers
            equations.append({
                "result": int(arr[0]),
                "numbers": [int(val) for val in arr[1].strip().split()]
            })
    f.close()
    return equations

"""
Recursive function to determine if the current equation can be solved
Params:
    eq          : dict      = the equation
    i           : int (opt) = index in the array
    t_next      : int (opt) = next value in the array
    temp_result : int (opt) = sum or multiply value

Returns: Boolean
"""
def is_equation_solvable(eq, i=None, t_next=None, temp_result=None, has_concat=False):
    # Executed on the first iteration
    if not i and not t_next and not temp_result:
        sum = eq["numbers"][0] + eq["numbers"][1]
        multiply = eq["numbers"][0] * eq["numbers"][1]
        concat = str(eq["numbers"][0]) + str(eq["numbers"][1])
        i = 1
    else:
        sum = temp_result + t_next
        multiply = temp_result * t_next
        concat = str(temp_result) + str(t_next)
    
    # End condition of the recursive function (when it reachs the end of the array)
    if len(eq["numbers"]) == i+1:
        if has_concat:
            if sum == eq["result"] or multiply == eq["result"] or int(concat) == eq["result"]:
                return True
            else:
                return False
        # return if the equation can be solved
        else:
            if sum == eq["result"] or multiply == eq["result"]:
                return True
            else:
                return False
    else:
        if has_concat:
            return is_equation_solvable(eq, i+1, eq["numbers"][i+1], sum, has_concat=True) or is_equation_solvable(eq, i+1, eq["numbers"][i+1], multiply, has_concat=True) or is_equation_solvable(eq, i+1, eq["numbers"][i+1], int(concat), has_concat=True)
        else: 
            return is_equation_solvable(eq, i+1, eq["numbers"][i+1], sum) or is_equation_solvable(eq, i+1, eq["numbers"][i+1], multiply)
    
"""
The puzzle answer of the part 1
Returns: 
    calibration_result: int
"""
def first_part():
    equations = read_equations()
    calibration_result = 0
    for eq in equations:
        if (is_equation_solvable(eq)):
            calibration_result += eq["result"]
    return calibration_result

"""
The puzzle answer of the part 2
"""
def second_part():
    equations = read_equations()
    calibration_result = 0
    for eq in equations:
        if (is_equation_solvable(eq, has_concat=True)):
            calibration_result += eq["result"]
    return calibration_result


if __name__ == "__main__":
    print(f"Part One: {first_part()}")
    print(f"Part Two: {second_part()}")
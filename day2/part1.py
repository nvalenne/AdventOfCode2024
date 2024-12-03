
with open("input.txt") as f:
    # Remove new line
    data = f.read().split("\n")
    # Remove spaces between numbers and get double arrays
    reportsArr = [x.split(" ") for x in data] 

    """
        After opening the file and extract data, it's time to use this unusual data
    """
    reportsSafe = 0
    for report in reportsArr:
        arrDiff = []
        # Get an array with the diffs between each values
        # Exemple : [-1, -1, -2, -3, -1]
        for i in range(len(report)-1):
            arrDiff.append(int(report[i+1]) - int(report[i]))

        increasing = all(int(diff) > 0 for diff in arrDiff)
        decreasing = all(int(diff) < 0 for diff in arrDiff)
        goodDiff = all(int(abs(diff)) >= 1 and int(abs(diff)) <= 3 for diff in arrDiff)

        # print(f'Array{arrDiff}\nIncreasing : {increasing}\n Decreasing : {decreasing}\n Good diff ?{goodDiff}\n\n')
        # If the two conditions are True, then it's a safe report
        if (goodDiff and (increasing or decreasing)):
            reportsSafe+=1
            print(f'[VERIFIED] \tArray ---{report}---Diff {arrDiff}')
        else:
            print(f'[NOT VERIFIED] \tArray ---{report}---Diff {arrDiff}')
    f.close() # Close the file
    print(reportsSafe)
    

        
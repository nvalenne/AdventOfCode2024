def is_report_safe(report):
    increasing = all(int(diff) > 0 for diff in report)
    decreasing = all(int(diff) < 0 for diff in report)
    goodDiff = all(int(diff) >= -3 and int(diff) <= 3 and int(diff) != 0 for diff in report)

    return goodDiff and (increasing or decreasing)


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


        # If the two conditions are True, then it's a safe report
        if (is_report_safe(arrDiff)):
            reportsSafe+=1

        else:
            for i in range(len(arrDiff)):
                arrDiffVariant = arrDiff.copy()
                arrDiffVariant.pop(i)
                if (is_report_safe(arrDiffVariant)):
                    reportsSafe+=1
                    print(f'[VERIFIED WITH ERROR] \tArray ---{report} with {arrDiffVariant}')
                    break
            
            
    
    f.close() # Close the file
    print(reportsSafe)
    

        
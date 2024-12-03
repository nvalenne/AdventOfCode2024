# Part 1

In this part, we have to determine how many of these 1000 reports are safe.

Conditions for a report to be safe:
1. The levels are either all increasing or all decreasing.
2. Any two adjacent levels differ by at least one and at most three.

## Solution

### 1. Open the input file `input.txt`
```py
with open("input.txt") as f:
    # Remove new line
    data = f.read().split("\n")
    # Remove spaces between numbers and get double arrays
    reportsArr = [x.split(" ") for x in data] 
    ...
```

### 2. Check for each line (one report)

```py
    reportsSafe = 0
    for report in reportsArr:
        arrDiff = []
        # Get an array with the diffs between each values
        # Exemple : [-1, -1, -2, -3, -1]
        for i in range(len(report)-1):
            arrDiff.append(int(report[i+1]) - int(report[i]))
        ...

```

#### 2.1 If levels are increasing or decreasing
```py
        ...
        increasing = all(int(diff) > 0 for diff in arrDiff)
        decreasing = all(int(diff) < 0 for diff in arrDiff)
        ...
```
#### 2.2 If level value between each of them differ between 1 and 3
#### 2.3 Register +1 for each safe report
```py
    ...
        # If the two conditions are True, then it's a safe report
        if (goodDiff and (increasing or decreasing)):
            reportsSafe+=1
    ...
```
### 3. Close the file and print the amount of safe reports 
```py
    f.close() # Close the file
    print(reportsSafe)
```



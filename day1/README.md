# Part 1

input.txt
```py
3   4
4   3
2   5
1   3
3   9
3   3
...
```

Split in two arrays
```py
left = [3,4,2,1,3,3]
right = [4,3,5,3,9,3]
```

Order by ascendant
```py
left = [1,2,3,3,3,4]
right = [3,3,3,4,5,9]
```

Comparison of all numbers in the two lists to get the distances \
`=> 3  - 1 	= 2` 	\
`=> 3  - 2	= 1`	\
`=> 3  - 3	= 0`	\
`=> 4  - 3	= 1`	\
`=> 5  - 3	= 2`	\
`=> 9 - 4	= 5`

Sum of all the distances
`2 + 1 + 0 + 1 + 2 + 5 = 11`

Total distance = `8`

For input.txt, the result is 


## Algorithm
```
- Open the file "input.txt"

For each line in file:

	leftArr, rightArr: [], []
	leftCol, rightCol = map(int, line.split())
	leftArr.append(leftCol)
	rightArr.append(rightCol)

- Close the file

- Sort by asc the two arrays

distTotal: 0
For each line:
	dist: 0
	left: leftArr[i]
	right: rightArr[i]

	dist: absolute of (right - left)

	distTotal += dist
```

# Part 2

In this part, we have to find the similarity score

input.txt
```py
3   4
4   3
2   5
1   3
3   9
3   3
...
```

1. Browse the left list
2. For each number, count the number of occurences in the right list
3. Multiply the number himself by his number of occurences
4. Calculate the sum of the results to get the similarity score

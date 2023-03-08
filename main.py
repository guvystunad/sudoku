sudoku = [
[[2, 1, 9], [5, 4, 3], [6, 7, 8]],
[[5, 4, 3], [8, 7, 6], [9, 1, 2]],
[[8, 7, 6], [2, 1, 9], [3, 4, 5]],
[[4, 3, 2], [7, 6, 5], [8, 9, 1]],
[[7, 6, 5], [1, 9, 8], [2, 3, 4]],
[[1, 9, 8], [4, 3, 2], [5, 6, 7]],
[[3, 2, 1], [6, 5, 4], [7, 8, 9]],
[[6, 5, 4], [9, 8, 7], [1, 2, 3]],
[[9, 8, 7], [3, 2, 1], [4, 5, 6]],
]

import copy
üks = copy.deepcopy(sudoku)
kaks = copy.deepcopy(sudoku)
kolm = copy.deepcopy(sudoku)
neli = copy.deepcopy(sudoku)
viis = copy.deepcopy(sudoku)
kuus = copy.deepcopy(sudoku)
seitse = copy.deepcopy(sudoku)
kaheksa = copy.deepcopy(sudoku)
üheksa = copy.deepcopy(sudoku)

for rida in üks:
    for kolmik in rida:
        if 1 in kolmik:
            for i in range(len(kolmik)):
                if kolmik[i] != 1:
                    kolmik[i] = 0
        else:
            for i in range(len(kolmik)):
                kolmik[i] = 'x'
        print(kolmik)
print(üks)
print(sudoku)

for rida in kaks:
    for kolmik in rida:
        for i in range(len(kolmik)):
            if kolmik[i] != 2:
                kolmik[i] = 0


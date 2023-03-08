sudoku = [
[[2, '', 9], ['', '', ''], [6, '', '']],
[['', 4, ''], [8, 7, ''], ['', 1, 2]],
[[8, '', ''], ['', 1, 9], ['', 4, '']],
[['', 3, ''], [7, '', ''], [8, '', 1]],
[['', 6, 5], ['', '', 8], ['', 3, '']],
[[1, '', ''], ['', 3, ''], ['', '', 7]],
[['', '', ''], [6, 5, ''], [7, '', 9]],
[[6, '', 4], ['', '', ''], ['', 2, '']],
[['', 8, 7], [3, '', 1], [4, 5, '']],
]

import copy
üks = copy.deepcopy(sudoku)

for rida in üks:
    for kolmik in rida:
        if 1 not in kolmik:
            for i in range(len(kolmik)):
                if kolmik[i] != '':
                    kolmik[i] = 0
                else:
                    kolmik[i] = 'x'
        else:
            for kolmik in rida:
                for i in range(len(kolmik)):
                    if kolmik[i] != 1:
                        kolmik[i] = 0

def uue_maatriksi_loomine(sudoku : list, number : int):
    for rida in sudoku:
        for kolmik in rida:
            if number not in kolmik:
                for i in range(len(kolmik)):
                    if kolmik[i] != '':
                        kolmik[i] = 0
                    else:
                        kolmik[i] = 'x'
            else:
                for kolmik in rida:
                    for i in range(len(kolmik)):
                        if kolmik[i] != number:
                            kolmik[i] = 0


for rida in üks:
    print(rida)
print(sudoku)


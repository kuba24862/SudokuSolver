import sudoku

print("Zadejete prosím jednotlivé řádky sudoku")
zadano = ["","","","","","","","","",]
mezi = ""
for i in range(9):     
    while True:
        if len(zadano[i]) == 9:
            break
        zadano[i] = input("řádek " + str(i+ 1) +": ")

vysldnesudoku = [[],[],[],[],[],[],[],[],[]]

for i in range(9):
    for y in range(9):
        vysldnesudoku[i].append(int(zadano[i][y]))

sudoej = sudoku.Sudokusolve(vysldnesudoku)

vysledke =sudoej.solve()

print(vysledke)
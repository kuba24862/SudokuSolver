# Dokumentace k programu na řešení sudoku:
Jednoduchá python aplikace/knihovna pro hledání řešení sudoku
# Požadavky

Python 3.8.0 (měl by fungovat jakýkoliv python 3+)
 Instalace knihovny numpy (python -m pip install notebook numpy scipy imageio matplotlib pillow)
 program je určen na použití jako

- knihovna (import sudoku)
- vyřešení zadaného sudoku (spustit main.py)

# Použití jako modul

## Vyřešení sudoku:

1. Vytvoření objektu třídy Sudokusolve(sudoku)

sudoku – seznam s sudokem

1. Zavolání metody solve

## Nápověda při řešení sudoku

1. Vytvoření objektu třídy Sudokusolve(sudoku)

sudoku – seznam s sudokem

1. Zavolání metody allChoice

# Použití pro vyřešení sudoku

# Třídy:

## SudokuChoice

Třída která se zabývá vypočtu chybějících čísel v zadaných sloupců, řádcích a čtverců

### Argumenty

sudoku {seznam} -- [[line1][line2][line3]...]
 [[5 3 0 0 7 0 0 0 0]
 [6 0 0 1 9 5 0 0 0]
 [0 9 8 0 0 0 0 6 0]
 [8 0 0 0 6 0 0 0 3]
 [4 0 0 8 0 3 0 0 1]
 [7 0 0 0 2 0 0 0 6]
 [0 6 0 0 0 0 2 8 0]
 [0 0 0 4 1 9 0 0 5]
 [0 0 0 0 8 0 0 7 9]]

### Metody

#### Square(self,line, Colums)

- Vrací prvky které chybí v daném čtverci
- Jako argumenty bere adresu daného čtverce (řádek, sloupec)

#### Lines(self,line)

- Vrací prvky které chybí v daném řádku
- Jako argument bere číslo řádku

#### Colums(self , Colums)

- Vrací prvky které chybí v daném řádku
- Jako argument bere číslo sloupce

## Sudokusolve

Řeší sudoku

### Argumenty

sudoku {seznam} -- [[line1][line2][line3]...]

[[5 3 0 0 7 0 0 0 0]
 [6 0 0 1 9 5 0 0 0]
 [0 9 8 0 0 0 0 6 0]
 [8 0 0 0 6 0 0 0 3]
 [4 0 0 8 0 3 0 0 1]
 [7 0 0 0 2 0 0 0 6]
 [0 6 0 0 0 0 2 8 0]
 [0 0 0 4 1 9 0 0 5]
 [0 0 0 0 8 0 0 7 9]]

### Dědičnost

Dědění probíhá z třídy SudokuChoice

### Metody

#### getCount(self)

- Vrací počet průběhu programu

#### solve(self)

- Vrací vyřešené sudoku

#### allChoice(self)

- Vrací sudoku kde na místech kde není jisté, co je , přidá seznam s možnostmi které jsou na daném místě možné
- Používá zděděné metody ze sudokuChoice

####

####

import numpy


class SudokuChoice():
    def __init__(self, sudoku):
        """Třídá která se zabývá vypočtu chybějicích čísel v zadaných sloupcí, řádcích a čtverců
    
        Arguments:   sudoku {array} -- [[line1][line2][line3]...]
        """
        self.sudokuNum = numpy.array(sudoku)

    def square(self, line, colums):
        """Jaké prvky chybí na daném sloupci 
        
        Arguments:
            line {int} -- kolikáty čtverec z vrchu to je ?
            colums {[type]} -- kolikáty čtverec z leva to je ?
        
        Returns:
            set -- množina ve které jsou chybějící prvky v daném čtverci
        """
        line = line*3
        colums = colums*3
        sudoku = self.sudokuNum
        sudoku = sudoku[range(line,line +3), colums:colums+3].tolist()
        # výběr daného čterce
        
        allnum = {1,2,3,4,5,6,7,8,9}
        # množina se všema čísla
        out = allnum - set(sudoku[0] + sudoku[1] + sudoku[2])
        # sloučení jedotlivých polí do jednoho pole
        #  převede se na množinu
        #  provede se rozdíl množin (vzniknemi co mi chybí)
        return out

    def lines(self, line):
        allnum = {1,2,3,4,5,6,7,8,9}
        # množina se všema čísla
        out = allnum - set(self.sudokuNum[line])
        # provede se rozdíl množin (vzniknemi co mi chybí)
        return out

    def colums(self, colums):
        allnum = {1,2,3,4,5,6,7,8,9}
        # množina se všema čísla
        out = allnum - set(self.sudokuNum[:, colums])
        # provede se rozdíl množin (vzniknemi co mi chybí)

        return out 

class Sudokusolve(SudokuChoice):
    """Třídá která se zabývá řešení sudoku, dědí ze Sudoku choice
    
    Arguments:
        sudoku {array} -- [[line1][line2][line3]...]
    
    """
    def __init__(self, sudoku):
        self.sudokuNum = numpy.array(sudoku)
        # převádím na rozšířený array kvůli manimuplacím a jednoduchosti.

    def getCount(self):
        """Vrací počet průchodů které bylo potřeba aby bylo sudoku vyřešeno
        """
        return self.count

    def solve(self):
        """Vyřeší sudoku
        
        Returns:
            sudoku -- vyřešené sudoku
        """
        count = 1 
        while count:
            sudoku = self.allChoice()
            # vrátí seznamy ve kterém jsou na místech kde nic není seznamy s možnosti co na daných místech mohou být
            # Bude se do něj ukládat to co se vyřeší

            for y in range(9):
                for i in range(9):
                    if (type(sudoku[y][i]) is list) and len(sudoku[y][i]) == 1:
                        # pokud je typ list (Nejedná se o číslo které je zadané nebo vypočítane), a zároveň pokud je delka toho arraye 1 (je tam jen jeden prvek)
                        sudoku[y][i] = sudoku[y][i][0]
                        # převede array s jendím prvkem na int
                    elif (type(sudoku[y][i]) is not int):
                        # Pokud se nejedná o int (je to seznam) s více prvky nastaví na dané místo nulu (zatím nevím co tam bude) 
                        sudoku[y][i] = 0
            self.sudokuNum = numpy.array(sudoku)
            # převede pole s řešením na rošířené pole 

            if (self.sudokuNum > 0).all():
                # porovná všechny prvky v array 
                # pokud jsou všechny True breakne se while
                break
            count+=1
        self.count = count
        # uložení počtu průběhů do objektu
        return sudoku

    def allChoice(self,):
        """vytvoření seznamu podle kterého se určuje kde co patří
        
        Returns:
            array -- Vrátí array ve kterém jsou obsaženy všechny čísla která mohou být na místech kde není nic zadáno
        """
        sudoku = self.sudokuNum.tolist()
        # převedení rozšířeného pole na normální

        for i in range(9):
            for y in range(9):
                if sudoku[i][y] == 0:
                    # zajímají mě jen prvky které maji hodnotu 0 (zatí nevím co tam potří)
                    sudoku[i][y] = list(self.colums(y) & self.lines(i) & self.square(i//3,y//3))
                    # metody výše vrací co v daném řádku, sloupci a čtverci (3x3) může být a vytvaří množinový průnik                   
                    # i = řádek
                    # y = konrétní pozice v řádku        
        return sudoku

vyhra = [5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]
vyhro = [8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,0,7,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]
sudoej = Sudokusolve(vyhra)


print(sudoej.sudokuNum)
sudoej.solve()
print(sudoej.sudokuNum)


            

def pretty_print(sudoku):
    for i in range(9):
        if i%3 == 0:
            print('')
        s = ''
        for j in range (9):
            if j % 3 == 0:
                s += '   '
                #print('   ')
            else:
                s+= (' ')

            s += str(sudoku[i][j])

                #print(' ')
            #print(sudoku[i][j])
        print(s)


def find_solution(sukoku):
    for i in range(9):
        for j in range(9):
            if sukoku[i][j] != 0:
                for k in range(9):
                    if check_row(sukoku[i], k):
                        if check_col([i][j], k):
                            if check_square(sukoku[i], sukoku[i][j], k):


"""
* Check if value is present in the row
* @param row value from 0 to 8* @value value value from 1 to 9
* returns True if value is not present, False otherwise
"""
def check_row(row, value):
    for i in range(9):
        if row[i] == value:
            return False
    return True


"""
* Check if value is present in the column
* @param col value from 0 to 8
* @value value value from 1 to 9
* returns True if value is not present, False otherwise
"""
def check_col(col, value):
    for i in range(9):
        if col[i] == value:
            return False
    return True


"""* Check if value is present in the square designated by
* row and col* @param row value from 0 to 8
* @param col value from 0 to 8* @value value value from 1 to 9
* returns true if value is not present, false otherwise
"""
def check_square(row, col, value):
    pass #TODO

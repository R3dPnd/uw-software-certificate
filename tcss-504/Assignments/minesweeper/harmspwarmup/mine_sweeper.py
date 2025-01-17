"""
The Problem

Have you ever played Minesweeper? It is a cute little game which comes
within a certain Operating System which name we cannot really remember.
Well, the goal of the game is to find where are all the mines within a MxN
field. To help you, the game shows a number in a square which tells you
how many mines there are adjacent to that square. For instance, suppose
the following 4x4 field with 2 mines (which are represented by an *
character):

*...
....
.*..
....

If we would represent the same field placing the hint numbers described
above, we would end up with:

*100
2210
1*10
1110

As you may have already noticed, each square may have at most 8 adjacent
squares.

The Input

The input will consist of an arbitrary number of fields. The first line of
each field contains two integers n and m (0 < n,m <= 100) which stands for
the number of lines and columns of the field respectively. The next n
lines contain exactly m characters and represent the field. Each safe
square is represented by an "." character (without the quotes) and each
mine square is represented by an "*" character (also without the quotes).
The first field line where n = m = 0 represents the end of input and
should not be processed.

The Output

For each field, you must print the following message in a line alone:

Field #x:

Where x stands for the number of the field (starting from 1). The next n
lines should contain the field with the "." characters replaced by the
number of adjacent mines to that square. There must be an empty line
between field outputs.

Steps
1. Read the input file
    * Read the input file line by line
    * Read the first line to get the number of rows and columns
    * Read the next n lines to get the grid
2. Parse the input file into a grid
    * Read the first line to get the number of rows and columns
    * Read the next n lines to get the grid
3. Generate the minesweeper from the input grid
    * For each cell in the grid, count the number of mines in the adjacent cells
    * If the cell is a mine, keep it as is
    * Otherwise, replace the cell with the count of mines
4. Write the output file
    * Write the output to a file
"""

'''
    Description: This function reads the input file and returns the grid of cells.
    Arguments:
        file: The input file to read
    Returns:
        The grid of cells
'''
def create_mine_fields(file_path):
    lines = []
    result = []
    with open(file_path, 'r') as file:
        fields = file.read().strip().split('\n')
    index = 0
    field_number = 1
    output = []
    while index < len(fields):
        n, m = map(int, fields[index].split())
        if n == 0 and m == 0:
            break
        index += 1
        field = []
        for _ in range(n):
            field.append(fields[index])
            index += 1
        field = generate_minesweeper(n, m, field)
        output.append(f"Field #{field_number}:")
        output.append(field)
        field_number += 1
    return '\n'.join(output).strip()

'''
    Description: This function counts the number of mines in the adjacent cells of a given cell.
    Arguments:
        x: The x-coordinate of the cell
        y: The y-coordinate of the cell
        field: The grid of cells
    Returns:
        The number of mines in the adjacent cells of the given cell
'''
def count_mines(n, m, x, y, field):
    count = 0
    for i in range(max(0, x - 1), min(n, x + 2)):
        for j in range(max(0, y - 1), min(m, y + 2)):
            if field[i][j] == '*':
                count += 1
    return count
    
'''
    Description: This function generates the minesweeper grid from the input grid.
    Arguments:
        n: The number of rows in the grid
        m: The number of columns in the grid
        field: The input grid
    Returns:
        The minesweeper grid with the counts of mines in the adjacent cells
'''
def generate_minesweeper(n, m, field):
    result = ""
    for i in range(n):
        row = ''
        for j in range(m):
            if field[i][j] == '*':
                row += '*'
            else:
                row += str(count_mines(n, m, i, j, field))
        result += row + '\n'
    return result

'''
    Description: This function writes the output to a file.
    Arguments:
        file: The output file to write to
        output: The output string to write to the file
'''
def write_output(input, output_path):
    with open(output_path, 'w') as f:
        f.write(input)
      
'''
    Description: This function reads the input file, generates the minesweeper grid, and writes the output to a file.
'''  
def main():
    fields = create_mine_fields('mines.txt')
    write_output(fields, "minesweeper_output.txt")
main()
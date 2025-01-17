def count_adjacent_mines(field, n, m, row, col):
    # Directions for the 8 adjacent cells
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < m and field[r][c] == '*':
            count += 1
    return count

def process_field(field, n, m):
    result = []
    for i in range(n):
        row_result = ""
        for j in range(m):
            if field[i][j] == '*':
                row_result += '*'
            else:
                mines_count = count_adjacent_mines(field, n, m, i, j)
                row_result += str(mines_count)
        result.append(row_result)
    return result

def main():
    with open('mines.txt', 'r') as file:
        data = file.read().splitlines()
    
    field_number = 1
    index = 0
    while index < len(data):
        n, m = map(int, data[index].split())
        if n == 0 and m == 0:
            break
        index += 1
        field = []
        for _ in range(n):
            field.append(data[index])
            index += 1
        
        if field_number > 1:
            print()  # Print a blank line between fields
        
        print(f"Field #{field_number}:")
        processed_field = process_field(field, n, m)
        for line in processed_field:
            print(line)
        
        field_number += 1

if __name__ == "__main__":
    main()
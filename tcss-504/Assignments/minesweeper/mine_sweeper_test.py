from mine_sweeper import generate_minesweeper, read_input, write_output

def test(file_name):
    input_data = read_input(file_name)
    index = 0
    field_number = 1
    output = []
    
    while index < len(input_data):
        n, m = map(int, input_data[index].split())
        if n == 0 and m == 0:
            break
        index += 1
        field = []
        for _ in range(n):
            field.append(input_data[index])
            index += 1
        result = generate_minesweeper(n, m, field)
        output.append(f"Field #{field_number}:")
        output.extend(result)
        output.append('')
        field_number += 1
        
    write_output(file_name + '_output.txt', '\n'.join(output).strip())
        
test("sample.txt")

def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()

    # convert the sequence to array
    roll_list = []
    for l in lines:
        line_list = [c for c in l]
        # print(line_list)
        roll_list.append(line_list)

    # part 1
    total_row = len(roll_list)
    total_col = len(roll_list[0])
    sum = 0
    valid_positions = []
    for row_index, row in enumerate(roll_list):

        for col_index, col in enumerate(row):
            surround_sum = 0
            # calculate the 8 positions,and summarize the total of the roll
            # for the positions that are invalid, discard them
            if roll_list[row_index][col_index] == '@':
                positions = get_positions(total_row, total_col, (row_index, col_index))
                for position in positions:
                    if roll_list[position[0]][position[1]] == '@':
                        surround_sum += 1

                if surround_sum < 4:
                    sum += 1
                    valid_positions.append((row_index, col_index))

    # for position in valid_positions:
    #     print(position)

    print(f"sum: {sum}")


    # part 2
    sum2 = 0
    next_list = roll_list
    while True:
        last_sum = sum2
        next_list, sum2 = calc_posi(next_list, sum2)
        print(f"sum2: {sum2}")
        if last_sum == sum2:
            break
    print("-" * 100)
    print(f"sum2: {sum2}")


def get_positions(total_row, total_col, current_postion):
    positions = []
    current_row, current_col = current_postion

    for row_index in range(current_row - 1, current_row + 2):
        for col_index in range(current_col - 1, current_col + 2):

            if 0 <= row_index < total_row and 0 <= col_index < total_col and (current_postion != (row_index, col_index)):
                positions.append((row_index, col_index))

    return positions

def calc_posi(roll_list, sum):
    valid_positions = []
    for row_index, row in enumerate(roll_list):

        for col_index, col in enumerate(row):

            surround_sum = 0
            if roll_list[row_index][col_index] == '@':
                positions = get_positions(len(roll_list), len(roll_list[0]), (row_index, col_index))
                for position in positions:
                    if roll_list[position[0]][position[1]] == '@':
                        surround_sum += 1

                if surround_sum < 4:
                    sum += 1
                    valid_positions.append((row_index, col_index))

    if len(valid_positions) != 0:
        for position in valid_positions:
            roll_list[position[0]][position[1]] = '.'

    print("-" * 100)
    for row in roll_list:
        print("".join(row))
    return roll_list, sum





if __name__ == '__main__':
    main()
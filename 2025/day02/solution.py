
def main():
    with open("data.txt") as f:
        data = f.readline().strip()

    seqs = data.split(",")
    sum = 0
    for seq in seqs:
        start_index = int(seq.split("-")[0])
        end_index = int(seq.split("-")[1])
        # print(start_index, end_index)

        # dest_num = 11
        # part 1
        # while dest_num <= end_index:
        #     if start_index <= dest_num <= end_index:
        #         sum += dest_num
        #     dest_num = generate_next_id(str(dest_num))

        # part2
        ids = generate_all_ids_repeat(start_index, end_index)
        # print(ids)
        for id in ids:
            sum += id

    print(sum)



def generate_next_id(num_str):
    first_part = int(num_str[:len(num_str)//2]) + 1
    second_part = int(num_str[len(num_str)//2:]) + 1
    return int(str(first_part) + str(second_part))


def generate_all_ids_repeat(start_index, end_index):
    id_list = []
    initial_num = 1
    while True:

        if len(str(initial_num)) * 2 > len(str(end_index)):
            break

        dest_num = initial_num

        while True:
            dest_num = int(str(dest_num) + str(initial_num))
            if start_index <= dest_num <= end_index:
                if dest_num not in id_list:
                    id_list.append(dest_num)

            if dest_num >= end_index:
                break


        initial_num += 1





    return id_list








if __name__ == '__main__':
    main()
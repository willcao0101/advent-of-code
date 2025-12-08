


def main():
    # read the file
    with open("data.txt") as f:
        seqs = f.read().splitlines()

    # part 1
    sum = 0
    for seq in seqs:
        # find the max num and the max num is not the last num
        first_num = 0
        fn_index = 0
        for index, c in enumerate(seq):
            if int(c) > first_num and index != len(seq) - 1:
                first_num = int(c)
                fn_index = index
        print(seq)
        # print(f"first: {first_num}, first_index: {fn_index}")

        # find the second max number from the index of max number
        second_num = seq[fn_index]
        sn_index = fn_index
        for index in range(fn_index + 1, len(seq)):
            if int(seq[index]) > int(second_num):
                second_num = int(seq[index])
                sn_index = index
        # print(f"second: {second_num}, second_index: {sn_index}")
        print(f"the number is {first_num}{second_num}")

        sum += int(str(first_num) + str(second_num))

    print(f"the sum is {sum}")
    print("-"*100)

    sum2 = 0
    for seq in seqs:
        print("seq:" + seq)
        sum_seq = find_number(seq)
        sum2 += int(str(sum_seq))
    print(f"the sum is {sum2}")  # 3121910778619




def find_number(seq):
    print("-"*100)
    ln_index = -1
    dest_str = ""
    for number_index in range(12):  # represent the index of the dest number
        current_number = int(seq[ln_index + 1])
        ln_index = ln_index + 1
        for index in range(ln_index, len(seq) - (11 - number_index)):  # 0 - 14
            if int(seq[index]) > current_number:
                current_number = int(seq[index])
                ln_index = index

        # print(f"final number:{seq[ln_index]},final number index:{ln_index}")
        dest_str += seq[ln_index]
        # print(f"number index: {number_index}, dest str: {dest_str}, ln_index: {ln_index}")
    print(f"the number is {dest_str}")
    return int(dest_str)


if __name__ == "__main__":
    main()
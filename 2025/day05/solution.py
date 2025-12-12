
def main():
    with open("data.txt") as f:
        lines = f.read().splitlines()

    split_index = lines.index("")
    range_list = lines[:split_index]
    id_list = lines[split_index + 1:]
    print(range_list)
    print(id_list)

    # part 1
    ranges = [(int(range_str.strip().split("-")[0]), int(range_str.strip().split("-")[1])) for range_str in range_list]
    # sort the ranges
    ranges.sort()
    # merge the overlap range
    merged_ranges = []
    for start, end in ranges:
        if not merged_ranges or start > merged_ranges[-1][1] + 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    fresh_list = []
    for id in id_list:
        if is_fresh(int(id), merged_ranges):
            fresh_list.append(id)

    print(len(fresh_list))

    # part 2
    sum = 0
    for start, end in merged_ranges:
        sum += end - start + 1

    print(sum)


def is_fresh(x, merged_ranges):
    for a, b in merged_ranges:
        if a <= x <= b:
            return True
    return False


if __name__ == '__main__':
    main()
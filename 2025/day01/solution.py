

def main():
    # read txt file
    with open("data.txt") as f:
        data = f.readlines()

    password = 0
    point = 50
    for d in data:
        direction = d.strip()[:1]
        step = int(d.strip()[1:])
        if direction == "L":
            step = -1 * step
            current_step = (point + step % 100) % 100
            # print(current_step)
            point = current_step
        else:
            current_step = (point + step % 100) % 100
            # print(current_step)
            point = current_step

        if current_step == 0:
            password += 1

    print(f"password: {password}")



if __name__ == '__main__':
    main()
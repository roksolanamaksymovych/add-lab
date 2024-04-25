def find_max_experience(levels, experience):
    max_experience = 0
    queue = [(0, 0, 0)]

    while queue:
        level, position, current_experience = queue.pop(0)
        current_experience += experience[level][position]
        if level == levels - 1:
            max_experience = max(max_experience, current_experience)
        else:
            queue.append((level + 1, position, current_experience))
            queue.append((level + 1, position + 1, current_experience))

    return max_experience



def main():
    with open("career.in", "r") as file_in:
        levels = int(file_in.readline().strip())
        experience = []
        for line in file_in:
            row = list(map(int, line.split()))
            experience.append(row)

    max_exp = find_max_experience(levels, experience)

    with open("career.out", "w") as file_out:
        file_out.write(str(max_exp))


if __name__ == "__main__":
    main()

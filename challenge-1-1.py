input_path = "challenge-1-input.txt"

lines = []


def main():
    total_sum = 0
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            total_sum += parse_calibration_number(line.strip())
    f.close()
    print(total_sum)


def parse_calibration_number(line: str) -> int:
    first_number = next(char for char in line if char.isdigit())
    last_number = next(char for char in reversed(line) if char.isdigit())
    return int(first_number + last_number)


main()

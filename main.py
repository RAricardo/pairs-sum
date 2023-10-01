import sys
from pairs_sum import pairs_sum

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <comma-separated-array> <target-sum>")
        sys.exit(1)

    input_array = [int(x) for x in sys.argv[1].split(",")]
    target_sum = int(sys.argv[2])

    # pairs_sum O(n) implementation
    result = pairs_sum(input_array, target_sum)

    for pair in result:
        print(*pair, sep=', ')

if __name__ == "__main__":
    main()

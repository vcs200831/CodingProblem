def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []  # No solution found


def main():
    # Example test cases
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # Output: [0, 1]

    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))  # Output: [1, 2]

    nums = [0, 8, 11, -5]
    target = 6
    print(twoSum(nums, target))  # Output: [1, 2]

    nums = [1, 2, 3, 4, 5]
    target = 10
    print(twoSum(nums, target))  # Output: [3, 4]

    nums = [1, 2, 3, 4, 5]
    target = 7
    print(twoSum(nums, target))  # Output: [2, 3]


if __name__ == "__main__":
    main()



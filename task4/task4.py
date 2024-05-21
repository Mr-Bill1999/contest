import argparse

nums = []


parser = argparse.ArgumentParser()
parser.add_argument('nums_file', type=str, help='Path to nums of array.')
args = parser.parse_args()


with open(args.nums_file, 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

min_sum = 2147483647

if nums:
    for i in range(len(nums)):
        num = nums[i]
        sum_f_num = 0
        for j in range(len(nums)):
            sum_f_num += abs(nums[j] - num)
        if sum_f_num < min_sum:
            min_sum = sum_f_num
else:
    min_sum = 0

print(min_sum)



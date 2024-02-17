def add(num_string):
    if not num_string:
        return 0
    nums = list(map(int, num_string.split(',')))
    return sum(nums)
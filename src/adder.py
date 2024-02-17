def add(num_string):
    if not num_string:
        return 0
    num_string = num_string.replace('\n', ',')
    nums = list(map(int, num_string.split(',')))
    return sum(nums)
def add(num_string):
    if not num_string:
        return 0
    delimiter = ','
    if num_string.startswith('//'):
        delimiter, num_string = num_string[2:].split('\n',1)
    num_string = num_string.replace('\n', delimiter)
    nums = list(map(int, num_string.split(delimiter)))
    return sum(nums)
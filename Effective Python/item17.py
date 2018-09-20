import logging

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)


visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)


def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    print(result)
    return result


visits = [15, 35, 80]
normalize_defensive(visits)
visits = ReadVisits(path)
normalize_defensive(visits)


try:
    it = iter(visits)
    normalize_defensive(it)
except:
    logging.exception('Expected')
else:
    assert False
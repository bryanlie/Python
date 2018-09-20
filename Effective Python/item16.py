from itertools import islice


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = 'Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, \
 and dedicated to the proposition that all men are created equal.'
result = list(index_words_iter(address))
print(result[:10])


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


address_lines = """Four score and seven years
ago our fathers brought forth on this
continent a new nation, conceived in liberty,
and dedicated to the proposition that all men
are created equal."""

with open('address.txt', 'w') as f:
    f.write(address_lines)

with open('address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 10)
    print(list(results))

import json

handle = open('random_data.txt', 'w', encoding='utf-8')
handle.write('Lisa\nloves\nDan\nNew\nChapter\n')
handle.close()

handle = open('random_data.txt') # may raise IOError
try:
    data = handle.read() # may raise UnicodeDecodeError
finally:
    handle.close()


def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # may raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]


assert load_json_key('{"foo": "bar"}', 'foo') == 'bar'
try:
    load_json_key('{"foo": "bar"}', 'does not exist')
    assert False
except KeyError:
    pass


try:
    load_json_key('{"foo": bad payload', 'foo')
    assert False
except KeyError:
    pass


UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+') # may raise IOError
    try:
        data = handle.read()  # may raise UnicodeDecodeError
        op = json.loads(data) # may raise ValueError
        value = (
            op['numerator'] /
            op['denominator'] # may raise ZeroDivisorError
        )
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()


temp_path = 'random_data.json'
handle = open(temp_path, 'w')
handle.write('{"numerator": 1, "denominator": 10}')
handle.close()
assert divide_json(temp_path) == 0.1

handle = open(temp_path, 'w')
handle.write('{"numerator": 1, "denominator": 0}')
handle.close()
assert divide_json(temp_path) is UNDEFINED


handle = open(temp_path, 'w')
handle.write('{"numerator": 1 bad data')
handle.close()
try:
    divide_json(temp_path)
    assert False
except ValueError:
    pass
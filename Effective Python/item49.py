def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

assert palindrome('tacocat')
assert not palindrome('banana')

print(repr(palindrome.__doc__))

import itertools
def find_anagrams(word, dictionary):
    """Find all anagrams for a word.
    This function only runs as fast as the test for
    membership in the 'dictionary' container. It will
    be slow if the dictionary is a list and fast if
    it's a set.
    Args:
        word: String of the target word.
        dictionary: Container with all strings that
            are known to be actual words.
    Returns:
        List of anagrams that were found. Empty if
        none were found.
    """
    permutations = itertools.permutations(word, len(word))
    possible = (''.join(x) for x in permutations)
    found = {word for word in possible if word in dictionary}
    return list(found)

assert find_anagrams('pancakes', ['scanpeak']) == ['scanpeak']
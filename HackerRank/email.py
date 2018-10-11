'''

A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.

Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line. 

e.g. input 

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

output
DEXTER <dexter@hotmail.com>

'''

import email.utils
import re


n = int(input())

for _ in range(n):
    line = email.utils.parseaddr(input())
    e = line[1]

    match = re.match(r"(^[a-zA-Z][_a-zA-Z0-9-\.]+)@([a-zA-Z]+)(\.[a-zA-Z]{1,3})$", e)

    if match:
        print(email.utils.formataddr(line))

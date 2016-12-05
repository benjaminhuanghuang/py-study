# call function until a sentinel Value
with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)

# bad
blocks = []
while True:
    block = f.read(32)
    if block =='':
        break
    blocks.append(block)

import functools
# better
blocks = []
for block in iter(partial(f.read, 32), '')
    blocks.append(block)
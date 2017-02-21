# coding=utf-8

import re

# (T|t)可以匹配多个模式，同时也是一个分组，会被捕获
print re.findall(r'(T|t)he', 'The the')  # ['T', 't']
# 方括号也可以匹配多模式
print re.findall(r'[T|t]he', 'The the')  # ['The', 'the']
# 非捕获分组
print re.findall(r'(?:T|t)he', 'The the')  # ['The', 'the']
# 使用(?i)忽略大小写
print re.findall(r'(?i)the', 'the The THE')  # ['the', 'The', 'THE']

# 替换
print re.sub(r'([\w! ]+)',
             r'<h1>\1</h1>',
             'Welcome to home!')  # <h1>Welcome to home!</h1>
# \1和\g<1>等价
print re.sub(r'([\w! ]+)',
             r'<h1>\g<1></h1>',
             'Welcome to home!')  # <h1>Welcome to home!</h1>

print re.sub(r'(world) (hello)',
             r'\2 \1',
             'world hello')  # hello world

# 命名分组在sub中的引用
print re.sub(r'(?P<title>[\w! ]+)',
             r'<h1>\g<title></h1>',
             'Welcome to home!')  # <h1>Welcome to home!</h1>

# 命名分组，忽略大小写匹配两个一样的单词
pattern = re.compile(r'(?P<a>(?i)\b\w+\b) (?P=a)')
print pattern.match('hello hello').group()  # hello hello
print pattern.match('Hello hello').group()  # Hello hello

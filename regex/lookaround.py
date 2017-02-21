# coding=utf-8

import re

#
# Positive lookaheads
print re.search(r'(good) (?=job)', 'good job').group()  # good
print re.search(r'(good) (?=job)', 'good work')  # None
print re.match(r'(good) (?=job)', 'good')  # None

#
# Negative Lookaheads
print re.match(r'(good) (?!job)', 'good job')  # None
print re.match(r'(good) (?!job)', 'good work').group()  # good
print re.match(r'(good) (?!job)', 'good')  # None

# 匹配非连续出现的数字，\1 这种语法表示之前捕获的组
print re.match(r'(?:(\d)(?!\1))+', '3456').group()  # 3456
print re.match(r'(?:(\d)(?!\1))+', '112233')  # None

#
# Negative Lookbehinds）
print re.search(r'(?<!good) (job)', 'good job')  # None
print re.search(r'(?<!good) (job)', 'a job').group()  # job
print re.search(r'(?<!good) (job)', 'job')  # None

# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h, --help 查看帮助
    -d         动车
    -g         高铁
    -k         快速
    -t         特快
    -z         直达

Examples:
    tickets 上海 北京 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt


def get_opt():
    """command-line interface"""

    arguments = docopt(__doc__)
    '''
    {'-d': True,
     '-g': True,
     '-k': False,
     '-t': False,
     '-z': False,
     '<date>': '2016-10-10',
     '<from>': '\xe6\x88\x90\xe9\x83\xbd',
     '<to>': '\xe5\x8d\x97\xe4\xba\xac'}
    '''
    print arguments


if __name__ == '__main__':
    get_opt()

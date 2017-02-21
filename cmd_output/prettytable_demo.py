# -*- coding: utf-8 -*-

'''

Colormama can not work with python 2.7

'''

from prettytable import PrettyTable
from colorama import init, Fore

header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()


def trains():
    for _ in range(3):
        train = [
            100,
            '\n'.join([Fore.GREEN + 'from_station_name' + Fore.RESET,
                       Fore.RED + 'to_station_name' + Fore.RESET]),

            '\n'.join([Fore.GREEN + 'start_time' + Fore.RESET,
                       Fore.RED + 'arrive_time' + Fore.RESET]),

            "duration",
            'zy_num',
            'ze_num',
            'rw_num',
            'yw_num',
            'yz_num',
            'wz_num'
        ]
        yield train

def pretty_print():
    pt = PrettyTable()
    pt.field_names = header
    for train in trains():
        pt.add_row(train)
    print(pt)


if __name__ == '__main__':
    init()
    pretty_print()

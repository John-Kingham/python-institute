import sys

sys.path.append(
    r"c:\Users\jskin\Documents\software-engineering\Python Institute\python-institute\PCAP\Module_1"
)

from py.modules.module import sum_list, prod_list

zeroes: list[int]
ones: list[int]

zeroes = [0, 0, 0, 0, 0]
ones = [1, 1, 1, 1, 1]
print(sum_list(zeroes))
print(prod_list(ones))

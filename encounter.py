import random
import re
from box.table import *
from box.reader import *

def main():
    tables = createTables()
    artic = tables[0]
    print(artic.get(10).name)
    print(artic.get(25).name)
    print(artic.get(50).name)
    print(artic.get(75).name)
    print(artic.get(00).name)

main()

import platform
import random
import re

from box.table import *
from box.reader import *

tables = createTables()
nl = "\n"
tab = "	"

output = 'biomes: Biome[] = [' + nl

for i, table in enumerate(tables):
        print(i%4)
        if (False == i%4):
                output += tab + 'new Biome(' + str(i) + ', "' + table.name + '", "", [' + nl
        output += tab + tab + 'new LevelRange(' + str(i%4) + ', "' + table.name + '", "", [' + nl
        for j, row in enumerate(table.rows):
                output += tab + tab + tab + 'new Encounter(' + str(row.begin) + ', ' + str(row.end-1) + ', "' + row.name + '"),' + nl

        output += tab + tab + ']),' + nl
        if (False == (i+1)%4):
                output += tab + ']),' + nl

output += ']'
saveText(output)

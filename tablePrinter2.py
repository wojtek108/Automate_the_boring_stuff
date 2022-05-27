
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(table):
    colWidths = [0] * len(table)
    
    for a in range(len(table)):
        colWidths[a] = len(max(table[a], key = len))

    for x in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][x].rjust(colWidths[i]), end = ' ')
        print()

tablePrinter(tableData)

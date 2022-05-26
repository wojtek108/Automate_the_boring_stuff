tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(table):
    colWidths = [0] * len(table)

    for a in range(len(table)):
        for b in range(len(table[a])):
            if len(table[a][b]) > colWidths[a]:
                      colWidths[a] = len(table[a][b])

    # initial solution
    for x in range(len(table[0])):
        print(table[0][x].rjust(colWidths[0]) + table[1][x].rjust(colWidths[1] + 1) + table[2][x].rjust(colWidths[2] + 1))


    print()
    print()
    # improved solution
    for x in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][x].rjust(colWidths[i]), end = ' ')
        print()

tablePrinter(tableData)

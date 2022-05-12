test = {'2h': 'wpawn', '6g':'bpawn', '8d': 'wpawn', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4f': 'bking'}



piecesList = ['wpawn', 'bpawn', 'wbishop', 'bbishop', 'wknight',
            'bknight', 'wrook', 'brook', 'wqueen', 'bqueen',
            'wking', 'bking']

 
def pf(x):
    pc = {}
    for n in x.values():
        pc[n] = pc.get(n, 0) + 1
    for p in piecesList:
        pc.setdefault(p, 0)

    numberOfPieces = 0
    for v in pc.values():
        numberOfPieces = numberOfPieces + v
    return pc, numberOfPieces


# function returning list of squares and dictionary of squares and coresponding colors
def allSquares():
    squares = []
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    b = ['B', 'W'] *4
    a = ['W', 'B'] *4 
    ab = []
    for n in range(1, 9):
        if n % 2 == 1:
            ab.append(a)
        elif n % 2 == 0:
            ab.append(b)
        for l in columns:
            square = str(n) + l
            squares.append(square)
    c = ab[1] + ab[2] + ab[3] + ab[4]+ ab[5] + ab[6] + ab[7] + ab[0]
    dic = {}
    for i in range(64):
        dic[squares[i]] = c[i]
    return squares, dic


# function checking if all squares and pieces to check belong to real board
def pCheck(a):
    squares, coloredSquares = allSquares()
    for k in a.keys():
        if k not in squares:
            print(k)
            return False
    for v in a.values():
        if v not in piecesList:
            print(v)
            return False

# checking correct number of pieces
def numberPieces(x):
    pc, np = pf(x)
    if pc['bking'] == 1 and pc['wking'] == 1:
        return True
    else: 
        return False
    if pc['bpawn'] <= 8 and pc['wpawn'] <= 8:
        return True
    else: 
        return False
    if np > 32:
        return False

# no two white or black squared bishops
def goodBishops(x):
    squares, board = allSquares()
    pc, xx = pf(x) 
    bb = []
    wb = []
    
    if pc['bbishop'] == 2:
        for k, v in x.items():
            if v == 'bbishop':
                bb.append(board[k])
        if bb[0] == bb[1]:
            print(bb)
            return False
        
    if pc['wbishop'] == 2:
        for k, v in x.items():
            if v == 'wbishop':
                wb.append(board[k])
        if wb[0] == wb[1]:
            print(wb)
            return False

# no white or black pawns on first or eight rank
def pawnRanks(x):
    wp = []
    bp = []
    firstRank = ['1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h']
    lastRank = ['8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h']
    for k, v in x.items():
        if v == 'bpawn':
            bp.append(k)
        if v == 'wpawn':
            wp.append(k)
    for i in wp:
        if i in firstRank:
            return False
    for i in bp:
        if i in lastRank:
            return False

# kings are not next to each other
def kings(x):
    kk = []
    for k, v in x.items():
        if v == 'wking':
            kk.append(k)
        elif v == 'bking':
            kk.append(k)
    kkk = []
    for i in kk:
        kkk.append([i[1:], i[:-1]])
    dd = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8'}
    for k, v in dd.items():
        for n in range(2):
            if k == kkk[n][0]:
                kkk[n][0] = v
    for i in range(2):
        for n in range(2):
            kkk[i][n] = int(kkk[i][n])
    if kkk[0][0] - kkk[1][0] == 0 and (kkk[0][1] - kkk[1][1] == 1 or  kkk[0][1] - kkk[1][1]== -1):
        return False
    if kkk[0][0] - kkk[1][0] == 1 and (kkk[0][1] - kkk[1][1] == 1 or  kkk[0][1] - kkk[1][1]== -1 or kkk[0][1] - kkk[1][1] == 0):
        return False
    if kkk[0][0] - kkk[1][0] == -1 and (kkk[0][1] - kkk[1][1] == 1 or  kkk[0][1] - kkk[1][1]== -1 or kkk[0][1] - kkk[1][1] == 0):
        return False

def main(x):
    pf(x)
    if pCheck(x) == False:  
        print('False squares or pieces')
    elif numberPieces(x) == False:
        print('False number of pieces')
    elif  goodBishops(x) == False:
        print('False bishops')
    elif pawnRanks(x) == False:
        print('False pawn ranks')
    elif kings(x) == False:
        print('False kings position')
    else:
        print('True')

main(test)


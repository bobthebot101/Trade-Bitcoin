def tran(id, trans):

    if id == 000000:
        tran = [000000, 000000, 0.00]
        tran0 = tran[0]
        tran1 = tran[1]
        tran2 = tran[2]
        if trans == 'tran':
            return tran
        if trans == 'tran0':
            return tran0
        if trans == 'tran1':
            return tran1
        if trans == 'tran2':
            return tran2


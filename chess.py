def findQueens(Queens=[0] * 8, i=0):
    # Если на доске уже 8 ферзей, то рекурсия останавливается
    if i == 8:
        arr = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                arr[i][Queens[i]] = 1
        print(Queens)
        return arr
    else:
        for j in range(8):
            # Проверяем свободно ли поле
            if checkField(i, j, Queens):
                # Если да, записываем координату ферзя
                Queens[i] = j
                # Снова вызываем функцию со следующей строки
                chessBoard = findQueens(Queens, i + 1)
                # если переменная не пустая, выходим в предыдующую функцию с этой перемееной
                if chessBoard:
                    return chessBoard


# Проверяет поле на атаку другими ферзями
def checkField(i, j, Queens):
    r = i
    c = j
    # В столбце
    for k in range(i):
        if j == Queens[k]:
            return False
    # В ниспадающей диагонали
    while i >= 0 and j >= 0:
        if Queens[i] == j:
            return False
        i -= 1
        j -= 1
    # В растущей диагонали
    while r >= 0 and c <= 7:
        if Queens[r] == c:
            return False
        r -= 1
        c += 1
    return True


findQueens()
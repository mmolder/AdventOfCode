def getRow(partition, minRow, maxRow):
    if partition[0] == 'F':
        return getRow(partition[1:], minRow, int((minRow+maxRow)/2-0.5)) if len(partition) > 4 else int(minRow)
    elif partition[0] == 'B':
        return getRow(partition[1:], int((minRow+maxRow)/2+0.5), maxRow) if len(partition) > 4 else int(maxRow)

def getColumn(partition, minColumn, maxColumn):
    if partition[0] == 'L':
        return getColumn(partition[1:], minColumn, int((minColumn+maxColumn)/2-0.5)) if len(partition) > 1 else int(minColumn)
    elif partition[0] == 'R':
        return getColumn(partition[1:], int((minColumn+maxColumn)/2+0.5), maxColumn) if len(partition) > 1 else int(maxColumn)

def missing_elements(seatIds):
    start, end = seatIds[0], seatIds[-1]
    return sorted(set(range(start, end + 1)).difference(seatIds))

def task1():
    seatIds = []
    for boarding_pass in boarding_passes:
        row = getRow(boarding_pass, 0, 127)
        column = getColumn(boarding_pass[-3:], 0, 7)
        seatIds.append(row * 8 + column)
    print(max(seatIds))

def task2():
    seatIds = []
    for boarding_pass in boarding_passes:
        row = getRow(boarding_pass, 0, 127)
        column = getColumn(boarding_pass[-3:], 0, 7)
        seatIds.append(row * 8 + column)
    sorted_seats = sorted(seatIds, key=lambda x: x)
    print(missing_elements(sorted_seats))

boarding_passes = []

with open('2020/input_5.csv', 'r') as file:
    for boarding_pass in file:
        boarding_passes.append(boarding_pass.strip())

task1()
task2()
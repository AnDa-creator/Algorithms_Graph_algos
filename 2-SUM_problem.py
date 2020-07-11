import csv


def createArray(file):
    with open(file, 'r') as data:
        print('Reading Data...')
        reader = csv.reader(data)
        length = 10**6 # TODO Put the number of datapoints here
        hashTable = [0 for _ in range(0, length + 1)]
        i = 1
        for line in reader:
            if line[0] != '':
                hashTable[i] = int(line[0])
                i += 1

    print("Hash created...")
    return hashTable


def findTarget(hashTable):
    count = 0
    dataset = []
    print("Finding Targets___ ")
    t = -10000 # TODO set t lower limit
    while t != 10001:          # TODO set t (upper limit + 1)
        found = False
        H = {}
        for i in range(1, len(hashTable)):
            num = hashTable[i]
            y = t - hashTable[i]
            if t % 20 == 0:
                if i % 500000 == 0 and i >= 500000:
                    print("at {} for {}, also count now is {}".format(i,t, count))
            # print("H is {}".format(H))
            if y in H and y != hashTable[i]:
                # print(y)
                found = True
                break
            H[num] = i

        if found:
            count += 1
        t += 1
    return count, dataset


if __name__ == '__main__':
    Table = createArray("2-SumText.txt")
    val, data = findTarget(Table)
    print(val)
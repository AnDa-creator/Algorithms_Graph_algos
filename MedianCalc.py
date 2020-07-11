from heapq import heapify, heappop, heappush
import csv
import time


def medianHeap(List_num):
    new_list = List_num[:]
    median = 0
    heapify(new_list)
    if len(new_list) >= 2:
        # print('hi')
        decider = len(List_num)
        if decider % 2 == 0:
            for number in range(decider//2 ):
                # print(new_list)
                # heapify(new_list)
                median = heappop(new_list)
        else:
            for number in range(decider//2 + 1):
                # print(new_list)
                # heapify(new_list)
                median = heappop(new_list)

        # print(median)
        return median
    else:
        return List_num[0]

def medianSearch(List_num):
    new_list = List_num[:]
    # print(new_list)
    new_list.sort()
    if len(new_list) == 1:
        return new_list[0]
    elif len(new_list) % 2 == 0:
        return new_list[len(new_list) // 2 - 1]
    else:
        return new_list[len(new_list)//2 ]

if __name__ == '__main__':
    time1 = time.time()
    with open('median.txt', 'r') as test_file:
        reader = csv.reader(test_file)
        list_num = []
        running_median = []
        iterate_count = 0
        for num in reader:
            iterate_count += 1
            list_num.append(int(num[0]))
            new_median = medianHeap(list_num)
            if iterate_count >= 200 and iterate_count % 200 == 0:
                print("The new median: {} and iteration number is {}".format(new_median, iterate_count))
            running_median.append(new_median)
    time2 = time.time()
    with open('median.txt', 'r') as test_file:
        list_num2 = []
        running_median2 = []
        iterate_count2 = 0
        reader2 = csv.reader(test_file)
        for line in reader2:
            iterate_count2 += 1
            list_num2.append(int(line[0]))
            new_median_2 = medianSearch(list_num2)
            # print(new_median_2)
            if iterate_count2 >= 200 and iterate_count2 % 200 == 0:
                print("The new median(Search tree): {} and iteration number is {}".format(new_median_2, iterate_count2))
            running_median2.append(new_median_2)
        time3 = time.time()

    final_sum = sum(running_median2)
    print("Final sum in Search_case was {}".format(final_sum))
    final_mod = final_sum % 10**4
    print("Final value found is: {}".format(final_mod))
    print("Time for heap case: {}".format(time2 - time1))
    print("Time for Search case: {}".format(time3 - time2))







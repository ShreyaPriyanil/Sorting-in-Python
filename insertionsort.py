def insertionSort(alist):
    for index in range(1,len(alist)):
        print("TRAVERSAL #: ",index)
        position = index

        while position>0 and alist[position-1]>alist[position]:
            temp = alist[position]
            alist[position] = alist[position-1]
            alist[position-1] = temp
            position = position-1
        print("ARRAY AFTER TRAVERSAL #:",index," ", alist)

alist = [5,4,3,2,1]
print("---------------------NEW---------------------")
insertionSort(alist)
print(alist)

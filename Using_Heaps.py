import csv
import heapq
import sys



'''EFFICIENT APPROACH USING HEAPS'''


print('\n\nSOLUTION USING HEAPS\n')

with open(sys.argv[1],'r') as marks:
    c_reader = csv.reader(marks)

    next(c_reader)



    total = []
    mheap = []
    bheap = []
    eheap = []
    pheap = []
    cheap = []
    hheap = []

    for line in c_reader:
        ltotal = 0
        for i in range(1,7):
            ltotal += int(line[i])
        heapq.heappush(total,(ltotal,line[0]))

        heapq.heappush(mheap,(int(line[1]),line[0]))
        heapq.heappush(bheap,(int(line[2]),line[0]))
        heapq.heappush(eheap,(int(line[3]),line[0]))
        heapq.heappush(pheap,(int(line[4]),line[0]))
        heapq.heappush(cheap,(int(line[5]),line[0]))
        heapq.heappush(hheap,(int(line[6]),line[0]))

    print('\nTopper in Math is: ',heapq.nlargest(1,mheap)[0][1])        
    print('Topper in Biology is: ',heapq.nlargest(1,bheap)[0][1])  
    print('Topper in English is: ',heapq.nlargest(1,eheap)[0][1])  
    print('Topper in Physics is: ',heapq.nlargest(1,pheap)[0][1])  
    print('Topper in Chemistry is: ',heapq.nlargest(1,cheap)[0][1])  
    print('Topper in Hindi is: ',heapq.nlargest(1,hheap)[0][1]) 
    print('\n\nBest students in the class are : ',heapq.nlargest(3,total))  


'''Big O Notation for finding individual subject toppers is O(nlogn) 
   So in each line we're inserting 6 subject marks to 6 heaps so 6logn which is going to be iterated n times so O(6nlogn) = O(nlogn)'''

'''Big O Notation for finding Top Three Students is O(nlogn)
   We're inserting ltotal to one heap which takes O(logn) and that is repeated n times so O(nlogn)'''

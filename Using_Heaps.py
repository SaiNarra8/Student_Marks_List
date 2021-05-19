import csv
import heapq
import sys



'''EFFICIENT APPROACH USING HEAPS'''


print('\n\nSOLUTION USING HEAPS\n')

with open(sys.argv[1],'r') as marks:
    c_reader = csv.reader(marks)

    next(c_reader)



    total = []
    mtopper = {'name':None,'marks':0}
    btopper = {'name':None,'marks':0}
    etopper = {'name':None,'marks':0}
    ptopper = {'name':None,'marks':0}
    ctopper = {'name':None,'marks':0}
    htopper = {'name':None,'marks':0}
    count = 0
    for line in c_reader:
        ltotal = 0
        for i in range(1,7):
            ltotal += int(line[i])
        heapq.heappush(total,(ltotal,line[0]))
        count+=1
        if(count == 4):
            heapq.heappop(total)
            count = 3

        if(int(line[1])>mtopper['marks']):
            mtopper['name'] = line[0]
            mtopper['marks'] = int(line[1])
        if(int(line[2])>btopper['marks']):
            btopper['name'] = line[0]
            btopper['marks'] = int(line[2])
        if(int(line[3])>etopper['marks']):
            etopper['name'] = line[0]
            etopper['marks'] = int(line[3])
        if(int(line[4])>ptopper['marks']):
            ptopper['name'] = line[0]
            ptopper['marks'] = int(line[4])
        if(int(line[5])>ctopper['marks']):
            ctopper['name'] = line[0]
            ctopper['marks'] = int(line[5])
        if(int(line[6])>htopper['marks']):
            htopper['name'] = line[0]
            htopper['marks'] = int(line[6])


    print('\n\nTopper in Math is: ',mtopper['name'])        
    print('Topper in Biology is: ',btopper['name'])  
    print('Topper in English is: ',etopper['name'])  
    print('Topper in Physics is: ',ptopper['name'])  
    print('Topper in Chemistry is: ',ctopper['name'])  
    print('Topper in Hindi is: ',htopper['name'])  
    print('\n\nBest students in the class are : ',heapq.nlargest(3,total))  


'''Big O Notation for finding individual subject toppers is O(n) 
       So in each iteration checking for five subjects gives O(5n) which is equal to O(n) so LINEAR TIME COMPLEXITY'''

'''Big O Notation for finding Top Three Students is O(nlogk) k being the no. of toppers required
   We're inserting ltotal to one heap which takes O(logk) since it has only k elements which is 3 here and that is repeated n times so O(nlogk)'''



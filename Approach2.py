import csv
import sys

with open(sys.argv[len(sys.argv)-1],'r') as marklist:
    csv_reader = csv.reader(marklist)
    next(csv_reader)
    
    
   
    mtopper = {'name':None,'marks':0}
    btopper = {'name':None,'marks':0}
    etopper = {'name':None,'marks':0}
    ptopper = {'name':None,'marks':0}
    ctopper = {'name':None,'marks':0}
    htopper = {'name':None,'marks':0}
    
    toppers = {
               'name1':None,'marks1':0,
               'name2':None,'marks2':0,
               'name3':None,'marks3':0
              }
    
    for line in csv_reader:
        ltotal = 0
        for i in range(1,7):
            ltotal += int(line[i])
        


        if(ltotal>toppers['marks1']):
            toppers['name1'] = line[0]
            toppers['marks1'] = ltotal
        

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



    marklist.seek(0)
    next(csv_reader)
    for line in csv_reader:
        ltotal = 0
        for i in range(1,7):
            ltotal += int(line[i])
        if(ltotal<toppers['marks1'] and ltotal>toppers['marks2']):
            toppers['name2'] = line[0]
            toppers['marks2'] = ltotal

    marklist.seek(0)
    next(csv_reader)
    for line in csv_reader:
        ltotal = 0
        for i in range(1,7):
            ltotal += int(line[i])
        if(ltotal<toppers['marks2'] and ltotal>toppers['marks3']):
            toppers['name3'] = line[0]
            toppers['marks3'] = ltotal


    print('\n\nTopper in Math is: ',mtopper['name'])        
    print('Topper in Biology is: ',btopper['name'])  
    print('Topper in English is: ',etopper['name'])  
    print('Topper in Physics is: ',ptopper['name'])  
    print('Topper in Chemistry is: ',ctopper['name'])  
    print('Topper in Hindi is: ',htopper['name']) 
    print('\n\nBest students in the class are : ',(toppers['name1']+' First Rank',toppers['name2']+' Second Rank',toppers['name3']+' Third Rank'))


    '''Big O Notation for finding individual subject toppers is O(n) 
       So in each iteration checking for five subjects gives O(5n) which is equal to O(n) so LINEAR TIME COMPLEXITY'''

    '''Big O Notation for finding individual topper is O(n)
       So it takes 3 iterations for Top 3 students so O(n) + O(n) + O(n) which is equal to O(n) so LINEAR TIME COMPLEXITY'''

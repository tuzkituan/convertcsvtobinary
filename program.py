import sys, csv

#read cac tham so trong command line   
inputfile = sys.argv[1]
outputfile = sys.argv[2]
  
# cac file de write
output_file = open(outputfile,'w')

nrow1 = 0
state_arr = []

#read csv
with open(inputfile, 'r') as csvFile:
    #so cot
    first_line = csvFile.readline()
    csvFile.seek(0)
    ncol = first_line.count(',') + 1 
    
    #read file ra bien data
    data = [row for row in csv.reader(csvFile)]   
    nrow = len(data)

    with open('attributes.csv', 'r') as csvFile1:
        state = [row for row in csv.reader(csvFile1)] 
        # #get so dong
        nrow1 = len(state)
        # print(state)
        for i in range(0,nrow1):
            state_arr.append(state[i][0])

    print(nrow1)

    output_file.write('name')
    for i in range(0,nrow1):
        output_file.write(','+str(state_arr[i]))
    output_file.write('\n')

    for x in range(0,nrow):
        output_file.write(str(data[x][0]))
        for z in state: #1 -> 70
            check = 0
            for y in range(0,ncol): 
                if (str(data[x][y]) == z[0]):
                    output_file.write(',y')
                    check = 1
            if (check == 0):
                output_file.write(',n')        
        output_file.write('\n')
        

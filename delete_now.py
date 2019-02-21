import os

files = os.listdir('C:\\Users\\AS00495100\\Desktop\\kuman dunp')

deleter_flag = False

op_location ='C:\\Users\\AS00495100\\Desktop\\kuman dunp\\op\\'

for file in files:

        output_file = open('C:\\Users\\AS00495100\\Desktop\\op\\'+file, 'w')
        textFile = open('C:\\Users\\AS00495100\\Desktop\\kuman dunp\\'+file,'r',encoding="utf8")
        for line in textFile:
            if line =='\n':
                deleter_flag=True
            if deleter_flag:
                output_file.write(line)
                deleter_flag=False
            else:
                print()

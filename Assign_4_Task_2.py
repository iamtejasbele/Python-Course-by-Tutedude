file1 = open('output.txt','w')
file1.write(input('Enter text to write to the file:')+'\n')
print('Data successfully written to output.txt')
file1.close()

file1 = open('output.txt','a')
file1.write(input('Enter additional text to append:'))
print('Data successfully appended')
file1.close()

file1 = open('output.txt','r')
reading_file = file1.read()
print('Final content of output.txt')
print(reading_file)
file1.close()


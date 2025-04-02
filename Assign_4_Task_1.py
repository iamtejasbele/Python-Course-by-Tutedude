try:
    file1 = open('sample.txt','r')
    reading_file = file1.readlines()
    n=0
    for i in reading_file:
        n=n+1
        print(f'Line {n}:',i)
    file1.close()
except:
    print('Error: The file','sample.txt','is not found')
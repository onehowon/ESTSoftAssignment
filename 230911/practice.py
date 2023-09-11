n = 5
arr1 = [9,20, 28, 18, 11]
arr2 = [30,1 ,21, 17, 28]

bin(arr1[0] | arr2[0])
bin(arr1[0] | arr2[0])[2:].replace('1', '#').replace('0',' ')
bin(3)[2:].zfill(5).replace('1', '#').replace('0', ' ')
pip install pylint
pylint test.py

def 구구단():
    for i in range(2, 10):
        for j in range(1, 10):
            print('{} * {} = {}'.format(i, j, i*j))
            
구구단()
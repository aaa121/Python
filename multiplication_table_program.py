# Multiplication Table

def multiplication_table(n):
    ''' int --> Table int

    :param n: The highest integer expected on the Table.
    :return: Multiplication Table of N x N
    Example:
    >>> multiplication_table(2)
    	 1	 2
    1	 1	 2
    2	 2	 4
    '''
    for i in range(1,n+1):
        print('\t',i,end='')
    for i in range(1,n+1):
        print()
        print(i,end='')
        for h in range(1,n+1):
            print('\t',i*h,end='')

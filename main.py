def main():
    ##################################################
    # Comlete your code here
    ##################################################


    val1 = int(input ('Enter your first number '))
    val2 = int(input('Enter your second number '))
    val3 = int(input('Enter your third number '))
    sum = val1 + val2 + val3 
    print ('Values: ', val1, val2, val3)
    print ('Total:  \t ', sum)
    avg = sum/3
    print (f'Average: \t {avg: .2f}')
    # print ('Average: \t {0: .2f}'.format(avg))





    pass


if __name__ == '__main__':
    main()

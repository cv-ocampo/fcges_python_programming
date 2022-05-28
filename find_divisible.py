# get the divisible value of the first 2 integer that is divisible by the 3rd integer
def find_divisible(a,b,k):
    count = 0
    for i in range(a,b):
        if(i % k == 0):
            count = count + 1
    return count

if __name__ == '__main__':
    print(find_divisible(0,11,2))

import math

def reverse(i):
    string = list(str(i))
    for j in range(math.floor(len(string)/2)):
        (string[j], string[len(string)-1-j]) = (string[len(string)-1-j], string[j])
    return int(''.join(string))

def is_palindrome(i):
    string = list(str(i))
    for j in range(math.floor(len(string)/2)):
        if (string[j] != string[len(string)-1-j]):
            return False
    return True

def main():
    #print(reverse(12345))
    #print(reverse(1234))

    count = 0
    for i in range(0, 10000):
        k = 0
        i_reverse = reverse(i)
        i += i_reverse
        k += 1
        print("%s <- 0" % i)
        while (k < 50):
            if (not is_palindrome(i)):
                i_reverse = reverse(i)
                i += i_reverse
                k += 1
                print(i) 
            else:
                print("%s <- pal" % i)
                count += 1
                break
            
    print(count)
    
if __name__ == '__main__':
    main()

    

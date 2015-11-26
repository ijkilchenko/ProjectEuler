def main():
    big_count = 0
    for i in range(100):
        for j in range(100):
            z = str(i**j)
            count = 0
            for s in z:
                count += int(s)
            if count > big_count:
                a, b = i, j
                big_count = count
    print(big_count)

if __name__ == '__main__':
    main()


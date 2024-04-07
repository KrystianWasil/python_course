import random

if __name__ == '__main__':
    rule = input("Enter rule: ")
    n = int(input("Enter len of str: "))
    k = int(input("Enter num of steps: "))
    new_sign = ['_','*']
    # slownik
    dictionary = {
        '***': rule[0],
        '**_': rule[1],
        '*_*': rule[2],
        '*__': rule[3],
        '_**': rule[4],
        '_*_': rule[5],
        '__*': rule[6],
        '___': rule[7]
    }

    # Tworzenie ciągu
    str = ''
    for _ in range(n):
        str += random.choice(['*', '_'])

    print("Początkowy ciąg:", str)

    # Zmienianie ciągu
    new_str = ''
    i = 0
    for _ in range(k):
        if i == n:
            str = new_str
            new_str = ''
            i = 0
        new_str += new_sign[int(dictionary[str[i-1]+str[i]+str[(i+1)*(i + 1 < n)]])]
        i+=1
    if k < n:
        for _ in range(n - k):
            new_str += '_'



    print("koncowy ciag: ", new_str)



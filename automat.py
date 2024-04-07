import random

if __name__ == '__main__':
    rule = input("Podaj regułę: ")
    n = int(input("Podaj długość ciągu: "))
    k = int(input("Podaj liczbę kroków: "))
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
    ciag = ''
    for _ in range(n):
        ciag += random.choice(['*', '_'])

    print("Początkowy ciąg:", ciag)

    # Zmienianie ciągu
    nowy_ciag = ''
    for i in range(k):
        nowy_ciag += new_sign[int(dictionary[ciag[i-1]+ciag[i]+ciag[(i+1)*(i + 1 < n)]])]

    print("koncowy ciag: ", nowy_ciag)



def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def main():
    angka = [5, 2, 9, 1, 5, 6]
    hasil = bubble_sort(angka)
    print("Hasil sorting:", hasil)


if __name__ == "__main__":
    main()
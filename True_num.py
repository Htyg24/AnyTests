N = int(input('Введите Количество знаков '))
K = int(input('Введите разрядность системы '))


def True_numbers(N, K):                # Количество "подходящих" чисел
    if N == 1:
        return K - 1                   # Количество не нулевых однозначных чисел
    if N == 2:
        return (K - 1) * K             # Количество двухзначных чисел
    return ((K - 1) *                  # Количество чисел которые могут стоять первыми(в самом большом разряде)
            (True_numbers(N - 1, K) +  # Количество чисел если последняя цифа 0
             True_numbers(N - 2, K)))  # Количество чисел если последняя цифра не 0

print(True_numbers(N, K))
input()
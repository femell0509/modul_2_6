def replay(): # Подбор пароля исходя от заданного числа
    def input_number():
        number = 0
        while number < 3 or number > 20:
            number = int(input('Введите число от 3 до 20: '))
        return number
    number = input_number()
    print('Ваше число: ', number)
    password = ''
    for i in range(1, number):
        for j in range(i+1, number):
            if number % (i + j) == 0:
                password += str(i) + str(j)
    print('Ваш пароль: ', password)

while 1 > 0:
    replay()

    # 13 - 112211310495867
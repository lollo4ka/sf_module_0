import numpy as np

def game_core(number):
    '''Сначала устанавливаем число равное середине отрезка, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    left = 1
    right = 101
    predict = 0
    while number != predict:
        count+=1
        predict = (left + right) // 2
        if number > predict: 
            left = predict + 1
        elif number < predict: 
            right = predict - 1
    return(count) # выход из цикла, если угадали
        
        
def score_game(core_fn):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(core_fn(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

if __name__ == '__main__':
    score_game(game_core)

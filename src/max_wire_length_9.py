def max_wire_length(distance_between_poles, pole_heights):
    number_of_poles = len(pole_heights)
    max_wire_lengths = [0] * number_of_poles

    for current_pole in range(number_of_poles-1):
        max_length = 0
        previous_pole = current_pole -1
            wire_length = ((distance_between_poles ** 2 + (max(pole_heights[current_pole], pole_heights[previous_pole]) - min(pole_heights[current_pole], pole_heights[previous_pole])) ** 2) ** 0.5)
            max_length = max(max_length, max_wire_lengths[previous_pole] + wire_length)
        max_wire_lengths[current_pole] = max_length

    return round(max(max_wire_lengths), 2)


# Зчитуємо вхідні дані з файлу
with open("max_wire_length_input.txt", "r") as file:
    distance_between_poles = int(file.readline())  # Зчитуємо відстань між опорами
    pole_heights = list(map(int, file.readline().split()))  # Зчитуємо висоти опор

# Викликаємо функцію для знаходження максимальної довжини дроту
result = max_wire_length(distance_between_poles, pole_heights)

# Записуємо результат у файл
with open("max_wire_length_output.txt", "w") as file:
    file.write("{:.2f}\n".format(result))

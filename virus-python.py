import random
import ctypes

# Приветственное сообщение
print("HAHAHAHAHAHAH YOU COMPUTER CRASHED")

# Генерируем случайное число
iol123n12 = random.uniform(50, 150)

# Функция для переворота экрана
def flip_screen():
    user32 = ctypes.windll.user32
    user32.SystemParametersInfoW(0x2A, 0, ctypes.byref(ctypes.c_int(1)), 1)

# Проверяем условие и переворачиваем экран
if iol123n12 > 100:
    flip_screen()  # Переворачиваем экран
    input(f"Число {iol123n12:.2f} больше 100. Нажмите Enter...")
else:
    input(f"Число {iol123n12:.2f} меньше или равно 100. Нажмите Enter...")

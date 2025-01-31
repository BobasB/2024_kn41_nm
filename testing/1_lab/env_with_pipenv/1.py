import numpy as np
import os

print(f"Ми запускаємось у середовищі: {os.environ.get("SERVER")}")
print(f"Версія програми: {os.environ["VERSION"]}")
print("Запускаємо програму у середовищі Pipenv")
l = np.array([1, 2, 4, 6])
print(f"Вимірність масиву: {l.ndim}")

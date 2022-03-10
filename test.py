import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002, 2003],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns = ["year", "state", "pop", "dept", "dates", "val"], index = ["one", "two", "three", "four", "five", "six"]) #формуємо таблицю
frame["dept"] = 2 #вставляємо значення всередину поля
frame["dates"] = np.arange(6) #вставляємо числа по черзі
val = pd.Series([7, 3, 2], index = ["one", "three", "six"])  #створюємо серію чисел
frame["val"] = val #вставляємо серію чисел лише в певні індекси
check = frame.state == "Ohio" #визначення потрібного статусу
frame["eastern"] = check #перевірка потрібного статусу
frame["count"] = frame.index #додавання поля аналогічному індексу
#del frame["eastern"] #видаляємо поле
head = frame.head() #отримуємо початок датасету
locked = frame.loc["three"]#отримуємо дані по індексу three
lock = pd.DataFrame(locked)

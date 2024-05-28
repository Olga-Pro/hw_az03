# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

# Импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

import numpy as np
import csv

# Настройка параметров
csv_file = 'divan_price.csv'  # Путь к CSV файлу
table_csv = ['Диван', 'Цена', 'Ссылка']  # Заголовок csv файла
kol_pages = 35  # количество страниц

def read_data_from_site(browser):
    # Чтение данных с сайта
    data = []
    # Строки таблицы
    rows = browser.find_elements(By.TAG_NAME, "tr")  # ищем все тэги "tr"
    # print(rows)

    for row in rows:  # Разбор строк таблицы
        cols = row.find_elements(By.TAG_NAME, 'td')  # ищем все тэги "td"
        my_str = []
        for col in cols:  # Забираем текстовое содержимое ячеек
            my_str.append(col.text)

        data.append(my_str)

    # Первый (0) элемент списка пустой, удаляем его
    data = data[1:]
    # print(data)
    return data

def write_csv(data):
    # Выгрузка данных в csv файл
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(table_csv)
        for i in range(0, len(data)):
            writer.writerows(data[i])

def parsing_from_site():
    #  Выгрузка данных с сайта divan.ru
    browser = webdriver.Chrome()  # Объект браузера
    try:
        # Страница сайта:
        url = "https://www.divan.ru/category/divany-i-kresla/page-"

        parsed_data = []

        # На сайте на момент выгрузки 35 страниц в разделе Диваны и кресла
        for page in range(1, kol_pages+1):
            # Формируем ссылку на конкретную страницу
            url_page = url+str(page).strip()
            # print(url_page)
            # Загрузка страницы
            browser.get(url_page)
            time.sleep(5)

            cur_page = read_data_from_site(browser)
            parsed_data.append(cur_page)
            # print(parsed_data)

        # Закрытие браузера
        browser.quit()

        # print(parsed_data)
        # Выгрузка в файл csv
        write_csv(parsed_data)

    except Exception as e:
        print(f"Ошибка. Исключение {type(e).__name__}")
        print(f"Сообщение исключения: {e}")


parsing_from_site()
# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

# Импорт библиотек
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

import pandas as pd
import csv

import matplotlib.pyplot as plt

# Настройка параметров
csv_file = 'divan_price.csv'  # Путь к CSV файлу
csv_file_res = 'result_price.csv'  # Путь к CSV файлу

table_csv = ['Диван', 'Цена', 'Ссылка']  # Заголовок csv файла
kol_pages = 35  # количество страниц


def read_data_from_site(browser):
    # Чтение данных с сайта
    data = []

    read_page = browser.find_elements(By.CLASS_NAME, 'lsooF')
    for element in read_page:
        name_element = element.find_element(By.CSS_SELECTOR, 'span').text
        price_element = element.find_element(By.CLASS_NAME, 'pY3d2').find_element(By.CSS_SELECTOR, 'span').text
        link_element = element.find_element(By.TAG_NAME, 'a').get_attribute('href')

        data.append([name_element, price_element, link_element])

    # print(data)

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


def clean_price(price):
    # Убрать "руб." и пробелы в цене и преобразовать в число
    return int(price.replace('руб.', '').replace(' ', ''))


def post_scv():
    # Обработка файла CSV
    # Убрать "руб." в цене
    # Удалить не диваны (кресла, кушетки и пр.)
    input_file = csv_file
    output_file = csv_file_res

    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                      encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Читаем заголовок и записываем его в новый файл
        header = next(reader)
        writer.writerow(header)

        # Обрабатываем и записываем данные строк
        for row in reader:
            if row[0].startswith('Диван'):
                clean_row = clean_price(row[1])
                writer.writerow([row[0], clean_row, row[2]])

    print(f"Обработанные данные сохранены в файл {output_file}")


def histo_divan():
    # Построение гистограммы

    # Чтение данных из CSV
    data = pd.read_csv(csv_file_res)

    # Cтолбец с ценами называется 'Цена'
    prices = data['Цена']

    plt.hist(prices, bins=50, edgecolor='black')

    # Добавление заголовка и меток осей
    plt.title('Гистограмма цен для диванов')
    plt.xlabel('Цена')
    plt.ylabel('Частота')

    # Показать гистограмму
    plt.show()


parsing_from_site()
post_scv()
histo_divan()

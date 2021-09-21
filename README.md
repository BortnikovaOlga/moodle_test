# Автоматизированные тесты для вебприложения 'Курсы' (Moodle)
### Python, Selenium, Allure

[![Build Status](https://app.travis-ci.com/BortnikovaOlga/moodle_test.svg?branch=master)](https://app.travis-ci.com/BortnikovaOlga/moodle_test)


>
## Устаноновка пакета
1. На компьютере должен быть установлен python 3.9.
1. Создайте отдельную директорию на локальном компьютере.
1. Скачайте в нее все файлы, расположеные в репозитории,
   `git clone <link on this repository>`
1. Установите зависимости командой `pip install -r <path to>\requirements.txt`
>
## Запуск тестов
1. Для запуска всех тестов выполните команду `pytest`,
   отдельные файлы тестов находятся в папке tests,
   команда для выполнения тестов из одного файла `pytest <test file name>`
2. Для вывода очета о выполненных тестах в Allure, необходимо :
- установить Allure https://docs.qameta.io/allure/#_get_started и Java на компьютер
- выполнить команду `pytest --alluredir=<allure reports dir>`
- вызвать Allure командой `allure serve <path to allure report dir>`

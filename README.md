# Автоматизированные UI тесты для образовательной платформы ['Moodle'](https://qacoursemoodle.innopolis.university)
### Python, Pytest, Selenium, Allure

[![Build Status](https://app.travis-ci.com/BortnikovaOlga/moodle_test.svg?branch=master)](https://app.travis-ci.com/BortnikovaOlga/moodle_test)

>
## Описание проекта
1. Данный учебный проект выполнен с целью изучения технологий автоматизации тестирования UI.
2. Для решения задачи написания автотестов
- применен паттерн проектирования 'Page Object'
- выбраны инструменты : python, [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html),
  [selenium](https://selenium-python.readthedocs.io/installation.html),
  [allure-pytest](https://docs.qameta.io/allure/#_pytest),
  [logging](https://docs.python.org/3/library/logging.html).
3. Автотесты написаны на выборочную функциональность образовательной платформы 'Moodle':
- авторизация пользователя ( .\tests\auth\test_auth.py ),
- обновление личной информации пользователя (.\tests\personal_data\test_update_profile.py),
- добавление нового курса (.tests\courses\test_add_course.py).
4. Описание тесткейсов (выполняемых шагов и ожидаемого результата) расположены в коде автотестов (*.py файлы) в виде docstring.
5. В проекте используется логгирование, конфигурация в log_settings.py
6. В проект включена проверка кода линтером [pre-commit](https://pre-commit.com/), настройки .pre-commit-config.yaml
7. В проект включена проверка выполнения тестов на ресурсе [travis-ci ](https://app.travis-ci.com/BortnikovaOlga/moodle_test), настройки .travis.yml
 >
## Устаноновка пакета
1. На компьютере должен быть установлен python 3.9.
2. Создайте отдельную папку на локальном компьютере.
3. Клонируйте в нее в репозиторий `git clone <link_on_this_repository>` или распакуйте в нее zip-архив (кнопка в github Code/Download ZIP).
4. Установите необходимые библиотеки, для этого в папке проекта выполните команду `pip install -r requirements.txt`
5. Если планируется работа с кодом, необходимо выполнить инсталляцию pre-commit `pip install pre-commit`
>
## Запуск тестов и вывод отчета в Allure
1. Для запуска всех тестов выполните команду `pytest`.
2. Отдельные файлы тестов находятся в папке tests во вложенных папках auth, personal_data, courses.
   - Для запуска тестов одного файла - выполните команду в папке с файлом `pytest <test_file_name>`.
   - Для запуска отдельного теста - команда `pytest <test_file_name>::<test_class_name>::<test_method_name>`
3. Для вывода очета о выполненных тестах в Allure, необходимо :
- установить Allure [инструкция по установке](https://docs.qameta.io/allure/#_get_started) и Java на компьютер
- выполнить команду `pytest --alluredir=<allure_reports_dir>`
- вызвать Allure командой `allure serve <path_to_allure_report_dir>`

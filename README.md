# kinopoisk_ui_and_api_autotest
Учебный репозиторий - Финальное задание

### Шаги

1. Клонировать проект себе на компьютер 'git clone https://github.com/Juriizorn/kinopoisk_ui_and_api_autotest.git'
2. Установить все зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек

- pytest
- selenium
- webdriver manager
- request
- sqlalchemy
- allure
- configparser
- json

### Структура

- ./test
- ./pages
- ./api
- ./db
- ./configuration - провайдер настроек
- - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
- - test_data.json

### Полезные ссылки

- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про configparser](https://docs.python.org/3/library/configparser.html)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)


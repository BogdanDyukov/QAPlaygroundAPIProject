# QA Playground Automation Tests

В этом проекте реализованы автоматизированные API тесты для
[платформы QA Playground](https://qa-playground.com/). 
Тесты написаны с использованием **Python**, **Pytest**, **Allure**, **Pydantic**, **Faker** и **Requests**. Документация: [Swagger](https://petstore.swagger.io/?url=https://release-gs.qa-playground.com/api/v1/swagger.json#/).

## Начало работы

### Клонирование репозитория

```bash
git clone https://github.com/BogdanDyukov/QAPlaygroundAPIProject.git
cd QAPlaygroundAPIProject
```

### Создание виртуального окружения

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск тестов

```bash
pytest -m "regression" --alluredir=./allure-results
```

### Просмотр Allure-отчета

```bash
allure serve allure-results
```

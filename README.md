<h1 align="center">Проект по автоматизации тестирования на web и mobile
<p align="center">
<a href="https://www.wikipedia.org/" target="_blank">
<img src="/Images/wiki_logo.png" alt="WikipediA" width="167" height="192"> </a> 
</p></h1>

## Содержание
+ [Тест-кейсы](#Тесты)
+ [Технологии и инструменты](#Технологии)
+ [Запуск автотестов из Jenkins](#Jenkins_web)
+ [Локальный запуск автотестов](#локальный_запуск)
+ [Отчеты о прохождении тестов Allure TestOps](#Allure)
+ [Оповещение о результатах через Telegram-бот](#Telegram) 
+ [Примеры прохождения тестов](#Примеры) 

<a name="Тесты">

## Тест-кейсы
### Список реализованных автотестов для web
- Тестирование главной страницы
- Тестирование поисковой строки
- Тестирование главного меню

### Список реализованных автотестов для mobile
- Тестирование поисковой строки
- Возврат на главную страницу из результатов поиска
- Переход на страницу с настройками
- Возврат на главную страницу со страницы настроек

<a name="Технологии">

## Структура проекта
### Технологии и инструменты
<p align="center">
<img width="6%" title="PyCharm" src="/Images/PyCharm_Icon.svg">
<img width="6%" title="Python" src="/Images/python-original.svg">
<img width="6%" title="Pytest" src="/Images/pytest-original.svg">
<img width="6%" title="Selenium" src="/Images/selenium.png">
<img width="6%" title="Selene" src="/Images/selenoid.png">
<img width="6%" title="GitHub" src="/Images/GitHub.svg">
<img width="6%" title="Jenkins" src="/Images/jenkins-original.svg">  
<img width="6%" title="Allure TestOps" src="/Images/allure.png">
<img width="6%" title="Telegram" src="/Images/telegram.svg">
<img width="6%" title="Browserstack" src="/Images/Browserstack.svg"> 
<img width="6%" title="Appium" src="/Images/Appium.svg"> 
</p>

<a name="Jenkins_web">

## Запуск автотестов из Jenkins
1. <a href="https://jenkins.autotests.cloud/job/C09-AlexanderOsipkin-unit24/" target="_blank">Открыть проект в Jenkins</a>
<img src="/Images/Screenshots/img1.png">
2. Нажать "Build with Parameters"
<img src="/Images/Screenshots/img2.png">
3. В поле "COMMENT" ввести комментарий и нажать на кнопку "Build"
<img src="/Images/Screenshots/img3.png">

<a name="локальный_запуск">

## Локальный запуск автотестов
1. Клонируйте репозиторий
```ruby
gh repo clone AlexanderOsipkin/qa_guru_python_9_24
```
2. Создайте и активируйте виртуальное окружение
  ```ruby
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```ruby
  pip install -r requirements.txt
  ```
4. Запустите автотесты 
  ```ruby
  pytest -sv
  ```
5. Получите отчёт allure
```ruby
allure serve allure-results
``` 

<a name="TestOPS">
  
## Интеграция с Allure TestOps
<a href="https://allure.autotests.cloud/project/4043/dashboards" target="_blank">Настроена интеграция с Allure TestOPS</a>
1. Автоматически-сгенерированные тест-кейсы:
<img src="/Images/Screenshots/img4.png">
2. История выполненных прогонов
<img src="/Images/Screenshots/img5.png">
<img src="/Images/Screenshots/img6.png">

<a name="Telegram">
  
## Уведомление о результатах тестирования через Telegram-бот
После завершения тестов приходит оповещение в Telegram с помощью заранее созданного Telegram-бота.

<img src="/Images/Screenshots/telegram-allure.png">

<a name="Примеры">

## Видео прохождения автотестов
### WEB
<img src="/Images/Videos/web-test.gif">

### mobile
<img src="/Images/Videos/mobile-test.gif">

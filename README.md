<h1 align="center">Проект по тестированию онлайн энциклопедии
<p align="center">
<a href="https://www.wikipedia.org/" target="_blank">
<img src="/Images/wiki_logo.png" alt="WikipediA" width="167" height="192"> </a> 
</p></h1>

## Содержание
+ [Тест-кейсы](#Тесты)
+ [Технологии и инструменты](#Технологии)
+ [Запуск автотестов из Jenkins для web](#Jenkins_web) 
+ [Оповещение о результатах через Telegram-бот](#Telegram) 
+ [Отчеты о прохождении тестов Allure TestOps](#Allure)
+ [Примеры прохождения тестов](#Примеры) 

<a name="Тесты">

### Список реализованных автотестов для web:
- Тестирование главной страницы
- Тестирование поисковой строки
- Тестирование главного меню

### Список реализованных автотестов для mobile:
- Тестирование поисковой строки
- Возврат на главную страницу из результатов поиска
- Переход на страницу с настройками
- Возврат на главную страницу со страницы настроек

<a name="Технологии">

## Структура проекта
### Проект реализован с использованием
<p align="center">
<img width="8%" title="PyCharm" src="/Images/PyCharm_Icon.svg">
<img width="8%" title="Python" src="/Images/python-original.svg">
<img width="8%" title="Pytest" src="/Images/pytest-original.svg">
<img width="8%" title="Selenium" src="/Images/selenium.png">
<img width="8%" title="Selene" src="/Images/selenoid.png">
<img width="8%" title="GitHub" src="/Images/GitHub.svg">
<img width="8%" title="Jenkins" src="/Images/jenkins-original.svg">  
<img width="8%" title="Allure TestOps" src="/Images/allure.png">
<img width="8%" title="Telegram" src="/Images/telegram.svg">
<img width="8%" title="Browserstack" src="/Images/Browserstack.svg"> 
<img width="8%" title="Appium" src="/Images/Appium.svg"> 
</p>

<a name="Jenkins">

## Запуск автотестов из Jenkins
Для удаленного запуска автотестов в <a href="https://jenkins.autotests.
cloud/job/C09-AlexanderOsipkin-unit24/" target="_blank">Jenkins</a> Задача создана, 
настроена и связана с репозиторием в GitHub.
<img width="1437" alt="image" src="">



<a name="Telegram">
  
## Уведомление о результатах тестирования через Telegram-бот
После завершения тестов приходит оповещение в Telegram с помощью заранее созданного Telegram-бота.

<img width="349" alt="image" src="">



<a name="TestOPS">
  
## Интеграция с Allure TestOps
Настроена интеграция Jenkins с Allure TestOPS.
При первом после интеграции прохождении тестов в Jenkins, в Allure TestOps были 
автоматически созданы такие тест-кейсы:

<img width="1432" alt="image" src="">

Можно посмотреть историю выполненных прогонов:
<img width="1435" alt="image" src="">
<img width="1432" alt="image" src="">

<a name="Тесты">

## Видео прохождения web автотеста

## Видео прохождения mobile автотеста
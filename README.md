# hello_backend

1. Установить и настроить связку веб-сервер + ваш язык программирования (выбор конкретных продуктов оставляем на вашей совести).
2. Примеры связок:

        nginx + uwsgi (Python)
        nginx + php-fpm (PHP)
        Tomcat (Java)
3. В папке /www/hello/ создать простейшее веб-приложение, которое выводит в браузер строку «Hello Web!».
4. Настроить веб-сервер таким образом, чтобы все запросы поступали в приложение через единую точку входа.
5. Открыть браузер и обратиться с его помощью к своему веб-серверу.
6. Увидеть приветствие.
7. PROFIT!!!!

Пример URL: http://localhost/hello/

**Подзадачи:**

Решение подзадач дописываем в приложение hello. В итоге весь код всех подзадач должен быть в одном файле.</br>
</br>
**1. GET handler**

1. Почитать про метод GET.
2. Написать обработчик GET-запросов, который выводит в браузер данные этого запроса в виде таблицы.
3. Параметры и значения передавать вручную через адресную строку браузера.
4. В таблицу результатов параметры выводить в алфавитном порядке.

**Пример URL:** http://localhost/hello/get/?first_name=Chu...=Godlike+Ranger</br>
**Пример таблицы:**

Параметр | Значение
--------|---------
first_name | Chuck
last_name | Norris
profession | Godlike Ranger
</br>
**2. POST handler**

1. Почитать про метод POST.
2. Скачать готовую форму.
3. Написать для этой формы POST-обработчик.
4. В обработчике получить запрос из формы и вывести в браузер данные этого запроса в виде таблицы.

**Пример URL:** http://localhost/hello/post/</br>
**Пример таблицы:**

Параметр | Значение
--------|---------
Имя | Гриша Лепс
Пол | Мужской
Образование | Низшее
Комментарий | Почему мои фанаты стали меньше пить?
Получать спам | Да
</br>
**3. Cookie counter**

1. Почитать, что такое cookie.
2. При первом заходе на страницу установить куку "page_visits=1".
3. При каждом последующем заходе — увеличить счетчик на единицу.
4. На странице отображать текущее показание счетчика.

**Пример URL:** http://localhost/hello/cookie/

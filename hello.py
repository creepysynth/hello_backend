#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

def cookie_counter(environ):
    counter = 1

    if 'HTTP_COOKIE' in environ:
        counter = int(environ['HTTP_COOKIE'].split('=')[1]) + 1
    return (
        ('200 OK', [('Content-Type','text/html'),
                    ('Set-Cookie', 'page_visits={}'.format(counter))]),
        ['page_visits = {}'.format(counter).encode('utf-8')]
    )

def get(environ):
    query = environ['QUERY_STRING'].split('&')
    query_dict = dict(i.split('=') for i in query)
    table = """
        <head>
          <title>GET</title>
          <meta charset="utf-8">
        </head>
        <body>
          <table border="2">
            <tr>
              <th>Параметр</th>
              <th>Значение</th>
            </tr>
            {rows}
          </table>
        </body>
    """
    row = """
        <tr>
          <td>{param}</td>
          <td>{value}</td>
        </tr>
    """
    rows = ''

    for key in sorted(query_dict):
        rows += row.format(param=key, value=query_dict[key])
    output = table.format(rows=rows)
    return (('200 OK', [('Content-Type','text/html')]),
            [output.encode('utf-8')])

def hello(environ):
    return (('200 OK', [('Content-Type','text/html')]),
            ['Hello Web!'.encode('utf-8')])

def post(environ):
    if environ['REQUEST_METHOD'] == 'POST':
        table = """
            <head>
              <meta charset="utf-8">
              <title>POST</title>
            </head>
            <body>
            <table border="2">
              <tr>
                <th>Параметр</th>
                <th>Значение</th>
              </tr>
              <tr>
                <td>Имя</td>
                <td>{name}</td>
              </tr>
              <tr>
                <td>Пол</td>
                <td>{sex}</td>
              </tr>
              <tr>
                <td>Образование</td>
                <td>{education}</td>
              </tr>
              <tr>
                <td>Комментарий</td>
                <td>{comment}</td>
              </tr>
              <tr>
                <td>Получать спам</td>
                <td>{spam}</td>
                </tr>
            </table>
            </body>
        """
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True
        )
        name = 'Не указано'
        sex = 'Не указан'
        education = {
            'low':'Низшее',
            'middle':'Среднее',
            'high':'Высшее'
        }
        spam = 'Нет'
        comment = post['comment'].value

        if post['name'].value:
            name = post['name'].value    
        if 'sex' in post:
            if post['sex'].value == 'female':
                sex = 'Женский'
            else:
                sex = 'Мужской'    
        if 'spam' in post:
            spam = 'Да'

        output = table.format(
            name=name,
            sex=sex,
            education=education[post['education'].value],
            comment=comment,
            spam=spam
        )
        return (('200 OK', [('Content-Type','text/html')]),
                [output.encode('utf-8')])
    return (('200 OK', [('Content-Type','text/html')]),
            [(open('form.html', 'rb')).read()])

def not_found(environ):
    return (('404 Not Found', [('Content-Type','text/html')]),
            ['404 Not Found'.encode('utf-8')])

def application(environ, start_response):
    path = environ['PATH_INFO']
    handler = {
        '/hello/':hello,
        '/hello/get/':get,
        '/hello/cookie/':cookie_counter,
        '/hello/post/':post
    }
    response, data = handler.get(path, not_found)(environ)

    start_response(*response)
    return data

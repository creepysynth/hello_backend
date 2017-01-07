#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

def cookie_counter(environ):
    counter = 1

    if 'HTTP_COOKIE' in environ:
        counter = environ['HTTP_COOKIE'].split('=')[1]
        counter = int(counter) + 1

    return counter

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
    """
    row = """
        <tr>
          <td>{param}</td>
          <td>{value}</td>
        </tr>
    """

    for key in sorted(query_dict):
        table += row.format(param=key, value=query_dict[key])

    return table + '</table></body>'

def post(environ):
    output = """
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
    post_env = environ.copy()
    post_env['QUERY_STRING'] = ''
    post = cgi.FieldStorage(
        fp=environ['wsgi.input'],
        environ=post_env,
        keep_blank_values=True
    )
    name = 'Не указано'
    sex = 'Не указан'
    education = 'Низшее'
    spam = 'Нет'
    comment = post['comment'].value

    if post['name'].value:
        name = post['name'].value
    
    if 'sex' in post:
        if post['sex'].value == 'female':
            sex = 'Женский'
        else:
            sex = 'Мужской'
    
    if post['education'].value == 'middle':
        education = 'Среднее'
    elif post['education'].value == 'high':
        education = 'Высшее'
    
    if 'spam' in post:
        spam = 'Да'

    return output.format(
        name=name, 
        sex=sex, 
        education=education, 
        comment=comment, 
        spam=spam
    )

def application(environ, start_response):
    path = environ['PATH_INFO']

    if environ['REQUEST_METHOD'] == 'POST':
        start_response('200 OK', [('Content-Type','text/html')])
        return [post(environ).encode('utf-8')]
    
    if path == '/hello/':    
        start_response('200 OK', [('Content-Type','text/html')])
        return ['Hello Web!'.encode('utf-8')]

    if path == '/hello/cookie/':
        page_visits = cookie_counter(environ)

        start_response('200 OK', [
                ('Content-Type','text/html'),
                ('Set-Cookie', 'page_visits={}'.format(page_visits))
            ]
        )
        return ['page_visits = {}'.format(page_visits).encode('utf-8')]
    
    if path == '/hello/get/':
        start_response('200 OK', [('Content-Type','text/html')])
        return [get(environ).encode('utf-8')]
    
    if path == '/hello/post/':
        start_response('200 OK', [('Content-Type','text/html')])
        return [(open('form.html', 'rb')).read()]
    
    start_response('404 Not Found', [('Content-Type','text/html')])
    return ['404 Not Found'.encode('utf-8')]
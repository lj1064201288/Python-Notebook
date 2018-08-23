from urllib import request

if __name__ == '__main__':
    try:
        response = request.urlopen('https://www.python.org')
        print(response.read().decode('utf-8'))

    except Exception as e:
        print(e)
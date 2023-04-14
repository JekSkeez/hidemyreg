import requests

url = 'https://hidemy.name/en/demo/'

if 'Your email' in requests.get(url).text:
    
    email = input('Введите электронную почту для получения тестового периода: ')

    response = requests.post('https://hidemy.name/en/demo/success/', data={
        "demo_mail": f"{email}"
    })

    if 'Your code has been sent to your' in response.text:
        confirm = input('Введите полученную ссылку для подтверждения e-mail адреса: ')
        
        while True:
            try:
                response = requests.get(confirm)
                if 'has been sent' in response.text:
                    print('Почта подтверждена. Код отправлен на вашу почту!')
                    break
                else:
                    confirm = input('Ссылка невалидная, повторите попытку: ')
            except:
                confirm = input('Ссылка невалидная, повторите попытку: ')
                continue


    else:
        print('Указанная почта не подходит для получения тестового периода ')

else:
    print('Невозможно получить тестовый период')

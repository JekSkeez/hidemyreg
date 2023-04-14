import requests

url = 'https://hidemy.name/en/demo/'

if 'Your email' in requests.get(url).text:
    
    email = input('Введите электронную почту для получения тестового периода: ')

    response = requests.post('https://hidemy.name/en/demo/success/', data={
        "demo_mail": f"{email}"
    })

    if 'Your code has been sent to your' in response.text:
        print('Код отправлен! Проверьте почту.')
    else:
        print('Указанная почта не подходит для получения тестового периода ')

else:
    print('Невозможно получить тестовый период')

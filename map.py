import requests

url = "https://static-maps.yandex.ru/1.x/"

ll = input()
if ll == '':
    ll = '37.531756,55.702947'
params = {
    "ll": ll,
    "spn": "0.15,0.025",    # Область показа: долгота, широта
    "l": "map",             # Тип карты: map, sat, skl и т.д.
    "size": "450,450",      # Размер изображения
    "api_key": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    with open('map_image.png', 'wb') as f:
        f.write(response.content)
    print("Изображение карты сохранено как 'map_image.png'")

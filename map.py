import requests

url = "https://static-maps.yandex.ru/1.x/"

ll = input()
spn = input()
if ll == '':
    ll = '37.531756,55.706950'
    spn = "0.14,0.000005"
params = {
    "ll": ll,
    "spn": spn,    # Область показа: долгота, широта
    "l": "map",             # Тип карты: map, sat, skl и т.д.
    "size": "450,450",      # Размер изображения
    "api_key": "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
}


#код для перелистывания вверх
ll = list(map(float, ll.split(',')))
ll[1] += 0.04
#вниз
ll = list(map(float, ll.split(',')))
ll[1] -= 0.04
#вправо
ll = list(map(float, ll.split(',')))
ll[0] += 0.04
#влево
ll = list(map(float, ll.split(',')))
ll[0] -= 0.04

#изменение масштаба
#-
spn = list(map(float, ll.split(',')))
spn[0] -= 0.01
#+
spn = list(map(float, ll.split(',')))
spn[0] += 0.01

spn = ','.join(list(map(str, spn)))
ll = ','.join(list(map(str, ll)))

#обновить картинку
response = requests.get(url, params=params)

if response.status_code == 200:
    with open('map_image.png', 'wb') as f:
        f.write(response.content)
    print("Изображение карты сохранено как 'map_image.png'")

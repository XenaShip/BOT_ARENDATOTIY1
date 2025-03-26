import os

import requests
from math import radians, sin, cos, sqrt, atan2

from dotenv import load_dotenv

load_dotenv()

YANDEX_GEOCODER_API_KEY = os.getenv("YANDEX_GEOCODER_API_KEY")
MOSCOW_METRO_STATIONS = {
    "Авиамоторная": (55.751682, 37.717821),
    "Автозаводская": (55.706451, 37.65868),
    "Академическая": (55.687674, 37.572232),
    "Александровский сад": (55.752194, 37.608414),
    "Алексеевская": (55.807355, 37.638602),
    "Алтуфьево": (55.897655, 37.587286),
    "Аннино": (55.583348, 37.596238),
    "Арбатская (синяя)": (55.752213, 37.603959),
    "Арбатская (голубая)": (55.752739, 37.605001),
    "Аэропорт": (55.800058, 37.531048),
    "Бабушкинская": (55.869944, 37.661632),
    "Багратионовская": (55.743117, 37.497338),
    "Баррикадная": (55.760324, 37.581974),
    "Бауманская": (55.772405, 37.678127),
    "Беговая": (55.773494, 37.541653),
    "Белорусская": (55.77638, 37.584577),
    "Беляево": (55.643149, 37.526092),
    "Бибирево": (55.883119, 37.60365),
    "Библиотека имени Ленина": (55.752287, 37.609344),
    "Боровицкая": (55.750796, 37.609365),
    "Ботанический сад": (55.844029, 37.638146),
    "Братиславская": (55.658515, 37.750725),
    "Бульвар Дмитрия Донского": (55.569411, 37.576221),
    "Варшавская": (55.653928, 37.620106),
    "ВДНХ": (55.821517, 37.6415),
    "Владыкино": (55.847951, 37.590127),
    "Водный стадион": (55.83918, 37.487288),
    "Войковская": (55.818994, 37.497082),
    "Волгоградский проспект": (55.72526, 37.68588),
    "Волжская": (55.690877, 37.752409),
    "Воробьевы горы": (55.710825, 37.55982),
    "Выставочная": (55.750341, 37.541725),
    "Выхино": (55.71525, 37.817894),
    "Говорово": (55.664095, 37.405136),
    "Динамо": (55.789476, 37.558498),
    "Добрынинская": (55.728914, 37.622527),
    "Домодедовская": (55.610028, 37.717725),
    "Достоевская": (55.781751, 37.613384),
    "Дубровка": (55.718387, 37.676119),
    "Жулебино": (55.684316, 37.856685),
    "Зябликово": (55.611637, 37.74511),
    "Измайловская": (55.787356, 37.781554),
    "Калужская": (55.656871, 37.540695),
    "Кантемировская": (55.635403, 37.656907),
    "Каховская": (55.653314, 37.606749),
    "Киевская": (55.744595, 37.56692),
    "Китай-город": (55.754592, 37.633996),
    "Коломенская": (55.678022, 37.663719),
    "Комсомольская": (55.776365, 37.656876),
    "Коньково": (55.633312, 37.518231),
    "Краснопресненская": (55.760172, 37.577751),
    "Красносельская": (55.780241, 37.666385),
    "Красные Ворота": (55.769808, 37.650984),
    "Крестьянская застава": (55.733383, 37.667472),
    "Кропоткинская": (55.745366, 37.603308),
    "Кузнецкий мост": (55.761195, 37.624417),
    "Кузьминки": (55.705181, 37.765574),
    "Кунцевская": (55.730201, 37.446024),
    "Курская": (55.758463, 37.659116),
    "Кутузовская": (55.74048, 37.534951),
    "Ленинский проспект": (55.706533, 37.584589),
    "Лермонтовский проспект": (55.702368, 37.851869),
    "Лубянка": (55.759813, 37.626047),
    "Люблино": (55.676565, 37.765277),
    "Марксистская": (55.741278, 37.653506),
    "Маяковская": (55.769808, 37.595426),
    "Медведково": (55.887642, 37.661231),
    "Международная": (55.747462, 37.533977),
    "Менделеевская": (55.781274, 37.598306),
    "Минская": (55.732548, 37.504122),
    "Митино": (55.84593, 37.361295),
    "Молодежная": (55.740166, 37.416717),
    "Нагатинская": (55.683785, 37.622041),
    "Нагорная": (55.672988, 37.610094),
    "Новокузнецкая": (55.741125, 37.629021),
    "Охотный ряд": (55.75715, 37.61577),
    "Партизанская": (55.787635, 37.750234),
    "Парк Культуры": (55.735473, 37.595391),
    "Парк Победы": (55.736251, 37.514865),
    "Перово": (55.750345, 37.788132),
    "Петровско-Разумовская": (55.836801, 37.573333),
    "Площадь Ильича": (55.747649, 37.682057),
    "Полежаевская": (55.777548, 37.516642),
    "Пражская": (55.612409, 37.603137),
    "Проспект Вернадского": (55.676903, 37.504874),
    "Пушкинская": (55.765396, 37.603475),
    "Речной вокзал": (55.855229, 37.476365),
    "Рижская": (55.792842, 37.63602),
    "Рязанский проспект": (55.717905, 37.792258),
    "Смоленская": (55.747073, 37.583913),
    "Таганская": (55.740994, 37.653306),
    "Тверская": (55.765911, 37.605013),
    "Улица Академика Янгеля": (55.595579, 37.601918),
    "Цветной бульвар": (55.771185, 37.620627),
    "Чеховская": (55.765837, 37.606637),
    "Чертановская": (55.640823, 37.606137),
    "Шаболовская": (55.718771, 37.608096),
}



def get_coordinates(address):
    """Получает координаты (широта, долгота) по адресу через API Яндекс Геокодера"""
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": YANDEX_GEOCODER_API_KEY,
        "geocode": address,
        "format": "json"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Ошибка API:", response.status_code, response.text)
        return None

    data = response.json()
    try:
        pos = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        lon, lat = map(float, pos.split())
        return lat, lon
    except (KeyError, IndexError):
        print("Ошибка: не удалось найти координаты для адреса:", address)
        return None


def haversine(lat1, lon1, lat2, lon2):
    R = 6371 * 1000
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def find_nearest_metro(lat, lon):
    """Ищет ближайшую станцию метро среди всех станций Москвы"""
    nearest_station = None
    min_distance = float("inf")

    for station, (m_lat, m_lon) in MOSCOW_METRO_STATIONS.items():
        distance = haversine(lat, lon, m_lat, m_lon)
        if distance < min_distance:
            min_distance = distance
            nearest_station = station, (m_lat, m_lon)

    return min_distance


if __name__ == "__main__":
    print("🔍 Запрос к Яндекс Геокодеру...")

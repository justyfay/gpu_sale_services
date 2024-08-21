import uuid
from collections import namedtuple
from typing import Type

from heplers.data.gpu_cards_random_data import gen_gpu_details_data


def net_video_data() -> list[dict]:
    products: list[dict] = []

    for i in range(100):
        gpu_details_data: Type[namedtuple] = gen_gpu_details_data()
        products.append({
            "productId": uuid.uuid4(),
            "name": f"Видеокарта {gpu_details_data.brand} {gpu_details_data.card_name}",
            "brandName": f"{gpu_details_data.brand}",
            "category": {
                "id": "5438",
                "name": "Видеокарты"
            },
            "materialCisNumber": "30069340",
            "description": f"Видеокарта {gpu_details_data.brand} {gpu_details_data.card_name} — устройство с частотой памяти, "
                           f"достигающей {gpu_details_data.memory_frequency} МГц, подходящее для запуска игр последних лет "
                           f"и работы с профессиональным графическим ПО. Видеопамять типа {gpu_details_data.gpu_memory_type} "
                           f"обладает объемом {gpu_details_data.gpu_memory_size} Гб. "
                           f"Разрядность шины — {gpu_details_data.gpu_memory_width}-битная. "
                           f"Число ALU (универсальные процессоры) — {gpu_details_data.universal_processors_count}.",
            "modelName": f"{gpu_details_data.card_name}",
            "properties": {
                "key": [
                    {
                        "name": "Заводские данные",
                        "priority": 1,
                        "properties": [
                            {
                                "id": 5552,
                                "name": "Гарантия",
                                "value": f"{gpu_details_data.guarantee_in_years} года",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 1,
                                "measure": None,
                                "iconPath": None
                            }
                        ]
                    },
                    {
                        "name": "Видеокарта",
                        "priority": 2,
                        "properties": [
                            {
                                "id": 2087,
                                "name": "Объем видеопамяти",
                                "value": f"{gpu_details_data.gpu_memory_size} ГБ",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 2,
                                "measure": None,
                                "iconPath": None
                            },
                            {
                                "id": 2383,
                                "name": "Тип видеопамяти",
                                "value": f"{gpu_details_data.gpu_memory_type}",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 3,
                                "measure": None,
                                "iconPath": None
                            },
                            {
                                "id": 2384,
                                "name": "Разрядность шины памяти",
                                "value": f"{gpu_details_data.gpu_memory_width}",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 4,
                                "measure": "Бит",
                                "iconPath": None
                            },
                            {
                                "id": 620,
                                "name": "Видеокарта",
                                "value": f"{gpu_details_data.card_name}",
                                "nameDescription": "Модуль компьютера, отвечающий за обработку графической составляющей данных.",
                                "valueDescription": None,
                                "priority": 8,
                                "measure": None,
                                "iconPath": None
                            }
                        ]
                    },
                    {
                        "name": "Видеопроцессор",
                        "priority": 5,
                        "properties": [
                            {
                                "id": 2385,
                                "name": "Частота графического процессора",
                                "value": f"{gpu_details_data.gpu_frequency}",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 5,
                                "measure": "МГц",
                                "iconPath": None
                            },
                            {
                                "id": 2386,
                                "name": "Число универсальных процессоров",
                                "value": f"{gpu_details_data.universal_processors_count}",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 15,
                                "measure": None,
                                "iconPath": None
                            }
                        ]
                    },
                    {
                        "name": "Электропитание",
                        "priority": 6,
                        "properties": [
                            {
                                "id": 2392,
                                "name": "Разъем питания",
                                "value": f"{gpu_details_data.power_connector}",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 6,
                                "measure": None,
                                "iconPath": None
                            },
                            {
                                "id": 2393,
                                "name": "Рекомендуемая мощность БП",
                                "value": f"{gpu_details_data.power_block}",
                                "nameDescription": None,
                                "valueDescription": None,
                                "priority": 7,
                                "measure": "Вт",
                                "iconPath": None
                            }
                        ]
                    },
                    {
                        "name": "Оперативная память",
                        "priority": 9,
                        "properties": [
                            {
                                "id": 634,
                                "name": "Частота памяти",
                                "value": f"{gpu_details_data.memory_frequency}",
                                "nameDescription": "Чем выше частота, тем быстрее будет передана информация на обработку и тем выше будет производительность устройства.",
                                "valueDescription": None,
                                "priority": 9,
                                "measure": "МГц",
                                "iconPath": None
                            }
                        ]
                    },
                ]
            },
            "brandNameTranslit": f"{gpu_details_data.brand.lower()}",
            "brandId": "1001",
            "brandLogoUrl": f"jcr:{uuid.uuid4()}",
            "isBrandVisible": True,
            "groups": [
                {
                    "name": "Компьютерные комплектующие",
                    "groupId": "17704",
                    "seoId": "5427",
                    "translitName": "komputernye-komplektuushhie",
                    "level": 0
                },
                {
                    "name": "Видеокарты",
                    "groupId": "17709",
                    "seoId": "5429",
                    "translitName": "videokarty",
                    "level": 1
                },
                {
                    "name": "Видеокарты",
                    "groupId": "17710",
                    "seoId": "5438",
                    "translitName": "videokarty",
                    "level": 2
                }
            ],
            "rating": {
                "star": 5,
                "count": 1,
                "percent": 101
            },
        })
    return products

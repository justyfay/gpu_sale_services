import uuid
from collections import namedtuple
from typing import Type

from heplers.data.gpu_cards_random_data import gen_gpu_details_data


def country_link_data(limit: int) -> list[dict]:
    products: list[dict] = []

    for i in range(limit):
        gpu_details_data: Type[namedtuple] = gen_gpu_details_data()

        products.append(
            {
                "product": {
                    "id": uuid.uuid4(),
                    "name": f"Видеокарта {gpu_details_data.brand} {gpu_details_data.card_name}",
                    "brandCompanyName": f"{gpu_details_data.brand}",
                    "propertiesGroup": [
                        {
                            "id": 1584,
                            "name": "Основные характеристики",
                            "properties": [
                                {
                                    "id": 1000003261,
                                    "name": "Интерфейс",
                                    "description": "",
                                    "value": f"{gpu_details_data.pci_interface}",
                                    "measure": "",
                                },
                                {
                                    "id": 4415,
                                    "name": "Техпроцесс",
                                    "description": "Технологический процесс, по которому изготовлен графический процессор. "
                                    "Техпроцесс определяет размеры полупроводниковых элементов, "
                                    "составляющих основу внутренних цепей графического процессора видеокарты.",
                                    "value": f"{gpu_details_data.technical_process_nanometers}",
                                    "measure": "нм",
                                },
                                {
                                    "id": 1000000623,
                                    "name": "Максимальное разрешение",
                                    "description": "Максимальное разрешение дисплея, поддерживаемое интерфейсными выходами видеокарты.",
                                    "value": f"{gpu_details_data.max_width}",
                                    "measure": "",
                                },
                                {
                                    "id": 198580,
                                    "name": "Число процессоров (ядер) CUDA",
                                    "description": "CUDA — это технология, запатентованная NVIDIA и используемая только в их видеокартах",
                                    "value": f"{gpu_details_data.cuda_count}",
                                    "measure": "",
                                },
                            ],
                        },
                        {
                            "id": 2540,
                            "name": "Охлаждение",
                            "properties": [
                                {
                                    "id": 4430,
                                    "name": "Система охлаждения",
                                    "description": "Система охлаждения графического процессора и видеопамяти"
                                    ". Чем выше производительность графического процессора и памяти, "
                                    "тем больше тепла они выделяют при работе. Система охлаждения "
                                    "позволяет надежно охлаждать видеокарту и отводить тепло из компьютерного корпуса.",
                                    "value": "активное",
                                    "measure": "",
                                },
                                {
                                    "id": 5390,
                                    "name": "Конструкция системы охлаждения",
                                    "description": "Ширина видеокарты, характеризует сколько места в корпусе при "
                                    "установке займет конкретная видеокарта. Из-за сильного "
                                    "тепловыделения высокопроизводительных видеокарт система охлаждения "
                                    "может занимать несколько слотов расширения в компьютерном корпусе. "
                                    "При этом система охлаждения видеокарты перекрывает соседние разъемы "
                                    "на материнской плате и не позволяет их использовать.",
                                    "value": f"{gpu_details_data.cooling_system_design}",
                                    "measure": "",
                                },
                                {
                                    "id": 198577,
                                    "name": "Тип вентилятора",
                                    "description": "",
                                    "value": f"{gpu_details_data.cooling_type}",
                                    "measure": "",
                                },
                                {
                                    "id": 198563,
                                    "name": "Количество вентиляторов",
                                    "description": "",
                                    "value": f"{gpu_details_data.cooling_count}",
                                    "measure": "",
                                },
                            ],
                        },
                        {
                            "id": 1585,
                            "name": "Технологии",
                            "properties": [
                                {
                                    "id": 162391,
                                    "name": "Поддержка технологий NVIDIA",
                                    "description": "",
                                    "value": f"{gpu_details_data.technologies}",
                                    "measure": "",
                                },
                                {
                                    "id": 155528,
                                    "name": "Поддержка трассировки лучей",
                                    "description": "Это технология, позволяющая создавать в играх реалистичные освещение, "
                                    "отражения, тени и, как следствие, приближенную к реальности картинку.",
                                    "value": f"{gpu_details_data.tracing}",
                                    "measure": "",
                                },
                                {
                                    "id": 158136,
                                    "name": "Поддержка DLSS",
                                    "description": "Сглаживание с алгоритмами глубокого обучения — это технология "
                                    "рендеринга на базе искусственного интеллекта, которая улучшает "
                                    "производительность и качество графики благодаря использованию "
                                    "специализированных тензорных ядер в видеокартах GeForce RTX.",
                                    "value": f"{gpu_details_data.dlss}",
                                    "measure": "",
                                },
                                {
                                    "id": 198572,
                                    "name": "Поддержка OpenGL",
                                    "description": "",
                                    "value": f"{gpu_details_data.opengl}",
                                    "measure": "",
                                },
                                {
                                    "id": 198570,
                                    "name": "Поддержка DirectX",
                                    "description": "",
                                    "value": f"{gpu_details_data.direct_x}",
                                    "measure": "",
                                },
                            ],
                        },
                        {
                            "id": 1586,
                            "name": "Разъемы",
                            "properties": [
                                {
                                    "id": 4424,
                                    "name": "Разъемов HDMI",
                                    "description": "Наличие в видеокарте разъема HDMI, который используется для передачи "
                                    "цифрового видеосигнала. Интерфейс HDMI разработан для передачи "
                                    "видео высокой четкости HDTV.",
                                    "value": f"{gpu_details_data.hdmi_ports}",
                                    "measure": "",
                                },
                                {
                                    "id": 4678,
                                    "name": "Версия разъема HDMI",
                                    "description": "Версия разъемов HDMI. В зависимости от версии, разъемы HDMI обладают "
                                    "различными характеристиками. Следует отметить, что изображение в "
                                    "формате 3D поддерживется только разъемами версии 1.4 и выше.",
                                    "value": f"{gpu_details_data.hdmi_port_version}",
                                    "measure": "",
                                },
                                {
                                    "id": 4426,
                                    "name": "Количество разъемов DisplayPort",
                                    "description": "Наличие в мониторе разъема Display Port, который используется для "
                                    "передачи цифрового видеосигнала. В отличии от разъемов DVI и HDMI, "
                                    "интерфейс Display Port имеет более широкий канал для передачи данных "
                                    "и большую максимальную длину кабеля.",
                                    "value": f"{gpu_details_data.display_ports}",
                                    "measure": "",
                                },
                                {
                                    "id": 4690,
                                    "name": "Версия разъема DisplayPort",
                                    "description": "Версия разъемов Display Port. В зависимости от версии, разъемы "
                                    "Display Port обладают различными характеристиками.",
                                    "value": f"{gpu_details_data.display_port_version}",
                                    "measure": "",
                                },
                                {
                                    "id": 176972,
                                    "name": "Количество поддерживаемых мониторов",
                                    "description": "",
                                    "value": f"{gpu_details_data.monitor_count}",
                                    "measure": "",
                                },
                            ],
                        },
                        {
                            "id": 1588,
                            "name": "Размеры",
                            "properties": [
                                {
                                    "id": 4432,
                                    "name": "Длина видеокарты",
                                    "description": "Длина видеокарты от планки с видеовыходами, до окончания "
                                    "текстолита или системы охлаждения.",
                                    "value": f"{gpu_details_data.gpu_width}",
                                    "measure": "мм",
                                },
                                {
                                    "id": 176969,
                                    "name": "Высота видеокарты",
                                    "description": "",
                                    "value": f"{gpu_details_data.gpu_height}",
                                    "measure": "мм",
                                },
                                {
                                    "id": 176974,
                                    "name": "Толщина видеокарты",
                                    "description": "",
                                    "value": f"{gpu_details_data.gpu_thickness}",
                                    "measure": "мм",
                                },
                            ],
                        },
                        {
                            "id": 1718,
                            "name": "Упаковка",
                            "properties": [
                                {
                                    "id": 166024,
                                    "name": "Габариты упаковки (ед) ДхШхВ",
                                    "description": "",
                                    "value": gpu_details_data.package_size,
                                    "measure": "м",
                                },
                                {
                                    "id": 171239,
                                    "name": "Вес упаковки (ед)",
                                    "description": "",
                                    "value": gpu_details_data.package_weight,
                                    "measure": "кг",
                                },
                            ],
                        },
                    ],
                }
            }
        )
    return products

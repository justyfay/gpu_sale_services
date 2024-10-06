import random
from collections import namedtuple

brands = ["MSI", "ASUS", "ASRock", "GIGABYTE", "Palit"]
graphic_cards = [
    "GeForce RTX 3060",
    "GeForce RTX 3050",
    "GeForce RTX 5090",
    "GeForce RTX 4090",
    "Radeon RX 580",
    "GeForce RTX 4060",
    "GeForce RTX 5070",
    "GeForce RTX 4070",
    "GeForce GTX 1650",
    "GeForce RTX 2060",
    "GeForce RTX 3070",
    "Radeon RX 6600",
    "GeForce GTX 1050 Ti",
    "GeForce GTX 1060",
    "GeForce RTX 4070 SUPER",
    "GeForce GTX 1080 Ti",
    "Radeon RX 5700 XT",
    "GeForce GTX 1660 SUPER",
    "GeForce RTX 4060 Ti 8 GB",
    "Radeon RX 6700 XT",
    "GeForce RTX 3060 Ti",
    "GeForce RTX 4070 Ti SUPER",
    "GeForce RTX 3050 8 GB",
    "Radeon 780M",
    "Radeon RX 570",
    "Radeon RX 7800 XT",
    "GeForce RTX 3080",
    "GeForce GTX 1070",
    "Radeon RX 7900 XTX",
    "Radeon RX 7700 XT",
    "GeForce RTX 4080 SUPER",
    "GeForce RTX 2060 SUPER",
    "Radeon Vega 8",
    "Radeon RX 7600",
    "GeForce RTX 2080 Ti",
    "GeForce GTX 960",
    "GeForce GTX 1080",
    "GeForce RTX 3090",
    "GeForce GTX 1660 Ti",
    "Radeon RX 6600 XT",
    "GeForce RTX 4050",
    "GeForce GTX 750 Ti",
    "GeForce RTX 4070 Ti",
    "GeForce GTX 970",
    "Radeon RX 7900 GRE",
    "Radeon RX 6750 XT",
    "GeForce GTX 1050",
    "GeForce RTX 4080",
    "Radeon RX 6650 XT",
    "Radeon RX 550",
    "GeForce RTX 3070 Ti",
]
guarantee_in_years = [2, 3]
gpu_memory_size_in_gigabyte = [4, 8, 16, 24]
gpu_memory_type = ["GDPR6", "GDPR5", "GDPR4"]
gpu_memory_width = [128, 192, 256, 512, 384]
memory_frequency = [3000, 9000, 8000, 11400, 12000, 20000, 224000]
power_connector = ["8 pin", "6 + 2 pin", "6 pin", "12VHPWR", "12V-2X6"]
power_block = [450, 400, 350, 500, 650, 800]
pci_interface = ["PCIe 4.0", "PCIe 5.0", "PCIe 6.0"]
technical_process_nanometers = [1.6, 1.4, 2, 3, 4, 5, 6, 10, 12]
max_width = ["2560x1440", "7680 х 4320", "1920 x 1480"]
cooling_system_design = ["трехслотовая", "двухслотовая"]
cooling_type = ["осевой", "диаметральный", "центробежный"]
technologies = [
    "NVIDIA DLSS",
    "NVIDIA Reflex",
    "NVIDIA STUDIO",
    "NVIDIA Ray Tracing",
    "NVIDIA G-Sync",
    "NVIDIA Broadcast",
    "NVIDIA Game Ready",
    "NVIDIA Shadow Play",
    "NVIDIA Ansel",
    "NVIDIA Freestyle",
    "NVIDIA NVENC",
    "NVIDIA VR Works",
    "NVIDIA CUDA",
]
tracing = ["есть", "нет"]
dlss = ["есть", "нет"]
direct_x = ["DirectX 12 Ultimate", "DirectX 12", "DirectX 11"]
opengl = ["4.0", "4.1", "4.2", "4.3", "4.4", "4.5", "4.6"]
hdmi_port_version = ["2.0", "2.1", "2.1a"]
display_port_version = ["1.2", "1.3", "1.4a"]


def gen_gpu_details_data() -> type[namedtuple]:
    data: type[tuple] = namedtuple(
        typename="data",
        field_names=(
            "brand",
            "card_name",
            "guarantee_in_years",
            "gpu_memory_size",
            "gpu_memory_type",
            "gpu_memory_width",
            "memory_frequency",
            "gpu_frequency",
            "universal_processors_count",
            "power_connector",
            "power_block",
            "pci_interface",
            "technical_process_nanometers",
            "max_width",
            "cuda_count",
            "cooling_system_design",
            "cooling_type",
            "cooling_count",
            "technologies",
            "tracing",
            "dlss",
            "direct_x",
            "opengl",
            "hdmi_ports",
            "hdmi_port_version",
            "display_ports",
            "display_port_version",
            "monitor_count",
            "gpu_width",
            "gpu_height",
            "gpu_thickness",
            "package_size",
            "package_weight",
        ),
    )
    return data(
        brand=random.choice(brands),
        card_name=random.choice(graphic_cards),
        guarantee_in_years=random.choice(guarantee_in_years),
        gpu_memory_size=random.choice(gpu_memory_size_in_gigabyte),
        gpu_memory_type=random.choice(gpu_memory_type),
        gpu_memory_width=random.choice(gpu_memory_width),
        memory_frequency=random.choice(memory_frequency),
        gpu_frequency=random.choice(range(1807, 3345)),
        universal_processors_count=random.randint(3584, 4678),
        power_connector=random.choice(power_connector),
        power_block=random.choice(power_block),
        pci_interface=random.choice(pci_interface),
        technical_process_nanometers=random.choice(technical_process_nanometers),
        max_width=random.choice(max_width),
        cuda_count=random.choice(range(10240, 12400)),
        cooling_system_design=random.choice(cooling_system_design),
        cooling_type=random.choice(cooling_type),
        cooling_count=random.choice(range(1, 3)),
        technologies=list(set(random.choices(technologies, k=random.choice(range(2, 5))))),
        tracing=random.choice(tracing),
        dlss=random.choice(dlss),
        direct_x=random.choice(direct_x),
        opengl=random.choice(opengl),
        hdmi_ports=random.choice(range(1, 2)),
        hdmi_port_version=random.choice(hdmi_port_version),
        display_ports=random.choice(range(1, 2)),
        display_port_version=random.choice(display_port_version),
        monitor_count=random.choice(range(2, 6)),
        gpu_width=random.choice(range(270, 370)),
        gpu_height=random.choice(range(123, 145)),
        gpu_thickness=random.choice(range(51, 69)),
        package_size=(
            f"0.{random.choice(range(29, 49))}x0."
            f"{random.choice(range(10, 17))}x0."
            f"{random.choice(range(22, 34))}"
        ),
        package_weight=f"{random.choice(range(2, 3))}.{random.choice(range(311, 589))}",
    )

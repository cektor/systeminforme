import platform
import subprocess

def get_os_info():
    # İşletim sistemi adını ve sürümünü al
    os_name = platform.system()
    os_version = platform.release()

    return f"{os_name} {os_version}"

def get_cpu_info():
    # CPU modelini al
    cpu_info = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq | awk -F': ' '{print $2}'", shell=True)
    cpu_model = cpu_info.decode("utf-8").strip()

    return cpu_model

def get_memory_info():
    # Toplam bellek miktarını al
    mem_info = subprocess.check_output("free -h | awk '/^Mem:/ {print $2}'", shell=True)
    total_memory = mem_info.decode("utf-8").strip()

    return total_memory

def get_gpu_info():
    # Ekran kartı bilgilerini al
    gpu_info = subprocess.check_output("lspci | grep -i vga | awk -F': ' '{print $2}'", shell=True)
    gpu_model = gpu_info.decode("utf-8").strip()

    return gpu_model

def main():
    print("Sistem Bilgileri")
    print("-----------------")
    print("İşletim Sistemi:", get_os_info())
    print("CPU Modeli:", get_cpu_info())
    print("Toplam Bellek:", get_memory_info())
    print("Ekran Kartı Modeli:", get_gpu_info())

if __name__ == "__main__":
    main()


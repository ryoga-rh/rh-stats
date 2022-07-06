from dis import dis
from traceback import print_tb
import psutil
import platform
from datetime import datetime
import os
from colorama import *
import sys

def limpiar():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    limpiar()
    print(f"""
          
{Fore.LIGHTBLUE_EX}──▒▒▒▒▒▒─{Fore.LIGHTYELLOW_EX}──▄████▄
{Fore.LIGHTBLUE_EX}─▒─▄▒─▄▒─{Fore.LIGHTYELLOW_EX}─███▄█▀
{Fore.LIGHTBLUE_EX}─▒▒▒▒▒▒▒─{Fore.LIGHTYELLOW_EX}▐████──█─█
{Fore.LIGHTBLUE_EX}─▒▒▒▒▒▒▒─{Fore.LIGHTYELLOW_EX}─█████▄
{Fore.LIGHTBLUE_EX}─▒─▒─▒─▒─{Fore.LIGHTYELLOW_EX}──▀████▀

          """)

def infobasica():
    plataforma = platform.uname()
    limpiar()
    print(Fore.LIGHTGREEN_EX)
    print("<" + "=" * 40 + " Informacion Basica Del Sistema " + "=" * 40 + ">")
    print("#")
    print("# Sistema Operativo: ")
    print(f"# {plataforma.system}")
    print(f"#")
    print(f"# Nombre del nodo: ")
    print(f"# {plataforma.node}")
    print(f"#")
    print(f"# Libreria :")
    print(f"# {plataforma.release}")
    print(f"#")
    print(f"# Version")
    print(f"# {plataforma.version}")
    print(f"#")
    print(f"# Procesador")
    print(f"# {plataforma.processor}")
    print(f"#")
    print(f"# Maquina")
    print(f"# {plataforma.machine}")
    print(Fore.RESET)

def cpu():
    limpiar()
    infobasica()
    cpu = psutil.cpu_freq()
    print(Fore.LIGHTGREEN_EX)
    print("<" + "=" * 39 + " CPU Info " + "=" * 39 + ">")
    print("#")
    print(f"# Nucleos Fisicos")
    print(f"# {psutil.cpu_count(logical= False)}")
    print(f"#")
    print(f"# Nucleos Totales")
    print(f"# {psutil.cpu_count(logical=True)}")
    print(f"#")
    print("# Maxima Frecuencia del CPU")
    print(f"# {cpu.max: .2f}Mhz")
    print("#")
    print("# Minima Frecuencia del CPU")
    print(f"# {cpu.min: .2f}Mhz")
    print("#")
    print("# Frecuencia Actual")
    print(f"# {cpu.current: .2f}Mhz")
    print("#")
    print(Fore.RESET)
    
def memoria():
    limpiar()
    memory = psutil.virtual_memory()
    disponible = memory.total
    print(f"{Fore.LIGHTGREEN_EX}")
    print("<" + "=" * 39 + " Memory Info " + "=" * 39 + ">")
    print("#")
    print("# Total ")
    print(f"# {memory.total :,}")
    print("# Disponible")
    print(f"# {disponible :,}")
    print("#")
    print("# ")

menu()

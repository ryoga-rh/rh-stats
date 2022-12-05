from dis import dis
from traceback import print_tb
import psutil
import platform
from datetime import datetime
import time
import os
from colorama import *
import sys
import signal

def limpiar():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def ctrlc(signal, freame):
    limpiar()
    logo()
    print(Fore.RED+"Precionaste ctrl c, el proceso termino, saliendo...")
    time.sleep(2)
    salida()

signal.signal(signal.SIGINT, ctrlc)

def salida():
    limpiar()


def logo():
    limpiar()
    print(f"""    
    ──{Fore.LIGHTBLUE_EX}▒▒▒▒▒▒{Fore.WHITE}───{Fore.LIGHTYELLOW_EX}▄████▄{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒─▄▒─▄▒{Fore.WHITE}──{Fore.LIGHTYELLOW_EX}███▄█▀{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒▒▒▒▒▒▒{Fore.WHITE}─{Fore.LIGHTYELLOW_EX}▐████{Fore.WHITE}──{Fore.LIGHTYELLOW_EX}█{Fore.WHITE}─{Fore.LIGHTYELLOW_EX}█{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒▒▒▒▒▒▒{Fore.WHITE}──{Fore.LIGHTYELLOW_EX}█████▄{Fore.WHITE}
    ─{Fore.LIGHTBLUE_EX}▒─▒─▒─▒{Fore.WHITE}───{Fore.LIGHTYELLOW_EX}▀████▀{Fore.WHITE}
    {Fore.RESET}
              """)

def menu():
    logo()
    print(f"{Fore.LIGHTCYAN_EX}Estas son las funciones que tiene esta herramienta por ahora...{Fore.RESET}")
    print(f"""
    {Fore.LIGHTGREEN_EX}1.- Informacion Basica: Tiene informacion basica de tu dispositivo, como Sistema operativo, Librerias, Version y otras cosas.
    2.- Informacion del cpu: Nucleos y frecuencia
    3.- Memoria: Memoria total y disponible
    """)
    eleccion = input("Que quieres ver ahora? ")
    if eleccion == "1" or eleccion == "basica":
        infobasica()
    elif eleccion == "2" or eleccion == "cpu":
        cpu()
    elif eleccion == "3" or eleccion == "memoria":
        memoria()
    else:
        print("Opcion no valida, intentalo de nuevo")
        menu()

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
    print(f"# Procesadores Logicos")
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


def load_animation():
    load_str = "..."
    ls_len = len(load_str)

    animacion = "|/-\\"
    contador = 0

    tiempocontador = 0

    i = 0

    while (tiempocontador != 100):

        time.sleep(0.075)

        load_str_list = list(load_str)

        x = ord(load_str_list[i])

        y = 0

        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        sys.stdout.write("\r" + res + animacion[contador])
        sys.stdout.flush()

        load_str = res

        contador = (contador + 1) % 4
        i = (i + 1) % ls_len
        tiempocontador = tiempocontador + 1

    if os.name == "nt":
        os.system("cls")


    else:
        os.system("clear")




def procesoTerminado():
    print(f"""
El proceso termino, Que deseas hacer ahora? 
1.- Volver al menu
2.- Salir

""")

load_animation()
menu()


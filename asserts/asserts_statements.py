# Based on file ../debug/debugging.py
# File on https://github.com/FernandoTorresL/Curso_Python_Intermedio/blob/main/asserts/asserts_statements.py
def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ")

    assert num.isnumeric(), "Debes ingresar un número positivo"
    assert int(num) > 0, "Debes ingresar un número positivo"

    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()

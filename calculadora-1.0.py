print("ola we soy la calculadora puke release 1.0")



def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

while True:
    print("1: suma")
    print("2: resta")
    print("3: multiplicacion")
    print("4: division")
    print("5: salir")

    opción = input("Elige una operación, te doy la respuesta y me apagas: ")

    if opción == "5":
       print("por fiiiiiin")
       break

    if opción in ["1", "2", "3", "4"]:
      número1 = float(input("ingresa el primer numero w:"))
      número2 = float(input("ingresa el segundo w:"))

      if opción == "1":
        print("ira w la suma", suma(número1, número2))


      elif opción == "2":
          print("la resta ahora w:", resta(número1, número2))


      elif opción == "3":
          print("la multiplicación ahora w como la ves:", multiplicacion(número1, número2))



      elif opción == "4":
          print("oh q la chingada toca la división y ya apágame:", division(número1, número2))

def calcular(num1, operador, num2):
  """
  Realiza operaciones aritméticas básicas según el operador.
  """
  if operador == "+":
    return num1 + num2
  elif operador == "-":
    return num1 - num2
  elif operador == "*":
    return num1 * num2
  elif operador == "/":
    return num1 / num2
  else:
    print("Operador inválido")
    return None

while True:
  # Obtén la entrada del usuario
  num1 = float(input("Ingresa el primer número: "))
  operador = input("Ingresa el operador (+, -, *, /): ")
  num2 = float(input("Ingresa el segundo número: "))

  # Realiza el cálculo
  resultado = calcular(num1, operador, num2)

  # Imprime el resultado (maneja el potencial None por operador inválido)
  if resultado is not None:
    print("Resultado:", resultado)

  # Pregunta al usuario si desea continuar
  opcion = input("¿Deseas continuar? (s/n): ")
  if opcion.lower() != "s":
    break

print("Calculadora cerrada.")

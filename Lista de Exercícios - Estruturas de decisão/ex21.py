horas = int(input("Digite as horas (0-23): "))
minutos = int(input("Digite os minutos (0-59): "))

segundos = horas * 3600 + minutos * 60

print(f"{horas}h{minutos} = {segundos} segundos.")
velocidade_veiculo = 61
multa = 0

if velocidade_veiculo > 80:
    multa = 360
    print(f"A velocidade de {velocidade_veiculo} recebe uma multa de: R${multa}")
elif velocidade_veiculo > 60:
    multa = 180
    print(f"A velocidade de {velocidade_veiculo} recebe uma multa de: R${multa}")
else:
    print(f"Não existe multa para velocidade de {velocidade_veiculo}")
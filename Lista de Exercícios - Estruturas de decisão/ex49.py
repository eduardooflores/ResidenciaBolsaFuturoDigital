from datetime import datetime

nascimento_primeiro_irmao = input("Digite a data de nascimento do primeiro irmão (formato DD/MM/YYYY): ")
data_nascimento_primeiro_irmao = datetime.strptime(nascimento_primeiro_irmao, "%d/%m/%Y")

nascimento_segundo_irmao = input("Digite a data de nascimento do segundo irmão (formato DD/MM/YYYY): ")
data_nascimento_segundo_irmao = datetime.strptime(nascimento_segundo_irmao, "%d/%m/%Y")

nascimento_terceiro_irmao = input("Digite a data de nascimento do terceiro irmão (formato DD/MM/YYYY): ")
data_nascimento_terceiro_irmao = datetime.strptime(nascimento_terceiro_irmao, "%d/%m/%Y")

if (data_nascimento_primeiro_irmao == data_nascimento_segundo_irmao
    and data_nascimento_primeiro_irmao == data_nascimento_terceiro_irmao):
    print("TRIGEMEOS")
elif (data_nascimento_primeiro_irmao == data_nascimento_segundo_irmao
      or data_nascimento_primeiro_irmao == data_nascimento_terceiro_irmao
      or data_nascimento_segundo_irmao == data_nascimento_terceiro_irmao):
    print("GEMEOS")
else:
    print("Irmãos")

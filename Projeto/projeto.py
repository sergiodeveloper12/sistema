import datetime
import re 
print('Bem vindo ao CSA Yudi')
hoje = datetime.date.today()
print(hoje)

print(" Escolha as opções:")
def verificar_usuario(opcao):
    if opcao is 1:
        return "Bem-vindo colaborador Assai!"
    elif opcao is 2:
        return "Bem-vindo prestador de serviço!"
    else:
        return "Acesso restrito"
   

opcao = int( input("Digite 1 para colaborador, 2 para prestador de serviço ou 'sair' para sair: "))
mensagem = verificar_usuario(opcao)

print(mensagem)
matricula = int(input("Digite sua Matricula:"))
def Verifica_Matricula (matricula):
    padrão = r"^\d{7}$"
    if re.match (padrão, matricula):
        return True
        
    else:
        return False
    

def Matricula_verificada(matricula):
    if matricula == matricula:
         return 'matricula valida'
    else:
        return "digite novemente"
    

print ('Escolha sseu serviço')



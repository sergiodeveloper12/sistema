import datetime
import re 
import webbrowser
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
    
print("Bem vindo {}".format (matricula)) 

 
print ('Digite 1 para acessar o Horus')
print  ('Digite 2 para acessar o emporium')
print  ('Digite 3 para RUB')
print ('Digite 4 para user o endpoint')
serviço = int(input("Digite a opção:"))

if serviço is 1:
        webbrowser.open('https://horus-next.corp.assai.com.br/auth/login')
elif serviço is 2:
        webbrowser.open('http://10.173.0.49/index.php?jscr=1')
elif serviço is 3:
       webbrowser.open('https://rub.corp.assai.com.br/vue/#/core/dashboard')
elif serviço is 4:
      webbrowser.open('https://epcentral.corp.assai.com.br:8383/client#/login')




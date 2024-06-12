print("___Crie sua Senha___\n Atenção!  \n A senha deve conter pelo menos 16 caracteres, incluindo pelo menos duas letras maiúsculas, dois números e dois caracteres especiais.\n")

#variaveis de entrada
senha=input("Digite a senha:")
senha2=input("Digite a senha novamente:")


totalDeCaracteres=len(senha)

maiusculo=0
numer=0
especiais=0



if totalDeCaracteres<16:
    print("Senha inválida,a senha deve ter pelo menos 16 caracteres")
else:

    for iten in senha:
        if iten.isupper()==True:
            maiusculo+=1
        elif iten.isdigit()==True:
            numer+=1
        elif iten.isalnum()==False:
            especiais+=1


if maiusculo<2:
    avaliar_maisculo=False
    print("Senha inválida, falta letras maiúsculas")
else:
    avaliar_maisculo=True
    

if numer<2:
    avaliar_numero=False
    print("Senha inválida, falta números")
else:
    avaliar_numero=True
    

if especiais<2:
    avaliar_especiais=False
    print("Senha inválida, falta caracteres especiais")  
else:
    avaliar_especiais=True
        
    
    
if senha2 != senha:
    print("Erro! \n As senhas não se assemelham")
           

elif avaliar_maisculo==True and avaliar_numero==True and avaliar_especiais==True:
    print("senha válida \n Senha Criada")               




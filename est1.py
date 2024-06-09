
#Estoque de Frutas

def adicionar(nome,precoUNI,quantidade):
    fruta={
        "nome":nome,
        "quantidade":quantidade,
        "preco":precoUNI
    }
    estoque.append(fruta)
    print("---------------")
    print("Fruta adicionada ao estoque")


def mostrar():
    if not estoque:
        print(" ======== ")
        print("Estoque vazio")
    else:
        print("Estoque atual:")
        for fruta in estoque:
            print("---------------")
            print(f"Nome: {fruta['nome']}, Quantidade: {fruta['quantidade']}, Preço: {fruta['preco']}")
    

def removerFruta(nome):
    for iten in estoque:
        if iten["nome"]==nome:
            estoque.remove(iten)
            print("---------------")
            print("fruta excluida")
        else:
            print("---------------")
            print("fruta não existe no estoque")
        
                
def atualizarEstoque(nome,quantidade):
    for iten in estoque:
        if iten["nome"]==nome:
            iten["quantidade"]=quantidade
            print("---------------")
            print(f"Quantidade de: {nome}, atualizada para: {quantidade}")
        else:
            print("---------------")
            print("fruta não existe no estoque")


estoque=[]

while True:
    print("____________________")
    print("1- Adicionar")
    print("2- Atualizar")
    print("3- Remover")
    print("5- Mostrar Estoque")
    print("0- Desligar")

    resposta=input("Escolha:")

    if resposta=="1":
        nome=str(input("Nome da fruta:"))
        precoUNI=float(input("Preco:"))
        quantidade=int(input("Quantidade:"))
        adicionar(nome,precoUNI,quantidade)
        #print(estoque)

    if resposta=="2":
        nome=str(input("Nome da fruta:"))
        quantidade=int(input("Atualizar quantidade:"))
        atualizarEstoque(nome,quantidade)
    
    if resposta=="3":
        nome=str(input("Nome da fruta para excluir:"))
        removerFruta(nome)

    if resposta=="5":
        mostrar()
    
    if resposta=="0":
        break



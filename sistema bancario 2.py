# separar as funções de saque, deposito e extrato em funções def
# criar func cadastrar usuario e cadastrar conta bancaria
# saque deve receber argumentos por keyword - saldo, valor, extrato, limite, numero_saques, limite_saques / retorno saldo, extrato
# depoisto deve receber argumentos por posição - saldo, valor, extrato / saldo, extrato
# extrato deve receber por keyword e posição - posicional - saldo / keyword - extrato
# criar usuario - deve armazenar os usuarios em lista, composto por nome, data de nascimento, cpf e endereço (endereço str:logradouro - num - bairro - cidade/sigla estado) somente numeros do cpf, nao podendo repetir cpf pra mais de um user
# conta corrente - armazenar contas em lista composto por agencia, num conta, usuario. num conta sequencial iniciando por 1, agencia (0001 fix). usuario pode ter multiplas contas porem a conta pertence a somente um usario
# vincular usuario a conta - filtre a lista de user buscando num de cpf de cada usuario

def menu():
    menu = """\n
    ===============MENU===============
    [d] Depositar
    [s] Sacar
    [e] Extrato 
    [nc] Nova Conta
    [nu] Novo Usuário
    [lc] Lista Contas
    [q] Sair
    =>"""
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falho! O valor do saque excedeu o limite")

    elif excedeu_saques:
        print("Operação falhou! Limite de saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Operação realizada com sucesso!")

    else:
        print("Operação falho! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("=======================EXTRATO=======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=====================================================")


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente.")
        return
    
    nome = input("Digite seu nome: ")
    data_nasc = input("Informe sua data de nascimento (dd/mm/aaaa):")
    endereco = input("Informe seu endereço (logradouro, num - bairro - cidade/siglado estado):")

    usuarios.append({"nome": nome, "data_nasc": data_nasc,"cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado [0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não encontrado! Encerrando criação de conta.")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:{conta["agencia"]}
        C/C:{conta["numero_conta"]}
        Titular:{conta["usuario"]["nome"]}
        """
    print("=" * 100)
    print(linha)

def main():

    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
                               limite=limite, numero_saques=numero_saques, limite_saque=limite_saque)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = (len(contas)) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
        
            if conta:
                contas.append(conta)
    
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Operação invalida.")

main()
# Dicionário para armazenar os usuários
usuarios = {}

# Função para criar um usuário
def criar_usuario(nome, cpf):
    usuarios[cpf] = {
        'nome': nome,
        'cpf': cpf,
        'contas': []  # Lista para armazenar as contas do usuário
    }

# Função para criar uma conta vinculada a um usuário
def criar_conta(cpf, numero_conta, saldo_inicial):
    conta = {
        'agencia': "0001",
        'numero_conta': numero_conta,
        'saldo': saldo_inicial
    }
    
    # Adiciona a conta na lista de contas do usuário
    usuarios[cpf]['contas'].append(conta)

def mostrar_dados_usuario(cpf):
    usuario = usuarios.get(cpf)
    
    if usuario:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print("Contas vinculadas:")
        
        for conta in usuario['contas']:
            print(f"  Agência: {conta['agencia']}, Número da conta: {conta['numero_conta']}, Saldo: {conta['saldo']}")
    else:
        print("Usuário não encontrado.")

# Exemplo de uso
criar_usuario('João Silva', '123.456.789-00')

criar_conta('123.456.789-00', '001', 1000.0)
criar_conta('123.456.789-00', '002', 500.0)

mostrar_dados_usuario('123.456.789-00')

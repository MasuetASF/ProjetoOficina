from view.formatter import mensagem

def formatar_clientes(lista):
    return [
        {"id": c[0], "nome": c[1], "telefone": c[2], "email": c[3]}
        for c in lista
    ]
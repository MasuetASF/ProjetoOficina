from view.formatter import mensagem

def formatar_veiculos(lista):
    return [
        {"id": v[0], "modelo": v[1], "placa": v[2], "ano": v[3], "cliente": v[4]}
        for v in lista
    ]
from view.formatter import mensagem

def formatar_ordens(lista):
    return [
        {
            "id": o[0],
            "cliente": o[1],
            "veiculo": o[2],
            "placa": o[3],
            "descricao": o[4],
            "status": o[5],
            "valor": o[6],
            "data_abertura": o[7],
            "data_fechamento": o[8],
        }
        for o in lista
    ]
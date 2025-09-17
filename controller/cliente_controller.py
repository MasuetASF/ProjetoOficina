from flask import Blueprint, jsonify, request
from model.cliente_model import adicionar_cliente,listar_clientes,deletar_cliente,atualizar_cliente
from view.cliente_view import formatar_clientes, mensagem
cliente_bp = Blueprint("cliente_bp", __name__)

@cliente_bp.route("/clientes", methods=["POST"])
def criar_cliente():
    data = request.json
    adicionar_cliente(
        data["nome"],
        data["telefone"],
        data["email"])
    return jsonify({"mensagem": "Cliente cadastrado com sucesso!"}), 201

@cliente_bp.route("/clientes", methods=["GET"])
def obter_clientes():
    clientes = listar_clientes()
    return jsonify(formatar_clientes(clientes))

@cliente_bp.route("/clientes/<int:cliente_id>", methods=["PUT"])
def editar_cliente(cliente_id):
    data = request.json
    linhas = atualizar_cliente(
        cliente_id,
        data["nome"],
        data["telefone"],
        data["email"])
    if linhas == 0:
        return jsonify({"erro": "Cliente não encontrado"}), 404
    return jsonify({"mensagem": "Cliente atualizado com sucesso!"})

@cliente_bp.route("/clientes/<int:cliente_id>", methods=["DELETE"])
def excluir_cliente(cliente_id):
    linhas = deletar_cliente(cliente_id)
    if linhas == 0:
        return jsonify({"erro": "Cliente não encontrado"}), 404
    return jsonify({"mensagem": "Cliente removido com sucesso!"})
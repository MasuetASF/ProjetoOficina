from flask import request, jsonify, Blueprint
from model.ordem_model import adicionar_ordem,listar_ordens, deletar_ordem,atualizar_ordem
from view.ordem_view import formatar_ordens,mensagem


ordem_bp = Blueprint("ordem_bp", __name__)

@ordem_bp.route('/ordens', methods=['POST'])
def criar_ordem():
    data = request.json
    novo_id = adicionar_ordem(
        data['cliente_id'],
        data['veiculo_id'],
        data['descricao'],
        data.get('valor')
    )
    return jsonify(mensagem(f'Ordem criada com o ID: {novo_id}')), 201

@ordem_bp.route('/ordens', methods=['GET'])
def obter_ordens():
    return jsonify(formatar_ordens(listar_ordens())), 200

@ordem_bp.route('/ordens/<int:ordem_id>', methods=['PUT'])
def editar_ordem(ordem_id):
    data = request.json
    linhas = atualizar_ordem(
        ordem_id,
        data['cliente_id'],
        data['veiculo_id'],
        data['descricao'],
        data['status'],
        data['valor']
    )
    if linhas == 0:
        jsonify({"erro": "Ordem não encontrada"}), 404
    return jsonify({"mensagem": "Ordem atualizada com sucesso"}), 200

@ordem_bp.route('/ordens/<int:ordem_id>', methods=['DELETE'])
def deletar_ordem(ordem_id):
    linhas = deletar_ordem(ordem_id)
    if linhas == 0:
        jsonify({"erro": "ordem não encontrada"}), 404
    jsonify({"mensagem": "Ordem deletada com sucesso"}), 200
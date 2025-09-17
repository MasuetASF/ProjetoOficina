from flask import request, jsonify, Blueprint
from model.ordem_model import adicionar_ordem,listar_ordens
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
def list_ordens():
    return jsonify(formatar_ordens(listar_ordens())), 200

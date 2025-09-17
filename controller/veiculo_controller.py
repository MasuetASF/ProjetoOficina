from flask import Blueprint, request, jsonify
from model.veiculo_model import adicionar_veiulo, listar_veiculos
from view.veiculo_view import formatar_veiculos, mensagem

veiculo_bp = Blueprint("veiculo_bp", __name__)

@veiculo_bp.route("/veiculos", methods=["POST"])
def post_veiculo():
    data = request.json
    novo_id = adicionar_veiulo(
        data["cliente_id"],
        data["modelo"],
        data["placa"],
        data.get("ano"))
    return jsonify(mensagem(f'Veiculo criado com o ID: {novo_id}')), 201

@veiculo_bp.route('/veiculos', methods=['GET'])
def get_veiculos():
    return jsonify(formatar_veiculos(listar_veiculos())), 200



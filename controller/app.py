from flask import Flask
from db.db import inicializar_banco

# Inicializa o app Flask
app = Flask(__name__)

# Inicializa tabelas do banco
inicializar_banco()

# Importa e registra os blueprints
from cliente_controller import cliente_bp
from controller.veiculo_controller import veiculo_bp
from controller.ordem_controller import ordem_bp

app.register_blueprint(cliente_bp)
app.register_blueprint(veiculo_bp)
app.register_blueprint(ordem_bp)


if __name__ == "__main__":
    app.run(debug=True)
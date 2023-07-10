from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète_iciyftf'  # Remplacez par votre propre clé secrète
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lamine:passer@localhost/examengl'  # Remplacez avec vos informations de connexion à la base de données

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import os
import yaml
from utils import logger
from database import generate_unique_code

def load_config(env='development'):
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config.get(env, config['default'])

environment = os.getenv('ENV', 'development')
config = load_config(environment)


app = Flask(__name__)
app.config['DEBUG'] = config['debug']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.json
    category1 = data.get('category1')
    category2 = data.get('category2')

    if category1 and category2:
        code = generate_unique_code(category1, category2)
        return jsonify({'generated_code': code})
    else:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    logger(f"Starting {config['app_name']} in {config['environment']} mode")
    app.run(debug=config['debug'])

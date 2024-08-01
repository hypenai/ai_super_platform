import yaml
import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def get_hyperparameters():
    hyperparameters_path = os.path.join(os.path.dirname(__file__), 'hyperparameters.json')
    with open(hyperparameters_path, 'r') as file:
        hyperparameters = json.load(file)
    return hyperparameters

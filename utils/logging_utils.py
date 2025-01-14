import logging
from config.config import load_config

def setup_logger():
    config = load_config()
    logging.basicConfig(
        level=config['logging']['level'],
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename=config['logging']['file']
    )
    return logging.getLogger('AI_Super_Platform')

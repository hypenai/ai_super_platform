import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from setup import project_root

import argparse
from src.data_processing import preprocess_data
from src.model_training import train_model
from utils.logging_utils import setup_logger

def main(mode):
    logger = setup_logger()
    logger.info(f"AI Super Platform initiated in {mode} mode")

    if mode == 'train':
        logger.info("Starting data preprocessing")
        processed_data = preprocess_data()
        logger.info("Data preprocessing completed")

        logger.info("Starting model training")
        trained_model = train_model(processed_data)
        logger.info("Model training completed")

        # Save the trained model
        # implement model saving logic here

    elif mode == 'inference':
        # Load the trained model
        # implement model loading logic here

        logger.info("Starting inference")
        # implement inference logic here
        logger.info("Inference completed")

    else:
        logger.error(f"Unknown mode: {mode}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Super Platform")
    parser.add_argument('--mode', type=str, choices=['train', 'inference'], required=True,
                        help='Mode of operation: train or inference')
    args = parser.parse_args()
    main(args.mode)

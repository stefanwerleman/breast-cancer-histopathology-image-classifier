"""
Main script to begin training the model.
"""

import argparse
import sys
import logging
from pathlib import Path

from src import paths
from src.log.log import initialize_logger

logger = logging.getLogger(__file__)

TRAIN_LOG_PATH = paths.LOG_DIR / "train.log"


def main(args: argparse.Namespace) -> int:
    
    logger.info("Start of training.")
    logger.info("Arguments: %s", args)
    
    exit_code: int = 0
    
    try:
        pass
    except Exception as ex:
        logger.exception(ex)
        exit_code = 1
    finally:
        logger.info("End of training.")
    
    return exit_code


if __name__ == "__main__":
    initialize_logger(log_path=TRAIN_LOG_PATH)
    
    parser = argparse.ArgumentParser(prog="Breast Cancer Training Script",
                                     description="Main script to train the classificiation model.")
    
    parser.add_argument("-e", "--epoch", required=True, type=int,
                        help="Number of epochs for training.")
    
    args, _ = parser.parse_known_args()

    sys.exit(main(args=args))

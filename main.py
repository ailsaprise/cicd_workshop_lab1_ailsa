# standard
import datetime as dt
import logging
from pathlib import Path

from dotenv import load_dotenv

# custom
from src.analysis import run_analysis
from src.config_handler import write_config
from src.dhsc_logger import configure_dhsc_logger

logger = logging.getLogger(__name__)


def main():
    config = {}
    config["input_dir"] = Path("input")
    config["output_dir"] = Path("output")
    config["timestamp"] = dt.datetime.now().strftime("%Y%m%d")

    # load in environment values
    load_dotenv()

    # set logging to both file and console with nicer defaults
    configure_dhsc_logger(filepath=config["output_dir"] / "log.txt")

    logger.info("--------- Start pipeline ---------")

    # call main analysis code
    run_analysis(config)

    # save the timestamped config so settings are recorded
    config_dump_path = config["output_dir"] / f"{config['timestamp']}_config.yaml"
    logger.info("Saving config to %s", config_dump_path)
    write_config(config, config_dump_path)

    logger.info("--------- End pipeline ---------")


if __name__ == "__main__":
    main()

import os
import time

from ception.config.interface import Config


def setup_experiment(cfg: Config) -> None:
    """
    Setup the experiment with the given configuration

    Args:
        cfg (Config): Configuration dictionary
    """

    # Create the experiment directory with the timestamp
    save_dir = cfg.experiment.save_dir
    experiment_name = cfg.experiment.name
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    cfg.experiment.save_dir = f"{save_dir}/{experiment_name}_{timestamp}/"
    os.makedirs(cfg.experiment.save_dir)
    print(f"CEPTION: Experiment directory: {cfg.experiment.save_dir} created.")

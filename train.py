import os
import torch
import hydra
from utils.util import pp
import lightning as L
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_name='config', config_path='configs', version_base=None)
def main(cfg: DictConfig) -> None:
    pp('Params', str(cfg))



if __name__ == "__main__":
    main()
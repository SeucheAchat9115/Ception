from dataclasses import dataclass

@dataclass
class DefaultConfig():
    experiment.task: str
    data.batch_size: int

    @classmethod
    def from_dict():
        pass


def load_default_config() -> Dict:
    cfg = DefaultConfig()
    return cfg

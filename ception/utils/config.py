from dataclasses import dataclass

@dataclass
class ExperimentConfig():
    experiment_name: str
    experiment_description: str

    @classmethod
    def from_dict(self, experiment_config: dict):
        return ExperimentConfig(
            experiment_name=experiment_config['experiment_name'],
            experiment_description=experiment_config['experiment_description']
        )

@dataclass
class DataConfig():
    train_data_path: str
    test_data_path: str

    @classmethod
    def from_dict(self, data_config: dict):
        return DataConfig(
            train_data_path=data_config['train_data_path'],
            test_data_path=data_config['test_data_path']
        )

@dataclass
class ModelConfig():
    model_name: str
    num_classes: int
    input_size: int
    pretrained: bool

    @classmethod
    def from_dict(self, model_config: dict):
        return ModelConfig(
            model_name=model_config['model_name'],
            num_classes=model_config['num_classes'],
            input_size=model_config['input_size'],
            pretrained=model_config['pretrained']
        )

@dataclass
class TrainingConfig():
    batch_size: int
    num_epochs: int
    learning_rate: float

    @classmethod
    def from_dict(self, training_config: dict):
        return TrainingConfig(
            batch_size=training_config['batch_size'],
            num_epochs=training_config['num_epochs'],
            learning_rate=training_config['learning_rate']
        )

@dataclass
class EvaluationConfig():
    metric_name: str

    @classmethod
    def from_dict(self, evaluation_config: dict):
        return EvaluationConfig(
            metric_name=evaluation_config['metric_name']
        )

@dataclass
class Config():
    experiment: ExperimentConfig
    data: DataConfig
    model: ModelConfig
    training: TrainingConfig
    evaluation: EvaluationConfig

    @classmethod
    def from_dict(self, config: dict):
        return Config(
            experiment=ExperimentConfig.from_dict(config['experiment']),
            data=DataConfig.from_dict(config['data']),
            model=ModelConfig.from_dict(config['model']),
            training=TrainingConfig.from_dict(config['training']),
            evaluation=EvaluationConfig.from_dict(config['evaluation'])
        )


def load_default_config() -> dict:
    cfg = Config()
    return cfg

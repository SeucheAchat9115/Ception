from ception.config.base import BaseConfig


class EvaluationConfig(BaseConfig):
    """Configuration class for the evaluation settings"""

    metric_name: str | None

    def __init__(
        self,
        metric_name=None,
    ) -> None:
        """
        Initialize the configuration for the evaluation settings

        Args:
            metric_name (str): Name of the evaluation metric
        """
        super().__init__(metric_name=metric_name)

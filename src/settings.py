from pydantic_settings import BaseSettings


class ExperimentSettings(BaseSettings):
    TOTAL_EPOCHS: int = 100


settings = ExperimentSettings()

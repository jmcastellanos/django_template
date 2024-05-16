import enum


@enum.unique
class Environment(enum.Enum):
    local = "local"
    development = "development"
    production = "production"

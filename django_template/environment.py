import enum


@enum.unique
class Environment(enum.Enum):
    local = "local"
    development = "development"
    production = "production"

    # Using the next line the enum will fail for the unique decorator
    # test = "local"

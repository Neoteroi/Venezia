from roconfiguration import Configuration


def load_configuration() -> Configuration:
    configuration = Configuration()

    configuration.add_yaml_file("settings.yaml")
    configuration.add_environmental_variables("APPSETTING_", strip_prefix=True)

    return configuration

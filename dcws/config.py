from dynaconf import Dynaconf

# Configures Dynaconf in a global variable.
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['dcws/resources/settings.yaml'],
    environments=True,
    load_dotenv=True,
)

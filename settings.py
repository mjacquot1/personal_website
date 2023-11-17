import os
from decouple import Config, RepositoryEnv

# Set config to this for python-decouple.
# This will pull the right .env file based on docker-compose deployment
def return_config_env_variables():
    prod_env_path = '.env.prod'
    dev_env_path = '.env.dev'

    if os.path.isfile(prod_env_path):
        used_env_path = prod_env_path
    else:
        used_env_path = dev_env_path

    # Load in the right .env file, depending on the system
    config = Config(RepositoryEnv(used_env_path))

    return config
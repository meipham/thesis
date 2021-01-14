import yaml

"""
#### FOR USAGE: 

import yaml_config

config = yaml_config.Configurate()
train_path = config["Datapath"]["Train"]
test_path = config["Datapath"]["Test"]

"""

CONFIG_FILE = "config.yaml"

def Configurate():
    config = None
    with open("config.yaml", 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config
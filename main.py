import yaml


if __name__ == "__main__":
    config = yaml.safe_load(open("config.yml"))
    TRAIN_DATA_PATH = config["datapath"]["train"]
    TEST_DATA_PATH = config["datapath"]["test"]



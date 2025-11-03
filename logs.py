import logging
import logging.config
import yaml

def setup_logging(config_path='logging.yaml'):
    try:
        with open(config_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        
        # This allows using 'ext://sys.stdout' or 'ext://sys.stderr' in the YAML file
        logging.config.dictConfig(config)
    except FileNotFoundError:
        print(f"Error: Config file '{config_path}' not found.")
        # Fallback to basic configuration if the file is missing
        logging.basicConfig(level=logging.INFO)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        logging.basicConfig(level=logging.INFO)

setup_logging()
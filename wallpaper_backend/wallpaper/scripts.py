import json

def load_config(config_path):
    ''' Load config.json file '''
    with open(config_path, 'r', encoding="utf-8") as j:
        config = json.load(j)
        return config
    
def print_json(i):
    ''' Print a list/dict in json '''
    print(json.dumps(i, indent=4, ensure_ascii=False))
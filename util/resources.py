from json import load

with open ("config.json", "r") as config_file:
    config_data = load(config_file)
    TOKEN = config_data["token"]
    api_key = config_data["api_key"]

with open ("items.json", "r") as items_file:
    items_data = load(items_file)
    ITEMS = items_data["items"]

with open ("blocks.json", "r") as blocks_file:
    blocks_data = load(blocks_file)
    BLOCKS = blocks_data["blocks"]

with open ("data.json", "r") as data_file:
    data = load(data_file)
    users = data["users"]
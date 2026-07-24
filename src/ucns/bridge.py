# Existing + minimal additions for new schema
# Append only
class BridgeRecord:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Existing bridge code unchanged except new schema support

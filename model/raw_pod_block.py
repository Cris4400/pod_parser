class RawPodBlock:
    
    def __init__(self, id, name, raw_data, children_blocks):
        self.id = id
        self.name = name
        self.raw_data = raw_data
        self.children_blocks = children_blocks
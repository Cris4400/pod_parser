from utils.blocks import *

export_options = {}
lights = []

def pod_processor(raw_pod_blocks):
    for raw_pod_block in raw_pod_blocks:
        print(raw_pod_block.name)
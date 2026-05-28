import sys
from reader.pod_reader import pod_reader
from processor.pod_processor import pod_processor

def main():
    if len(sys.argv) < 2:
        return

    file_name = sys.argv[1]
    pod_block_tree = pod_reader(file_name)
    pod_processor(pod_block_tree)

if __name__ == "__main__":
    main()
import os
from collections import Counter

def check_instances(label_dir="labels", max_threshold=32):
    """
    Checks how many objects (instances) each YOLO label file contains.

    Args:
        label_dir (str): Path to the directory containing YOLO label `.txt` files.
        max_threshold (int): Max expected number of objects per image.
    """
    print(f"Checking YOLO labels in: {os.path.abspath(label_dir)}\n")
    over_limit_files = []
    instance_distribution = Counter()

    for label_file in os.listdir(label_dir):
        if label_file.endswith(".txt"):
            label_path = os.path.join(label_dir, label_file)
            with open(label_path, "r") as f:
                lines = f.readlines()
                num_instances = len(lines)
                instance_distribution[num_instances] += 1
                if num_instances > max_threshold:
                    over_limit_files.append((label_file, num_instances))

    print(f" Found {len(over_limit_files)} files with more than {max_threshold} instances:\n")
    for file, count in over_limit_files:
        print(f"  {file}: {count} instances")

    print("\n Instance distribution summary:")
    for count, freq in sorted(instance_distribution.items()):
        print(f"  {count} instances: {freq} file(s)")

if __name__ == "__main__":
    check_instances(label_dir="C:/Users/moham/OneDrive/Desktop/data/labels/train", max_threshold=32)

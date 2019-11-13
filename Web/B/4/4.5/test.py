import time
from tqdm import tqdm
import yaml


for i in tqdm(range(10000)):
    time.sleep(0.001)

fp = open("example.yaml")
example = yaml.load(fp)
fp.close()
print(example)
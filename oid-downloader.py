from pymongo import MongoClient
from urllib.request import urlretrieve
from urllib.parse import urlparse
from tqdm import tqdm
import os


class TqdmProgress(tqdm):
    def report_hook(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


client = MongoClient()
db = client.oid
train_images = db.train_images
val_images = db.val_images
test_images = db.test_images

os.chdir('./train/')
for img in train_images.find({'downloaded': False}):
    if not img['downloaded']:
        url = urlparse(img['url'])
        filename = os.path.basename(url.path)
        with TqdmProgress(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=filename) as t:
            urlretrieve(img['url'], filename, t.report_hook)
        print(f'File downloaded is {filename}')
        img['downloaded'] = True
        train_images.update_one({'_id': img['_id']}, {
                                "$set": img}, upsert=False)
print('**************************** Done downloading train images!')

os.chdir('../validation/')
for img in val_images.find({'downloaded': False}):
    if not img['downloaded']:
        url = urlparse(img['url'])
        filename = os.path.basename(url.path)
        with TqdmProgress(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=filename) as t:
            urlretrieve(img['url'], filename, t.report_hook)
        img['downloaded'] = True
        train_images.update_one({'_id': img['_id']}, {
                                "$set": img}, upsert=False)
print('**************************** Done downloading validation images!')

os.chdir('../test/')
for img in test_images.find({'downloaded': False}):
    if not img['downloaded']:
        url = urlparse(img['url'])
        filename = os.path.basename(url.path)
        with TqdmProgress(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=filename) as t:
            urlretrieve(img['url'], filename, t.report_hook)
        img['downloaded'] = True
        train_images.update_one({'_id': img['_id']}, {
                                "$set": img}, upsert=False)
print('**************************** Done downloading test images!')

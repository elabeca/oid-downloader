from pymongo import MongoClient
from urllib.request import urlretrieve
from urllib.parse import urlparse
from tqdm import tqdm
from multiprocessing import Pool
import os


class TqdmProgress(tqdm):
    def report_hook(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


client = MongoClient()
db = client.oid


def download_and_update(img_tuple):
    (img, img_collection) = img_tuple
    url = urlparse(img['url'])
    filename = os.path.basename(url.path)
    # with TqdmProgress(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=filename) as t:
    #    urlretrieve(img['url'], filename, t.report_hook)
    urlretrieve(img['url'], filename)
    img['downloaded'] = True
    img_collection.update_one({'_id': img['_id']},
                              {"$set": img},
                              upsert=False)
    print('%s...' % filename)


def download_img_set(path, img_collection):
    os.chdir(path)
    for img in img_collection.find({'downloaded': False}):
        if not img['downloaded']:
            download_and_update((img, img_collection))
    print('**************************** Done downloading %s image set' % path)


download_img_set('./train/', db.train_images)
download_img_set('../validation/', db.val_images)
download_img_set('../test/', db.test_images)

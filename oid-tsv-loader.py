import csv
from pymongo import MongoClient

client = MongoClient()
db = client.oid
train_images = db.train_images
val_images = db.val_images
test_images = db.test_images

for num in range(0, 9):
    with open('open-images-dataset-train' + str(num) + '.tsv', 'rt') as tsvin_train:
        tsvreader = csv.reader(tsvin_train, delimiter='\t')
        next(tsvreader)
        for row in tsvreader:
            train_images.insert_one(
                {'url': row[0], 'content-length': row[1], 'downloaded': False})

with open('open-images-dataset-validation.tsv', 'rt') as tsvin_val:
    tsvreader = csv.reader(tsvin_val, delimiter='\t')
    next(tsvreader)
    for row in tsvreader:
        val_images.insert_one(
            {'url': row[0], 'content-length': row[1], 'downloaded': False})

with open('open-images-dataset-test.tsv', 'rt') as tsvin_test:
    tsvreader = csv.reader(tsvin_test, delimiter='\t')
    next(tsvreader)
    for row in tsvreader:
        test_images.insert_one(
            {'url': row[0], 'content-length': row[1], 'downloaded': False})

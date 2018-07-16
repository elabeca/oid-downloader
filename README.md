# Open Image Dataset V4 downloader

This downloader downloads the ~9 million images part of the Open Image Dataset V4. Mongo is used to keep state on the overall download progress and for error recovery. Should you need to stop, pause and restart the download, only images not downloaded will be downloaded.

## Get the .tsv files from these locations:

The tsv files for the train set, in 10 partitions:  
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train0.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train1.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train2.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train3.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train4.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train5.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train6.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train7.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train8.tsv<br>
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-train9.tsv<br>

The tsv file for the validation set:  
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-validation.tsv

The tsv file for the test set:  
https://storage.googleapis.com/cvdf-datasets/oid/open-images-dataset-test.tsv

## First load up the database

```
python oid-tsv-loader.py
```

## Second download all images (~18 TB)

```
python oid-downloader.py
```
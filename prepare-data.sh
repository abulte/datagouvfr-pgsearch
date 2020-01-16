# all datasets
# csvcut -z 1310720 -c id,title,description,organization -d ';' data/export-dataset-20200111-064915.csv > data/export.csv

# only france in spatial.zones
csvgrep -z 1310720 -c spatial.zones -r 'France' -d ';' data/export-dataset-20200111-064915.csv|csvcut -z 1310720 -c id,title,url,description,organization>data/export.csv

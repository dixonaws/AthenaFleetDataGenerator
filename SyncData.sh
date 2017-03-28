#!/bin/bash

# generate gzip files
for i in $(ls -lah data/csv |awk '{print $9}'); do gzip --fast --keep data/csv/$i; done
for i in $(ls -lah data/csv |grep gz |awk '{print $9}'); do mv data/csv/$i data/gzip/; done

aws --profile dixonaws@amazon.com s3 sync data/csv/ s3://fleetbriefing-data/data/csv --acl "public-read" --delete

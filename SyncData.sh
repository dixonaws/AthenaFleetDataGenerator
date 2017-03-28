#!/bin/bash

aws --profile dixonaws@amazon.com s3 sync data/csv/ s3://fleetbriefing-data/data/ --acl "public-read" --delete

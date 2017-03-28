#!/bin/bash

aws --profile dixonaws@amazon.com s3 sync ../fleetbriefing-data/data s3://fleetbriefing-data/data/ --acl "public-read" --delete

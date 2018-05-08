#!/bin/bash

function check_cmdline_arguments {
	# check for a command line argument
	if [ -z "$1" ]; then
		echo "FATAL: You must specify an AWS profile as the first argument to this script. The AWS profile must exist in the credentials file, commonly found at ~/.aws/credentials."
		exit
	fi

	if [ -z "$2" ]; then
		echo "FATAL: You must specify an S3 bucket to publish the sample data files, e.g., s3://fleetbriefing-data."
		exit
	fi


}

# generate gzip files, quick and dirty
echo "Generating list of CSV files, gzipping, moving... "
for i in $(ls -lah data/csv/*.csv |awk '{print $9}'); do

    gzip --fast --keep -f $i
    echo -n "."
done

echo "Moving gzip files...
for i in $(ls -lah data/csv |grep gz |awk '{print $9}'); do
    print $i
    mv data/csv/$i data/gzip/
done

echo "Uploading to S3..."
#aws --profile dixonaws@amazon.com s3 sync data/gzip s3://fleetbriefing-data/gzip --acl "public-read" --delete




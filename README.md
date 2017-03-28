<h1>AthenaFleetDataGenerator</h1>
A Python program to generate sample rental data (GenerateData.py), and a program to 
upload the sample data to an S3 bucket (SyncData.sh).
<p>
GenerateData.py generates 10,000 fake car rental invoice records with the following fields:
<ul>
<li>rental_date string</li>
<li>dropoff_date string</li>
<li>renterid string</li>
<li>rental_agreement string</li>
<li>rental_invoice string</li>
<li>vehicle_tag string</li>
<li>vehicle_state string</li>
<li>vehicle_class string</li>
<li>distance_driven int</li>
<li>pickup_location string</li>
<li>rental_duration int</li>
<li>charges float</li>
</ul>
<p>
Run the data generation script with the following 
command to generate 10,000 records in ./data/csv/invoice<i>x</i>.csv where
<i>x</i> is the invoice number (tested with Python 
2.7.10 on macOS 10.12.4). You may need to create the data/csv
directories yourself. macOS with an SSD takes less than 
60 seconds to generate 10,000 sample invoice records.<p>
<code>python GenerateData.py 10000</code>
<p>&nbsp;<p>

This repo also incudes a program to sync the sample
invoices to s3. SyncData.sh uses the AWS CLI to sync
the contents of your local data/csv to 
s3://fleetbriefing-data/data. Usage is simple:<p>
<code>./SyncData.sh</code>
<p>&nbsp;<p>

SyncData.sh will take a little more time to run. First, it deletes
the existing invoices from s3://fleetbriefing-data/data,
then uploads each new invoice to S3.
<code>
real	2m43.106s<br>
user	1m14.285s<br>
sys	0m19.118s</code>
<p>&nbsp;<p>


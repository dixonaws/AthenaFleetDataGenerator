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


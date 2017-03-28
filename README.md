<h1>AthenaFleetDataGenerator</h1>
Query rental data in S3 via SQL. Provide your accessKey and secretKey as arguments when running 
AthenaTest (get at https://github.com/dixonaws/AthenaJDBCTest), as follows:<p>
<code>java -classpath ... AthenaTest (accessKey) (secretKey)</code>
<p>
This repo includes a Python program to generate sample rental data (GenerateData.py), and a program to 
upload the sample data to an S3 bucket (SyncData.sh).

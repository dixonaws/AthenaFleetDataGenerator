#!/usr/bin/python

import time
import random
import sys

# generate some fake invoice data
# each CSV should contain one invoice
# filenames do not matter
# structure of the files must be as follows:

#  rental_date string,
#  dropoff_date string,
#  renterid string,
#  rental_agreement string,
#  rental_invoice string,
#  vehicle_tag string,
#  vehicle_state string,
#  vehicle_class string,
#  distance_driven int,
#  pickup_location string,
#  rental_duration int,
#  charges float

# example:
# 03-10-2017,01-12-2017,001,334899532,30329177623,BPGT63,FL,SRAR,375,JAX,3,167.43


def main():
    print "FleetDataGenerator v1.1"
    print "Generate simulated rental car invoices in /tmp/data/csv"
    print '--------------------------------------------------'
    print 'Preparing to generate ' + str(sys.argv[1]) + ' invoice(s)...'

    # the number of records to generate
    intRecordsToGenerate=int(sys.argv[1])

    intPoint = intRecordsToGenerate / 100
    intIncrement = intRecordsToGenerate / 20

    # write intRecordsToGenerate individual records
    print 'Writing records to ./data/csv...'
    for i in range(1, intRecordsToGenerate):
        # form the random data with the following fields:
        # rental date (random date between 2010 and 2016)
        # dropoff date (default all to 3-10-2017)
        # renter id
        # rental agreement number
        # rental invoice number
        # vehicle tag (license plate number)
        # rental state
        # vehicle class (default to SRAR)
        # distance driven (up to 900 miles)
        # airport code
        # rental duration
        # pickup location

        var_rental_date = str(random.randint(01, 12)) + "-" + str(random.randint(01, 30)) + "-" + str(
            random.randint(2010, 2016))
        var_dropoff_date = "03-10-2017"
        var_renterid = str(random.randint(10000, 99999))            # random renterid
        var_rental_agreement = str(random.randint(10000, 99999))    # random string for rental agreement
        var_rental_invoice = str(random.randint(10000, 99999))      # random string for invoice

        # generate a random vehicle tag
        tag=random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"], 6)

        var_vehicle_tag = str(tag[0]) + str(tag[1]) + str(tag[2]) + str(tag[3]) + str(tag[4]) + str(tag[5])
        vehicle_state=(["FL", "OH", "MI", "MN", "GA", "VA"])
        var_vehicle_state = (random.sample(vehicle_state, 1))[0]
        vehicle_class=(["SRAR", "SUV", "SEDAN", "TRUCK", "COUPE", "SPECIAL", "LUXURY"])
        var_vehicle_class = (random.sample(vehicle_class, 1))[0]
        var_distance_driven = str(random.randint(0, 900))

        # choose from a list of random airport codes
        airport_code=(["ATL", "LAX", "JAX", "RDW", "RTP", "DTW", "MDW", "GRR", "ORD", "DFW", "DEN", "JFK", "SFO", "CLT", "LAS", "PHX", "IAH", "IAD", "DCA", "EWR", "MCO", "SEA", "MSP", "PHL", "BOS", "LGA", "BWI", "SAN", "TPA", "CLE", "PDX"])
        var_pickup_location = (random.sample(airport_code, 1))[0]
        var_rental_duration = str(random.randint(1, 7))
        var_charges = str(round((random.uniform(50.00, 799.99)),2))

        # form the record from our var_* variables above
        var_record = str(
            var_rental_date + "," + var_dropoff_date + "," + var_renterid + "," + var_rental_agreement + "," + var_rental_invoice + "," + var_vehicle_tag + "," + var_vehicle_state + "," + var_vehicle_class + "," + str(
                var_distance_driven) + "," + var_pickup_location + "," + str(var_rental_duration) + "," + str(
                var_charges))

        var_filename="/tmp/data/csv/invoice" + str(i) + ".csv"

        f=open(var_filename,"w")
        f.write(var_record)
        f.close()

        # print a progress bar
        if (i % (5 * intPoint) == 0):
            sys.stdout.write("\r[" + "=" * (i / intIncrement) + " " * ((intRecordsToGenerate - i) / intIncrement) + "] " + str(i / intPoint) + "%")
            sys.stdout.flush()


    # for i

    # print progress complete
    sys.stdout.write("\r[====================] 100%")
    sys.stdout.flush()
    print ' Done.'

main()

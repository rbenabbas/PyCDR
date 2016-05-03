# PyCDR
Python script to search and report on CUCM CDR CSV files.

Purpose: Searches the Cisco Call Manager (CUCM) Call Detail Records (CDR) csv file for an extension, and saves the Date/Time, call duration, calling number, and called number to a new csv file.

If you manage Cisco CUCM and get requests for Call Detail Records, you know how frustrating it can be to import the csv file to Excel,
delete out all but 4 of over 60 columns, search thousands of rows of data to narrow down to the one extension, and convert epoch time to something a human understands.

The first time I had to fulfill a request for call records, it took me most of the day to figure it out. Before I wrote this script it took me an average of a couple hours per request (including multitasking). That's two hours too long. With this script and Python installed, you can have a csv file to import into Excel in seconds.

Directions: Download the CDR from https://<cucmserver>/ccmservice/, select the date range, and DO NOT CHECK 'CMR RECORDS'! Run this script and specify three command line arguments:

1. The path and name of the input csv file
2. The path and name of the output csv file
3. The extension to search for

Example: PyCDR.py "/path/to/cdr.txt" "/path/to/output.txt" 4357

Import the output csv into Excel and format as you please.

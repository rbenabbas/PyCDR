# PyCDR
Python script to search and report on CUCM CDR CSV files.

 +Purpose: Searches the Cisco Call Manager (CUCM) Call Detail Records (CDR) csv file for an extension,
 +and saves the Date/Time, call duration, calling number, and called number to a new csv file.
 +
 +Directions: Download the CDR from https://<cucmserver>/ccmservice/, select the date range,
 +and DO NOT CHECK 'CMR RECORDS'!
 +Run this script and specify three command line arguments:
 +1. The path and name of the input csv file
 +2. The path and name of the output csv file
 +3. The extension to search for
 +
 +Example: PyCDR.py "/path/to/cdr.txt" "/path/to/output.txt" 4357
 +"""

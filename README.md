# UmbrellaBulkDeleteComputer
API workflow to delete set number of roaming computers provided through a CSV File. This script has been tested with Umbrella v1 Management APIs and requires Python 3 running on the end machine. 

Umbrella Management API does not provide BULK option by default and also has a rate limit in place as following.  

- 5 requests per second
- 14 requests per minute
- 350 requests per 30 minutes

When a rate limit is reached, the API returns the Too Many Requests error with the HTTP response code 429, for the remainder of the time-period. 

The script has been written to not hit this rate limit as we are using a timer of 6 seconds per API requests. 

This workflow requires CSV File as an input - Sample CSV file is provided in this repository itself. Fill the CSV file with required input and run any of the script present in respective folder. 




Once the required details are provided, the output is seen as below(This is just an example):



This script also provides you with a log file in the same folder with success and failure responses.
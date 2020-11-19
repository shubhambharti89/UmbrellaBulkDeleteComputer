import json
import requests
from requests.auth import HTTPBasicAuth
import time
import csv
from ratelimiter import RateLimiter

def limited(until):
    duration = int(round(until - time.time()))
    print('Rate limited, sleeping for {:d} seconds'.format(duration))

rate_limiter = RateLimiter(max_calls=350, period=1800, callback=limited)

# Function to convert a CSV to JSON
def csvtojson(csvFilePath):

    computername = []
    
    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.reader(csvf)

        for rows in csvReader:
            computername.append(rows[0])

    return computername

print("Please make sure that the device name present in the sheet is validated. \nIt should not have any random alphabets present as name because the API filters the name with \" contains \" rather than \" equals \"." )
csvFilePath = input("Please enter the CSV Filepath (For eg. : path/to/file/objects.csv) :")

org_id = <"ORGID">
mgmt_api_key = <"MANAGEMENT API KEY">

mgmt_api_secret = input("Please provide the Management API Secret : ")

header = {'content-type': 'application/json'}

names = csvtojson(csvFilePath)
count = 0
logfile = "log_"+ str(time.perf_counter_ns()) + ".txt"
log = open(logfile,"w+")

for name in names:
    with rate_limiter:
        count+=1
        delete_computer_url = 'https://management.api.umbrella.com/v1/organizations/'+org_id+'/roamingcomputers/'+name

        response = requests.request("DELETE", delete_computer_url, headers=header, auth=HTTPBasicAuth(mgmt_api_key, mgmt_api_secret))

        if response.status_code == 204 or 200 :
            print(str(count) + " : " +name + " : Computer has been successfully deleted")
            log.write(name + " : Computer has been successfully deleted \n")
        
        else :
            print(str(count)+ " : " + name + " : Issue found with this computer. Please check the logs for more details")
            log.write(name + " : " +response.text + "\n")  
        


log.write("************************************************************\n")
log.write("Task Completed : Total number of devices worked upon : "+ str(count) + ".\n")
log.write("************************************************************")


print ("\n************************************************************")
print(" Task Completed : Total number of devices worked upon : "+ str(count) + ". Please look at the logs for any issues.")
print ("************************************************************")

log.close

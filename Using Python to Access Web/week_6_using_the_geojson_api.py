# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
# API End Points

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

# http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

# Test Data / Sample Execution

# You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJ9e_QQm0sDogRhUPatldEFxw".

# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2291 characters
# Place id ChIJ9e_QQm0sDogRhUPatldEFxw
# Turn In

# Please run your program to find the place_id for this location:

# Irkutsk State University
# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJweC ..."
# Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"
data_address = "Irkutsk State University"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Setting the GET parameters on the URL
parms = dict()
parms['key'] = api_key
parms['address'] = data_address
paramsurl = urllib.parse.urlencode(parms)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl + paramsurl
print("DATA URL: ", queryurl)

#Obtaining and reading the data
uh = urllib.request.urlopen(queryurl, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
#Parsing the data and looking for the field we want.
#That field is inside the "Results" array, in its first item (if our address is
#correct we can assume that the result would be the correct one) and on its
#"place_id" field

try:
   	js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

place_id = js["results"][0]["place_id"]
print("PLACE ID: ", place_id)

#Answering Project 1 questions

from ProjectDocumentation import username, password, cluster, uri, client, db, collection
#import regex in this file
import re
import ProjectFunctions



#1. How many records are in the collection?

document_count = collection.count_documents({})
print(f"There are {document_count} inspections in this collection.")

#2. How many inspections were in 2015, and how many were in 2016?

year = "2015"
year_regex = re.compile(year)

document_count = collection.count_documents({"date": year_regex})
print(f"There are {document_count} inspections in the year {year}.")

year = "2016"
year_regex = re.compile(year)

document_count = collection.count_documents({"date": year_regex})
print(f"There are {document_count} inspections in the year {year}.")

#3. Prompt User to check if violation was issued to a business
#    Will use "ATLIXCO DELI GROCERY INC." as a test business name,
#    should say no violations

ProjectFunctions.check_business_violation()

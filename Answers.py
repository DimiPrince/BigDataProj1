#Answering Project 1 questions
from ProjectDocumentation import username, password, cluster, uri, client, db, collection
import re #import regex in this file
import ProjectFunctions
#import random  update: dont need this library because of mongoDB aggregate function


#1. How many records are in the collection?
print('Question 1.')

document_count = collection.count_documents({})
print(f"There are {document_count} inspections in this collection.")

#2. How many inspections were in 2015, and how many were in 2016?
print('Question 2.')

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
print('Question 3.')

ProjectFunctions.check_business_violation()

#4. How many business violations in the Bronx and New York.
    #checking for bronx first
print('Question 4.')

countBRONX = collection.count_documents({"address.city": "BRONX", "result": "Violation Issued"})
print(f"There are {countBRONX} businesses in the Bronx where a violation was issued.")

    #checking for Brooklyn
countBROOKLYN = collection.count_documents({"address.city": "BROOKLYN", "result": "Violation Issued"})
print(f"There are {countBROOKLYN} businesses in Brooklyn where a violation was issued.")

print(f"In total, there are {countBRONX + countBROOKLYN} businesses with violations in Bronx and Brooklyn combined.")

    #displaying difference
print(f"The difference is {countBROOKLYN - countBRONX} , with Brooklyn having more businesses with violations than the Bronx.")
  
    #printing first 5 locations in Brooklyn 

documentsBROOKLYN = collection.find({"address.city": "BROOKLYN"}).limit(5)

print("\nThe first 5 locations in Brooklyn are the following : \n")

for document in documentsBROOKLYN:
    print(f"Business Name: {document['business_name']}")
    print(f"Address: {document['address']}")
    print("\n")

    #printing first 5 locations in the Bronx

print("The first 5 locations in the Bronx are the following : \n")

documentsBRONX = collection.find({"address.city": "BRONX"}).limit(5)
for document in documentsBRONX:
    print(f"Business Name: {document['business_name']}")
    print(f"Address: {document['address']}")
    print("\n")

'''5.   Prompt the user to input a zip-code. The output will give you the total
number of businesses within that zip-code. Output should also randomly
print out any five businesses’ name obtained from your list '''
print('Question 5.')


zipcode = int(input("Enter a zip code:"))  # Convert input to integer

documentZIP = collection.count_documents({"address.zip": zipcode})

if documentZIP != 0:
    print(f"There are {documentZIP} businesses in the zip code {zipcode}.")
    print("Here is a random list of businesses in this zip code:")
    # Choosing random documents, dont need random library because of mongoDB aggregate function
    documentsRANDOM = collection.aggregate([
        {"$match": {"address.zip": zipcode}}, #creating zip code as filter
        {"$sample": {"size": min(5, documentZIP)}} #for slecting how many document fit condition
    ])

    for doc in documentsRANDOM:
        print(doc['business_name'])
else:
    print("No businesses found in that zip code.")


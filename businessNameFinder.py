#BigData project 1
#/usr/local/bin/python3 -m pip install pymongo
#interpreter bottom right in VS code, some libraries can be installed in one interpreter but not another

#can test if you are being connected to the database by using the following code

from ProjectDocumentation import username, password, cluster, uri, client, db, collection

#use "ATLIXCO DELI GROCERY INC." as a test business name
def BusinessFinder():
    business_name = input("Enter a business name: ")
    document = collection.find_one({"business_name": business_name})
    if document is not None:
        print(f"Business found: {document}")
    else:
        print("No business found with that name.")

BusinessFinder()

#should prompt user then print business if document exist

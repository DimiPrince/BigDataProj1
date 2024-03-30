#functions needed for the project

from ProjectDocumentation import username, password, cluster, uri, client, db, collection

def check_business_violation():
    business_name = input("Enter a business name: ")
    document = collection.find_one({"business_name": business_name})
    if document is not None:
        if document['result'] == "No Violation Issued":
            print(f"The business '{business_name}' has no violations.")
        else:
            print(f"The business '{business_name}' has a violation.")
    else:
        print("Business Not found.")

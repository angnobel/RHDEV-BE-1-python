# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call
# 2. Determine the memberships status of all applicants
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

bannedVisitors = ["Amy", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}




def OutputFormat():
    output={
        "successfulApplicants": [],
        "bannedApplicants": [],
        "totalCost": 0,
        "tickets": [],
    }
    return output

def Banned(app, output):
    if app in bannedVisitors:
        output[Banned].append(app)
        return True
    return False

def Ticket(app, output):
    ticket={
        "name": app,
        "membershipStatus": memberStatus.get(app, False),
        "price": 3.5 if memberStatus.get(app, False) else 5
    }
    output['tickets'].append(ticket)
    output['successfulApplicants'].append(app)
    output['totalCost']+=ticket['price']


def processRequest(request):
    if len(request["applicants"]) == 0:
        return{"Error":"No Applicants"}
    output = OutputFormat
    for app in request["applicants"]:
        if Banned(app, output):
            continue
        Ticket(app, output)

    return output



    try:
        if len(request["applicants"])==0:
            raise Exception({"Error": "No Applicants"})
        output = OutputFormat()
        for app in request["applicants"]:
            if Banned(app, output):
                continue
            Ticket(app, output)
        return output
    except Exception as e:
        return "Oops something went wrong"
    


print(processRequest(request))
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

def initOutputFormat():
    output={
        "successfulApplicants":[],
        "bannedApplicants":[],
        "totalCost":0,
        "tickets":[],
    }
    return output

def banFilter(app, output):
    if app in bannedVisitors:
        output['bannedApplicants'].append(app)
        return True
    return False

def ticketProcessing(app, output):
    ticket={
        "name": app,
        "membershipStatus": memberStatus.get(app, False),
        "price": 3.5 if memberStatus.get(app, False) else 5
    }
    output['tickets'].append(ticket)
    output['successfulApplicants'].append(app)
    output['totalCost']+=ticket['price']

def processRequest(request):
    if len(request["applicants"])==0:
        return {"error": "No applicants"}
    output = initOutputFormat()
    for app in request["applicants"]:
        if banFilter(app, output):
            continue
        ticketProcessing(app, output)
    
    return output


print(processRequest(request))

# {
#   successfulApplicants:
#   bannedApplicatns:
#   totalCost:
#   tickets: [
#       {
#            "name": ,
#            "membershipStatus": ,
#            "price":
#       }, ....
#   ]
#
# }


# OR

# {"error": "No applicants"}

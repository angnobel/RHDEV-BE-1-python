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


def processRequest(request):
    try:
        if 'applicants' not in request or len(request['applicants'])==0:
            raise ValueError
    except:
        return {'error':'empty'}
    v=5
    m=3.5
    banned=list(filter(lambda b:b if b in bannedVisitors else None,request['applicants']))
    allowed=list(filter(lambda s:s if s not in bannedVisitors else None,request['applicants']))
    output={'successfulApplicants':allowed,'bannedVisitors':banned,'TotalCost':0,'tickets':[]}
    for i in allowed:
        iprice=0
        if i not in memberStatus:
            memberStatus[i]=False
        if memberStatus[i]==True:
            iprice+=3.5
        else:
            iprice=5
        output['TotalCost']+=iprice
        output['tickets']+=[{'name':i,'membershipStatus':memberStatus[i],'price':iprice}]
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

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
  def ban(visitor):
    return visitor in bannedVisitors
    
  def successfulapp(visitor):
    return visitor not in allresults["bannedApplicants"]
    
  def checkmembership(name):
    if name in memberStatus.keys():
      return memberStatus[name] #return True
      
    else:
      memberStatus[name] = False
      return memberStatus[name]

  def checkprice(name):
    if memberStatus[name] == True:
      return 3.50

    else:
      return 5
  try: 
    if len(request["applicants"]) == 0:
      raise ValueError

    allresults = {}
    allresults["bannedApplicants"] = list(filter(ban,request["applicants"]))
    allresults["successfulApplicants"] = list(filter(successfulapp, request["applicants"]))
    allresults["tickets"] = []
    total = 0 

    for name in allresults["successfulApplicants"]: #create one dictionary for each name
      eachdict = {"name": name,"membershipStatus": checkmembership(name),"price":checkprice(name)}
      total += checkprice(name)
      allresults["tickets"].append(eachdict)

    allresults["totalCost"] = total

    return allresults

  except ValueError:
    return {"error": "No applicants"}
    
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

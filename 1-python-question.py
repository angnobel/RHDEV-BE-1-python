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
        if "applicants" not in request.keys() or len(request["applicants"]) == 0:
            raise ValueError

        output = {"successfulApplicants" : [], "bannedApplicants" : [], "totalCost" : [], "tickets" : [],}

        #filter out banned applicants
        output["bannedApplicants"] = list(filter(lambda x: x in bannedVisitors, request["applicants"]))
        #filter out successful applicants
        output["successfulApplicants"] = list(filter(lambda x: x not in bannedVisitors, request["applicants"]))

        #check total cost
        totalCost = 0.0
        for i in output["successfulApplicants"]:
            if memberStatus[i] == True:
                totalCost += 3.50
            else:
                totalCost += 5
        output["totalCost"].append(totalCost)

        #checks tickets
        ticket = {"name": [],"membershipStatus":[],"price":[]}
        for i in output["successfulApplicants"]:
            ticket["name"].append(i)
            if memberStatus[i] == True:
                ticket["membershipStatus"].append("True")
                ticket["price"].append("3.50")
            else:
                ticket["membershipStatus"].append("False")
                ticket["price"].append("5.00")
        return output
            
    except:
        return {"error": "No applicants"}



print(processRequest(request))

# {
#   successfulApplicants:
#   bannedApplicants:
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

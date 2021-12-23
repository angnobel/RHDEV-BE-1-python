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
        def banned(x):
            return True if x in bannedVisitors else False

        def successful(x):
            return True if x not in bannedVisitors else False

        def membership(x):
            if memberStatus.get((request.get("applicants"))[x]) is True:
                return True
            else:
                return False

        members = []
        for i in range(len(request)):
            if membership(i) is True:
                members.append(request.get("applicants"))

        bannedApplicants = list(filter(banned, request.get("applicants")))
        successfulApplicants = list(filter(successful, request.get("applicants")))

        ticketDetails = []
        for i in range(len(request.get("applicants"))):
            if ((request.get("applicants"))[i] in members):
                current = {"name": request.get("applicants")[i],
                "membership": True,
                "price": 3.50}
                ticketDetails.append(current)

            elif ((request.get("applicants"))[i] not in members and (request.get("applicants"))[i] in successfulApplicants):
                current = {"name": request.get("applicants")[i],
                "membership": False,
                "price": 5.00}
                ticketDetails.append(current)                

        processed = {
            "successfulApplicants": successfulApplicants,
            "bannedApplicants": bannedApplicants,
            "totalCost": (((len(members)) * 3.5) + ((len)(successfulApplicants)- len(members)) * 5.0),
            "tickets": ticketDetails
        }

        return processed

    except Exception:
        print("error: No Applicants")

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
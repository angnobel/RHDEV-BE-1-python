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
        def notBanned(x):
            return True if x in bannedVisitors else False

        def banned(x):
            return True if x in bannedVisitors else False

        def membership(x):
            if memberStatus.get((request.get("applicants")[x])) is True:
                return True
            else:
                return False
        

        members = []
        for i in range(4):
            if membership(i) is True:
                members.append(request.get("applicants")[i])

        # Answering Question 1
        successfulApplicants = list(filter(notBanned, request.get("applicants")))
        bannedApplicants = list(filter(banned, request.get("applicants")))

        partOne = {
            "successfulApplicants": successfulApplicants,
            "bannedApplicants": bannedApplicants,
            "totalCost": (((len(members)) * 3.5) + ((len)(successfulApplicants)- len(members)) * 5.0)
        }

        #printing process
        for key in partOne:
            print(key, ':', partOne[key])
        print()

        print("tickers: [")
        print()

        #Creating an empty dictionary
        results = {}
        k = 0
        while (k < len(request.get("applicants"))):
            if ((request.get("applicants"))[k] in members):
                results["name"] = request.get("applicants")[k]
                results["membership"] = True
                results["price"] = 3.50
                for key in results:
                    print(key, ':', results[key])
                print()

            elif ((request.get("applicants"))[k] not in members and (request.get("applicants"))[k] in successfulApplicants):
                results["name"] = (request.get("applicants"))[k]
                results["membershipStatus"] = False
                results["price"] = 5.00
                for key in results:
                    print(key, ':', results[key])
                print()
            
            k += 1
    except Exception:
        print("{error: No applicants}")

    

    print("]")

processRequest(request)

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

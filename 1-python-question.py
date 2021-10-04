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
    except:
        return {"error": "No applicants"}

    # create result dictionary to return and process each applicant in request
    result = {"successfulApplicants": [], "bannedApplicants": [], "totalCost": 0, "tickets": []}
    for i in request["applicants"]:

        # filter through banned visitors
        if i in bannedVisitors:
            result["bannedApplicants"].append(i)

        else:
            result["successfulApplicants"].append(i)

            # temporary instance of ticket dictionary
            tmp = {"name": i}        

            # determine membership status of successful applicants
            if i in memberStatus.keys():
                tmp["membershipStatus"] = memberStatus[i]
            else:
                tmp["membershipStatus"] = False

            # calculate price of ticket and add to total cost
            if tmp["membershipStatus"]:
                tmp["price"] = 3.50
            else:
                tmp["price"] = 5.00
            result["totalCost"] += tmp["price"]

            # add current ticket instance to result dictionary
            result["tickets"].append(tmp)

    return result


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

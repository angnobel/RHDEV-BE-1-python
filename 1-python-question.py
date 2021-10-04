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

def checkMember(target, memberStatus):
    # params:
    # target(str): person to check member status of
    # memberStatus(dict): dictionary of membership statuses
    if target in memberStatus.keys():
        return memberStatus[target]
    return False

def totalPrice(tickets):
    # params:
    # tickets(list): contains list of ticket instances
    try:
        total = 0.0
        for i in tickets:
            if not isinstance(i, dict):
                raise ValueError
            if "price" not in i.keys():
                raise KeyError
            total += i["price"]

        return total

    except ValueError:
        return None
    except KeyError:
        return None

def checkPrice(isMember):
    try:
        if isMember:
            return 3.50
        return 5.00
    except:
        return None


def processRequest(request):
    try:
        if "applicants" not in request.keys() or len(request["applicants"]) == 0:
            raise ValueError

        result = {"successfulApplicants": [], "bannedApplicants": [], "tickets": []}

        # filter out banned and non-banned applicants
        result["bannedApplicants"] = list(filter(lambda x: x in bannedVisitors, request["applicants"]))
        result["successfulApplicants"] = list(filter(lambda x: x not in bannedVisitors, request["applicants"]))

        # generate tickets based on successful applicants
        for i in result["successfulApplicants"]:
            tmp = {"name": i, "membershipStatus": checkMember(i, memberStatus)}
            tmp["price"] = checkPrice(tmp["membershipStatus"])
            result["tickets"].append(tmp)

        # calculate total cost based on generated tickets
        result["totalCost"] = totalPrice(result["tickets"])
        return result

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

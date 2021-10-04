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
    # function to check banned visitors
    def check_banned(name):
        return name in bannedVisitors
    # function to check member status
    def check_member(name):
        if name not in memberStatus:
            memberStatus[name] = False
        return memberStatus[name]
    # function to give price based on membership status
    def ticketPrice(name):
        if check_member(name): 
            return 3.5
        else: 
            return 5

    applicant_list = request["applicants"]

    result = {}
    result["bannedApplicants"] = list(filter(check_banned, applicant_list))
    result["successfulApplicants"] = []
    result["totalCost"] = 0
    result["tickets"] = []

    for applicant in applicant_list:
        if applicant not in result["bannedApplicants"]:
            result["successfulApplicants"].append(applicant)
            memberStat = check_member(applicant)
            
            ticket = {
                "name": applicant,
                "membershipStatus": memberStat,
                "price": ticketPrice(applicant)
                }
            result["tickets"].append(ticket)
            result["totalCost"] += ticketPrice(applicant)

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

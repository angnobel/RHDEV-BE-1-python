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

    class EmptyApplicantsException(Exception):
        pass

    try:
        applicants = request["applicants"]
        if len(applicants) == 0:
            raise EmptyApplicantsException
    except EmptyApplicantsException:
        return {"error": "No applicants"}

    to_return = {}

    successfulApplicants = list(filter(lambda x: x if x not in bannedVisitors else None, applicants ))
    bannedApplicants = list(filter(lambda x: x if x in bannedVisitors else None, applicants ))

    #find prices
    member_tickets = []
    total_price = 0 
    for i in successfulApplicants:
        try:
            member = memberStatus[i]
        except KeyError:
            member = False
        
        if member:
            price = 3.50
        else:
            price = 5

        ticket = {
            "name" : i,
            "membershipStatus" : member,
            "price" : price,
        }

        member_tickets.append(ticket)
        total_price += price
    
    to_return["successfulApplicants"] = successfulApplicants
    to_return["bannedApplicants"] = bannedApplicants
    to_return["totalCost"] = total_price
    to_return["tickets"] = member_tickets

    return to_return


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

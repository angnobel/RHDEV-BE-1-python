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

banned_visitors = ["Amy", "Grace", "Bruce"]
member_status = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

def CheckBannedVisitors(applicant):
    for banned_visitor in banned_visitors:
        return banned_visitor == applicant

def CheckSuccessfulApplicants(applicant):
    for banned_visitor in banned_visitors:
        return banned_visitor != applicant

def Ticket(applicant):
    membership_status = (applicant in member_status) and (member_status[applicant]==True)
    if membership_status == True:
        price = 5
    else:
        price = 3.50
    ticket = {
        "name": applicant,
        "membershipStatus": membership_status,
        "price": price,
    }
    return ticket

def ProcessRequest(request):
    try:
        if request["applicants"] == []:
            raise ValueError("No applicants found!")
        successful_applicants = list(filter(CheckSuccessfulApplicants, request['applicants']))
        banned_applicants = list(filter(CheckBannedVisitors, request['applicants']))
        total_cost = 0
        ticket_list = []
        for applicant in successful_applicants:
            ticket = Ticket(applicant)
            total_cost += ticket["price"]
            ticket_list.append(ticket)
        result = {
                "successfulApplicants" : successful_applicants,
                "bannedApplicants" : banned_applicants,
                "totalCost": total_cost,
                "tickets": ticket_list,
        }
        return result
    except ValueError as err:
        return err

print(ProcessRequest(request))

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



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
    def bannedppl(name):
        if name in bannedVisitors:
            return True
        else:
            return False
    identity_of_banned = list(filter(bannedppl, request['applicants']))

    def checkmembership(members,member_status):
        for applicant in members:
            for key,value in member_status.items():
                if key == applicant:
                    print('Name: {} Status: {}'.format(key,value))
            if applicant not in member_status.keys():
                print('Name: {} Status: Request not yet verified'.format(applicant))

    def calculate_visitor_total_price(member_status):
        total_price = 0
        for key,value in member_status.items():
            if value == True:
                total_price += 3.50
            else:
                total_price += 5
        return total_price

    def visitor_ticketing(member_status):
        ticketing_dict = {}
        for key,value in member_status.items():
            if value == True:
                ticketing_dict[key] = 'Member Ticket for $3.50'
            else:
                ticketing_dict[key] = 'Non-member Ticket for $5.00'
        return ticketing_dict

    def check_applicants(applicants):
        try: 
            applicants[0]
            return applicants
        except IndexError:
            return None

    checkmembership(request['applicants'],memberStatus)
    print('$',calculate_visitor_total_price(memberStatus))
    print(visitor_ticketing(memberStatus))
    print(check_applicants(request["applicants"]))

    return 


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

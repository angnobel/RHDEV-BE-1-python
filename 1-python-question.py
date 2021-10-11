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
    if(len(request["applicants"]) <= 0):
        return {"error": "No applicants"}
        
    
    #Q1
    def checkIfBanned(person):
        for bannedPerson in bannedVisitors:
            if person == bannedPerson:
                return False
        return True
    
    successfulApplicants = list(filter(checkIfBanned, request["applicants"]))
    
    #Q2
    def checkIfMember(person): 
        if person in memberStatus:
            return memberStatus[person]
        return False
    
    memberList = list(filter(checkIfMember, successfulApplicants))
    
    #Q3
    def calculateTotalPrice():
        numberOfMembers = len(memberList)
        remainingPeople = len(successfulApplicants) - numberOfMembers 
        return numberOfMembers * 3.5 + remainingPeople * 5
    
    totalCost = calculateTotalPrice()

    #Q4
    def createDictForPerson(name, status, price):
        return {
            "name": name,
            "membershipStatus": status,
            "price": price
        }
    tickets = []
    for onePerson in memberList:
        tickets.append(createDictForPerson(onePerson, "member", 3.5))
    for onePerson in successfulApplicants:
        if (onePerson not in memberList):
            tickets.append(createDictForPerson(onePerson, "non-member", 5))

        

    return {
        "successfulApplicants": successfulApplicants,
        "totalCost": totalCost,
        "tickets": tickets
    }
    


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

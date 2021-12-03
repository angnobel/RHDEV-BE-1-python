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

allapplicants = request["applicants"]

def processRequest(request):

    result =  {
   "successfulApplicants": [],
   "bannedApplicants": [],
   "totalCost": 0,
   "tickets": []

 }

   # 1. filter call banned visitors
  
    if (not(len(allapplicants) == 0)):
       def checkBan(i):
          return ((i in bannedVisitors) == True)
       

       result["bannedApplicants"] = list(filter(checkBan, allapplicants))
   
   # 2. check applicants' membership status
       def checkAllow(i):
           return ((i in bannedVisitors) == False)

       allowedVisitors = list(filter(checkAllow, allapplicants))

       def checkMember(i):
              return memberStatus.get(str(i)) == True

       def checkVisitor(i):
              return memberStatus.get(str(i)) == False or (not(i in memberStatus.keys()))
        

       Members = list(filter(checkMember, allowedVisitors))
       Visitors = list(filter(checkVisitor, allowedVisitors))
       result["successfulApplicants"] = Members + Visitors
       
   # 3. calculate total price
       totalprice = len(Members) * 3.50 + len(Visitors) * 5.00
       totalpricedisplay = "$" + str(totalprice)
       result["totalCost"] = totalpricedisplay
  
       ticket = result["tickets"]
   # 4. issue tickets
       for i in Members:
            ticket.append({"name": i, "membershipStatus": "Member", "price": "$3.50"})
      
       for i in Visitors:
            ticket.append({"name": i, "membershipStatus": "Visitor", "price": "$5.00"})

   # 5. throw error if applicant is empty
    elif len(allapplicants) == 0:
        error =  {"error": "No applicants"}
        raise EmptyApplicant(error)
       
    
    return result


print(processRequest(request))

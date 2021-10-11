from os import error
request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

def processRequest(request):
  class namaewa(Exception):
    pass
  try:
    bannedVisitors = ["Amy", "Grace", "Bruce"]
    memberStatus = {
      "Ally": True,
      "David": True,
      "Brendan": False
    }
    if request["applicants"] == []:
      raise namaewa
    Removednames = set(request["applicants"]).intersection(bannedVisitors)
    Removednames = list(Removednames)
    if Removednames:
      for x in Removednames:
        request["applicants"].remove(x)
    else:
      Removednames = "no banned visitors"                          #remove banned visitors from request 
    successfulApplicants_list = request["applicants"]
    member_ticket_list = []
    nonmember_ticket_list = []
    for name in request["applicants"]:
      if memberStatus.get(name):                                 
        ticket = {"name" : name, "membershipStatus": True , "price": 3.50 }
        member_ticket_list.append(ticket)                          #add member to member list
      else:
        ticket = {"name":name,"membershipStatus":False , "price":5 }
        nonmember_ticket_list.append(ticket)                       #add non member to non member list
    ticket_list = member_ticket_list + nonmember_ticket_list       #add member and non member list to final list
    total_price = 0
    for dict in ticket_list:
      total_price += dict.get("price")                             #calculate total ticket price
    ticket_dict = {
                    "successfulApplicants" : successfulApplicants_list, 
                    "bannedApplicatns" : Removednames, 
                    "totalCost": total_price, 
                    "tickets": ticket_list 
                  }
    return ticket_dict
  except namaewa as e:
    return {"error" : "No applicants"}
  except Exception as e:
    return "ooops something went wrong "

print(processRequest(request))





   
















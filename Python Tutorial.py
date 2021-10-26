
request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

bannedVisitors = ["Amy", "Grace", "Bruce"]


memberStatus = {
  "Ally": True,
  "David": True,
  "Brendan": False
  }

def processRequest(request):
  try:
    if request["applicants"] == []:
      raise ValueError
    
    Removednames = list(filter(lambda a :a in bannedVisitors, request["applicants"]))

    if Removednames:
      for x in Removednames:
        request["applicants"].remove(x)          #remove banned visitors from request
                     
    ticket_list = []
    total_price = 0

    for x in request["applicants"]:
      if x not in memberStatus or  memberStatus[x] == False:
        ticket = {"name" : x, "membershipStatus": False , "price":5  }
        ticket_list.append(ticket)   
        total_price += 5
      

      else:
        ticket = {"name":x,"membershipStatus": True , "price": 3.50 }
        ticket_list.append(ticket)
        total_price += 3.5


    ticket_dict = {
                    "bannedApplicatns" : Removednames, 
                    "totalCost": total_price, 
                    "tickets": ticket_list 
                  }

    return ticket_dict

  except ValueError as e:
    return {"error" : "No applicants"}
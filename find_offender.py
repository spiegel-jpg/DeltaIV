import json 

f = open('accesslogs.json') # Open log file and read it 
d = {} # dictionary to hold username and ip address.
data = json.load(f)

for items in data:
    ip_address = items['client_details'][0]['src_ip']
    user_name = items['client_details'][0]['user_name']
    if user_name not in d: # If username not in dictionary, add username and ip address to dictionary. 
        d[user_name] = [ip_address]
    else:
        if ip_address not in d[user_name]: # Chek if IP address is same or not. If not, add to list. 
            d[user_name].append(ip_address)
#print(d)
for username, ip_address in d.items():
    if len(ip_address) > 1:
        print("The only log with same username but two distinct IP Addresses:",username + " ->", ip_address)
        print("-----------------------")
        print("This means that one of the IP address belongs to the offender. Upon manual inspection," 
              "the IP address 182.196.54.157 belongs to a username dfardy9. Notably, the offender also "
              "accesses a url (my.api.mockaroo.com) which is unique across the entire dataset.")

print([k for k,v in d.items() if v == ['182.196.54.157']], "is the offender!!!!")
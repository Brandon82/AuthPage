import urllib.request as urllib2
from licensing.models import *
from licensing.methods import Key, Helpers

class AuthHelper:
    def __init__(self, auth, RSAPubKey, pID):
        self.rsa_pub_key = ''
        self.access_token = auth
        self.product_id = pID
        self.connected = False

    def check_connnection(self):
        try:
            urllib2.urlopen('http:google.com', timeout=1)
            self.connected = True
        except urllib2.URLError as err:
            self.connected = False
    
    def authorize(self, key):
        self.check_connnection()
        if self.connected:
            result = Key.activate(token=self.access_token,\
                rsa_pub_key=self.rsa_pub_key,\
                product_id=17806, \
                key=key,\
                machine_code=Helpers.GetMachineCode(v=2))
            if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
                return False
            else:
                return True
        else:
            return False
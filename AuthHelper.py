import urllib.request as urllib2
from licensing.models import *
from licensing.methods import Key, Helpers

class AuthHelper:
    def __init__(self, auth, RSAPubKey, pID):
        self.rsa_pub_key = ''
        self.access_token = auth
        self.product_id = pID
        self.connected = False
        self.result = []

    def check_connnection(self):
        try:
            urllib2.urlopen('http:google.com', timeout=1)
            self.connected = True
        except urllib2.URLError as err:
            self.connected = False
        
    def get_expiration(self):
        return str(self.result[0].expires)
    
    def authorize(self, key):
        self.check_connnection()
        if self.connected:
            self.result = Key.activate(token=self.access_token,\
                rsa_pub_key=self.rsa_pub_key,\
                product_id=17806, \
                key=key,\
                machine_code=Helpers.GetMachineCode(v=2))
            if self.result[0] == None or not Helpers.IsOnRightMachine(self.result[0], v=2):
                return False
            else:
                return True
        else:
            return False
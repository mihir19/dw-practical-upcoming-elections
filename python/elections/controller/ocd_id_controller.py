STATE_OCD_ID = "ocd-division/country:us/state:"
CITY_OCD_ID = "/place:"
ELECTION_URL = "https://api.turbovote.org/elections/upcoming?district-divisions="

import requests
import json
class OCDIDController(object):
    def __init__(self, address):
        """
        :param state (string)
        :param city (string)
        """
        self.state = address["state"].lower()
        self.city = address["city"].lower().replace(" ", "_")
    
    def prepare(self):
        state_ocd_id = "{0}{1}".format(STATE_OCD_ID, self.state)
        city_ocd_id = "{0}{1}{2}".format(state_ocd_id, CITY_OCD_ID, self.city)
        return [state_ocd_id,city_ocd_id]
    
    def get_elections(self, data):
        url_param = ",".join(data)
        url = "{0}{1}".format(ELECTION_URL, url_param)
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers).json()
        return response
        


from elections.controller.ocd_id_controller import OCDIDController
import requests
def test_clean_form_data():
    form_data = {
        "state": "CA",
        "city": "Los Angeles"
    }
    ocd_o = OCDIDController(address=form_data)
    assert ocd_o.state == form_data["state"].lower()
    assert ocd_o.city == form_data["city"].lower().replace(" ", "_")

def test_prepare():
    expected_result = ["ocd-division/country:us/state:ma","ocd-division/country:us/state:ma/place:wayland"]
    form_data = {
        "state": "MA",
        "city": "Wayland"
    }
    ocd_o = OCDIDController(address=form_data)
    res = ocd_o.prepare()
    assert res == expected_result

def test_get_elections():
    form_data = {
        "state": "MA",
        "city": "Wayland"
    }
    
    ocd_o = OCDIDController(address=form_data)
    res = ocd_o.get_elections(data=ocd_o.prepare())
    url = "https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wayland"
    assert res == requests.get(url, headers = {'Accept': 'application/json'}).json()
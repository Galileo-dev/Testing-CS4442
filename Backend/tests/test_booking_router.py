import json
import fastapi
import random
    
    
def test_add_booking(client, firebase_test_token):
    
    hour = random.randint(0, 24)
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)   
     
    booking = {
        "room_id": "conferenceroom",
        "unparsed_date_time": None,
        "date_time": None,
        "date_time_str": "08-08 " + hour + ":36",
        "length_in_mins": 45
    }
    
    response = client.post(
        "/add_booking", headers={"Authorization": f"Bearer {firebase_test_token}"}, json=booking
    )

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json()['result'] == 'success'

def test_bearer_token(client):
    
    response = client.delete(
        f"/cancel_booking/conferenceroom/wrongid", headers={"Authorization": f"Bearer notoken"}
    )

    assert response.status_code == fastapi.status.HTTP_401_UNAUTHORIZED

from firebase_admin import credentials, firestore

class Database:
    
    cred = credentials.ApplicationDefault()
    db = firestore.client()
    
    def getFirstRoom(self):
        rooms_ref = self.db.collection('rooms')
        rooms = rooms_ref.stream()
        room = next(rooms)
        return room.to_dict()["displayName"]
    
    def getFirstUser(self):
        users_ref = self.db.collection('users')
        users = users_ref.stream()
        user = next(users)
        return user.to_dict()["displayName"]
    
    def getNameFromUID(self, uid: str):
        users_ref = self.db.collection('users')
        users = users_ref.stream()
        for user in users:
            if user.id == uid:
                return user.to_dict()        
        return None
    
    # def addReservation(self, room: str, uid: str, )
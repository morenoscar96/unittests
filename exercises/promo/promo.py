from datetime import datetime

class Promo:

    def __init__(self, name: str, expires: datetime) -> None:
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        print("Called")
        if self.expires < datetime.now():
            return True
        return False

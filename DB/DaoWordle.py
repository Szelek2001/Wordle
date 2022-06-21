from hashlib import md5

from sqlalchemy.orm import sessionmaker
from DB.Player import Player, engine

#klasa do dostępu do danych
class Dao:
    Session = sessionmaker(bind=engine)

    def _createSession(self):
        session = Dao.Session()
        return session

    def _add(self, value, session=None):
        if session is None:
            session = self._createSession()

        session.add(value)
        session.commit()

    def _delete(self, value, session=None):
        if session is None:
            session = self._createSession()

        session.delete(value)
        session.commit()

    def _get(self, type, key, session=None):
        # sprawdzanie sesji czy istnieje
        flag = session is None
        if session is None:
            session = self._createSession()

        result = session.query(type).get(key)

        if not flag:
            session.commit()

        return result

#klasa Wordle dostępu do danych dziedzidcząca po DAO
class DaoWordle(Dao):
    Session = sessionmaker(bind=engine)

    # tworzę obiekt sesji

    @staticmethod
    def create_session():
        session = DaoWordle.Session()
        return session

    # Dodawanie rekordu do Bazy danych
    def add(self, value):
        super()._add(value)

    # pobieranie
    def get(self, login):
        result = super()._get(Player, login)
        return result

    # aktulizacja wyniku po zwycięstwie

    def update_win(self, login, number):
        session = self.create_session()
        player = session.query(Player).get(login)
        player.win = player.win + 1
        player.game = player.game + 1

        if number == 1:
            player.A1 = player.A1 + 1
        if number == 2:
            player.A2 = player.A2 + 1
        if number == 3:
            player.A3 = player.A3 + 1
        if number == 4:
            player.A4 = player.A4 + 1
        if number == 5:
            player.A5 = player.A5 + 1
        if number == 6:
            player.A6 = player.A6 + 1

        session.flush()
        session.commit()

    # aktulizacja wyniku po porażce

    def update_lost(self, login):
        session = self.create_session()
        player = session.query(Player).get(login)
        player.lose = player.lose + 1
        player.game = player.game + 1
        session.flush()
        session.commit()

    # Sprawdzam czy istnieje taki użytkownik

    def check_usr(self, login):
        user = self.get(login)
        if user is None:
            return False
        else:
            return True

    # Sprawdzam poprawność hasła

    def checkpass(self, login, password):
        user = self.get(login)
        return user.password == md5(password.encode()).hexdigest()

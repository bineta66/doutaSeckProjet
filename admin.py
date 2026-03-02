import bcrypt
from db import Database

class Admin:

    def inscrire(self, username, password):
        db = Database()
        db.execute("SELECT id FROM admin WHERE username=%s", (username,))
        if db.fetchone():
            db.close()
            print("Ce username existe déjà")
            return False
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db.execute("INSERT INTO admin(username,password) VALUES(%s,%s)", (username, hashed), commit=True)
        db.close()
        print("Administrateur inscrit avec succès")
        return True

    def login(self, username, password):
        db = Database()
        db.execute("SELECT * FROM admin WHERE username=%s", (username,))
        user = db.fetchone()
        db.close()
        if not user:
            return False
        if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user
        return False
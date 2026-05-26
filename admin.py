import hmac
import hashlib

try:
    import bcrypt  # type: ignore
    _HAS_BCRYPT = True
except ModuleNotFoundError:  # pragma: no cover
    bcrypt = None
    _HAS_BCRYPT = False

from db import Database


class Admin:
    def _hash_password(self, password: str) -> str:
        """Retourne une représentation du hash.

        - Si bcrypt disponible : format bcrypt standard.
        - Sinon : hash HMAC-SHA256 avec une clé dérivée (fallback).

        Remarque: le fallback n’est pas aussi robuste que bcrypt.
        """
        if _HAS_BCRYPT:
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            return hashed

        # Fallback sans dépendance externe
        # On encode un sel dérivé de la version du programme / contexte.
        salt = "doutaSeckProjet"
        key = hashlib.sha256(salt.encode("utf-8")).digest()
        digest = hmac.new(key, password.encode("utf-8"), hashlib.sha256).hexdigest()
        return f"fallback_hmac_sha256${digest}"

    def _verify_password(self, password: str, stored_hash: str) -> bool:
        if _HAS_BCRYPT:
            return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))

        if not stored_hash.startswith("fallback_hmac_sha256$"):
            return False

        salt = "doutaSeckProjet"
        key = hashlib.sha256(salt.encode("utf-8")).digest()
        expected = hmac.new(key, password.encode("utf-8"), hashlib.sha256).hexdigest()
        got = stored_hash.split("$", 1)[1]
        return hmac.compare_digest(expected, got)

    def inscrire(self, username, password):
        db = Database()
        db.execute("SELECT id FROM admin WHERE username=%s", (username,))
        if db.fetchone():
            db.close()
            print("Ce username existe déjà")
            return False

        hashed = self._hash_password(password)
        db.execute(
            "INSERT INTO admin(username,password) VALUES(%s,%s)",
            (username, hashed),
            commit=True,
        )
        db.close()
        if _HAS_BCRYPT:
            print("Administrateur inscrit avec succès (bcrypt)")
        else:
            print("Administrateur inscrit avec succès (fallback hash)")
        return True

    def login(self, username, password):
        db = Database()
        db.execute("SELECT * FROM admin WHERE username=%s", (username,))
        user = db.fetchone()
        db.close()

        if not user:
            return False

        if self._verify_password(password, user["password"]):
            return user
        return False


# doutaSeckProjet

## Personnalisation de la connexion à la base

Le fichier `db.py` utilise des variables d'environnement pour se connecter à MySQL. Vous pouvez personnaliser ces valeurs sans toucher au code en définissant :

- `DB_HOST` : hôte de la base (par défaut `localhost`)
- `DB_PORT` : port MySQL (par défaut `3306`)
- `DB_USER` : utilisateur MySQL (par défaut `root`)
- `DB_PASSWORD` : mot de passe MySQL (par défaut `hellome13`)
- `DB_NAME` : nom de la base de données (par défaut `centre_douta_seck`)

Par exemple :

```bash
export DB_HOST=localhost
export DB_PORT=3306
export DB_USER=root
export DB_PASSWORD=hellome13
export DB_NAME=centre_douta_seck
```

Puis lancez l'application avec :

```bash
python main.py
```

> Si vous ne définissez pas ces variables, le code utilisera les valeurs par défaut indiquées ci-dessus.

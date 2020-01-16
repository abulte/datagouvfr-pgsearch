# datagouvfr-pgsearch

Search in data.gouv.fr's catalog with PostgreSQL.

- get the catalog from https://www.data.gouv.fr/fr/datasets/catalogue-des-donnees-de-data-gouv-fr/
- filter data: `spatial.zones` contains `France` and keep only the column we need
- insert in a PostgreSQL database
- expose a simple API

```shell
docker-compose up -d
sh prepare-data.sh
python cmd.py load
python app.py
```

🤜 http://localhost:5000?q=entreprises

```json
{
  "data": [
    [
      "544a1f9cc751df69c59bbff8",
      "Agreste - Les entreprises d'exploitations forestières et entreprises de sciage, de rabotage et d’imprégnation du bois",
      "Caractéristiques comptables financières et d’emploi des entreprises\nLes principales variables de synthèse : nombre d’entreprises, effectifs salariés moyens, chiffre d’affaires, exportations et livraisons intracommunautaires, valeur ajoutée, excédent brut",
      "Ministère de l'Agriculture et de l'Alimentation"
    ],
    [
      "5369986ea3a729239d204f67",
      "Les principales entreprises étrangères ayant des accords de coopération avec des entreprises françaises de défense",
      "CA total, CA de défense, Effectifs, accords de coopération",
      "Ministère des Armées"
    ],
    [
      "5b7ffc618b4c4169d30727e0",
      "Base Sirene des entreprises et de leurs établissements (SIREN, SIRET)",
      "\n\n\n- Pour vous abonner à notre lettre d'information **Sirene open data actualités**, suivez ce lien : https://insee.fr/fr/information/1405555\n- Pour consulter nos lettres d'information **Sirene open data actualités**, suivez ce lien : https://insee.fr/fr",
      "Institut National de la Statistique et des Etudes Economiques (Insee)"
    ],
    [
      "5d9215888b4c415092182f79",
      "Enquête sur les entreprises et le développement durable ",
      "L’objectif de l’enquête sur les entreprises et le développement durable (EnDD) est de mesurer l’implication des entreprises dans une démarche de développement durable dans ses différentes dimensions (environnementale, sociale, économique). L’enquête  vis",
      "Institut National de la Statistique et des Etudes Economiques (Insee)"
    ],
    [
      "5be2c158634f411a17542f57",
      "chefs d’exploitation ou d’entreprise agricole par EPCI 2017",
      "Le champ des chefs d’exploitation ou d’entreprise agricole exclut les exploitants agricoles ou les chefs d’entreprise agricole dont l’exploitation procure une activité inférieure à l’activité minimale d’assujettissement (AMA).\nLa loi d’avenir pour l’agri",
      "Mutualité Sociale Agricole"
    ],
    [
      "5be2c2e2634f411df372f474",
      "installations de chefs d’exploitation ou d’entreprise agricole par EPCI 2016",
      "Le champ des chefs d’exploitation ou d’entreprise agricole exclut les exploitants agricoles ou les chefs d’entreprise agricole dont l’exploitation procure une activité inférieure à l’activité minimale d’assujettissement (AMA).\nLa loi d’avenir pour l’agri",
      "Mutualité Sociale Agricole"
    ],
    [
      "53698f4ea3a729239d2036ee",
      "Base de données des obligations d'information pesant sur les entreprises",
      "La base de données des obligations d'information pesant sur les entreprises concerne l'ensemble des informations que les entreprises doivent communiquer à une autorité publique ou à des tiers. Ce recensement des obligations qui s'imposent aux entreprises",
      "Premier ministre"
    ],
    [
      "5a0b0be188ee3871db07ce4e",
      "ACCO : Accords d’entreprise",
      "**Ce jeu de données provient d'un service public certifié**\n\n\nLes accords d’entreprise diffusés conformément à l’article du décret n° 2017-752 du 3 mai 2017 relatif à la publicité des accords collectifs. \n\n\nCes accords peuvent concerner : \n\n- les groupes",
      "Premier ministre"
    ],
    [
      "5369a052a3a729239d206338",
      "Statistiques annuelles d'entreprises : Esane",
      "Le dispositif ÉSANE (Élaboration des Statistiques Annuelles d'Entreprises) propose chaque année une photographie de la population des unités légales (sociétés, entreprises individuelles, parties d'administrations publiques et certaines associations) ou d",
      "Institut National de la Statistique et des Etudes Economiques (Insee)"
    ],
    [
      "53699260a3a729239d203ee9",
      "Démographie des entreprises",
      "Ce jeu de données provient de la Banque de Données Macro-économiques de l'INSEE. La BDM est la principale base de données de séries et indices sur l'ensemble des domaines économiques et sociaux. Elle met à disposition toutes les informations nécessaires ",
      "Institut National de la Statistique et des Etudes Economiques (Insee)"
    ]
  ],
  "time": 0.11758780479431152
}
```

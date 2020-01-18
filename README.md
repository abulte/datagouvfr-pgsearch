# datagouvfr-pgsearch

Search in data.gouv.fr's catalog with PostgreSQL.

- get the catalog from https://www.data.gouv.fr/fr/datasets/catalogue-des-donnees-de-data-gouv-fr/
- filter data: `spatial.zones` contains `France` and keep only the column we need
- insert in a PostgreSQL database
- fetch the `nb_hits` metric from stats.data.gouv.fr
- expose a simple API

## Quickstart

```shell
docker-compose up -d
sh prepare-data.sh
python cmd.py load
python cmd.py fetch_stats
python app.py
```

🤜 http://localhost:5000/?q=entreprises
🤜 http://localhost:5000/api?q=entreprises

```json
{
  "data": [
    {
      "_id": "58e53811c751df03df38f42d",
      "description": "Le Répertoire National des Associations (RNA) contient l’ensemble des associations relevant de la loi 1901, à savoir toutes les associations de France, dont le siège est déclaré en métropole ou dans les départements d’outre-mer, sauf dans les département",
      "nb_hits": 12203,
      "organization": "Ministère de l'Intérieur",
      "title": "Répertoire National des Associations"
    },
    {
      "_id": "5b7ffc618b4c4169d30727e0",
      "description": "\n\n\n- Pour vous abonner à notre lettre d'information **Sirene open data actualités**, suivez ce lien : https://insee.fr/fr/information/1405555\n- Pour consulter nos lettres d'information **Sirene open data actualités**, suivez ce lien : https://insee.fr/fr",
      "nb_hits": 5919,
      "organization": "Institut National de la Statistique et des Etudes Economiques (Insee)",
      "title": "Base Sirene des entreprises et de leurs établissements (SIREN, SIRET)"
    },
    {
      "_id": "5710b9f088ee383cf54d8898",
      "description": "**Attention : le jeu de données contient plus de 2 millions de lignes. Il convient de disposer d’un logiciel permettant d’afficher l’ensemble de ces lignes.**\n\nLa base de données publique Transparence - Santé rend accessible l'ensemble des informations d",
      "nb_hits": 1965,
      "organization": "Ministère des Solidarités et de la Santé",
      "title": "Transparence-santé"
    },
    {
      "_id": "5943d4c188ee38742a95eb0d",
      "description": "La Commission européenne a adopté la carte française des zones d’aides à finalité régionale (AFR) pour la période 2014-2020, mise en œuvre par le [décret n° 2014-758 du 2 juillet 2014 relatif aux zones d'aide à finalité régionale (AFR) et aux zones d'aid",
      "nb_hits": 1086,
      "organization": "Commissariat général à l'égalité des territoires",
      "title": "Zone d'Aide à Finalité Régionale (AFR)"
    },
    {
      "_id": "5369965fa3a729239d204999",
      "description": "Vous pouvez consulter les taux votés ainsi que l'ensemble des données (bases, taux et produits) par collectivité territoriale. Les données sont disponibles en pièces jointes et pour une partie sur le site : <https://www.impots.gouv.fr/portail/statistique",
      "nb_hits": 698,
      "organization": "Ministère de l'économie et des finances",
      "title": "Impôts locaux"
    },
    {
      "_id": "53ca2be2a3a7294a1ddd7847",
      "description": "Les données ''ASSOCIATIONS'' sont extraites du JOAFE (JOURNAL OFFICIEL DES ASSOCIATIONS ET FONDATIONS D'ENTREPRISE)\n\nLe Journal officiel des associations, associations syndicales de propriétaires et fondations d’entreprise publie :\n\nLes déclarations de c",
      "nb_hits": 447,
      "organization": "Premier ministre",
      "title": "ASSOCIATIONS"
    },
    {
      "_id": "559395f1c751df0f51a453b9",
      "description": "Annonces publiées au Bodacc (Bulletin officiel des annonces civiles et commerciales).\n\nLe Bodacc (Bulletin officiel des annonces civiles et commerciales), régi par l’article R 123-209 du code de commerce, publie les avis prévus par ce code et les textes ",
      "nb_hits": 343,
      "organization": "Premier ministre",
      "title": "BODACC"
    },
    {
      "_id": "544a1f9cc751df69c59bbff8",
      "description": "Caractéristiques comptables financières et d’emploi des entreprises\nLes principales variables de synthèse : nombre d’entreprises, effectifs salariés moyens, chiffre d’affaires, exportations et livraisons intracommunautaires, valeur ajoutée, excédent brut",
      "nb_hits": 0,
      "organization": "Ministère de l'Agriculture et de l'Alimentation",
      "title": "Agreste - Les entreprises d'exploitations forestières et entreprises de sciage, de rabotage et d’imprégnation du bois"
    },
    {
      "_id": "5369986ea3a729239d204f67",
      "description": "CA total, CA de défense, Effectifs, accords de coopération",
      "nb_hits": 0,
      "organization": "Ministère des Armées",
      "title": "Les principales entreprises étrangères ayant des accords de coopération avec des entreprises françaises de défense"
    },
    {
      "_id": "5d9215888b4c415092182f79",
      "description": "L’objectif de l’enquête sur les entreprises et le développement durable (EnDD) est de mesurer l’implication des entreprises dans une démarche de développement durable dans ses différentes dimensions (environnementale, sociale, économique). L’enquête  vis",
      "nb_hits": 0,
      "organization": "Institut National de la Statistique et des Etudes Economiques (Insee)",
      "title": "Enquête sur les entreprises et le développement durable "
    }
  ],
  "time": 0.15753912925720215
}
```

## Deploy

```
git push dokku master
```

"""
Contains data on legislators that is not provided by the API. Although st sync
most data that we can from the API, we expect these values to change rarely and
it's fine to have them be fixed.
"""

D = "D"
R = "R"

# The API does provide "name", but we have it here too so allow overriding
# the rendering of the name, and also because it makes this dict much easier
# to read.
COUNCIL_DATA_BY_LEGISLATOR_ID = {
    7739: {
        "name": "Adrienne E. Adams",
        "twitter": "AdrienneEAdams1",
        "party": "D",
        "borough": "Queens",
    },
    7747: {
        "name": "Alicka Ampry-Samuel",
        "twitter": "CMAlickaASamuel",
        "party": "D",
        "borough": "Brooklyn",
    },
    7742: {
        "name": "Diana Ayala",
        "twitter": "DianaAyalaNYC",
        "party": "D",
        "borough": "Manhattan and Bronx",
    },
    7623: {
        "name": "Inez D. Barron",
        "twitter": "CMInezDBarron",
        "party": "D",
        "borough": "Brooklyn",
    },
    7264: {
        "name": "Joseph C. Borelli",
        "twitter": "JoeBorelliNYC",
        "party": "R",
        "borough": "Staten Island",
    },
    7748: {
        "name": "Justin L. Brannan",
        "twitter": "JustinBrannan",
        "party": "D",
        "borough": "Brooklyn",
    },
    7561: {
        "name": "Fernando Cabrera ",
        "twitter": "FCabreraNY",
        "party": "D",
        "borough": "Bronx",
    },
    7562: {
        "name": "Margaret S. Chin",
        "twitter": "CM_MargaretChin",
        "party": "D",
        "borough": "Manhattan",
    },
    7604: {
        "name": "Robert E. Cornegy, Jr.",
        "twitter": "rc4bk",
        "party": "D",
        "borough": "Brooklyn",
    },
    7628: {
        "name": "Laurie A. Cumbo",
        "twitter": "cmlauriecumbo",
        "party": "D",
        "borough": "Brooklyn",
    },
    7744: {
        "name": "Ruben Diaz, Sr.",
        "twitter": "revrubendiaz",
        "party": "D",
        "borough": "Bronx",
    },
    7563: {
        "name": "Daniel Dromm",
        "twitter": "Dromm25",
        "party": "D",
        "borough": "Queens",
    },
    7113: {
        "name": "Mathieu Eugene",
        "twitter": "CMMathieuEugene",
        "party": "D",
        "borough": "Brooklyn",
    },
    7622: {
        "name": "Vanessa L. Gibson",
        "twitter": "Vanessalgibson",
        "party": "D",
        "borough": "Bronx",
    },
    7743: {
        "name": "Mark Gjonaj ",
        "twitter": "MarkGjonajNY",
        "party": "D",
        "borough": "Bronx",
    },
    7691: {
        "name": "Barry S. Grodenchik",
        "twitter": "BarryGrodenchik",
        "party": "D",
        "borough": "Queens",
    },
    7746: {
        "name": "Robert F. Holden",
        "twitter": "BobHoldenNYC",
        "party": "D",
        "borough": "Queens",
    },
    7631: {
        "name": "Corey D. Johnson",
        "twitter": "NYCSpeakerCoJo",
        "party": "D",
        "borough": "Manhattan",
    },
    7632: {
        "name": "Ben Kallos",
        "twitter": "BenKallos",
        "party": "D",
        "borough": "Manhattan",
    },
    7565: {
        "name": "Peter A. Koo",
        "twitter": "CMPeterKoo",
        "party": "D",
        "borough": "Queens",
    },
    386: {
        "name": "Karen Koslowitz",
        "twitter": "CMKoslowitz",
        "party": "D",
        "borough": "Queens",
    },
    7566: {
        "name": "Brad S. Lander",
        "twitter": "bradlander",
        "party": "D",
        "borough": "Brooklyn",
    },
    7567: {
        "name": "Stephen T. Levin",
        "twitter": "StephenLevin33",
        "party": "D",
        "borough": "Brooklyn",
    },
    7634: {
        "name": "Mark Levine",
        "twitter": "MarkLevineNYC",
        "party": "D",
        "borough": "Manhattan",
    },
    7635: {
        "name": "Alan N. Maisel",
        "twitter": None,
        "party": "D",
        "borough": "Brooklyn",
    },
    5953: {
        "name": "Steven Matteo",
        "twitter": "StevenMatteo",
        "party": "R",
        "borough": "Staten Island",
    },
    7636: {
        "name": "Carlos Menchaca",
        "twitter": "cmenchaca",
        "party": "D",
        "borough": "Brooklyn",
    },
    7637: {
        "name": "I. Daneek Miller",
        "twitter": "IDaneekMiller",
        "party": "D",
        "borough": "Queens",
    },
    7745: {
        "name": "Francisco P. Moya",
        "twitter": "FranciscoMoyaNY",
        "party": "D",
        "borough": "Queens",
    },
    430: {
        "name": "Bill Perkins",
        "twitter": None,
        "party": "D",
        "borough": "Manhattan",
    },
    7741: {
        "name": "Keith Powers",
        "twitter": "KeithPowersNYC",
        "party": "D",
        "borough": "Manhattan",
    },
    7638: {
        "name": "Antonio Reynoso",
        "twitter": "ReynosoBrooklyn",
        "party": "D",
        "borough": "Brooklyn",
    },
    7740: {
        "name": "Carlina Rivera ",
        "twitter": "CarlinaRivera",
        "party": "D",
        "borough": "Manhattan",
    },
    7541: {
        "name": "Ydanis A. Rodriguez",
        "twitter": "ydanis",
        "party": "D",
        "borough": "Manhattan",
    },
    7568: {
        "name": "Deborah L. Rose",
        "twitter": "CMDebiRose",
        "party": "D",
        "borough": "Staten Island",
    },
    7639: {
        "name": "Helen K. Rosenthal",
        "twitter": "HelenRosenthal",
        "party": "D",
        "borough": "Manhattan",
    },
    7714: {
        "name": "Rafael Salamanca, Jr.",
        "twitter": "Salamancajr80",
        "party": "D",
        "borough": "Bronx",
    },
    7641: {
        "name": "Mark Treyger",
        "twitter": "MarkTreyger718",
        "party": "D",
        "borough": "Brooklyn",
    },
    7510: {
        "name": "Eric A. Ulrich",
        "twitter": "eric_ulrich",
        "party": "R",
        "borough": "Queens",
    },
    7642: {
        "name": "Paul A. Vallone",
        "twitter": "PaulVallone",
        "party": "D",
        "borough": "Queens",
    },
    7569: {
        "name": "James G. Van Bramer",
        "twitter": "JimmyVanBramer",
        "party": "D",
        "borough": "Queens",
    },
    7749: {
        "name": "Kalman Yeger",
        "twitter": "KalmanYeger",
        "party": "D",
        "borough": "Brooklyn",
    },
    7780: {
        "name": "Public Advocate Jumaane Williams",
        "twitter": "JumaaneWilliams",
        "party": "D",
        "borough": "",
    },
    7785: {
        "name": "Farah N. Louis",
        "twitter": "CMFarahLouis",
        "party": "D",
        "borough": "Brooklyn",
    },
    7793: {
        "name": "Darma V. Diaz",
        "twitter": None,
        "party": "D",
        "borough": "Brooklyn",
    },
    7794: {
        "name": "Kevin C. Riley",
        "twitter": "CMKevinCRiley",
        "party": "D",
        "borough": "Bronx",
    },
    5273: {
        "name": "James F. Gennaro",
        "twitter": "JimGennaro",
        "party": "D",
        "borough": "Queens",
    },
    7796: {
        "name": "Selvena N. Brooks-Powers",
        "twitter": "Powers4Queens",
        "party": "D",
        "borough": "Queens",
    },
    7799: {
        "name": "Eric Dinowitz",
        "twitter": "EricDinowitz",
        "party": "D",
        "borough": "Bronx",
    },
    7798: {
        "name": "Oswald Feliz",
        "twitter": "OswaldFeliz",
        "party": "D",
        "borough": "Bronx",
    },
}
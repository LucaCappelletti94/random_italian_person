random_italian_person
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy|
|code_climate_maintainability| |pip| |downloads|

Python package to generate an Italian person randomly.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install random_italian_person

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime
get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Python package to generate an Italian person randomly.

Usage examples
-----------------------------------------------

.. code:: python

    from random_italian_person import RandomItalianPerson

    person = RandomItalianPerson()

    print(person.describe())
    # 'Rodrigo Benedetti è nata/o a Molazzana (LU) il 1972-12-18. Ora vive a Cagliari (CA) in Via Giuseppe Garibaldi 109.'

Generate a CSV of random italian persons
-----------------------------------------------
One of the most common usages for this library is to render
fake datasets for testing porposes. For instance,
to generate a CSV with 5 random person you can use:

.. code:: python

    import pandas as pd
    from random_italian_person import RandomItalianPerson

    df = pd.DataFrame([
        RandomItalianPerson().data
        for _ in range(5)
    ])

The obtained dataframe will look like:

+-----------------------+------------+-----------+-----------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+-------------------+----------------+-------+----------------+-----------------+------------------+
| region                | province   | surname   | name      | sex   | birth_municipality   | birth_province   | birth_region   |   birth_cap | birth_province_code   | birthdate   | address           | house_number   |   cap | municipality   | province_code   | codice_fiscale   |
+=======================+============+===========+===========+=======+======================+==================+================+=============+=======================+=============+===================+================+=======+================+=================+==================+
| Marche                | Macerata   | Di Felice | Giacomina | F     | Mosciano Sant'angelo | Teramo           | Abruzzo        |       64023 | TE                    | 1945-09-18  | Viale De Amicis   | 76             | 62020 | Colmurano      | MC              | DFLGMN45P58F764B |
+-----------------------+------------+-----------+-----------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+-------------------+----------------+-------+----------------+-----------------+------------------+
| Friuli Venezia Giulia | Udine      | Galli     | Imen      | F     | Isola Dovarese       | Cremona          | Lombardia      |       26031 | CR                    | 1942-03-10  | Via Udine         | 2              | 33020 | Verzegnis      | UD              | GLLMNI42C50E356T |
+-----------------------+------------+-----------+-----------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+-------------------+----------------+-------+----------------+-----------------+------------------+
| Abruzzo               | Pescara    | Rosso     | Eva       | F     | Cellarengo           | Asti             | Piemonte       |       14010 | AT                    | 2001-12-31  | Via G. Fonzi      | 58             | 65010 | Spoltore       | PE              | RSSVEA01T71C438U |
+-----------------------+------------+-----------+-----------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+-------------------+----------------+-------+----------------+-----------------+------------------+
| Emilia Romagna        | Bologna    | Grasso    | Emanuele  | M     | Caposele             | Avellino         | Campania       |       83040 | AV                    | 1942-08-27  | Via G. Massarenti | 223/5          | 40138 | Bologna        | BO              | GRSMNL42M27B674L |
+-----------------------+------------+-----------+-----------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+-------------------+----------------+-------+----------------+-----------------+------------------+
| Sicilia               | Palermo    | Pastorino | Lenuta    | F     | Borzonasca           | Genova           | Liguria        |       16041 | GE                    | 1972-09-05  | Via Montalbo      | 124            | 90142 | Palermo        | PA              | PSTLNT72P45B067T |
+-----------------------+------------+-----------+-----------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+-------------------+----------------+-------+----------------+-----------------+------------------+

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/random_italian_person.png
   :target: https://travis-ci.org/LucaCappelletti94/random_italian_person
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_italian_person&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_italian_person
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_italian_person&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_italian_person
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_italian_person&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_italian_person
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/random_italian_person/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/random_italian_person?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/random-italian-person.svg
    :target: https://badge.fury.io/py/random-italian-person
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/random-italian-person
    :target: https://pepy.tech/badge/random-italian-person
    :alt: Pypi total project downloads

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/1e0b901c55b7446bacd7bc5a0fbcbf71
    :target: https://www.codacy.com/manual/LucaCappelletti94/random_italian_person?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/random_italian_person&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/5a97d2474feee23f4516/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/random_italian_person/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/5a97d2474feee23f4516/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/random_italian_person/test_coverage
    :alt: Code Climate Coverate

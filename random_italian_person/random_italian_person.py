import os
import pandas as pd
import numpy as np
import json
from typing import Dict
from codicefiscale import codicefiscale
from .utils import random_birthday


class RandomItalianPerson:

    municipalities = None
    names = None
    surnames = None

    def __init__(self):
        if RandomItalianPerson.municipalities is None:
            RandomItalianPerson.municipalities = pd.read_csv(
                "{}/datasets/municipalities.csv".format(
                    os.path.dirname(os.path.abspath(__file__))),
                dtype={"cap": str}
            )
        if RandomItalianPerson.names is None:
            RandomItalianPerson.names = pd.read_csv(
                "{}/datasets/names.csv".format(
                    os.path.dirname(os.path.abspath(__file__)))
            )
            RandomItalianPerson.frequencies = (
                RandomItalianPerson.names.number / RandomItalianPerson.names.number.sum()
            ).values
            RandomItalianPerson.names = RandomItalianPerson.names.drop(columns=[
                                                                       "number"])

        if RandomItalianPerson.surnames is None:
            RandomItalianPerson.surnames = pd.read_csv(
                "{}/datasets/surnames.csv".format(
                    os.path.dirname(os.path.abspath(__file__)))
            )

        surname_data = RandomItalianPerson.surnames.sample(n=1)
        name_data = RandomItalianPerson.names.iloc[np.random.choice(
            RandomItalianPerson.names.index, p=RandomItalianPerson.frequencies)]
        municipality_data = RandomItalianPerson.municipalities[
            RandomItalianPerson.municipalities.province.isin(
                surname_data.province)
        ].sample(n=1)

        self._data = {
            **surname_data.reset_index(drop=True).iloc[0].to_dict(),
            **name_data.to_dict(),
            **municipality_data.reset_index(drop=True).iloc[0].to_dict(),
            "birthdate": random_birthday().isoformat()
        }

        self._data["codice_fiscale"] = codicefiscale.encode(
            surname=self.surname,
            name=self.name,
            sex=self.sex,
            birthdate=self.birthdate,
            birthplace=self.municipality
        )

    @property
    def name(self) -> str:
        return self._data["name"]

    @property
    def surname(self) -> str:
        return self._data["surname"]

    @property
    def province(self) -> str:
        return self._data["province"]

    @property
    def province_code(self) -> str:
        return self._data["province"]

    @property
    def region(self) -> str:
        return self._data["region"]

    @property
    def municipality(self) -> str:
        return self._data["municipality"]

    @property
    def birthdate(self) -> str:
        return self._data["birthdate"]

    @property
    def sex(self) -> str:
        return self._data["sex"]

    @property
    def codice_fiscale(self) -> str:
        return self._data["codice_fiscale"]

    @property
    def data(self) -> Dict:
        return self._data

    def __repr__(self) -> str:
        return json.dumps(self._data, indent=4)

    __str__ = __repr__

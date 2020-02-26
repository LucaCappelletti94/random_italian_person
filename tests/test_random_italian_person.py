from random_italian_person import RandomItalianPerson
from tqdm.auto import tqdm


def test_random_italian_person():
    for _ in tqdm(range(1000)):
        RandomItalianPerson()

    person = RandomItalianPerson()
    assert person.describe() == person.describe()
    assert person.data == person.data
    assert str(person) == str(person)

from random_italian_person import RandomItalianPerson
from collections import Counter
from tqdm.auto import tqdm

def test_random_italian_person():
    for _ in tqdm(range(10000)):
        RandomItalianPerson()
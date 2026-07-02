from dataclasses import dataclass


@dataclass
class Character:
    name: str
    gender: str
    age: str
    appearance: str
    personality: str
    clothing: str
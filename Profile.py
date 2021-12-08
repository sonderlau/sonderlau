from dataclasses import dataclass
from typing import Tuple


class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        return dataclass(unsafe_hash=True, frozen=True)(new_cls)


class Bio(metaclass=Meta):
    name        : str = "Sonder Lau"
    job         : str = "Student"
    designation : str = "Recommendation System Engineer"
    base        : str = "Hangzhou, ZheJiang, China"
    blog        : str = "https://sekai.pro"


class Stack(metaclass=Meta):
    languages   : Tuple[str, ...] = ("Python", "C++", "Javascript")
    databases   : Tuple[str, ...] = ("MySQL", "Mongo")
    misc        : Tuple[str, ...] = ("Docker", "Linux", "Vim")
    ongoing     : Tuple[str, ...] = ("Rust", "Algorithm", "AI", "Recommendation System")


class Recent(metaclass=Meta):
    project     : Tuple[str, ...] = ("FlowerColor", "Python Scraper")
    working     : Tuple[str, ...] = ("Assignments", "Exams")
    learning    : Tuple[str, ...] = ("Algebra", "Probability Theory")

<img src="https://raw.githubusercontent.com/sonderlau/sonderlau/main/imgs/banner.png">

<p align="center">
    <img src="https://badges.pufler.dev/visits/sonderlau/sonderlau" />
    <img src="https://badges.pufler.dev/repos/sonderlau" />
    <img src="https://badges.pufler.dev/commits/monthly/sonderlau" />
</p>

<p padding-left="30%">
-  University Student | Majoring in Computer Science <br />
- 🔭 I’m currently working on a project named FlowerColor <br />
- 🌱 I’m currently learning Software Design <br />
</p>

```python
from dataclasses import dataclass
from typing import Tuple


class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        return dataclass(unsafe_hash=True, frozen=True)(new_cls)


class Bio(metaclass=Meta):
    name        : str = "🤝Sonder Lau"
    job         : str = "🏛Student"
    designation : str = "🔣Recommendation System Engineer"
    base        : str = "🏠Hangzhou, ZheJiang, China"
    blog        : str = "🐚https://sekai.pro"


class Stack(metaclass=Meta):
    languages   : Tuple[str, ...] = ("Python", "C++", "Javascript")
    databases   : Tuple[str, ...] = ("MySQL", "Mongo")
    misc        : Tuple[str, ...] = ("Docker", "Linux", "Vim")
    ongoing     : Tuple[str, ...] = ("Rust", "Algorithm", "AI", "Recommendation System")


class Recent(metaclass=Meta):
    project     : Tuple[str, ...] = ("FlowerColor", "Python Scraper")
    working     : Tuple[str, ...] = ("Assignments", "Exams")
    learning    : Tuple[str, ...] = ("Algebra", "Probability Theory")
```

<h2 align="center">Github Metrics</h2>


<div align="center">
    <img src="https://github-readme-streak-stats.herokuapp.com?user=SonderLau&theme=react&hide_border=true" alt="Github Streak" />
    <img src="https://github-readme-stats.vercel.app/api?username=SonderLau&show_icons=true&count_private=true&hide=prs&theme=react" alt="info" />
    <img src="https://activity-graph.herokuapp.com/graph?username=SonderLau&theme=react-dark" alt="Ashutosh's github activity graph" />
    <img src="https://raw.githubusercontent.com/sonderlau/sonderlau/2f094c013a2cd4e882136e56adff66e189c7b5ef/github-contribution-grid-snake.svg" />
</div>




  

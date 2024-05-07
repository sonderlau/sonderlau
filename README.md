<img src="https://raw.githubusercontent.com/sonderlau/sonderlau/main/imgs/banner.png">



```python
from dataclasses import dataclass
from typing import Tuple


class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        return dataclass(unsafe_hash=True, frozen=True)(new_cls)


class Bio(metaclass=Meta):
    name        : str = "🤝Sonder Liu"
    job         : str = "🏛Postgraduate Student"
    designation : str = "🔣Lovely man"
    base        : str = "🏠Hangzhou, ZheJiang Province, China"
    blog        : str = "🐚Upcoming..."


class Stack(metaclass=Meta):
    languages   : Tuple[str, ...] = ("Python", "C++")
    databases   : Tuple[str, ...] = ("SQLite", "Postgres")
    devices     : Tuple[str, ...] = ("MacBook Pro", "iPad Pro", "OnePlus 12")
    ongoing     : Tuple[str, ...] = ("DL Model", "Paper reading")


class Recent(metaclass=Meta):
    project     : Tuple[str, ...] = ("Weather forecast with Deep Learning")
    working     : Tuple[str, ...] = ("None")
    learning    : Tuple[str, ...] = ("Linear Algebra", "Probability Theory")
```

<h2 align="center">Github Metrics</h2>


<div align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=SonderLau&show_icons=true&count_private=true&hide=prs&theme=react" alt="info" />
    <img src="https://raw.githubusercontent.com/sonderlau/sonderlau/2f094c013a2cd4e882136e56adff66e189c7b5ef/github-contribution-grid-snake.svg" />
</div>




  

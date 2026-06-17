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
    job         : str = "🏛PhD. Student"
    designation : str = "🔣Lovely man"
    base        : str = "🏠Nanjing, Jiangsu Province, China"
    blog        : str = "🐚 https://sonderlau.github.io"


class Stack(metaclass=Meta):
    languages   : Tuple[str, ...] = ("Python", "C++")
    databases   : Tuple[str, ...] = ("Postgres")
    devices     : Tuple[str, ...] = ("MacBook Pro", "iPad Pro", "Sony WH1000-XM5", "OnePlus 12")
    ongoing     : Tuple[str, ...] = ("DL Model", "Paper reading")


class Recent(metaclass=Meta):
    project     : Tuple[str, ...] = ("Precipitation nowcasting with Deep Learning")
    working     : Tuple[str, ...] = ("None")
    learning    : Tuple[str, ...] = ("Linear Algebra", "Probability Theory")
```

<div align="center">
I merely added complexity to the foundations laid by others, and then told laypeople that this is a "moat".

</div>




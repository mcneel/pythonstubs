from typing import Tuple, Set, Iterable, List, overload


class GH_GenericLayout:
    def Horizontal_ByIndex(area: Rectangle, stack: List, expand: bool) -> List: ...
    @overload
    def Horizontal_ByPosition(area: Rectangle, stack: List, expand: bool) -> List: ...
    @overload
    def Horizontal_ByPosition(area: Rectangle, stack: List, expand: bool, radical: int) -> List: ...
    def Vertical_ByIndex(area: Rectangle, stack: List, expand: bool) -> List: ...
    @overload
    def Vertical_ByPosition(area: Rectangle, stack: List, expand: bool) -> List: ...
    @overload
    def Vertical_ByPosition(area: Rectangle, stack: List, expand: bool, radical: int) -> List: ...

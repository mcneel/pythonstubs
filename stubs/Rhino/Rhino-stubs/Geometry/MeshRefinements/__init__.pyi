from typing import Tuple, Set, Iterable, List, overload


class CreaseEdges:
    NakedFixed = 0
    NakedSmooth = 1
    CornerFixedOtherCreased = 2
    Auto = 3


class LoopFormula:
    Loop = 0
    Warren = 1
    WarrenWeimer = 2


class RefinementSettings:
    def __init__(self): ...
    @property
    def ContinueRequest(self) -> CancellationToken: ...
    @property
    def HasPull(self) -> bool: ...
    @property
    def Level(self) -> int: ...
    @property
    def NakedEdgeMode(self) -> CreaseEdges: ...
    @ContinueRequest.setter
    def ContinueRequest(self, value: CancellationToken) -> None: ...
    @Level.setter
    def Level(self, value: int) -> None: ...
    @NakedEdgeMode.setter
    def NakedEdgeMode(self, value: CreaseEdges) -> None: ...

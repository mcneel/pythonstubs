from typing import Tuple, Set, Iterable, List


class CreaseEdges:
    NakedFixed = 0
    NakedSmooth = 1
    CornerFixedOtherCreased = 2
    Auto = 3


class RefinementSettings:
    def __init__(self): ...
    @property
    def Level(self) -> int: ...
    @Level.setter
    def Level(self, value: int) -> None: ...
    @property
    def HasPull(self) -> bool: ...
    @property
    def ContinueRequest(self) -> CancellationToken: ...
    @ContinueRequest.setter
    def ContinueRequest(self, value: CancellationToken) -> None: ...
    @property
    def NakedEdgeMode(self) -> CreaseEdges: ...
    @NakedEdgeMode.setter
    def NakedEdgeMode(self, value: CreaseEdges) -> None: ...


class LoopFormula:
    Loop = 0
    Warren = 1
    WarrenWeimer = 2

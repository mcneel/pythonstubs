__all__ = ['Actions']
from typing import Tuple, Set, Iterable, List, overload


class GH_ArchivedUndoAction(GH_UndoAction):
    def Read(self, reader: GH_IReader) -> bool: ...
    def Write(self, writer: GH_IWriter) -> bool: ...


class GH_ObjectUndoAction(GH_UndoAction):
    pass


class GH_UndoAction:
    @property
    def ExpiresDisplay(self) -> bool: ...
    @property
    def ExpiresSolution(self) -> bool: ...
    @property
    def State(self) -> GH_UndoState: ...
    def Read(self, reader: GH_IReader) -> bool: ...
    def Redo(self, doc: GH_Document) -> None: ...
    def Undo(self, doc: GH_Document) -> None: ...
    def Write(self, writer: GH_IWriter) -> bool: ...


class GH_UndoException:
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, args: Set(Object)): ...


class GH_UndoRecord:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, action: IGH_UndoAction): ...
    @overload
    def __init__(self, name: str, actions: Set(IGH_UndoAction)): ...
    @overload
    def __init__(self, name: str, actions: Iterable[IGH_UndoAction]): ...
    def AddAction(self, action: IGH_UndoAction) -> None: ...
    @property
    def ActionCount(self) -> int: ...
    @property
    def Actions(self) -> List[IGH_UndoAction]: ...
    @property
    def ExpiresDisplay(self) -> bool: ...
    @property
    def ExpiresSolution(self) -> bool: ...
    @property
    def Guid(self) -> Guid: ...
    @property
    def Name(self) -> str: ...
    @property
    def State(self) -> GH_UndoState: ...
    @property
    def Time(self) -> DateTime: ...
    def Redo(self, doc: GH_Document) -> None: ...
    @Name.setter
    def Name(self, Value: str) -> None: ...
    def Undo(self, doc: GH_Document) -> None: ...


class GH_UndoServer:
    def __init__(self, owner: GH_Document): ...
    def AppendToDebugLog(self, writer: GH_DebugDescriptionWriter) -> None: ...
    def Clear(self) -> None: ...
    def ClearRedo(self) -> None: ...
    def ClearUndo(self) -> None: ...
    @property
    def FirstRedoName(self) -> str: ...
    @property
    def FirstUndoName(self) -> str: ...
    @property
    def MaxRecords(self) -> int: ...
    @property
    def RedoCount(self) -> int: ...
    @property
    def RedoGuids(self) -> List: ...
    @property
    def RedoNames(self) -> List: ...
    @property
    def UndoCount(self) -> int: ...
    @property
    def UndoGuids(self) -> List: ...
    @property
    def UndoNames(self) -> List: ...
    def MergeRecords(self, count: int) -> bool: ...
    def PerformRedo(self) -> None: ...
    def PerformUndo(self) -> None: ...
    @overload
    def PushUndoRecord(self, record: GH_UndoRecord) -> None: ...
    @overload
    def PushUndoRecord(self, name: str, action: GH_UndoAction) -> Guid: ...
    def RemoveRecord(self, id: Guid) -> bool: ...
    @MaxRecords.setter
    def MaxRecords(self, Value: int) -> None: ...


class GH_UndoState:
    undo = 0
    redo = 1


class IGH_UndoAction:
    @property
    def ExpiresDisplay(self) -> bool: ...
    @property
    def ExpiresSolution(self) -> bool: ...
    @property
    def State(self) -> GH_UndoState: ...
    def Redo(self, doc: GH_Document) -> None: ...
    def Undo(self, doc: GH_Document) -> None: ...

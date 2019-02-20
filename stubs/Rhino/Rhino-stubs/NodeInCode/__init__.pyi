from typing import Tuple, Set, Iterable, List

class Components:
    @property
    def NodeInCodeFunctions () -> NodeInCodeTable: ...
    def FindComponent (fullName : str) -> ComponentFunctionInfo: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ComponentFunctionInfo:
    @property
    def Name (self) -> str: ...
    @property
    def Namespace (self) -> str: ...
    @property
    def IsDefault (self) -> bool: ...
    @property
    def Description (self) -> str: ...
    @property
    def InputNames (self) -> IReadOnlyList: ...
    @property
    def InputDescriptions (self) -> IReadOnlyList: ...
    @property
    def InputTypeNames (self) -> IReadOnlyList: ...
    @property
    def InputsOptional (self) -> IReadOnlyList: ...
    @property
    def OutputNames (self) -> IReadOnlyList: ...
    @property
    def OutputDescriptions (self) -> IReadOnlyList: ...
    @property
    def OutputTypeNames (self) -> IReadOnlyList: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def ToString (self) -> str: ...
    @property
    def FullName (self) -> str: ...
    @property
    def FullScriptingName (self) -> str: ...
    def Evaluate (self, args : IEnumerable, keepTree : bool) -> Tuple[Set(Object), Set(str)]: ...
    def Invoke (self, args : Set(Object)) -> Set(Object): ...
    def InvokeSilenceWarnings (self, args : Set(Object)) -> Set(Object): ...
    def InvokeKeepTree (self, args : Set(Object)) -> Set(Object): ...
    def InvokeKeepTreeSilenceWarnings (self, args : Set(Object)) -> Set(Object): ...
    @property
    def Delegate (self) -> Delegate: ...
    @property
    def DelegateNoWarnings (self) -> Delegate: ...
    @property
    def DelegateTree (self) -> Delegate: ...
    @property
    def DelegateTreeNoWarnings (self) -> Delegate: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class NodeInCodeTable:
    def __init__(self, items : Iterable[ComponentFunctionInfo]): ...
    @property
    def Count (self) -> int: ...
    def Add (self, item : ComponentFunctionInfo) -> None: ...
    def TryGetMember (self, binder : GetMemberBinder) -> Tuple[bool, Object]: ...
    def GetDynamicMemberNames (self) -> Iterable[str]: ...
    def TryInvokeMember (self, binder : InvokeMemberBinder, args : Set(Object)) -> Tuple[bool, Object]: ...
    def TryGetIndex (self, binder : GetIndexBinder, indexes : Set(Object)) -> Tuple[bool, Object]: ...
    def TrySetMember (self, binder : SetMemberBinder, value : Object) -> bool: ...
    def TryDeleteMember (self, binder : DeleteMemberBinder) -> bool: ...
    def TryConvert (self, binder : ConvertBinder) -> Tuple[bool, Object]: ...
    def TryCreateInstance (self, binder : CreateInstanceBinder, args : Set(Object)) -> Tuple[bool, Object]: ...
    def TryInvoke (self, binder : InvokeBinder, args : Set(Object)) -> Tuple[bool, Object]: ...
    def TryBinaryOperation (self, binder : BinaryOperationBinder, arg : Object) -> Tuple[bool, Object]: ...
    def TryUnaryOperation (self, binder : UnaryOperationBinder) -> Tuple[bool, Object]: ...
    def TrySetIndex (self, binder : SetIndexBinder, indexes : Set(Object), value : Object) -> bool: ...
    def TryDeleteIndex (self, binder : DeleteIndexBinder, indexes : Set(Object)) -> bool: ...
    def GetMetaObject (self, parameter : Expression) -> DynamicMetaObject: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...

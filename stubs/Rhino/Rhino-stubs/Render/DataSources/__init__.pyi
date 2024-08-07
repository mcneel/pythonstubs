from typing import Tuple, Set, Iterable, List, overload


class AssignBys:
    Unset = 0
    Layer = 1
    Parent = 2
    Object = 3
    Varies = 4
    PlugIn = 5


class ContentFactories:
    def __init__(self, pRdkContentFactories: IntPtr): ...
    def Dispose(self) -> None: ...
    def FindFactory(self, uuid: Guid) -> ContentFactory: ...
    def FirstFactory(self) -> ContentFactory: ...
    @property
    def CppPointer(self) -> IntPtr: ...
    def NextFactory(self) -> ContentFactory: ...


class ContentFactory:
    def __init__(self, pRdkContentFactory: IntPtr): ...
    def ContentTypeId(self) -> Guid: ...
    def Dispose(self) -> None: ...
    @property
    def CppPointer(self) -> IntPtr: ...
    def Kind(self) -> RenderContentKind: ...
    def NewContent(self) -> RenderContent: ...


class MetaData:
    def __init__(self, pMetaData: IntPtr): ...
    def ContentInstanceId(self) -> Guid: ...
    def Dispose(self) -> None: ...
    def Geometry(self) -> str: ...
    @property
    def CppPointer(self) -> IntPtr: ...


class Modes:
    Unset = 0
    Grid = 1
    List = 2
    Tree = 3


class RdkEdit:
    def __init__(self, pRdkEdit: IntPtr): ...
    def Dispose(self) -> None: ...
    def Execute(self, collection: RenderContentCollection) -> bool: ...
    @property
    def CppPointer(self) -> IntPtr: ...


class RdkSelectionNavigator:
    def __init__(self, pRhinoSettings: IntPtr): ...
    def Add(self, selectedContentArray: RenderContentCollection) -> None: ...
    def CanGoBackwards(self) -> bool: ...
    def CanGoForwards(self) -> bool: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    @property
    def CppPointer(self) -> IntPtr: ...
    def GoBackwards(self, selectedContentArray: RenderContentCollection) -> Tuple[bool, RenderContentCollection]: ...
    def GoForwards(self, selectedContentArray: RenderContentCollection) -> Tuple[bool, RenderContentCollection]: ...


class RhinoSettings:
    def __init__(self, pRhinoSettings: IntPtr): ...
    def ActiveView(self) -> RhinoView: ...
    def Dispose(self) -> None: ...
    @property
    def CppPointer(self) -> IntPtr: ...
    @property
    def CustomImageSizeIsPreset(self) -> bool: ...
    def GetCustomRenderSizes(self) -> List: ...
    def GetRenderSettings(self) -> RenderSettings: ...
    def GroundPlaneOnInViewDisplayMode(self, view: RhinoView) -> bool: ...
    def RenderingView(self) -> ViewInfo: ...
    @CustomImageSizeIsPreset.setter
    def CustomImageSizeIsPreset(self, value: bool) -> None: ...
    def SetGroundPlaneOnInViewDisplayMode(self, view: RhinoView, bOn: bool) -> None: ...
    def SetRenderSettings(self, renderSettings: RenderSettings) -> None: ...
    def ViewSupportsShading(self, view: RhinoView) -> bool: ...


class Shapes:
    Square = 0
    Wide = 1


class Sizes:
    Unset = 0
    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4

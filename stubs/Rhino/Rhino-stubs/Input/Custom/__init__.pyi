from typing import Tuple, Set, Iterable, List, overload


class CommandLineOption:
    @property
    def CurrentListOptionIndex(self) -> int: ...
    @property
    def EnglishName(self) -> str: ...
    @property
    def Index(self) -> int: ...
    @property
    def LocalName(self) -> str: ...
    @property
    def StringOptionValue(self) -> str: ...
    def IsValidOptionName(optionName: str) -> bool: ...
    def IsValidOptionValueName(optionValue: str) -> bool: ...


class ConeConstraint:
    #None = 0
    Vertical = 1
    AroundCurve = 2


class CylinderConstraint:
    #None = 0
    Vertical = 1
    AroundCurve = 2


class GeometryAttributeFilter:
    WireCurve = 1
    EdgeCurve = 2
    ClosedCurve = 4
    OpenCurve = 8
    SeamEdge = 16
    ManifoldEdge = 32
    NonmanifoldEdge = 64
    MatedEdge = 112
    SurfaceBoundaryEdge = 128
    TrimmingBoundaryEdge = 256
    BoundaryEdge = 384
    ClosedSurface = 512
    OpenSurface = 1024
    TrimmedSurface = 2048
    UntrimmedSurface = 4096
    SubSurface = 8192
    TopSurface = 16384
    ManifoldPolysrf = 32768
    NonmanifoldPolysrf = 65536
    ClosedPolysrf = 131072
    OpenPolysrf = 262144
    ClosedMesh = 524288
    OpenMesh = 1048576
    BoundaryInnerLoop = 2097152
    MatedInnerLoop = 4194304
    InnerLoop = 6291456
    BoundaryOuterLoop = 8388608
    MatedOuterLoop = 16777216
    OuterLoop = 25165824
    SpecialLoop = 33554432
    AcceptAllAttributes = 4294967295


class GetArc:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def AllowDeformable(self) -> bool: ...
    @property
    def DefaultRadius(self) -> float: ...
    @property
    def Deformable(self) -> bool: ...
    @property
    def DeformableDegree(self) -> int: ...
    @property
    def DeformablePointCount(self) -> int: ...
    def Get(self) -> Tuple[Result, Arc]: ...
    @AllowDeformable.setter
    def AllowDeformable(self, value: bool) -> None: ...
    @DefaultRadius.setter
    def DefaultRadius(self, value: float) -> None: ...
    @Deformable.setter
    def Deformable(self, value: bool) -> None: ...
    @DeformableDegree.setter
    def DeformableDegree(self, value: int) -> None: ...
    @DeformablePointCount.setter
    def DeformablePointCount(self, value: int) -> None: ...


class GetBaseClass:
    def AcceptColor(self, enable: bool) -> None: ...
    def AcceptCustomMessage(self, enable: bool) -> None: ...
    def AcceptEnterWhenDone(self, enable: bool) -> None: ...
    def AcceptNothing(self, enable: bool) -> None: ...
    def AcceptNumber(self, enable: bool, acceptZero: bool) -> None: ...
    def AcceptPoint(self, enable: bool) -> None: ...
    def AcceptString(self, enable: bool) -> None: ...
    def AcceptUndo(self, enable: bool) -> None: ...
    @overload
    def AddOption(self, englishOption: str) -> int: ...
    @overload
    def AddOption(self, optionName: LocalizeStringPair) -> int: ...
    @overload
    def AddOption(self, englishOption: str, englishOptionValue: str) -> int: ...
    @overload
    def AddOption(self, optionName: LocalizeStringPair, optionValue: LocalizeStringPair) -> int: ...
    @overload
    def AddOption(self, optionName: LocalizeStringPair, optionValue: LocalizeStringPair, hiddenOption: bool) -> int: ...
    @overload
    def AddOption(self, englishOption: str, englishOptionValue: str, hiddenOption: bool) -> int: ...
    @overload
    def AddOptionColor(self, englishName: str, colorValue: OptionColor) -> Tuple[int, OptionColor]: ...
    @overload
    def AddOptionColor(self, optionName: LocalizeStringPair, colorValue: OptionColor) -> Tuple[int, OptionColor]: ...
    @overload
    def AddOptionColor(self, optionName: LocalizeStringPair, colorValue: OptionColor, prompt: str) -> Tuple[int, OptionColor]: ...
    @overload
    def AddOptionColor(self, englishName: str, colorValue: OptionColor, prompt: str) -> Tuple[int, OptionColor]: ...
    @overload
    def AddOptionDouble(self, englishName: str, numberValue: OptionDouble) -> Tuple[int, OptionDouble]: ...
    @overload
    def AddOptionDouble(self, optionName: LocalizeStringPair, numberValue: OptionDouble) -> Tuple[int, OptionDouble]: ...
    @overload
    def AddOptionDouble(self, englishName: str, numberValue: OptionDouble, prompt: str) -> Tuple[int, OptionDouble]: ...
    @overload
    def AddOptionDouble(self, optionName: LocalizeStringPair, numberValue: OptionDouble, prompt: str) -> Tuple[int, OptionDouble]: ...
    @overload
    def AddOptionEnumList(self, englishOptionName: str, defaultValue: T) -> int: ...
    @overload
    def AddOptionEnumList(self, englishOptionName: str, defaultValue: T, include: Set(T)) -> int: ...
    def AddOptionEnumSelectionList(self, englishOptionName: str, enumSelection: Iterable[T], listCurrentIndex: int) -> int: ...
    @overload
    def AddOptionInteger(self, englishName: str, intValue: OptionInteger) -> Tuple[int, OptionInteger]: ...
    @overload
    def AddOptionInteger(self, optionName: LocalizeStringPair, intValue: OptionInteger) -> Tuple[int, OptionInteger]: ...
    @overload
    def AddOptionInteger(self, englishName: str, intValue: OptionInteger, prompt: str) -> Tuple[int, OptionInteger]: ...
    @overload
    def AddOptionInteger(self, optionName: LocalizeStringPair, intValue: OptionInteger, prompt: str) -> Tuple[int, OptionInteger]: ...
    @overload
    def AddOptionList(self, englishOptionName: str, listValues: Iterable[str], listCurrentIndex: int) -> int: ...
    @overload
    def AddOptionList(self, optionName: LocalizeStringPair, listValues: Iterable[LocalizeStringPair], listCurrentIndex: int) -> int: ...
    @overload
    def AddOptionToggle(self, englishName: str, toggleValue: OptionToggle) -> Tuple[int, OptionToggle]: ...
    @overload
    def AddOptionToggle(self, optionName: LocalizeStringPair, toggleValue: OptionToggle) -> Tuple[int, OptionToggle]: ...
    def ClearCommandOptions(self) -> None: ...
    def ClearDefault(self) -> None: ...
    def Color(self) -> Color: ...
    def CommandResult(self) -> Result: ...
    def CustomMessage(self) -> Object: ...
    def Dispose(self) -> None: ...
    def EnableTransparentCommands(self, enable: bool) -> None: ...
    def GetSelectedEnumValue(self) -> T: ...
    def GetSelectedEnumValueFromSelectionList(self, selectionList: Iterable[T]) -> T: ...
    def GotDefault(self) -> bool: ...
    def Line2d(self) -> Set(Point): ...
    def Number(self) -> float: ...
    def Option(self) -> CommandLineOption: ...
    def OptionIndex(self) -> int: ...
    def PickRectangle(self) -> Rectangle: ...
    def Point(self) -> Point3d: ...
    def Point2d(self) -> Point: ...
    def PostCustomMessage(messageData: Object) -> None: ...
    def Rectangle2d(self) -> Rectangle: ...
    def Result(self) -> GetResult: ...
    def SetCommandPrompt(self, prompt: str) -> None: ...
    def SetCommandPromptDefault(self, defaultValue: str) -> None: ...
    def SetDefaultColor(self, defaultColor: Color) -> None: ...
    def SetDefaultInteger(self, defaultValue: int) -> None: ...
    def SetDefaultNumber(self, defaultNumber: float) -> None: ...
    def SetDefaultPoint(self, point: Point3d) -> None: ...
    def SetDefaultString(self, defaultValue: str) -> None: ...
    def SetWaitDuration(self, milliseconds: int) -> None: ...
    def StringResult(self) -> str: ...
    def Vector(self) -> Vector3d: ...
    def View(self) -> RhinoView: ...


class GetCancel(GetBaseClass):
    def __init__(self): ...
    def add_TaskCompleted(self, value: EventHandler) -> None: ...
    @property
    def Progress(self) -> IProgress: ...
    @property
    def ProgressMessage(self) -> str: ...
    @property
    def ProgressReporting(self) -> bool: ...
    @property
    def Token(self) -> CancellationToken: ...
    def remove_TaskCompleted(self, value: EventHandler) -> None: ...
    @ProgressMessage.setter
    def ProgressMessage(self, value: str) -> None: ...
    @ProgressReporting.setter
    def ProgressReporting(self, value: bool) -> None: ...
    @overload
    def Wait(self, task: Task, doc: RhinoDoc) -> Result: ...
    @overload
    def Wait(self, task: Task, doc: RhinoDoc) -> Result: ...
    @overload
    def WaitAll(self, tasks: Iterable[Task], doc: RhinoDoc) -> Result: ...
    @overload
    def WaitAll(self, tasks: Iterable[Task], doc: RhinoDoc) -> Result: ...


class GetCircle:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def AllowDeformable(self) -> bool: ...
    @property
    def DefaultSize(self) -> float: ...
    @property
    def Deformable(self) -> bool: ...
    @property
    def DeformableDegree(self) -> int: ...
    @property
    def DeformablePointCount(self) -> int: ...
    @property
    def InDiameterMode(self) -> bool: ...
    def Get(self) -> Tuple[Result, Circle]: ...
    @AllowDeformable.setter
    def AllowDeformable(self, value: bool) -> None: ...
    @DefaultSize.setter
    def DefaultSize(self, value: float) -> None: ...
    @Deformable.setter
    def Deformable(self, value: bool) -> None: ...
    @DeformableDegree.setter
    def DeformableDegree(self, value: int) -> None: ...
    @DeformablePointCount.setter
    def DeformablePointCount(self, value: int) -> None: ...
    @InDiameterMode.setter
    def InDiameterMode(self, value: bool) -> None: ...


class GetCone:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def AllowInputAngle(self) -> bool: ...
    @property
    def ApexAngleDegrees(self) -> float: ...
    @property
    def BaseAngleDegrees(self) -> float: ...
    @property
    def Cap(self) -> bool: ...
    @property
    def ConeConstraint(self) -> ConeConstraint: ...
    @property
    def DefaultSize(self) -> float: ...
    @property
    def Height(self) -> float: ...
    @property
    def InDiameterMode(self) -> bool: ...
    def Get(self) -> Tuple[Result, Cone]: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int) -> Tuple[Result, int, int, Cone]: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int, capStyle: int) -> Tuple[Result, int, int, int, Cone]: ...
    @AllowInputAngle.setter
    def AllowInputAngle(self, value: bool) -> None: ...
    @ApexAngleDegrees.setter
    def ApexAngleDegrees(self, value: float) -> None: ...
    @BaseAngleDegrees.setter
    def BaseAngleDegrees(self, value: float) -> None: ...
    @Cap.setter
    def Cap(self, value: bool) -> None: ...
    @ConeConstraint.setter
    def ConeConstraint(self, value: ConeConstraint) -> None: ...
    @DefaultSize.setter
    def DefaultSize(self, value: float) -> None: ...
    @Height.setter
    def Height(self, value: float) -> None: ...
    @InDiameterMode.setter
    def InDiameterMode(self, value: bool) -> None: ...


class GetCylinder:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def BothSidesOption(self) -> bool: ...
    @property
    def Cap(self) -> bool: ...
    @property
    def CylinderConstraint(self) -> CylinderConstraint: ...
    @property
    def DefaultSize(self) -> float: ...
    @property
    def Height(self) -> float: ...
    @property
    def InDiameterMode(self) -> bool: ...
    def Get(self) -> Tuple[Result, Cylinder]: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int) -> Tuple[Result, int, int, Cylinder]: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int, capStyle: int) -> Tuple[Result, int, int, int, Cylinder]: ...
    @BothSidesOption.setter
    def BothSidesOption(self, value: bool) -> None: ...
    @Cap.setter
    def Cap(self, value: bool) -> None: ...
    @CylinderConstraint.setter
    def CylinderConstraint(self, value: CylinderConstraint) -> None: ...
    @DefaultSize.setter
    def DefaultSize(self, value: float) -> None: ...
    @Height.setter
    def Height(self, value: float) -> None: ...
    @InDiameterMode.setter
    def InDiameterMode(self, value: bool) -> None: ...


class GetEllipsoid:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def FirstPoint(self) -> Point3d: ...
    @property
    def IsModeFromFoci(self) -> bool: ...
    @property
    def MarkFoci(self) -> bool: ...
    def Get(self) -> Tuple[Result, NurbsSurface]: ...
    @property
    def SecondPoint(self) -> Point3d: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int) -> Tuple[Result, int, int, Mesh]: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int, quadCaps: bool) -> Tuple[Result, int, int, bool, Mesh]: ...
    @MarkFoci.setter
    def MarkFoci(self, value: bool) -> None: ...


class GetFileNameMode:
    Open = 0
    OpenTemplate = 1
    OpenImage = 2
    OpenRhinoOnly = 3
    OpenTextFile = 5
    OpenWorksession = 6
    Import = 7
    Attach = 8
    LoadPlugIn = 9
    Save = 10
    SaveSmall = 11
    SaveTemplate = 12
    SaveImage = 13
    Export = 14
    SaveTextFile = 17
    SaveWorksession = 18


class GetInteger(GetBaseClass):
    def __init__(self): ...
    def Get(self) -> GetResult: ...
    @overload
    def Number(self) -> int: ...
    def SetLowerLimit(self, lowerLimit: int, strictlyGreaterThan: bool) -> None: ...
    def SetUpperLimit(self, upperLimit: int, strictlyLessThan: bool) -> None: ...


class GetLine:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    def EnableAllVariations(self, on: bool) -> None: ...
    def EnableFromBothSidesOption(self, on: bool) -> None: ...
    def EnableFromMidPointOption(self, on: bool) -> None: ...
    @property
    def AcceptZeroLengthLine(self) -> bool: ...
    @property
    def FeedbackColor(self) -> Color: ...
    @property
    def FirstPointPrompt(self) -> str: ...
    @property
    def FixedLength(self) -> float: ...
    @property
    def GetLineMode(self) -> GetLineMode: ...
    @property
    def HaveFeedbackColor(self) -> bool: ...
    @property
    def MidPointPrompt(self) -> str: ...
    def Get(self) -> Tuple[Result, Line]: ...
    @property
    def SecondPointPrompt(self) -> str: ...
    @AcceptZeroLengthLine.setter
    def AcceptZeroLengthLine(self, value: bool) -> None: ...
    @FeedbackColor.setter
    def FeedbackColor(self, value: Color) -> None: ...
    @FirstPointPrompt.setter
    def FirstPointPrompt(self, value: str) -> None: ...
    @FixedLength.setter
    def FixedLength(self, value: float) -> None: ...
    @GetLineMode.setter
    def GetLineMode(self, value: GetLineMode) -> None: ...
    @MidPointPrompt.setter
    def MidPointPrompt(self, value: str) -> None: ...
    @SecondPointPrompt.setter
    def SecondPointPrompt(self, value: str) -> None: ...
    def SetFirstPoint(self, point: Point3d) -> None: ...


class GetLineMode:
    TwoPoint = 0
    SurfaceNormal = 1
    Angled = 2
    Vertical = 3
    FourPoint = 4
    Bisector = 5
    Perpendicular = 6
    Tangent = 7
    CurveEnd = 8
    CPlaneNormalVector = 9


class GetNumber(GetBaseClass):
    def __init__(self): ...
    def Get(self) -> GetResult: ...
    def SetLowerLimit(self, lowerLimit: float, strictlyGreaterThan: bool) -> None: ...
    def SetUpperLimit(self, upperLimit: float, strictlyLessThan: bool) -> None: ...


class GetObject(GetBaseClass):
    def __init__(self): ...
    def ActiveGetObject(doc: RhinoDoc) -> GetObject: ...
    def AppendToPickList(self, objref: ObjRef) -> None: ...
    def ClearObjects(self) -> None: ...
    def CustomGeometryFilter(self, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex) -> bool: ...
    def DisablePreSelect(self) -> None: ...
    def EnableClearObjectsOnEntry(self, enable: bool) -> None: ...
    def EnableHighlight(self, enable: bool) -> None: ...
    def EnableIgnoreGrips(self, enable: bool) -> None: ...
    def EnablePostSelect(self, enable: bool) -> None: ...
    def EnablePreSelect(self, enable: bool, ignoreUnacceptablePreselectedObjects: bool) -> None: ...
    def EnablePressEnterWhenDonePrompt(self, enable: bool) -> None: ...
    def EnableSelPrevious(self, enable: bool) -> None: ...
    def EnableUnselectObjectsOnExit(self, enable: bool) -> None: ...
    def Get(self) -> GetResult: ...
    @property
    def AlreadySelectedObjectSelect(self) -> bool: ...
    @property
    def BottomObjectPreference(self) -> bool: ...
    @property
    def ChooseOneQuestion(self) -> bool: ...
    @property
    def DeselectAllBeforePostSelect(self) -> bool: ...
    @property
    def GeometryAttributeFilter(self) -> GeometryAttributeFilter: ...
    @property
    def GeometryFilter(self) -> ObjectType: ...
    @property
    def GroupSelect(self) -> bool: ...
    @property
    def InactiveDetailPickEnabled(self) -> bool: ...
    @property
    def ObjectCount(self) -> int: ...
    @property
    def ObjectsWerePreselected(self) -> bool: ...
    @property
    def OneByOnePostSelect(self) -> bool: ...
    @property
    def ProxyBrepFromSubD(self) -> bool: ...
    @property
    def ReferenceObjectSelect(self) -> bool: ...
    @property
    def SerialNumber(self) -> UInt32: ...
    @property
    def SubObjectSelect(self) -> bool: ...
    def GetMultiple(self, minimumNumber: int, maximumNumber: int) -> GetResult: ...
    def Object(self, index: int) -> ObjRef: ...
    def Objects(self) -> Set(ObjRef): ...
    def PassesGeometryAttributeFilter(self, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex) -> bool: ...
    @AlreadySelectedObjectSelect.setter
    def AlreadySelectedObjectSelect(self, value: bool) -> None: ...
    @BottomObjectPreference.setter
    def BottomObjectPreference(self, value: bool) -> None: ...
    @ChooseOneQuestion.setter
    def ChooseOneQuestion(self, value: bool) -> None: ...
    @DeselectAllBeforePostSelect.setter
    def DeselectAllBeforePostSelect(self, value: bool) -> None: ...
    @GeometryAttributeFilter.setter
    def GeometryAttributeFilter(self, value: GeometryAttributeFilter) -> None: ...
    @GeometryFilter.setter
    def GeometryFilter(self, value: ObjectType) -> None: ...
    @GroupSelect.setter
    def GroupSelect(self, value: bool) -> None: ...
    @InactiveDetailPickEnabled.setter
    def InactiveDetailPickEnabled(self, value: bool) -> None: ...
    @OneByOnePostSelect.setter
    def OneByOnePostSelect(self, value: bool) -> None: ...
    @ProxyBrepFromSubD.setter
    def ProxyBrepFromSubD(self, value: bool) -> None: ...
    @ReferenceObjectSelect.setter
    def ReferenceObjectSelect(self, value: bool) -> None: ...
    @SubObjectSelect.setter
    def SubObjectSelect(self, value: bool) -> None: ...
    def SetCustomGeometryFilter(self, filter: GetObjectGeometryFilter) -> None: ...
    def SetPressEnterWhenDonePrompt(self, prompt: str) -> None: ...


class GetObjectGeometryFilter:
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> bool: ...
    def Invoke(self, rhObject: RhinoObject, geometry: GeometryBase, componentIndex: ComponentIndex) -> bool: ...


class GetOption(GetBaseClass):
    def __init__(self): ...
    def Get(self) -> GetResult: ...


class GetPoint(GetBaseClass):
    def __init__(self): ...
    def add_DynamicDraw(self, value: EventHandler) -> None: ...
    def add_MouseDown(self, value: EventHandler) -> None: ...
    def add_MouseMove(self, value: EventHandler) -> None: ...
    def add_PostDrawObjects(self, value: EventHandler) -> None: ...
    def AddConstructionPoint(self, point: Point3d) -> int: ...
    def AddConstructionPoints(self, points: Set(Point3d)) -> int: ...
    def AddSnapPoint(self, point: Point3d) -> int: ...
    def AddSnapPoints(self, points: Set(Point3d)) -> int: ...
    def ClearConstraints(self) -> None: ...
    def ClearConstructionPoints(self) -> None: ...
    def ClearSnapPoints(self) -> None: ...
    @overload
    def Constrain(self, circle: Circle) -> bool: ...
    @overload
    def Constrain(self, line: Line) -> bool: ...
    @overload
    def Constrain(self, arc: Arc) -> bool: ...
    @overload
    def Constrain(self, cylinder: Cylinder) -> bool: ...
    @overload
    def Constrain(self, sphere: Sphere) -> bool: ...
    @overload
    def Constrain(self, mesh: Mesh, allowPickingPointOffObject: bool) -> bool: ...
    @overload
    def Constrain(self, from_: Point3d, to: Point3d) -> bool: ...
    @overload
    def Constrain(self, surface: Surface, allowPickingPointOffObject: bool) -> bool: ...
    @overload
    def Constrain(self, curve: Curve, allowPickingPointOffObject: bool) -> bool: ...
    @overload
    def Constrain(self, plane: Plane, allowElevator: bool) -> bool: ...
    @overload
    def Constrain(self, brep: Brep, wireDensity: int, faceIndex: int, allowPickingPointOffObject: bool) -> bool: ...
    def ConstrainDistanceFromBasePoint(self, distance: float) -> None: ...
    def ConstrainToConstructionPlane(self, throughBasePoint: bool) -> bool: ...
    def ConstrainToTargetPlane(self) -> None: ...
    def ConstrainToVirtualCPlaneIntersection(self, plane: Plane) -> bool: ...
    def DrawLineFromPoint(self, startPoint: Point3d, showDistanceInStatusBar: bool) -> None: ...
    def EnableCurveSnapArrow(self, drawDirectionArrowAtSnapPoint: bool, reverseArrow: bool) -> None: ...
    def EnableCurveSnapPerpBar(self, drawPerpBarAtSnapPoint: bool, drawEndPoints: bool) -> None: ...
    def EnableCurveSnapTangentBar(self, drawTangentBarAtSnapPoint: bool, drawEndPoints: bool) -> None: ...
    def EnableDrawLineFromPoint(self, enable: bool) -> None: ...
    def EnableNoRedrawOnExit(self, noRedraw: bool) -> None: ...
    def EnableObjectSnapCursors(self, enable: bool) -> None: ...
    def EnableSnapToCurves(self, enable: bool) -> None: ...
    @overload
    def Get(self) -> GetResult: ...
    @property
    def DynamicDrawColor(self) -> Color: ...
    @property
    def FullFrameRedrawDuringGet(self) -> bool: ...
    @property
    def OsnapEventType(self) -> OsnapModes: ...
    @overload
    def Get(self, onMouseUp: bool) -> GetResult: ...
    @overload
    def Get(self, onMouseUp: bool, get2DPoint: bool) -> GetResult: ...
    @property
    def Tag(self) -> Object: ...
    def GetConstructionPoints(self) -> Set(Point3d): ...
    def GetPlanarConstraint(self, vp: RhinoViewport) -> Tuple[bool, RhinoViewport, Plane]: ...
    def GetSnapPoints(self) -> Set(Point3d): ...
    def InterruptMouseMove(self) -> bool: ...
    def PermitConstraintOptions(self, permit: bool) -> None: ...
    def PermitElevatorMode(self, permitMode: int) -> None: ...
    def PermitFromOption(self, permit: bool) -> None: ...
    def PermitObjectSnap(self, permit: bool) -> None: ...
    def PermitOrthoSnap(self, permit: bool) -> None: ...
    def PermitTabMode(self, permit: bool) -> None: ...
    def PointOnBrep(self) -> Tuple[BrepFace, float, float]: ...
    def PointOnCurve(self) -> Tuple[Curve, float]: ...
    def PointOnObject(self) -> ObjRef: ...
    def PointOnSurface(self) -> Tuple[Surface, float, float]: ...
    def remove_DynamicDraw(self, value: EventHandler) -> None: ...
    def remove_MouseDown(self, value: EventHandler) -> None: ...
    def remove_MouseMove(self, value: EventHandler) -> None: ...
    def remove_PostDrawObjects(self, value: EventHandler) -> None: ...
    @DynamicDrawColor.setter
    def DynamicDrawColor(self, value: Color) -> None: ...
    @FullFrameRedrawDuringGet.setter
    def FullFrameRedrawDuringGet(self, value: bool) -> None: ...
    @Tag.setter
    def Tag(self, value: Object) -> None: ...
    def SetBasePoint(self, basePoint: Point3d, showDistanceInStatusBar: bool) -> None: ...
    def SetCursor(self, cursor: CursorStyle) -> None: ...
    def TryGetBasePoint(self) -> Tuple[bool, Point3d]: ...


class GetPointDrawEventArgs(DrawEventArgs):
    @property
    def CurrentPoint(self) -> Point3d: ...
    @property
    def Source(self) -> GetPoint: ...


class GetPointMouseEventArgs:
    @property
    def ControlKeyDown(self) -> bool: ...
    @property
    def LeftButtonDown(self) -> bool: ...
    @property
    def MiddleButtonDown(self) -> bool: ...
    @property
    def Point(self) -> Point3d: ...
    @property
    def RightButtonDown(self) -> bool: ...
    @property
    def ShiftKeyDown(self) -> bool: ...
    @property
    def Source(self) -> GetPoint: ...
    @property
    def Viewport(self) -> RhinoViewport: ...
    @property
    def WindowPoint(self) -> Point: ...


class GetPolyline:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def FirstPointPrompt(self) -> str: ...
    @property
    def FourthPointPrompt(self) -> str: ...
    @property
    def MaxPointCount(self) -> int: ...
    @property
    def MinPointCount(self) -> int: ...
    def Get(self) -> Tuple[Result, Polyline]: ...
    @property
    def SecondPointPrompt(self) -> str: ...
    @property
    def ThirdPointPrompt(self) -> str: ...
    @FirstPointPrompt.setter
    def FirstPointPrompt(self, value: str) -> None: ...
    @FourthPointPrompt.setter
    def FourthPointPrompt(self, value: str) -> None: ...
    @MaxPointCount.setter
    def MaxPointCount(self, value: int) -> None: ...
    @MinPointCount.setter
    def MinPointCount(self, value: int) -> None: ...
    @SecondPointPrompt.setter
    def SecondPointPrompt(self, value: str) -> None: ...
    @ThirdPointPrompt.setter
    def ThirdPointPrompt(self, value: str) -> None: ...
    def SetFirstPoint(self, point: Point3d) -> None: ...


class GetSphere:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def DefaultSize(self) -> float: ...
    @property
    def InDiameterMode(self) -> bool: ...
    def Get(self) -> Tuple[Result, Sphere]: ...
    def GetMesh(self, style: MeshSphereStyle, verticalFaces: int, aroundFaces: int, triangleSubdivisions: int, quadSubdivisions: int) -> Tuple[Result, MeshSphereStyle, int, int, int, int, Sphere]: ...
    @DefaultSize.setter
    def DefaultSize(self, value: float) -> None: ...
    @InDiameterMode.setter
    def InDiameterMode(self, value: bool) -> None: ...


class GetString(GetBaseClass):
    def __init__(self): ...
    def Get(self) -> GetResult: ...
    def GetLiteralString(self) -> GetResult: ...


class GetTorus:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def AroundDirectionCount(self) -> int: ...
    @property
    def AroundDirectionMinimumCount(self) -> int: ...
    @property
    def DefaultSize(self) -> float: ...
    @property
    def FixInnerRadius(self) -> bool: ...
    @property
    def InDiameterMode(self) -> bool: ...
    @property
    def InSecondDiameterMode(self) -> bool: ...
    @property
    def PromptForMeshDensity(self) -> bool: ...
    def Get(self) -> Tuple[Result, Torus]: ...
    @property
    def SecondSize(self) -> float: ...
    @property
    def VerticalDirectionCount(self) -> int: ...
    @property
    def VerticalDirectionMinimumCount(self) -> int: ...
    def GetMesh(self, verticalFaces: int, aroundFaces: int) -> Tuple[Result, int, int, Torus]: ...
    @AroundDirectionCount.setter
    def AroundDirectionCount(self, value: int) -> None: ...
    @AroundDirectionMinimumCount.setter
    def AroundDirectionMinimumCount(self, value: int) -> None: ...
    @DefaultSize.setter
    def DefaultSize(self, value: float) -> None: ...
    @FixInnerRadius.setter
    def FixInnerRadius(self, value: bool) -> None: ...
    @InDiameterMode.setter
    def InDiameterMode(self, value: bool) -> None: ...
    @InSecondDiameterMode.setter
    def InSecondDiameterMode(self, value: bool) -> None: ...
    @PromptForMeshDensity.setter
    def PromptForMeshDensity(self, value: bool) -> None: ...
    @SecondSize.setter
    def SecondSize(self, value: float) -> None: ...
    @VerticalDirectionCount.setter
    def VerticalDirectionCount(self, value: int) -> None: ...
    @VerticalDirectionMinimumCount.setter
    def VerticalDirectionMinimumCount(self, value: int) -> None: ...


class GetTransform(GetPoint):
    def AddTransformObjects(self, list: TransformObjectList) -> None: ...
    def CalculateTransform(self, viewport: RhinoViewport, point: Point3d) -> Transform: ...
    @property
    def HaveTransform(self) -> bool: ...
    @property
    def ObjectList(self) -> TransformObjectList: ...
    @property
    def Transform(self) -> Transform: ...
    def GetXform(self) -> GetResult: ...
    @HaveTransform.setter
    def HaveTransform(self, value: bool) -> None: ...
    @Transform.setter
    def Transform(self, value: Transform) -> None: ...


class GetTruncatedCone:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def Cap(self) -> bool: ...
    @property
    def CylinderConstraint(self) -> CylinderConstraint: ...
    @property
    def DefaultSize(self) -> float: ...
    @property
    def Height(self) -> float: ...
    @property
    def InDiameterMode(self) -> bool: ...
    def Get(self) -> Tuple[Result, Brep]: ...
    @property
    def SecondRadius(self) -> float: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int) -> Tuple[Result, int, int, Mesh]: ...
    @overload
    def GetMesh(self, verticalFaces: int, aroundFaces: int, capStyle: int) -> Tuple[Result, int, int, int, Mesh]: ...
    @Cap.setter
    def Cap(self, value: bool) -> None: ...
    @CylinderConstraint.setter
    def CylinderConstraint(self, value: CylinderConstraint) -> None: ...
    @DefaultSize.setter
    def DefaultSize(self, value: float) -> None: ...
    @Height.setter
    def Height(self, value: float) -> None: ...
    @InDiameterMode.setter
    def InDiameterMode(self, value: bool) -> None: ...
    @SecondRadius.setter
    def SecondRadius(self, value: float) -> None: ...


class MeshHitFlag:
    Vertex = 0
    Edge = 1
    Face = 2
    Invalid = -1


class MeshPickStyle:
    WireframePicking = 0
    ShadedModePicking = 1
    VertexOnlyPicking = 2


class MeshSphereStyle:
    UV = 0
    Triangle = 1
    Quad = 2


class OptionColor:
    def __init__(self, initialValue: Color): ...
    def Dispose(self) -> None: ...
    @property
    def CurrentValue(self) -> Color: ...
    @property
    def InitialValue(self) -> Color: ...
    @CurrentValue.setter
    def CurrentValue(self, value: Color) -> None: ...


class OptionDouble:
    @overload
    def __init__(self, initialValue: float): ...
    @overload
    def __init__(self, initialValue: float, lowerLimit: float, upperLimit: float): ...
    @overload
    def __init__(self, initialValue: float, setLowerLimit: bool, limit: float): ...
    def Dispose(self) -> None: ...
    @property
    def CurrentValue(self) -> float: ...
    @property
    def InitialValue(self) -> float: ...
    @CurrentValue.setter
    def CurrentValue(self, value: float) -> None: ...


class OptionInteger:
    @overload
    def __init__(self, initialValue: int): ...
    @overload
    def __init__(self, initialValue: int, lowerLimit: int, upperLimit: int): ...
    @overload
    def __init__(self, initialValue: int, setLowerLimit: bool, limit: int): ...
    def Dispose(self) -> None: ...
    @property
    def CurrentValue(self) -> int: ...
    @property
    def InitialValue(self) -> int: ...
    @CurrentValue.setter
    def CurrentValue(self, value: int) -> None: ...


class OptionToggle:
    @overload
    def __init__(self, initialValue: bool, offValue: str, onValue: str): ...
    @overload
    def __init__(self, initialValue: bool, offValue: LocalizeStringPair, onValue: LocalizeStringPair): ...
    def Dispose(self) -> None: ...
    @property
    def CurrentValue(self) -> bool: ...
    @property
    def InitialValue(self) -> bool: ...
    @CurrentValue.setter
    def CurrentValue(self, value: bool) -> None: ...


class PickContext:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def GetObjectUsed(self) -> GetObject: ...
    @property
    def PickGroupsEnabled(self) -> bool: ...
    @property
    def PickLine(self) -> Line: ...
    @property
    def PickMode(self) -> PickMode: ...
    @property
    def PickStyle(self) -> PickStyle: ...
    @property
    def SubObjectSelectionEnabled(self) -> bool: ...
    @property
    def View(self) -> RhinoView: ...
    @overload
    def PickFrustumTest(self, box: BoundingBox) -> Tuple[bool, bool]: ...
    @overload
    def PickFrustumTest(self, point: Point3d) -> Tuple[bool, float, float]: ...
    @overload
    def PickFrustumTest(self, points: Set(Point3d)) -> Tuple[bool, int, float, float]: ...
    @overload
    def PickFrustumTest(self, cloud: PointCloud) -> Tuple[bool, int, float, float]: ...
    @overload
    def PickFrustumTest(self, line: Line) -> Tuple[bool, float, float, float]: ...
    @overload
    def PickFrustumTest(self, bezier: BezierCurve) -> Tuple[bool, float, float, float]: ...
    @overload
    def PickFrustumTest(self, curve: NurbsCurve) -> Tuple[bool, float, float, float]: ...
    @overload
    def PickFrustumTest(self, mesh: Mesh, pickStyle: MeshPickStyle) -> Tuple[bool, Point3d, float, float, MeshHitFlag, int]: ...
    @overload
    def PickFrustumTest(self, mesh: Mesh, pickStyle: MeshPickStyle) -> Tuple[bool, Point3d, Point2d, Point2d, float, float, MeshHitFlag, int]: ...
    def PickMeshTopologyVertices(self, mesh: Mesh) -> Set(int): ...
    @PickGroupsEnabled.setter
    def PickGroupsEnabled(self, value: bool) -> None: ...
    @PickLine.setter
    def PickLine(self, value: Line) -> None: ...
    @PickMode.setter
    def PickMode(self, value: PickMode) -> None: ...
    @PickStyle.setter
    def PickStyle(self, value: PickStyle) -> None: ...
    @SubObjectSelectionEnabled.setter
    def SubObjectSelectionEnabled(self, value: bool) -> None: ...
    @View.setter
    def View(self, value: RhinoView) -> None: ...
    def SetPickTransform(self, transform: Transform) -> None: ...
    def UpdateClippingPlanes(self) -> None: ...


class PickMode:
    Wireframe = 1
    Shaded = 2


class PickStyle:
    #None = 0
    PointPick = 1
    WindowPick = 2
    CrossingPick = 3


class TaskCompleteEventArgs:
    def __init__(self, task: Task, doc: RhinoDoc): ...
    @property
    def Doc(self) -> RhinoDoc: ...
    @property
    def Redraw(self) -> bool: ...
    @property
    def Task(self) -> Task: ...
    @Doc.setter
    def Doc(self, value: RhinoDoc) -> None: ...
    @Redraw.setter
    def Redraw(self, value: bool) -> None: ...
    @Task.setter
    def Task(self, value: Task) -> None: ...

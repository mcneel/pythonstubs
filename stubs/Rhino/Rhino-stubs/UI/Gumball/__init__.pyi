from typing import Tuple, Set, Iterable, List, overload


class GumballAppearanceSettings:
    def __init__(self): ...
    @property
    def ArcThickness(self) -> int: ...
    @property
    def ArrowHeadLength(self) -> int: ...
    @property
    def ArrowHeadWidth(self) -> int: ...
    @property
    def AxisThickness(self) -> int: ...
    @property
    def ColorMenuButton(self) -> Color: ...
    @property
    def ColorX(self) -> Color: ...
    @property
    def ColorY(self) -> Color: ...
    @property
    def ColorZ(self) -> Color: ...
    @property
    def FreeTranslate(self) -> int: ...
    @property
    def MenuDistance(self) -> int: ...
    @property
    def MenuEnabled(self) -> bool: ...
    @property
    def MenuSize(self) -> int: ...
    @property
    def PlanarTranslationGripCorner(self) -> int: ...
    @property
    def PlanarTranslationGripSize(self) -> int: ...
    @property
    def Radius(self) -> int: ...
    @property
    def RelocateEnabled(self) -> bool: ...
    @property
    def RotateXEnabled(self) -> bool: ...
    @property
    def RotateYEnabled(self) -> bool: ...
    @property
    def RotateZEnabled(self) -> bool: ...
    @property
    def ScaleGripSize(self) -> int: ...
    @property
    def ScaleXEnabled(self) -> bool: ...
    @property
    def ScaleYEnabled(self) -> bool: ...
    @property
    def ScaleZEnabled(self) -> bool: ...
    @property
    def TranslateXEnabled(self) -> bool: ...
    @property
    def TranslateXYEnabled(self) -> bool: ...
    @property
    def TranslateYEnabled(self) -> bool: ...
    @property
    def TranslateYZEnabled(self) -> bool: ...
    @property
    def TranslateZEnabled(self) -> bool: ...
    @property
    def TranslateZXEnabled(self) -> bool: ...
    @ArcThickness.setter
    def ArcThickness(self, value: int) -> None: ...
    @ArrowHeadLength.setter
    def ArrowHeadLength(self, value: int) -> None: ...
    @ArrowHeadWidth.setter
    def ArrowHeadWidth(self, value: int) -> None: ...
    @AxisThickness.setter
    def AxisThickness(self, value: int) -> None: ...
    @ColorMenuButton.setter
    def ColorMenuButton(self, value: Color) -> None: ...
    @ColorX.setter
    def ColorX(self, value: Color) -> None: ...
    @ColorY.setter
    def ColorY(self, value: Color) -> None: ...
    @ColorZ.setter
    def ColorZ(self, value: Color) -> None: ...
    @FreeTranslate.setter
    def FreeTranslate(self, value: int) -> None: ...
    @MenuDistance.setter
    def MenuDistance(self, value: int) -> None: ...
    @MenuEnabled.setter
    def MenuEnabled(self, value: bool) -> None: ...
    @MenuSize.setter
    def MenuSize(self, value: int) -> None: ...
    @PlanarTranslationGripCorner.setter
    def PlanarTranslationGripCorner(self, value: int) -> None: ...
    @PlanarTranslationGripSize.setter
    def PlanarTranslationGripSize(self, value: int) -> None: ...
    @Radius.setter
    def Radius(self, value: int) -> None: ...
    @RelocateEnabled.setter
    def RelocateEnabled(self, value: bool) -> None: ...
    @RotateXEnabled.setter
    def RotateXEnabled(self, value: bool) -> None: ...
    @RotateYEnabled.setter
    def RotateYEnabled(self, value: bool) -> None: ...
    @RotateZEnabled.setter
    def RotateZEnabled(self, value: bool) -> None: ...
    @ScaleGripSize.setter
    def ScaleGripSize(self, value: int) -> None: ...
    @ScaleXEnabled.setter
    def ScaleXEnabled(self, value: bool) -> None: ...
    @ScaleYEnabled.setter
    def ScaleYEnabled(self, value: bool) -> None: ...
    @ScaleZEnabled.setter
    def ScaleZEnabled(self, value: bool) -> None: ...
    @TranslateXEnabled.setter
    def TranslateXEnabled(self, value: bool) -> None: ...
    @TranslateXYEnabled.setter
    def TranslateXYEnabled(self, value: bool) -> None: ...
    @TranslateYEnabled.setter
    def TranslateYEnabled(self, value: bool) -> None: ...
    @TranslateYZEnabled.setter
    def TranslateYZEnabled(self, value: bool) -> None: ...
    @TranslateZEnabled.setter
    def TranslateZEnabled(self, value: bool) -> None: ...
    @TranslateZXEnabled.setter
    def TranslateZXEnabled(self, value: bool) -> None: ...


class GumballDisplayConduit:
    def __init__(self): ...
    def CheckShiftAndControlKeys(self) -> None: ...
    def Dispose(self) -> None: ...
    @property
    def BaseGumball(self) -> GumballObject: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def Gumball(self) -> GumballObject: ...
    @property
    def GumballTransform(self) -> Transform: ...
    @property
    def InRelocate(self) -> bool: ...
    @property
    def PickResult(self) -> GumballPickResult: ...
    @property
    def PreTransform(self) -> Transform: ...
    @property
    def TotalTransform(self) -> Transform: ...
    def PickGumball(self, pickContext: PickContext, getPoint: GetPoint) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @PreTransform.setter
    def PreTransform(self, value: Transform) -> None: ...
    @overload
    def SetBaseGumball(self, gumball: GumballObject) -> None: ...
    @overload
    def SetBaseGumball(self, gumball: GumballObject, appearanceSettings: GumballAppearanceSettings) -> None: ...
    def UpdateGumball(self, point: Point3d, worldLine: Line) -> bool: ...


class GumballFrame:
    @property
    def Plane(self) -> Plane: ...
    @property
    def ScaleGripDistance(self) -> Vector3d: ...
    @property
    def ScaleMode(self) -> GumballScaleMode: ...
    @Plane.setter
    def Plane(self, value: Plane) -> None: ...
    @ScaleGripDistance.setter
    def ScaleGripDistance(self, value: Vector3d) -> None: ...
    @ScaleMode.setter
    def ScaleMode(self, value: GumballScaleMode) -> None: ...


class GumballMode:
    #None = 0
    Menu = 1
    TranslateFree = 2
    TranslateX = 3
    TranslateY = 4
    TranslateZ = 5
    TranslateXY = 6
    TranslateYZ = 7
    TranslateZX = 8
    ScaleX = 9
    ScaleY = 10
    ScaleZ = 11
    ScaleXY = 12
    ScaleYZ = 13
    ScaleZX = 14
    RotateX = 15
    RotateY = 16
    RotateZ = 17
    ExtrudeX = 18
    ExtrudeY = 19
    ExtrudeZ = 20


class GumballObject:
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def Frame(self) -> GumballFrame: ...
    @Frame.setter
    def Frame(self, value: GumballFrame) -> None: ...
    def SetFromArc(self, arc: Arc) -> bool: ...
    @overload
    def SetFromBoundingBox(self, boundingBox: BoundingBox) -> bool: ...
    @overload
    def SetFromBoundingBox(self, frame: Plane, frameBoundingBox: BoundingBox) -> bool: ...
    def SetFromCircle(self, circle: Circle) -> bool: ...
    def SetFromCurve(self, curve: Curve) -> bool: ...
    def SetFromEllipse(self, ellipse: Ellipse) -> bool: ...
    def SetFromExtrusion(self, extrusion: Extrusion) -> bool: ...
    def SetFromHatch(self, hatch: Hatch) -> bool: ...
    def SetFromLight(self, light: Light) -> bool: ...
    def SetFromLine(self, line: Line) -> bool: ...
    def SetFromPlane(self, plane: Plane) -> bool: ...


class GumballPickResult:
    @property
    def Mode(self) -> GumballMode: ...
    def SetToDefault(self) -> None: ...


class GumballScaleMode:
    Independent = 0
    XY = 1
    YZ = 2
    ZX = 3
    XYZ = 4

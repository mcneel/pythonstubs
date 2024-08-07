from typing import Tuple, Set, Iterable, List, overload


class GH_ArcGetter:
    def GetArc() -> GH_Arc: ...
    def GetArcs() -> List: ...


class GH_BoxGetter:
    def GetBox() -> GH_Box: ...
    def GetBoxes() -> List: ...


class GH_BrepGetter:
    def GetBrep() -> GH_Brep: ...
    def GetBreps() -> List: ...


class GH_CircleGetter:
    def GetCircle() -> GH_Circle: ...
    def GetCircles() -> List: ...


class GH_CurveGetter:
    def GetCurve() -> GH_Curve: ...
    def GetCurves() -> List: ...


class GH_GeometryGetter:
    def GetGeometries() -> List: ...
    def GetGeometry() -> IGH_GeometricGoo: ...


class GH_LineGetter:
    def GetLine() -> GH_Line: ...
    def GetLines() -> List: ...


class GH_MeshGetter:
    def GetMesh() -> GH_Mesh: ...
    def GetMeshes() -> List: ...


class GH_PlaneGetter:
    def GetPlane() -> GH_Plane: ...
    def GetPlanes() -> List: ...


class GH_PointGetter:
    def __init__(self): ...
    def DefaultRefType(self) -> GH_PointRefType: ...
    @property
    def AcceptPreselected(self) -> bool: ...
    @property
    def PointRefType(self) -> GH_PointRefType: ...
    @overload
    def GetPoint(self) -> GH_Point: ...
    @overload
    def GetPoint(self, base: Point3d) -> GH_Point: ...
    @overload
    def GetPoint(prompt: str, basePoint: Point3d, outPoint: Point3d) -> Tuple[GH_GetterResult, Point3d]: ...
    def GetPoints(self) -> List: ...
    def RecreateSetup(self, pt: GH_Point) -> None: ...
    @AcceptPreselected.setter
    def AcceptPreselected(self, AutoPropertyValue: bool) -> None: ...
    @PointRefType.setter
    def PointRefType(self, AutoPropertyValue: GH_PointRefType) -> None: ...


class GH_RectangleGetter:
    def GetRectangle() -> GH_Rectangle: ...
    def GetRectangles() -> List: ...


class GH_SubDGetter:
    def GetSubD() -> GH_SubD: ...
    def GetSubDs() -> List: ...


class GH_SurfaceGetter:
    def GetSurface() -> GH_Surface: ...
    def GetSurfaces() -> List: ...


class GH_TransformGetter:
    pass


class GH_VectorGetter:
    def GetVector() -> GH_Vector: ...
    def GetVectors() -> List: ...

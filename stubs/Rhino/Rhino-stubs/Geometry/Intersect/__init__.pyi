from typing import Tuple, Set, Iterable, List

class Intersection:
    def LineLine (lineA : Line, lineB : Line, tolerance : float, finiteSegments : bool) -> Tuple[bool, float, float]: ...
    def LineLine (lineA : Line, lineB : Line) -> Tuple[bool, float, float]: ...
    def LinePlane (line : Line, plane : Plane) -> Tuple[bool, float]: ...
    def PlanePlane (planeA : Plane, planeB : Plane) -> Tuple[bool, Line]: ...
    def PlanePlanePlane (planeA : Plane, planeB : Plane, planeC : Plane) -> Tuple[bool, Point3d]: ...
    def PlaneCircle (plane : Plane, circle : Circle) -> Tuple[PlaneCircleIntersection, float, float]: ...
    def PlaneSphere (plane : Plane, sphere : Sphere) -> Tuple[PlaneSphereIntersection, Circle]: ...
    def LineCircle (line : Line, circle : Circle) -> Tuple[LineCircleIntersection, float, Point3d, float, Point3d]: ...
    def LineSphere (line : Line, sphere : Sphere) -> Tuple[LineSphereIntersection, Point3d, Point3d]: ...
    def LineCylinder (line : Line, cylinder : Cylinder) -> Tuple[LineCylinderIntersection, Point3d, Point3d]: ...
    def SphereSphere (sphereA : Sphere, sphereB : Sphere) -> Tuple[SphereSphereIntersection, Circle]: ...
    def LineBox (line : Line, box : BoundingBox, tolerance : float) -> Tuple[bool, Interval]: ...
    def LineBox (line : Line, box : Box, tolerance : float) -> Tuple[bool, Interval]: ...
    def CurvePlane (curve : Curve, plane : Plane, tolerance : float) -> CurveIntersections: ...
    def MeshPlane (mesh : Mesh, plane : Plane) -> Set(Polyline): ...
    def MeshPlane (mesh : Mesh, planes : Iterable[Plane]) -> Set(Polyline): ...
    def BrepPlane (brep : Brep, plane : Plane, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d)]: ...
    def CurveSelf (curve : Curve, tolerance : float) -> CurveIntersections: ...
    def CurveCurve (curveA : Curve, curveB : Curve, tolerance : float, overlapTolerance : float) -> CurveIntersections: ...
    def CurveLine (curve : Curve, line : Line, tolerance : float, overlapTolerance : float) -> CurveIntersections: ...
    def CurveSurface (curve : Curve, surface : Surface, tolerance : float, overlapTolerance : float) -> CurveIntersections: ...
    def CurveSurface (curve : Curve, curveDomain : Interval, surface : Surface, tolerance : float, overlapTolerance : float) -> CurveIntersections: ...
    def CurveBrep (curve : Curve, brep : Brep, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d)]: ...
    def CurveBrep (curve : Curve, brep : Brep, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d), Set(float)]: ...
    def CurveBrep (curve : Curve, brep : Brep, tolerance : float, angleTolerance : float) -> Tuple[bool, Set(float)]: ...
    def CurveBrepFace (curve : Curve, face : BrepFace, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d)]: ...
    def SurfaceSurface (surfaceA : Surface, surfaceB : Surface, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d)]: ...
    def BrepBrep (brepA : Brep, brepB : Brep, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d)]: ...
    def BrepSurface (brep : Brep, surface : Surface, tolerance : float) -> Tuple[bool, Set(Curve), Set(Point3d)]: ...
    def MeshMeshFast (meshA : Mesh, meshB : Mesh) -> Set(Line): ...
    def MeshMesh (meshes : Iterable[Mesh], tolerance : float, mode : SetsCombinations) -> Set(Polyline): ...
    def MeshMeshAccurate (meshA : Mesh, meshB : Mesh, tolerance : float) -> Set(Polyline): ...
    def MeshRay (mesh : Mesh, ray : Ray3d) -> float: ...
    def MeshRay (mesh : Mesh, ray : Ray3d) -> Tuple[float, Set(int)]: ...
    def MeshPolyline (mesh : Mesh, curve : PolylineCurve) -> Tuple[Set(Point3d), Set(int)]: ...
    def MeshLine (mesh : Mesh, line : Line) -> Tuple[Set(Point3d), Set(int)]: ...
    def RayShoot (ray : Ray3d, geometry : Iterable[GeometryBase], maxReflections : int) -> Set(Point3d): ...
    def ProjectPointsToMeshes (meshes : Iterable[Mesh], points : Iterable[Point3d], direction : Vector3d, tolerance : float) -> Set(Point3d): ...
    def ProjectPointsToMeshesEx (meshes : Iterable[Mesh], points : Iterable[Point3d], direction : Vector3d, tolerance : float) -> Tuple[Set(Point3d), Set(int)]: ...
    def ProjectPointsToBreps (breps : Iterable[Brep], points : Iterable[Point3d], direction : Vector3d, tolerance : float) -> Set(Point3d): ...
    def ProjectPointsToBrepsEx (breps : Iterable[Brep], points : Iterable[Point3d], direction : Vector3d, tolerance : float) -> Tuple[Set(Point3d), Set(int)]: ...
class SetsCombinations:
    Self = 0
    Cross = 1
    Both = 2
class PlaneCircleIntersection:
    None = 0
    Tangent = 1
    Secant = 2
    Parallel = 3
    Coincident = 4
class PlaneSphereIntersection:
    None = 0
    Point = 1
    Circle = 2
class LineCircleIntersection:
    None = 0
    Single = 1
    Multiple = 2
class LineSphereIntersection:
    None = 0
    Single = 1
    Multiple = 2
class LineCylinderIntersection:
    None = 0
    Single = 1
    Multiple = 2
    Overlap = 3
class SphereSphereIntersection:
    None = 0
    Point = 1
    Circle = 2
    Overlap = 3
class IntersectionEvent:
    def __init__(self): ...
    @property
    def IsPoint (self) -> bool: ...
    @property
    def IsOverlap (self) -> bool: ...
    @property
    def PointA (self) -> Point3d: ...
    @property
    def PointA2 (self) -> Point3d: ...
    @property
    def PointB (self) -> Point3d: ...
    @property
    def PointB2 (self) -> Point3d: ...
    @property
    def ParameterA (self) -> float: ...
    @property
    def ParameterB (self) -> float: ...
    @property
    def OverlapA (self) -> Interval: ...
    @property
    def OverlapB (self) -> Interval: ...
    def SurfacePointParameter (self) -> Tuple[float, float]: ...
    def SurfaceOverlapParameter (self) -> Tuple[Interval, Interval]: ...
class CurveIntersections:
    def Dispose (self) -> None: ...
    @property
    def Count (self) -> int: ...
    @property
    def Item (self, index : int) -> IntersectionEvent: ...
    def CopyTo (self, array : Set(IntersectionEvent), arrayIndex : int) -> None: ...
    def GetEnumerator (self) -> IEnumerator: ...
class MeshClash:
    @property
    def MeshA (self) -> Mesh: ...
    @property
    def MeshB (self) -> Mesh: ...
    @property
    def ClashPoint (self) -> Point3d: ...
    @property
    def ClashRadius (self) -> float: ...
    def Search (setA : Iterable[Mesh], setB : Iterable[Mesh], distance : float, maxEventCount : int) -> Set(MeshClash): ...
    def Search (meshA : Mesh, setB : Iterable[Mesh], distance : float, maxEventCount : int) -> Set(MeshClash): ...
    def Search (meshA : Mesh, meshB : Mesh, distance : float, maxEventCount : int) -> Set(MeshClash): ...
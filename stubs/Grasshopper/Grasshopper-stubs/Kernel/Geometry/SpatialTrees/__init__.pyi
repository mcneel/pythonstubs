from typing import Tuple, Set, Iterable, List, overload








class TreeDelegates:
    def Node2Coordinates(pt: Node2, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    def Node3Coordinates(pt: Node3, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    def Point2dCoordinates(pt: Point2d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    def Point2fCoordinates(pt: Point2d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    def Point3dCoordinates(pt: Point3d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    def Point3fCoordinates(pt: Point3d, x: float, y: float, z: float) -> Tuple[float, float, float]: ...
    def PointCoordinates(pt: Point, x: float, y: float, z: float) -> Tuple[float, float, float]: ...



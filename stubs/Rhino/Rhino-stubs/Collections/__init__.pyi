from typing import Tuple, Set, Iterable, List

class RhinoList:
    def PointCloudKNeighbors (pointcloud : PointCloud, needlePoints : Iterable[Point3d], amount : int) -> Iterable[Set(int)]: ...
    def Point3dKNeighbors (hayPoints : Iterable[Point3d], needlePoints : Iterable[Point3d], amount : int) -> Iterable[Set(int)]: ...
    def Point3fKNeighbors (hayPoints : Iterable[Point3f], needlePoints : Iterable[Point3f], amount : int) -> Iterable[Set(int)]: ...
    def Point2dKNeighbors (hayPoints : Iterable[Point2d], needlePoints : Iterable[Point2d], amount : int) -> Iterable[Set(int)]: ...
    def Point2fKNeighbors (hayPoints : Iterable[Point2f], needlePoints : Iterable[Point2f], amount : int) -> Iterable[Set(int)]: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class Point3dList:
    def __init__(self): ...
    def __init__(self, initialCapacity : int): ...
    def __init__(self, collection : Iterable[Point3d]): ...
    def __init__(self, initialPoints : Set(Point3d)): ...
    @property
    def BoundingBox (self) -> BoundingBox: ...
    def ClosestIndex (self, testPoint : Point3d) -> int: ...
    @property
    def X (self) -> XAccess: ...
    @property
    def Y (self) -> YAccess: ...
    @property
    def Z (self) -> ZAccess: ...
    def Add (self, x : float, y : float, z : float) -> None: ...
    def Transform (self, xform : Transform) -> None: ...
    def SetAllX (self, xValue : float) -> None: ...
    def SetAllY (self, yValue : float) -> None: ...
    def SetAllZ (self, zValue : float) -> None: ...
    def ClosestIndexInList (list : List[Point3d], testPoint : Point3d) -> int: ...
    def ClosestPointInList (list : List[Point3d], testPoint : Point3d) -> Point3d: ...
    def Duplicate (self) -> Point3dList: ...
    def ToArray (self) -> Set(Point3d): ...
    def TrimExcess (self) -> None: ...
    @property
    def Capacity (self) -> int: ...
    @Capacity.setter
    def Capacity (self, value : int) -> None: ...
    @property
    def Count (self) -> int: ...
    @property
    def NullCount (self) -> int: ...
    @property
    def Item (self, index : int) -> Point3d: ...
    @Item.setter
    def Item (self, index : int, value : Point3d) -> None: ...
    @property
    def First (self) -> Point3d: ...
    @First.setter
    def First (self, value : Point3d) -> None: ...
    @property
    def Last (self) -> Point3d: ...
    @Last.setter
    def Last (self, value : Point3d) -> None: ...
    def RemapIndex (self, index : int) -> int: ...
    def Clear (self) -> None: ...
    def Add (self, item : Point3d) -> None: ...
    def AddRange (self, collection : Iterable[Point3d]) -> None: ...
    def AddRange (self, collection : IEnumerable) -> None: ...
    def Insert (self, index : int, item : Point3d) -> None: ...
    def InsertRange (self, index : int, collection : Iterable[Point3d]) -> None: ...
    def Remove (self, item : Point3d) -> bool: ...
    def RemoveAll (self, match : Predicate) -> int: ...
    def RemoveNulls (self) -> int: ...
    def RemoveAt (self, index : int) -> None: ...
    def RemoveRange (self, index : int, count : int) -> None: ...
    def GetRange (self, index : int, count : int) -> RhinoList: ...
    def IndexOf (self, item : Point3d) -> int: ...
    def IndexOf (self, item : Point3d, index : int) -> int: ...
    def IndexOf (self, item : Point3d, index : int, count : int) -> int: ...
    def LastIndexOf (self, item : Point3d) -> int: ...
    def LastIndexOf (self, item : Point3d, index : int) -> int: ...
    def LastIndexOf (self, item : Point3d, index : int, count : int) -> int: ...
    def BinarySearch (self, item : Point3d) -> int: ...
    def BinarySearch (self, item : Point3d, comparer : IComparer) -> int: ...
    def BinarySearch (self, index : int, count : int, item : Point3d, comparer : IComparer) -> int: ...
    def Contains (self, item : Point3d) -> bool: ...
    def Exists (self, match : Predicate) -> bool: ...
    def Find (self, match : Predicate) -> Point3d: ...
    def FindLast (self, match : Predicate) -> Point3d: ...
    def FindAll (self, match : Predicate) -> RhinoList: ...
    def TrueForAll (self, match : Predicate) -> bool: ...
    def ForEach (self, action : Action) -> None: ...
    def FindIndex (self, match : Predicate) -> int: ...
    def FindIndex (self, startIndex : int, match : Predicate) -> int: ...
    def FindIndex (self, startIndex : int, count : int, match : Predicate) -> int: ...
    def FindLastIndex (self, match : Predicate) -> int: ...
    def FindLastIndex (self, startIndex : int, match : Predicate) -> int: ...
    def FindLastIndex (self, startIndex : int, count : int, match : Predicate) -> int: ...
    def Sort (self) -> None: ...
    def Sort (self, comparer : IComparer) -> None: ...
    def Sort (self, comparison : Comparison) -> None: ...
    def Sort (self, index : int, count : int, comparer : IComparer) -> None: ...
    def Sort (self, keys : Set(float)) -> None: ...
    def Sort (self, keys : Set(int)) -> None: ...
    def Reverse (self) -> None: ...
    def Reverse (self, index : int, count : int) -> None: ...
    def AsReadOnly (self) -> ReadOnlyCollection: ...
    def ConvertAll (self, converter : Converter) -> RhinoList: ...
    def CopyTo (self, array : Set(Point3d)) -> None: ...
    def CopyTo (self, array : Set(Point3d), arrayIndex : int) -> None: ...
    def CopyTo (self, index : int, array : Set(Point3d), arrayIndex : int, count : int) -> None: ...
    def Duplicate (self) -> RhinoList: ...
    def GetEnumerator (self) -> IEnumerator: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class CurveList:
    def __init__(self): ...
    def __init__(self, initialCapacity : int): ...
    def __init__(self, collection : Iterable[Curve]): ...
    def Add (self, line : Line) -> None: ...
    def Add (self, circle : Circle) -> None: ...
    def Add (self, arc : Arc) -> None: ...
    def Add (self, polyline : Iterable[Point3d]) -> None: ...
    def Add (self, ellipse : Ellipse) -> None: ...
    def Insert (self, index : int, line : Line) -> None: ...
    def Insert (self, index : int, circle : Circle) -> None: ...
    def Insert (self, index : int, arc : Arc) -> None: ...
    def Insert (self, index : int, polyline : Iterable[Point3d]) -> None: ...
    def Insert (self, index : int, ellipse : Ellipse) -> None: ...
    def Transform (self, xform : Transform) -> bool: ...
    def ToArray (self) -> Set(Curve): ...
    def TrimExcess (self) -> None: ...
    @property
    def Capacity (self) -> int: ...
    @Capacity.setter
    def Capacity (self, value : int) -> None: ...
    @property
    def Count (self) -> int: ...
    @property
    def NullCount (self) -> int: ...
    @property
    def Item (self, index : int) -> Curve: ...
    @Item.setter
    def Item (self, index : int, value : Curve) -> None: ...
    @property
    def First (self) -> Curve: ...
    @First.setter
    def First (self, value : Curve) -> None: ...
    @property
    def Last (self) -> Curve: ...
    @Last.setter
    def Last (self, value : Curve) -> None: ...
    def RemapIndex (self, index : int) -> int: ...
    def Clear (self) -> None: ...
    def Add (self, item : Curve) -> None: ...
    def AddRange (self, collection : Iterable[Curve]) -> None: ...
    def AddRange (self, collection : IEnumerable) -> None: ...
    def Insert (self, index : int, item : Curve) -> None: ...
    def InsertRange (self, index : int, collection : Iterable[Curve]) -> None: ...
    def Remove (self, item : Curve) -> bool: ...
    def RemoveAll (self, match : Predicate) -> int: ...
    def RemoveNulls (self) -> int: ...
    def RemoveAt (self, index : int) -> None: ...
    def RemoveRange (self, index : int, count : int) -> None: ...
    def GetRange (self, index : int, count : int) -> RhinoList: ...
    def IndexOf (self, item : Curve) -> int: ...
    def IndexOf (self, item : Curve, index : int) -> int: ...
    def IndexOf (self, item : Curve, index : int, count : int) -> int: ...
    def LastIndexOf (self, item : Curve) -> int: ...
    def LastIndexOf (self, item : Curve, index : int) -> int: ...
    def LastIndexOf (self, item : Curve, index : int, count : int) -> int: ...
    def BinarySearch (self, item : Curve) -> int: ...
    def BinarySearch (self, item : Curve, comparer : IComparer) -> int: ...
    def BinarySearch (self, index : int, count : int, item : Curve, comparer : IComparer) -> int: ...
    def Contains (self, item : Curve) -> bool: ...
    def Exists (self, match : Predicate) -> bool: ...
    def Find (self, match : Predicate) -> Curve: ...
    def FindLast (self, match : Predicate) -> Curve: ...
    def FindAll (self, match : Predicate) -> RhinoList: ...
    def TrueForAll (self, match : Predicate) -> bool: ...
    def ForEach (self, action : Action) -> None: ...
    def FindIndex (self, match : Predicate) -> int: ...
    def FindIndex (self, startIndex : int, match : Predicate) -> int: ...
    def FindIndex (self, startIndex : int, count : int, match : Predicate) -> int: ...
    def FindLastIndex (self, match : Predicate) -> int: ...
    def FindLastIndex (self, startIndex : int, match : Predicate) -> int: ...
    def FindLastIndex (self, startIndex : int, count : int, match : Predicate) -> int: ...
    def Sort (self) -> None: ...
    def Sort (self, comparer : IComparer) -> None: ...
    def Sort (self, comparison : Comparison) -> None: ...
    def Sort (self, index : int, count : int, comparer : IComparer) -> None: ...
    def Sort (self, keys : Set(float)) -> None: ...
    def Sort (self, keys : Set(int)) -> None: ...
    def Reverse (self) -> None: ...
    def Reverse (self, index : int, count : int) -> None: ...
    def AsReadOnly (self) -> ReadOnlyCollection: ...
    def ConvertAll (self, converter : Converter) -> RhinoList: ...
    def CopyTo (self, array : Set(Curve)) -> None: ...
    def CopyTo (self, array : Set(Curve), arrayIndex : int) -> None: ...
    def CopyTo (self, index : int, array : Set(Curve), arrayIndex : int, count : int) -> None: ...
    def Duplicate (self) -> RhinoList: ...
    def GetEnumerator (self) -> IEnumerator: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class TransformObjectList:
    def __init__(self): ...
    def Dispose (self) -> None: ...
    def GetBoundingBox (self, regularObjects : bool, grips : bool) -> BoundingBox: ...
    @property
    def DisplayFeedbackEnabled (self) -> bool: ...
    @DisplayFeedbackEnabled.setter
    def DisplayFeedbackEnabled (self, value : bool) -> None: ...
    def UpdateDisplayFeedbackTransform (self, xform : Transform) -> bool: ...
    def Clear (self) -> None: ...
    @property
    def Count (self) -> int: ...
    @property
    def GripCount (self) -> int: ...
    @property
    def GripOwnerCount (self) -> int: ...
    def Add (self, rhinoObject : RhinoObject) -> None: ...
    def Add (self, objref : ObjRef) -> None: ...
    def AddObjects (self, go : GetObject, allowGrips : bool) -> int: ...
    def GripArray (self) -> Set(GripObject): ...
    def GripOwnerArray (self) -> Set(RhinoObject): ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ArchivableDictionary:
    def __init__(self): ...
    def __init__(self, parentUserData : UserData): ...
    def __init__(self, version : int): ...
    def __init__(self, version : int, name : str): ...
    def Set (self, key : str, val : Iterable[Guid]) -> bool: ...
    def Set (self, key : str, val : Iterable[str]) -> bool: ...
    def Set (self, key : str, val : Color) -> bool: ...
    def Set (self, key : str, val : Point) -> bool: ...
    def Set (self, key : str, val : PointF) -> bool: ...
    def Set (self, key : str, val : Rectangle) -> bool: ...
    def Set (self, key : str, val : RectangleF) -> bool: ...
    def Set (self, key : str, val : Size) -> bool: ...
    def Set (self, key : str, val : SizeF) -> bool: ...
    def Set (self, key : str, val : Font) -> bool: ...
    def Set (self, key : str, val : Interval) -> bool: ...
    def Set (self, key : str, val : Point2d) -> bool: ...
    def Set (self, key : str, val : Point3d) -> bool: ...
    def Set (self, key : str, val : Point4d) -> bool: ...
    def Set (self, key : str, val : Vector2d) -> bool: ...
    def Set (self, key : str, val : Vector3d) -> bool: ...
    def Set (self, key : str, val : BoundingBox) -> bool: ...
    def Set (self, key : str, val : Ray3d) -> bool: ...
    def Set (self, key : str, val : Transform) -> bool: ...
    def Set (self, key : str, val : Plane) -> bool: ...
    def Set (self, key : str, val : Line) -> bool: ...
    def Set (self, key : str, val : Point3f) -> bool: ...
    def Set (self, key : str, val : Vector3f) -> bool: ...
    def Set (self, key : str, val : ArchivableDictionary) -> bool: ...
    def Set (self, key : str, val : MeshingParameters) -> bool: ...
    def Set (self, key : str, val : GeometryBase) -> bool: ...
    def Set (self, key : str, val : ObjRef) -> bool: ...
    def Set (self, key : str, val : Iterable[ObjRef]) -> bool: ...
    def Set (self, key : str, val : Iterable[GeometryBase]) -> bool: ...
    def SetEnumValue (self, enumValue : T) -> bool: ...
    def SetEnumValue (self, key : str, enumValue : T) -> bool: ...
    def GetEnumValue (self) -> T: ...
    def GetEnumValue (self, key : str) -> T: ...
    def TryGetEnumValue (self, key : str) -> Tuple[bool, T]: ...
    def RemoveEnumValue (self) -> bool: ...
    def AddContentsFrom (self, source : ArchivableDictionary) -> bool: ...
    def ReplaceContentsWith (self, source : ArchivableDictionary) -> bool: ...
    def Clone (self) -> ArchivableDictionary: ...
    def GetEnumerator (self) -> IEnumerator: ...
    @property
    def Version (self) -> int: ...
    @Version.setter
    def Version (self, value : int) -> None: ...
    @property
    def Name (self) -> str: ...
    @Name.setter
    def Name (self, value : str) -> None: ...
    def GetObjectData (self, info : SerializationInfo, context : StreamingContext) -> None: ...
    @property
    def ParentUserData (self) -> UserData: ...
    @property
    def Keys (self) -> Set(str): ...
    @property
    def Values (self) -> Set(Object): ...
    def ContainsKey (self, key : str) -> bool: ...
    @property
    def Item (self, key : str) -> Object: ...
    @Item.setter
    def Item (self, key : str, value : Object) -> None: ...
    def Clear (self) -> None: ...
    def Remove (self, key : str) -> bool: ...
    @property
    def Count (self) -> int: ...
    def TryGetValue (self, key : str) -> Tuple[bool, Object]: ...
    def TryGetString (self, key : str) -> Tuple[bool, str]: ...
    def GetString (self, key : str) -> str: ...
    def GetString (self, key : str, defaultValue : str) -> str: ...
    def TryGetDictionary (self, key : str) -> Tuple[bool, ArchivableDictionary]: ...
    def GetDictionary (self, key : str) -> ArchivableDictionary: ...
    def GetDictionary (self, key : str, defaultValue : ArchivableDictionary) -> ArchivableDictionary: ...
    def TryGetBytes (self, key : str) -> Tuple[bool, Set(Byte)]: ...
    def GetBytes (self, key : str) -> Set(Byte): ...
    def GetBytes (self, key : str, defaultValue : Set(Byte)) -> Set(Byte): ...
    def TryGetBool (self, key : str) -> Tuple[bool, bool]: ...
    def GetBool (self, key : str) -> bool: ...
    def GetBool (self, key : str, defaultValue : bool) -> bool: ...
    def TryGetFloat (self, key : str) -> Tuple[bool, Single]: ...
    def GetFloat (self, key : str) -> Single: ...
    def GetFloat (self, key : str, defaultValue : Single) -> Single: ...
    def TryGetDouble (self, key : str) -> Tuple[bool, float]: ...
    def GetDouble (self, key : str) -> float: ...
    def GetDouble (self, key : str, defaultValue : float) -> float: ...
    def GetInteger (self, key : str, defaultValue : int) -> int: ...
    def TryGetInteger (self, key : str) -> Tuple[bool, int]: ...
    def GetInteger (self, key : str) -> int: ...
    def Getint (self, key : str, defaultValue : int) -> int: ...
    def TryGetPoint3f (self, key : str) -> Tuple[bool, Point3f]: ...
    def GetPoint3f (self, key : str) -> Point3f: ...
    def GetPoint3f (self, key : str, defaultValue : Point3f) -> Point3f: ...
    def TryGetPoint3d (self, key : str) -> Tuple[bool, Point3d]: ...
    def GetPoint3d (self, key : str) -> Point3d: ...
    def GetPoint3d (self, key : str, defaultValue : Point3d) -> Point3d: ...
    def TryGetVector3d (self, key : str) -> Tuple[bool, Vector3d]: ...
    def GetVector3d (self, key : str) -> Vector3d: ...
    def GetVector3d (self, key : str, defaultValue : Vector3d) -> Vector3d: ...
    def TryGetGuid (self, key : str) -> Tuple[bool, Guid]: ...
    def GetGuid (self, key : str) -> Guid: ...
    def GetGuid (self, key : str, defaultValue : Guid) -> Guid: ...
    def TryGetPlane (self, key : str) -> Tuple[bool, Plane]: ...
    def GetPlane (self, key : str) -> Plane: ...
    def GetPlane (self, key : str, defaultValue : Plane) -> Plane: ...
    def Set (self, key : str, val : bool) -> bool: ...
    def Set (self, key : str, val : Byte) -> bool: ...
    def Set (self, key : str, val : SByte) -> bool: ...
    def Set (self, key : str, val : Int16) -> bool: ...
    def Set (self, key : str, val : UInt16) -> bool: ...
    def Set (self, key : str, val : int) -> bool: ...
    def Set (self, key : str, val : UInt32) -> bool: ...
    def Set (self, key : str, val : Int64) -> bool: ...
    def Set (self, key : str, val : Single) -> bool: ...
    def Set (self, key : str, val : float) -> bool: ...
    def Set (self, key : str, val : Guid) -> bool: ...
    def Set (self, key : str, val : str) -> bool: ...
    def Set (self, key : str, val : Iterable[bool]) -> bool: ...
    def Set (self, key : str, val : Iterable[Byte]) -> bool: ...
    def Set (self, key : str, val : Iterable[SByte]) -> bool: ...
    def Set (self, key : str, val : Iterable[Int16]) -> bool: ...
    def Set (self, key : str, val : Iterable[int]) -> bool: ...
    def Set (self, key : str, val : Iterable[Single]) -> bool: ...
    def Set (self, key : str, val : Iterable[float]) -> bool: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class XAccess:
    @property
    def Item (self, index : int) -> float: ...
    @Item.setter
    def Item (self, index : int, value : float) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class YAccess:
    @property
    def Item (self, index : int) -> float: ...
    @Item.setter
    def Item (self, index : int, value : float) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...
class ZAccess:
    @property
    def Item (self, index : int) -> float: ...
    @Item.setter
    def Item (self, index : int, value : float) -> None: ...
    def ToString (self) -> str: ...
    def Equals (self, obj : Object) -> bool: ...
    def GetHashCode (self) -> int: ...
    def GetType (self) -> Type: ...

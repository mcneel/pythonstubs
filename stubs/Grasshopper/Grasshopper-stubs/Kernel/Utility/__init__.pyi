from typing import Tuple, Set, Iterable, List, overload


class GH_Interval_Wrapper:
    def __init__(self, interval: Interval, wrapperdelegate: GH_IntervalWrapperDelegate): ...
    @property
    def A(self) -> float: ...
    @property
    def B(self) -> float: ...
    @property
    def Increasing(self) -> str: ...
    @property
    def Length(self) -> str: ...
    def InternalInterval(self) -> Interval: ...
    @A.setter
    def A(self, set_value: float) -> None: ...
    @B.setter
    def B(self, set_value: float) -> None: ...


class GH_Interval_Wrapper_TypeConverter:
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object, destinationType: Type) -> Object: ...


class GH_IntervalWrapperDelegate:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, sender: GH_Interval_Wrapper, interval: Interval, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, sender: GH_Interval_Wrapper, interval: Interval) -> None: ...


class GH_PlaneModifier:
    def Set_X(P: Plane, x_axis: Vector3d) -> Plane: ...
    def Set_Y(P: Plane, y_axis: Vector3d) -> Plane: ...
    def Set_Z(P: Plane, z_axis: Vector3d) -> Plane: ...


class GH_Point3d_Wrapper:
    def __init__(self, pt: Point3d, wrapperdelegate: GH_Point3dWrapperDelegate): ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
    def InternalPoint(self) -> Point3d: ...
    @X.setter
    def X(self, set_value: float) -> None: ...
    @Y.setter
    def Y(self, set_value: float) -> None: ...
    @Z.setter
    def Z(self, set_value: float) -> None: ...


class GH_Point3d_Wrapper_TypeConverter:
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object, destinationType: Type) -> Object: ...


class GH_Point3dWrapperDelegate:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, sender: GH_Point3d_Wrapper, point: Point3d, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, sender: GH_Point3d_Wrapper, point: Point3d) -> None: ...


class GH_PointRefUV_Wrapper:
    def __init__(self, ref: GH_PointRefData, wrapperdelegate: GH_PointRefUVWrapperDelegate): ...
    @property
    def U(self) -> float: ...
    @property
    def V(self) -> float: ...
    def InternalRefence(self) -> GH_PointRefData: ...
    @U.setter
    def U(self, set_value: float) -> None: ...
    @V.setter
    def V(self, set_value: float) -> None: ...


class GH_PointRefUV_Wrapper_TypeConverter:
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object, destinationType: Type) -> Object: ...


class GH_PointRefUVWrapperDelegate:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, sender: GH_PointRefUV_Wrapper, ref: GH_PointRefData, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, sender: GH_PointRefUV_Wrapper, ref: GH_PointRefData) -> None: ...


class GH_Vector3d_Wrapper:
    def __init__(self, vec: Vector3d, wrapperdelegate: GH_Vector3dWrapperDelegate): ...
    @property
    def Length(self) -> str: ...
    @property
    def Tiny(self) -> str: ...
    @property
    def X(self) -> float: ...
    @property
    def Y(self) -> float: ...
    @property
    def Z(self) -> float: ...
    def InternalVector(self) -> Vector3d: ...
    @X.setter
    def X(self, set_value: float) -> None: ...
    @Y.setter
    def Y(self, set_value: float) -> None: ...
    @Z.setter
    def Z(self, set_value: float) -> None: ...


class GH_Vector3d_Wrapper_TypeConverter:
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object, destinationType: Type) -> Object: ...


class GH_Vector3dWrapperDelegate:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, sender: GH_Vector3d_Wrapper, vector: Vector3d, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, sender: GH_Vector3d_Wrapper, vector: Vector3d) -> None: ...

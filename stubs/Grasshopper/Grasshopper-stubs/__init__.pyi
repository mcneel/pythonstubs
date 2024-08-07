__all__ = ['Documentation','Getters','GUI','Kernel','Plugin']
from typing import Tuple, Set, Iterable, List, overload


class AuthorAddressChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class AuthorCompanyChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class AuthorCopyrightChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class AuthorEMailChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class AuthorNameChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class AuthorPhoneChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class AuthorWebsiteChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasCreatedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, canvas: GH_Canvas, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, canvas: GH_Canvas) -> None: ...


class CanvasDestroyedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, canvas: GH_Canvas, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, canvas: GH_Canvas) -> None: ...


class CanvasFancyWiresChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasFullNamesChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasObjectIconsChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasObsoleteTagsChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasRadialMenuChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasToolbarChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CanvasZuiZoomLevelChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CentralSettings:
    def add_AuthorAddressChanged(obj: AuthorAddressChangedEventHandler) -> None: ...
    def add_AuthorCompanyChanged(obj: AuthorCompanyChangedEventHandler) -> None: ...
    def add_AuthorCopyrightChanged(obj: AuthorCopyrightChangedEventHandler) -> None: ...
    def add_AuthorEMailChanged(obj: AuthorEMailChangedEventHandler) -> None: ...
    def add_AuthorNameChanged(obj: AuthorNameChangedEventHandler) -> None: ...
    def add_AuthorPhoneChanged(obj: AuthorPhoneChangedEventHandler) -> None: ...
    def add_AuthorWebsiteChanged(obj: AuthorWebsiteChangedEventHandler) -> None: ...
    def add_CanvasFancyWiresChanged(obj: CanvasFancyWiresChangedEventHandler) -> None: ...
    def add_CanvasFullNamesChanged(obj: CanvasFullNamesChangedEventHandler) -> None: ...
    def add_CanvasObjectIconsChanged(obj: CanvasObjectIconsChangedEventHandler) -> None: ...
    def add_CanvasObsoleteTagsChanged(obj: CanvasObsoleteTagsChangedEventHandler) -> None: ...
    def add_CanvasRadialMenuChanged(obj: CanvasRadialMenuChangedEventHandler) -> None: ...
    def add_CanvasToolbarChanged(obj: CanvasToolbarChangedEventHandler) -> None: ...
    def add_CanvasZuiZoomLevelChanged(obj: CanvasZuiZoomLevelChangedEventHandler) -> None: ...
    def add_ComponentCascadeMenusChanged(obj: ComponentCascadeMenusChangedEventHandler) -> None: ...
    def add_CreateSolutionUndoRecordChanged(obj: CreateSolutionUndoRecordChangedEventHandler) -> None: ...
    def add_FormattingChanged(obj: FormattingChangedEventHandler) -> None: ...
    def add_LoadMechanismChanged(obj: LoadMechanismChangedEventHandler) -> None: ...
    def add_LoadProtectionChanged(obj: LoadProtectionChangedEventHandler) -> None: ...
    def add_PreviewBumpZBufferChanged(obj: PreviewBumpZBufferChangedEventHandler) -> None: ...
    def add_PreviewGumballsChanged(obj: PreviewGumballsChangedEventHandler) -> None: ...
    def add_PreviewMeshEdgesChanged(obj: PreviewMeshEdgesChangedEventHandler) -> None: ...
    def add_PreviewPlaneRadiusChanged(obj: PreviewPlaneRadiusChangedEventHandler) -> None: ...
    def add_PreviewPointStyleChanged(obj: PreviewPointStyleChangedEventHandler) -> None: ...
    def add_PruderyLevelChanged(obj: PruderyLevelChangedEventHandler) -> None: ...
    def add_RibbonAllIconsChanged(obj: RibbonAllIconsChangedEventHandler) -> None: ...
    def add_RibbonDrawTabIconsChanged(obj: RibbonDrawTabIconsChangedEventHandler) -> None: ...
    def add_RibbonSeparatorsChanged(obj: RibbonSeparatorsChangedEventHandler) -> None: ...
    def add_RibbonVisibleChanged(obj: RibbonVisibleChangedEventHandler) -> None: ...
    def add_TemplateFileChanged(obj: TemplateFileChangedEventHandler) -> None: ...
    def add_TooltipWiggleRadiusChanged(obj: TooltipWiggleRadiusChangedEventHandler) -> None: ...
    def add_UiScaleChanged(obj: UiScaleChangedEventHandler) -> None: ...
    @property
    def AuthorAddress() -> str: ...
    @property
    def AuthorCompany() -> str: ...
    @property
    def AuthorCopyright() -> str: ...
    @property
    def AuthorCopyrightFormatted() -> str: ...
    @property
    def AuthorDetails() -> IGH_Author: ...
    @property
    def AuthorEMail() -> str: ...
    @property
    def AuthorName() -> str: ...
    @property
    def AuthorPhone() -> str: ...
    @property
    def AuthorWebsite() -> str: ...
    @property
    def CanvasFancyWires() -> bool: ...
    @property
    def CanvasFullNames() -> bool: ...
    @property
    def CanvasMaxSearchResults() -> int: ...
    @property
    def CanvasObjectIcons() -> bool: ...
    @property
    def CanvasObsoleteTags() -> bool: ...
    @property
    def CanvasRadialMenu() -> bool: ...
    @property
    def CanvasSpaceIsRadialMenu() -> bool: ...
    @property
    def CanvasSpaceSearchRadialMessage() -> int: ...
    @property
    def CanvasToolbar() -> bool: ...
    @property
    def CanvasZuiZoomLevel() -> Single: ...
    @property
    def ComponentCascadeMenus() -> bool: ...
    @property
    def CreateSolutionUndoRecord() -> bool: ...
    @property
    def FormatDecimalDigits() -> int: ...
    @property
    def FormatENotationDigits() -> int: ...
    @property
    def FormatENotationLowerLimit() -> int: ...
    @property
    def FormatENotationLowerThreshold() -> float: ...
    @property
    def FormatENotationUpperLimit() -> int: ...
    @property
    def FormatENotationUpperThreshold() -> float: ...
    @property
    def FormatMultiplesOfOne() -> bool: ...
    @property
    def FormatMultiplesOfPi() -> bool: ...
    @property
    def InvalidBakeAllow() -> bool: ...
    @property
    def InvalidBakeAsk() -> bool: ...
    @property
    def IsTemplateFile() -> bool: ...
    @property
    def PreviewBumpZBuffer() -> bool: ...
    @property
    def PreviewGumballs() -> bool: ...
    @property
    def PreviewMeshEdges() -> bool: ...
    @property
    def PreviewPlaneRadius() -> float: ...
    @property
    def PreviewPointRadius() -> int: ...
    @property
    def PreviewPointStyle() -> PointStyle: ...
    @property
    def PreviewSelectionThickening() -> int: ...
    @property
    def PruderyLevel() -> GH_PruderyFilter: ...
    @property
    def RibbonDrawTabIcons() -> bool: ...
    @property
    def RibbonSeparators() -> bool: ...
    @property
    def RibbonShowObscure() -> bool: ...
    @property
    def RibbonVisible() -> bool: ...
    @property
    def ShowTutorials() -> bool: ...
    @property
    def TemplateFile() -> str: ...
    @property
    def TooltipWiggleRadius() -> int: ...
    @property
    def TrackFileStamps() -> bool: ...
    @property
    def TrackPluginLoading() -> bool: ...
    @property
    def TryDownloadMissingPlugins() -> bool: ...
    def GetLoadMechanism(pluginName: str) -> GH_LoadingDemand: ...
    def IsLoadProtected(pluginName: str) -> bool: ...
    def remove_AuthorAddressChanged(obj: AuthorAddressChangedEventHandler) -> None: ...
    def remove_AuthorCompanyChanged(obj: AuthorCompanyChangedEventHandler) -> None: ...
    def remove_AuthorCopyrightChanged(obj: AuthorCopyrightChangedEventHandler) -> None: ...
    def remove_AuthorEMailChanged(obj: AuthorEMailChangedEventHandler) -> None: ...
    def remove_AuthorNameChanged(obj: AuthorNameChangedEventHandler) -> None: ...
    def remove_AuthorPhoneChanged(obj: AuthorPhoneChangedEventHandler) -> None: ...
    def remove_AuthorWebsiteChanged(obj: AuthorWebsiteChangedEventHandler) -> None: ...
    def remove_CanvasFancyWiresChanged(obj: CanvasFancyWiresChangedEventHandler) -> None: ...
    def remove_CanvasFullNamesChanged(obj: CanvasFullNamesChangedEventHandler) -> None: ...
    def remove_CanvasObjectIconsChanged(obj: CanvasObjectIconsChangedEventHandler) -> None: ...
    def remove_CanvasObsoleteTagsChanged(obj: CanvasObsoleteTagsChangedEventHandler) -> None: ...
    def remove_CanvasRadialMenuChanged(obj: CanvasRadialMenuChangedEventHandler) -> None: ...
    def remove_CanvasToolbarChanged(obj: CanvasToolbarChangedEventHandler) -> None: ...
    def remove_CanvasZuiZoomLevelChanged(obj: CanvasZuiZoomLevelChangedEventHandler) -> None: ...
    def remove_ComponentCascadeMenusChanged(obj: ComponentCascadeMenusChangedEventHandler) -> None: ...
    def remove_CreateSolutionUndoRecordChanged(obj: CreateSolutionUndoRecordChangedEventHandler) -> None: ...
    def remove_FormattingChanged(obj: FormattingChangedEventHandler) -> None: ...
    def remove_LoadMechanismChanged(obj: LoadMechanismChangedEventHandler) -> None: ...
    def remove_LoadProtectionChanged(obj: LoadProtectionChangedEventHandler) -> None: ...
    def remove_PreviewBumpZBufferChanged(obj: PreviewBumpZBufferChangedEventHandler) -> None: ...
    def remove_PreviewGumballsChanged(obj: PreviewGumballsChangedEventHandler) -> None: ...
    def remove_PreviewMeshEdgesChanged(obj: PreviewMeshEdgesChangedEventHandler) -> None: ...
    def remove_PreviewPlaneRadiusChanged(obj: PreviewPlaneRadiusChangedEventHandler) -> None: ...
    def remove_PreviewPointStyleChanged(obj: PreviewPointStyleChangedEventHandler) -> None: ...
    def remove_PruderyLevelChanged(obj: PruderyLevelChangedEventHandler) -> None: ...
    def remove_RibbonAllIconsChanged(obj: RibbonAllIconsChangedEventHandler) -> None: ...
    def remove_RibbonDrawTabIconsChanged(obj: RibbonDrawTabIconsChangedEventHandler) -> None: ...
    def remove_RibbonSeparatorsChanged(obj: RibbonSeparatorsChangedEventHandler) -> None: ...
    def remove_RibbonVisibleChanged(obj: RibbonVisibleChangedEventHandler) -> None: ...
    def remove_TemplateFileChanged(obj: TemplateFileChangedEventHandler) -> None: ...
    def remove_TooltipWiggleRadiusChanged(obj: TooltipWiggleRadiusChangedEventHandler) -> None: ...
    def remove_UiScaleChanged(obj: UiScaleChangedEventHandler) -> None: ...
    @AuthorAddress.setter
    def AuthorAddress(Value: str) -> None: ...
    @AuthorCompany.setter
    def AuthorCompany(Value: str) -> None: ...
    @AuthorCopyright.setter
    def AuthorCopyright(Value: str) -> None: ...
    @AuthorEMail.setter
    def AuthorEMail(Value: str) -> None: ...
    @AuthorName.setter
    def AuthorName(Value: str) -> None: ...
    @AuthorPhone.setter
    def AuthorPhone(Value: str) -> None: ...
    @AuthorWebsite.setter
    def AuthorWebsite(Value: str) -> None: ...
    @CanvasFancyWires.setter
    def CanvasFancyWires(Value: bool) -> None: ...
    @CanvasFullNames.setter
    def CanvasFullNames(Value: bool) -> None: ...
    @CanvasMaxSearchResults.setter
    def CanvasMaxSearchResults(Value: int) -> None: ...
    @CanvasObjectIcons.setter
    def CanvasObjectIcons(Value: bool) -> None: ...
    @CanvasObsoleteTags.setter
    def CanvasObsoleteTags(Value: bool) -> None: ...
    @CanvasRadialMenu.setter
    def CanvasRadialMenu(Value: bool) -> None: ...
    @CanvasSpaceIsRadialMenu.setter
    def CanvasSpaceIsRadialMenu(Value: bool) -> None: ...
    @CanvasSpaceSearchRadialMessage.setter
    def CanvasSpaceSearchRadialMessage(Value: int) -> None: ...
    @CanvasToolbar.setter
    def CanvasToolbar(Value: bool) -> None: ...
    @CanvasZuiZoomLevel.setter
    def CanvasZuiZoomLevel(Value: Single) -> None: ...
    @ComponentCascadeMenus.setter
    def ComponentCascadeMenus(Value: bool) -> None: ...
    @CreateSolutionUndoRecord.setter
    def CreateSolutionUndoRecord(Value: bool) -> None: ...
    @FormatDecimalDigits.setter
    def FormatDecimalDigits(Value: int) -> None: ...
    @FormatENotationDigits.setter
    def FormatENotationDigits(Value: int) -> None: ...
    @FormatENotationLowerLimit.setter
    def FormatENotationLowerLimit(Value: int) -> None: ...
    @FormatENotationUpperLimit.setter
    def FormatENotationUpperLimit(Value: int) -> None: ...
    @FormatMultiplesOfOne.setter
    def FormatMultiplesOfOne(Value: bool) -> None: ...
    @FormatMultiplesOfPi.setter
    def FormatMultiplesOfPi(Value: bool) -> None: ...
    @InvalidBakeAllow.setter
    def InvalidBakeAllow(AutoPropertyValue: bool) -> None: ...
    @InvalidBakeAsk.setter
    def InvalidBakeAsk(AutoPropertyValue: bool) -> None: ...
    @PreviewBumpZBuffer.setter
    def PreviewBumpZBuffer(Value: bool) -> None: ...
    @PreviewGumballs.setter
    def PreviewGumballs(Value: bool) -> None: ...
    @PreviewMeshEdges.setter
    def PreviewMeshEdges(Value: bool) -> None: ...
    @PreviewPlaneRadius.setter
    def PreviewPlaneRadius(Value: float) -> None: ...
    @PreviewPointStyle.setter
    def PreviewPointStyle(Value: PointStyle) -> None: ...
    @PreviewSelectionThickening.setter
    def PreviewSelectionThickening(Value: int) -> None: ...
    @PruderyLevel.setter
    def PruderyLevel(Value: GH_PruderyFilter) -> None: ...
    @RibbonDrawTabIcons.setter
    def RibbonDrawTabIcons(Value: bool) -> None: ...
    @RibbonSeparators.setter
    def RibbonSeparators(Value: bool) -> None: ...
    @RibbonShowObscure.setter
    def RibbonShowObscure(Value: bool) -> None: ...
    @RibbonVisible.setter
    def RibbonVisible(Value: bool) -> None: ...
    @ShowTutorials.setter
    def ShowTutorials(Value: bool) -> None: ...
    @TemplateFile.setter
    def TemplateFile(Value: str) -> None: ...
    @TooltipWiggleRadius.setter
    def TooltipWiggleRadius(Value: int) -> None: ...
    @TrackFileStamps.setter
    def TrackFileStamps(value: bool) -> None: ...
    @TrackPluginLoading.setter
    def TrackPluginLoading(value: bool) -> None: ...
    @TryDownloadMissingPlugins.setter
    def TryDownloadMissingPlugins(value: bool) -> None: ...
    def SetLoadMechanism(pluginName: str, mechanism: GH_LoadingDemand) -> None: ...
    def SetLoadProtected(pluginName: str, loadProtect: bool) -> None: ...
    def UserOkayWithBakingInvalidObject(objectType: str) -> bool: ...


class ComponentCascadeMenusChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class CreateSolutionUndoRecordChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...






class EtoExtensions:
    @overload
    def ToEto(control: Control) -> Control: ...
    @overload
    def ToEto(control: Form) -> Window: ...
    @overload
    def ToEto(sdcolor: Color) -> Color: ...
    @overload
    def ToEto(font: Font) -> Font: ...
    @overload
    def ToEto(point: Point) -> Point: ...
    @overload
    def ToSD(rectangle: Rectangle) -> Rectangle: ...
    @overload
    def ToSD(size: Size) -> Size: ...
    @overload
    def ToSD(point: Point) -> Point: ...
    @overload
    def ToSD(color: Color) -> Color: ...
    @overload
    def ToSD(font: Font) -> Font: ...
    def ToWin32Window(window: Window) -> IWin32Window: ...


class EtoWin32Window:
    @property
    def Handle(self) -> IntPtr: ...


class Folders:
    @property
    def AppDataFolder() -> str: ...
    @property
    def AssemblyFolders() -> List: ...
    @property
    def AutoSaveFolder() -> str: ...
    @property
    def ClusterFolders() -> List: ...
    @property
    def CursorFolder() -> str: ...
    @property
    def CustomAssemblyFolders() -> List: ...
    @property
    def DefaultAssemblyFolder() -> str: ...
    @property
    def DefaultAssemblyFolderVersion6() -> str: ...
    @property
    def DefaultClusterFolder() -> str: ...
    @property
    def DefaultTemplateFolder() -> str: ...
    @property
    def DefaultUserObjectFolder() -> str: ...
    @property
    def Desktop() -> str: ...
    @property
    def DownloaderApplication() -> str: ...
    @property
    def FileViewerApplication() -> str: ...
    @property
    def IconFolder() -> str: ...
    @property
    def ImageStitcherApplication() -> str: ...
    @property
    def PluginFolder() -> str: ...
    @property
    def SDKDownloaderApplication() -> str: ...
    @property
    def SettingsFolder() -> str: ...
    @property
    def TemplateFolders() -> List: ...
    @property
    def ToolsFolder() -> str: ...
    @property
    def TutorialFiles() -> Set(str): ...
    @property
    def TutorialFolder() -> str: ...
    @property
    def UserObjectFolders() -> List: ...
    @property
    def VersionHistoryFile() -> str: ...
    @property
    def VersionHistoryUrl() -> str: ...
    @CustomAssemblyFolders.setter
    def CustomAssemblyFolders(Value: List) -> None: ...
    def ShowFolderInExplorer(folder: str) -> None: ...


class FormattingChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class Global_Proc:
    @property
    def Settings() -> GH_SettingsServer: ...
    @property
    def Version() -> GH_Version: ...
    @overload
    def UiAdjust(value: int) -> int: ...
    @overload
    def UiAdjust(value: Single) -> Single: ...


class Instances:
    def add_CanvasCreated(obj: CanvasCreatedEventHandler) -> None: ...
    def add_CanvasDestroyed(obj: CanvasDestroyedEventHandler) -> None: ...
    def DocumentEditorFadeIn() -> None: ...
    def DocumentEditorFadeOut() -> None: ...
    def EnforceInvariantCulture() -> None: ...
    @property
    def ActiveCanvas() -> GH_Canvas: ...
    @property
    def AutoHideBanner() -> bool: ...
    @property
    def AutoShowBanner() -> bool: ...
    @property
    def BakeIcon24() -> Bitmap: ...
    @property
    def ComponentServer() -> GH_ComponentServer: ...
    @property
    def CursorServer() -> GH_CursorServer: ...
    @property
    def DocumentAssociationServer() -> GH_DocumentAssociations: ...
    @property
    def DocumentEditor() -> GH_DocumentEditor: ...
    @property
    def DocumentServer() -> GH_DocumentServer: ...
    @property
    def EtoDocumentEditor() -> Window: ...
    @property
    def GrasshopperPluginId() -> Guid: ...
    @property
    def IsComponentServer() -> bool: ...
    @property
    def IsCursorServer() -> bool: ...
    @property
    def IsDocumentAssociationServer() -> bool: ...
    @property
    def IsDocumentEditor() -> bool: ...
    @property
    def IsDocumentEditorOnTopOfViewports() -> bool: ...
    @property
    def IsDocumentServer() -> bool: ...
    @property
    def IsMarkovChain() -> bool: ...
    @property
    def IsMruServer() -> bool: ...
    @property
    def IsRemotePanelVisible() -> bool: ...
    @property
    def MarkovChain() -> GH_MarkovChain: ...
    @property
    def MruServer() -> GH_MRU_Server: ...
    @property
    def RcpPanel() -> RemoteControlPanel: ...
    @property
    def RunningHeadless() -> bool: ...
    @property
    def Settings() -> GH_SettingsServer: ...
    def HideRemotePanel() -> bool: ...
    def InvalidateCanvas() -> None: ...
    def MyTypes() -> Set(Type): ...
    def RedrawAll() -> None: ...
    def RedrawCanvas() -> None: ...
    def ReloadMemoryAssemblies() -> List: ...
    def remove_CanvasCreated(obj: CanvasCreatedEventHandler) -> None: ...
    def remove_CanvasDestroyed(obj: CanvasDestroyedEventHandler) -> None: ...
    @AutoHideBanner.setter
    def AutoHideBanner(AutoPropertyValue: bool) -> None: ...
    @AutoShowBanner.setter
    def AutoShowBanner(AutoPropertyValue: bool) -> None: ...
    def ShowRemotePanel() -> bool: ...
    def UnloadAllObjects() -> None: ...


class LoadMechanismChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, pluginName: str, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, pluginName: str) -> None: ...


class LoadProtectionChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, pluginName: str, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self, pluginName: str) -> None: ...


class PreviewBumpZBufferChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class PreviewGumballsChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class PreviewMeshEdgesChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class PreviewPlaneRadiusChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class PreviewPointStyleChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class PruderyLevelChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class RibbonAllIconsChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class RibbonDrawTabIconsChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class RibbonSeparatorsChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class RibbonVisibleChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class TemplateFileChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class TooltipWiggleRadiusChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class Tracing:
    @overload
    def Assert(assert_id: Guid) -> None: ...
    @overload
    def Assert(assert_id: Guid, message: str) -> None: ...
    @overload
    def Assert(assert_id: Guid, exception: Exception) -> None: ...
    @overload
    def Assert(assert_id: Guid, message: str, exception: Exception) -> None: ...
    def DebugLogAddEntry(message: str) -> None: ...
    def DebugLogBeginBlock(name: str) -> None: ...
    def DebugLogEndBlock() -> None: ...


class UiScaleChangedEventHandler:
    def __init__(self, TargetObject: Object, TargetMethod: IntPtr): ...
    def BeginInvoke(self, DelegateCallback: AsyncCallback, DelegateAsyncState: Object) -> IAsyncResult: ...
    def EndInvoke(self, DelegateAsyncResult: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class Utility:
    @overload
    def FixNewlines(text: str) -> str: ...
    @overload
    def FixNewlines(text: str, newLinePattern: str) -> str: ...
    def InvokeDownloader(sourceUri: str, targetUri: str, silent: bool) -> None: ...
    def InvokeGetter(target: Object, property: str) -> Object: ...
    def InvokeGetterSafe(target: Object, property: str) -> Object: ...
    @overload
    def InvokeMethod(target: Object, method: str) -> Object: ...
    @overload
    def InvokeMethod(target: Object, method: str, params: Set(Object)) -> Object: ...
    @overload
    def InvokeMethodSafe(target: Object, method: str) -> Object: ...
    @overload
    def InvokeMethodSafe(target: Object, method: str, params: Set(Object)) -> Object: ...
    def InvokeSetter(target: Object, property: str, value: Object) -> None: ...
    def InvokeSetterSafe(target: Object, property: str, value: Object) -> None: ...
    def LikeOperator(text: str, pattern: str) -> bool: ...


class Versioning:
    @property
    def BuildDate() -> str: ...
    @property
    def Version() -> GH_Version: ...
    @property
    def VersionString() -> str: ...
    def SyncVersionHistoryData() -> None: ...
    def VersionHistoryData() -> Set(str): ...

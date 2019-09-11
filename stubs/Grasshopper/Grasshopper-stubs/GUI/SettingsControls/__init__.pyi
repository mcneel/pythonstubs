from typing import Tuple, Set, Iterable, List


class GH_AlignWidgetFrontEnd:
    def __init__(self): ...


class GH_AuthorSettings_FrontEnd:
    def __init__(self): ...


class GH_AutoSaveSettingsFrontEnd:
    def __init__(self): ...


class GH_CanvasOverlaySettingsFrontEnd:
    def __init__(self): ...


class GH_CanvasSettings_FrontEnd:
    def __init__(self): ...


class GH_CompassWidgetFrontEnd:
    def __init__(self): ...


class GH_DocumentPreviewColourSettingsFrontEnd:
    def __init__(self): ...


class GH_FontFamilySettingsFrontEnd:
    def __init__(self): ...
    def RepresentsStandardFamily(self) -> None: ...
    def RepresentsScriptFamily(self) -> None: ...
    def RepresentsConsoleFamily(self) -> None: ...


class GH_GHALoadingOptionsFrontEnd(GH_DoubleBufferedPanel):
    def __init__(self): ...


class GH_MenuShortcutFrontEnd:
    def __init__(self): ...


class GH_MessageWidgetFrontEnd:
    def __init__(self): ...


class GH_NumberFormattingSettingsFrontEnd:
    def __init__(self): ...


class GH_ObjectMenuSettingsFrontEnd:
    def __init__(self): ...


class GH_DefaultPreviewColourSettingsFrontEnd:
    def __init__(self): ...


class GH_PreviewSettingsFrontEnd:
    def __init__(self): ...


class GH_PruderySettingsFrontEnd:
    def __init__(self): ...


class GH_RecentFilesSettingsFrontEnd:
    def __init__(self): ...


class GH_GenericCapsulePaletteSettings:
    def __init__(self): ...
    @property
    def Palette(self) -> GH_PaletteStyle: ...
    @Palette.setter
    def Palette(self, Value: GH_PaletteStyle) -> None: ...


class GH_MarkovWidgetSettingFrontEnd:
    def __init__(self): ...


class GH_ProfilerWidgetFrontEnd:
    def __init__(self): ...


class GH_RibbonSettingsFrontEnd:
    def __init__(self): ...


class GH_SolverSettings_FrontEnd:
    def __init__(self): ...


class GH_TemplateFileSettings:
    def __init__(self): ...


class GH_TooltipSettings_FrontEnd:
    def __init__(self): ...


class GH_ZuiZoomFrontEnd:
    def __init__(self): ...

from typing import Tuple, Set, Iterable, List


class StaticIconType:
    OpenDirectory = 0
    CloseDirectory = 1


class IconSize:
    Large = 0
    Small = 1


class SystemIcons:
    def GetFileIcon(fileName: str, size: IconSize) -> Icon: ...
    def GetStaticIcon(type: StaticIconType, size: IconSize) -> Icon: ...


class IHandler:
    def GetFileIcon(self, fileName: str, size: IconSize) -> Icon: ...
    def GetStaticIcon(self, type: StaticIconType, size: IconSize) -> Icon: ...

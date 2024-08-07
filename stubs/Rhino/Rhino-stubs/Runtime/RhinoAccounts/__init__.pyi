from typing import Tuple, Set, Iterable, List, overload


class IOAuth2Token:
    @property
    def Exp(self) -> Nullable: ...
    @property
    def IsExpired(self) -> bool: ...
    @property
    def RawToken(self) -> str: ...
    @property
    def Scope(self) -> IReadOnlyCollection: ...


class IOpenIDConnectToken:
    @property
    def AdminGroups(self) -> IReadOnlyDictionary: ...
    @property
    def AllGroups(self) -> IReadOnlyDictionary: ...
    @property
    def AtHash(self) -> str: ...
    @property
    def Aud(self) -> str: ...
    @property
    def AuthTime(self) -> Nullable: ...
    @property
    def Emails(self) -> IReadOnlyCollection: ...
    @property
    def EmailVerified(self) -> Nullable: ...
    @property
    def Exp(self) -> Nullable: ...
    @property
    def Iat(self) -> Nullable: ...
    @property
    def IsExpired(self) -> bool: ...
    @property
    def Iss(self) -> str: ...
    @property
    def IsUpdated(self) -> bool: ...
    @property
    def Locale(self) -> str: ...
    @property
    def MemberGroups(self) -> IReadOnlyDictionary: ...
    @property
    def Name(self) -> str: ...
    @property
    def Nonce(self) -> str: ...
    @property
    def OwnerGroups(self) -> IReadOnlyDictionary: ...
    @property
    def Phone(self) -> str: ...
    @property
    def Picture(self) -> str: ...
    @property
    def RawToken(self) -> str: ...
    @property
    def Sub(self) -> str: ...
    @property
    def UpdatedAt(self) -> Nullable: ...


class IRhinoAccountsManager:
    def ExecuteProtectedCode(self, protectedCode: Action) -> None: ...
    def ExecuteProtectedCodeAsync(self, protectedCode: Func) -> Task: ...
    @overload
    def GetAuthTokensAsync(self, clientId: str, clientSecret: str, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def GetAuthTokensAsync(self, clientId: str, clientSecret: str, scope: Iterable[str], prompt: str, maxAge: Nullable, showUI: bool, progress: IProgress, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    def RevokeAuthTokenAsync(self, oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def TryGetAuthTokens(self, clientId: str, secretKey: SecretKey) -> Tuple: ...
    @overload
    def TryGetAuthTokens(self, clientId: str, scope: Iterable[str], secretKey: SecretKey) -> Tuple: ...
    def UpdateOpenIDConnectTokenAsync(self, currentToken: IOpenIDConnectToken, oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...


class ProgressState:
    AwaitingLogin = 0
    RetrievingTokens = 1
    AwaitingRedirect = 2
    Other = 3


class RhinoAccoountsProgressInfo:
    def __init__(self, state: ProgressState, metadata: Dictionary, customDescription: str): ...
    @property
    def Description(self) -> str: ...
    @property
    def Metadata(self) -> Dictionary: ...
    @property
    def State(self) -> ProgressState: ...


class RhinoAccountsAuthTokenMismatchException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, currentUsername: str, newUsername: str, innerException: Exception): ...


class RhinoAccountsCannotListenException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsException:
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsGroup:
    def __init__(self, id: str, name: str): ...
    @property
    def Id(self) -> str: ...
    @property
    def Name(self) -> str: ...


class RhinoAccountsInvalidResponseException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsInvalidStateException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsInvalidTokenException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsManager:
    def ExecuteProtectedCode(protectedCode: Action) -> None: ...
    def ExecuteProtectedCodeAsync(protectedCode: Func) -> Task: ...
    @overload
    def GetAuthTokensAsync(clientId: str, clientSecret: str, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def GetAuthTokensAsync(clientId: str, clientSecret: str, scope: Iterable[str], prompt: str, maxAge: Nullable, showUI: bool, progress: IProgress, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    def RevokeAuthTokenAsync(oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def TryGetAuthTokens(clientId: str, secretKey: SecretKey) -> Tuple: ...
    @overload
    def TryGetAuthTokens(clientId: str, scope: Iterable[str], secretKey: SecretKey) -> Tuple: ...
    def UpdateOpenIDConnectTokenAsync(currentToken: IOpenIDConnectToken, oauth2Token: IOAuth2Token, secretKey: SecretKey, cancellationToken: CancellationToken) -> Task: ...


class RhinoAccountsOperationInProgressException(RhinoAccountsException):
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, assembly: Assembly, innerException: Exception): ...


class RhinoAccountsProxyException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsServerException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RhinoAccountsServerNotReachableException(RhinoAccountsException):
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class SecretKey:
    def __init__(self): ...

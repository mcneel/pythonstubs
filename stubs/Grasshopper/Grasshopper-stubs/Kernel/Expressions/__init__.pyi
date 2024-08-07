from typing import Tuple, Set, Iterable, List, overload


class GH_CharType:
    undefined = 0
    whitespace = 1
    dot = 2
    comma = 3
    colon = 4
    semicolon = 5
    continuation = 6
    newline = 7
    operator = 20
    parenthesis_open = 21
    parenthesis_close = 22
    bracket_open = 23
    bracket_close = 24
    stringstart = 50
    stringend = 51
    stringbody = 52
    commentstart = 60
    commentend = 61
    commentbody = 62


class GH_CodeString:
    def __init__(self, input: str): ...
    def Flatten(self) -> str: ...
    @property
    def Segments(self) -> List: ...
    def ParseNewString(self, input: str) -> None: ...
    def Replace(self, search: str, replace: str, bIgnoreCase: bool, bOmitNonCode: bool) -> None: ...
    def ReplaceToken(self, search: str, replace: str, bIgnoreCase: bool, bOmitNonCode: bool) -> None: ...


class GH_CodeStringSegment:
    def __init__(self, nString: str, bIsCode: bool): ...
    @property
    def IsCode(self) -> bool: ...
    @property
    def String(self) -> str: ...
    @property
    def StringValue(self) -> str: ...
    def Replace(self, search: str, replace: str, bIgnoreCase: bool) -> None: ...
    def ReplaceToken(self, token: str, replace: str, bIgnoreCase: bool) -> None: ...
    @IsCode.setter
    def IsCode(self, Value: bool) -> None: ...
    @String.setter
    def String(self, Value: str) -> None: ...
    def ToString(self) -> str: ...


class GH_ExpressionParser:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, bThrowExceptions: bool): ...
    @overload
    def AddVariable(self, name: str, val: bool) -> None: ...
    @overload
    def AddVariable(self, name: str, val: int) -> None: ...
    @overload
    def AddVariable(self, name: str, val: float) -> None: ...
    @overload
    def AddVariable(self, name: str, val: Complex) -> None: ...
    @overload
    def AddVariable(self, name: str, val: str) -> None: ...
    @overload
    def AddVariable(self, name: str, val: Vector3d) -> None: ...
    @overload
    def AddVariable(self, name: str, val: Point3d) -> None: ...
    @overload
    def AddVariable(self, name: str, val: Plane) -> None: ...
    @overload
    def AddVariableEx(self, name: str, val: IGH_Goo) -> None: ...
    @overload
    def AddVariableEx(self, name: str, val: GH_Variant) -> None: ...
    def BalancedCharTest(str: str, char_open: Char, char_close: Char) -> Tuple[bool, int]: ...
    def CachedSymbols(self) -> Queue: ...
    def CacheSymbols(self, Expression: str) -> bool: ...
    def ClearSymbols(self) -> None: ...
    def ClearVariables(self) -> None: ...
    def DisplayFunctionList(self, wnd: IWin32Window) -> None: ...
    @overload
    def Evaluate(self) -> GH_Variant: ...
    @overload
    def Evaluate(self, qHint: Queue) -> GH_Variant: ...
    @overload
    def Evaluate(self, expression: str) -> GH_Variant: ...
    @property
    def ThrowExceptions(self) -> bool: ...
    @property
    def Variables(self) -> SortedDictionary: ...
    def IsValidVariableName(name: str) -> bool: ...
    @ThrowExceptions.setter
    def ThrowExceptions(self, Value: bool) -> None: ...


class GH_ExpressionString:
    def __init__(self, in: str): ...
    def BuildLUT(self) -> None: ...
    @property
    def Char(self, index: int) -> Char: ...
    @property
    def Next(self, index: int) -> Char: ...
    @property
    def Prev(self, index: int) -> Char: ...
    def IsWhiteSpace(self, index: int) -> bool: ...
    def ToString(self) -> str: ...


class GH_ExpressionSyntaxWriter:
    def RewriteAll(Expression: str) -> str: ...
    @overload
    def RewriteForEvaluator(Expression: str) -> str: ...
    @overload
    def RewriteForEvaluator(sCode: GH_CodeString) -> None: ...
    @overload
    def RewriteForGraphicInterface(expression: str) -> str: ...
    @overload
    def RewriteForGraphicInterface(code: GH_CodeString) -> None: ...


class GH_OperatorType:
    UnaryOnLeft = 0
    UnaryOnRight = 1
    Binary = 2


class GH_ParserOperator:
    def __init__(self, name: str, symbol: Char, precedence: GH_ParserPrecedence, type: GH_OperatorType, description: str): ...
    def CompareTo(self, other: GH_ParserOperator) -> int: ...
    def Equals(self, obj: Object) -> bool: ...


class GH_ParserPrecedence:
    #None = 0
    Level0 = 1
    Level1 = 2
    Level2 = 3
    Level3 = 4
    Level4 = 5
    Level5 = 6
    Invalid = -1


class GH_ParserSymbol:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, token: str, class: GH_ParserTokenClass, level: GH_ParserPrecedence): ...
    def CompareTo(self, other: GH_ParserSymbol) -> int: ...
    def Equals(self, obj: Object) -> bool: ...
    def ToString(self) -> str: ...


class GH_ParserTokenClass:
    Keyword = 1
    Identifier = 2
    Numeric = 3
    Literal = 4
    Operator = 5
    Punctuation = 6


class GH_ScriptVariant:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, val: float): ...
    @overload
    def __init__(self, val: int): ...
    @overload
    def __init__(self, val: Byte): ...
    @overload
    def __init__(self, val: bool): ...
    @overload
    def __init__(self, val: str): ...
    @overload
    def __init__(self, val: DateTime): ...
    @overload
    def __init__(self, val: Point3d): ...
    @overload
    def __init__(self, val: Vector3d): ...
    @overload
    def __init__(self, val: Plane): ...
    @property
    def Boolean(self) -> bool: ...
    @property
    def DateTime(self) -> DateTime: ...
    @property
    def Double(self) -> float: ...
    @property
    def Integer(self) -> int: ...
    @property
    def Object(self) -> Object: ...
    @property
    def Plane(self) -> Plane: ...
    @property
    def Point(self) -> Point3d: ...
    @property
    def String(self) -> str: ...
    @property
    def Type(self) -> GH_ScriptVariantType: ...
    @property
    def Vector(self) -> Vector3d: ...
    def op_Addition(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_BitwiseAnd(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_BitwiseOr(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_Concatenate(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_Division(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_Equality(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_ExclusiveOr(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> Point3d: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> str: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> float: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> int: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> bool: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> Plane: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> Vector3d: ...
    @overload
    def op_Explicit(in: GH_ScriptVariant) -> DateTime: ...
    def op_Exponent(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_False(A: GH_ScriptVariant) -> bool: ...
    def op_GreaterThan(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_GreaterThanOrEqual(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    @overload
    def op_Implicit(in: Plane) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: Point3d) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: DateTime) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: str) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: float) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: int) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: Vector3d) -> GH_ScriptVariant: ...
    @overload
    def op_Implicit(in: bool) -> GH_ScriptVariant: ...
    def op_Inequality(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_IntegerDivision(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_LeftShift(A: GH_ScriptVariant, B: int) -> GH_ScriptVariant: ...
    def op_LessThan(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_LessThanOrEqual(A: GH_ScriptVariant, B: GH_ScriptVariant) -> bool: ...
    def op_Modulus(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_Multiply(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_OnesComplement(A: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_RightShift(A: GH_ScriptVariant, B: int) -> GH_ScriptVariant: ...
    def op_Subtraction(A: GH_ScriptVariant, B: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_True(A: GH_ScriptVariant) -> bool: ...
    def op_UnaryNegation(A: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def op_UnaryPlus(A: GH_ScriptVariant) -> GH_ScriptVariant: ...
    def ToString(self) -> str: ...


class GH_ScriptVariantType:
    nothing = 0
    boolean = 1
    integer = 2
    double = 3
    string = 5
    datetime = 6
    point = 10
    vector = 11
    plane = 12
    object = 20


class GH_SignatureException:
    def __init__(self, args: List, name: str): ...
    @property
    def Message(self) -> str: ...


class GH_SolverException:
    def __init__(self, nMessage: str): ...


class GH_SyntaxException:
    def __init__(self, nMessage: str): ...


class GH_Variant:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: bool): ...
    @overload
    def __init__(self, value: int): ...
    @overload
    def __init__(self, value: float): ...
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, value: Complex): ...
    @overload
    def __init__(self, value: Point3d): ...
    @overload
    def __init__(self, value: Vector3d): ...
    @overload
    def __init__(self, value: Plane): ...
    @overload
    def __init__(self, other: GH_Variant): ...
    def Data(self) -> T: ...
    def Duplicate(self) -> GH_Variant: ...
    def Evaluate(self) -> bool: ...
    @property
    def _Bool(self) -> bool: ...
    @property
    def _Complex(self) -> Complex: ...
    @property
    def _Double(self) -> float: ...
    @property
    def _Int(self) -> int: ...
    @property
    def _Plane(self) -> Plane: ...
    @property
    def _Point(self) -> Point3d: ...
    @property
    def _String(self) -> str: ...
    @property
    def _Vector(self) -> Vector3d: ...
    @property
    def IsNumeric(self) -> bool: ...
    @property
    def Type(self) -> GH_VariantType: ...
    def ToGoo(self) -> IGH_Goo: ...
    def ToString(self) -> str: ...


class GH_VariantType:
    null = 0
    bool = 1
    int = 2
    double = 4
    string = 8
    point = 16
    plane = 32
    complex = 64
    unknown = -1

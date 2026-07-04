# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,10,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,
        7,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,
        8,5,0,0,1,8,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'double'", "'String'", "'Boolean'", 
                     "'public'", "'class'", "'System'", "'while'", "'do'", 
                     "'new'", "'static'", "'void'", "'break'", "'true'", 
                     "'for'", "'false'", "'>'", "'<'", "'<='", "'>='", "'='", 
                     "'=='", "'!='", "'++'", "'--'", "'+'", "'-'", "'/'", 
                     "'*'", "'%'", "'&&'", "'||'", "'.'", "';'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INT", "DOUBLE", "STRING", "BOOLEAN", 
                      "PUBLIC", "CLASS", "SYSTEM", "WHILE", "DO", "NEW", 
                      "STATIC", "VOID", "BREAK", "TRUE", "FOR", "FALSE", 
                      "MAYOR", "MENOR", "MENOR_IGUAL", "MAYOR_IGUAL", "ASIGNACION", 
                      "IGUAL_QUE", "DIFERENTE_QUE", "SUMA_U", "RESTA_U", 
                      "SUMA", "RESTA", "DIVISION", "MULTIPLICACION", "MODULO", 
                      "AND", "OR", "PUNTO", "PUNTO_COMA", "PAR_ABRE", "PAR_CIE", 
                      "COR_ABRE", "COR_CIE", "LLA_ABRE", "LLA_CIE", "ENTERO", 
                      "DECIMAL", "ID", "CADENA", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    INT=1
    DOUBLE=2
    STRING=3
    BOOLEAN=4
    PUBLIC=5
    CLASS=6
    SYSTEM=7
    WHILE=8
    DO=9
    NEW=10
    STATIC=11
    VOID=12
    BREAK=13
    TRUE=14
    FOR=15
    FALSE=16
    MAYOR=17
    MENOR=18
    MENOR_IGUAL=19
    MAYOR_IGUAL=20
    ASIGNACION=21
    IGUAL_QUE=22
    DIFERENTE_QUE=23
    SUMA_U=24
    RESTA_U=25
    SUMA=26
    RESTA=27
    DIVISION=28
    MULTIPLICACION=29
    MODULO=30
    AND=31
    OR=32
    PUNTO=33
    PUNTO_COMA=34
    PAR_ABRE=35
    PAR_CIE=36
    COR_ABRE=37
    COR_CIE=38
    LLA_ABRE=39
    LLA_CIE=40
    ENTERO=41
    DECIMAL=42
    ID=43
    CADENA=44
    WS=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






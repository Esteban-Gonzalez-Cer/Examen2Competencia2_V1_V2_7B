grammar Expr;
root: expr EOF;
expr: EOF;
XML_FORMAT: '<?'.*?'?>';

COMENTARIO: '<!--'.*?'-->';

AMP: '&amp;';
LT: '&lt;';
QUOT: '&quot;';
APOS: '&apos;';
GT:'&gt;';
CDATA: '<![CDATA['.*?']]>';
ABRIR: '<';
CERRAR_AUTO: '/>';
CERRAR: '>';
DIAGONAL: '/';
IGUAL: '=';
NOMBRE: [A-Za-z_:]+[A-Za-z_-]*;
CONTENIDO: ~[<>& \t\r\n]+;
CADENA: '"'~[\t\n]*'"';
 
WS: [ \t\n\r]+ -> skip;


# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = '2DUP ADD CHAR CONDICIONAL1 CONDICIONAL2 CR DASHDASH DIVIDE DOT EMIT FUNCTION FUNCTION_STRING ID INF INFEQ MINUS MINUS_MINUS MOD NEWLINE NOT NUMBER SPACE STRING SUP SUPEQ TIMESprogram : statementsstatements : statements statement\n                  | statementstatement : function_declaration\n                 | expressiontypes\n                 | function_dot\n                 | arithmetic_expression\n                 | comparison_expression\n                 | function_string\n                 | function_char\n                 | function_emit\n                 | space\n                 | cr\n                 | 2dup\n                 | condicinal1\n                 | condicinal2\n    function_declaration : FUNCTION\n    cr : CRfunction_char : CHARspace : SPACEfunction_string : FUNCTION_STRINGfunction_emit : EMITexpressiontypes : NUMBER function_dot : DOTarithmetic_expression : statement statement arithmetic_oparithmetic_op : ADD\n                     | MINUS\n                     | TIMES\n                     | DIVIDE\n                     | MODcomparison_expression : statement statement comparison_opcondicinal1 : CONDICIONAL1condicinal2 : CONDICIONAL22dup : 2DUPcomparison_op : INF\n                     | INFEQ\n                     | SUP\n                     | SUPEQ'
    
_lr_action_items = {'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[17,17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,17,17,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[18,18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,18,18,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'DOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[19,19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,19,19,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'FUNCTION_STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[20,20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,20,20,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'CHAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[21,21,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,21,21,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'EMIT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[22,22,22,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,22,22,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'SPACE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[23,23,23,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,23,23,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'CR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[24,24,24,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,24,24,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'2DUP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[25,25,25,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,25,25,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'CONDICIONAL1':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[26,26,26,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,26,26,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'CONDICIONAL2':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[27,27,27,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,27,27,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,-2,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'ADD':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,32,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'MINUS':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,33,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'TIMES':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,34,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'DIVIDE':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,35,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'MOD':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,36,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'INF':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,37,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'INFEQ':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,38,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'SUP':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,39,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),'SUPEQ':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-23,-24,-21,-19,-22,-20,-18,-34,-32,-33,40,-25,-31,-26,-27,-28,-29,-30,-35,-36,-37,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,],[2,]),'statement':([0,2,3,28,29,],[3,28,29,29,29,]),'function_declaration':([0,2,3,28,29,],[4,4,4,4,4,]),'expressiontypes':([0,2,3,28,29,],[5,5,5,5,5,]),'function_dot':([0,2,3,28,29,],[6,6,6,6,6,]),'arithmetic_expression':([0,2,3,28,29,],[7,7,7,7,7,]),'comparison_expression':([0,2,3,28,29,],[8,8,8,8,8,]),'function_string':([0,2,3,28,29,],[9,9,9,9,9,]),'function_char':([0,2,3,28,29,],[10,10,10,10,10,]),'function_emit':([0,2,3,28,29,],[11,11,11,11,11,]),'space':([0,2,3,28,29,],[12,12,12,12,12,]),'cr':([0,2,3,28,29,],[13,13,13,13,13,]),'2dup':([0,2,3,28,29,],[14,14,14,14,14,]),'condicinal1':([0,2,3,28,29,],[15,15,15,15,15,]),'condicinal2':([0,2,3,28,29,],[16,16,16,16,16,]),'arithmetic_op':([29,],[30,]),'comparison_op':([29,],[31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','forthYacc.py',9),
  ('statements -> statements statement','statements',2,'p_statements','forthYacc.py',13),
  ('statements -> statement','statements',1,'p_statements','forthYacc.py',14),
  ('statement -> function_declaration','statement',1,'p_statement','forthYacc.py',23),
  ('statement -> expressiontypes','statement',1,'p_statement','forthYacc.py',24),
  ('statement -> function_dot','statement',1,'p_statement','forthYacc.py',25),
  ('statement -> arithmetic_expression','statement',1,'p_statement','forthYacc.py',26),
  ('statement -> comparison_expression','statement',1,'p_statement','forthYacc.py',27),
  ('statement -> function_string','statement',1,'p_statement','forthYacc.py',28),
  ('statement -> function_char','statement',1,'p_statement','forthYacc.py',29),
  ('statement -> function_emit','statement',1,'p_statement','forthYacc.py',30),
  ('statement -> space','statement',1,'p_statement','forthYacc.py',31),
  ('statement -> cr','statement',1,'p_statement','forthYacc.py',32),
  ('statement -> 2dup','statement',1,'p_statement','forthYacc.py',33),
  ('statement -> condicinal1','statement',1,'p_statement','forthYacc.py',34),
  ('statement -> condicinal2','statement',1,'p_statement','forthYacc.py',35),
  ('function_declaration -> FUNCTION','function_declaration',1,'p_function_declaration','forthYacc.py',41),
  ('cr -> CR','cr',1,'p_cr','forthYacc.py',113),
  ('function_char -> CHAR','function_char',1,'p_function_char','forthYacc.py',118),
  ('space -> SPACE','space',1,'p_space','forthYacc.py',127),
  ('function_string -> FUNCTION_STRING','function_string',1,'p_function_string','forthYacc.py',132),
  ('function_emit -> EMIT','function_emit',1,'p_function_emit','forthYacc.py',143),
  ('expressiontypes -> NUMBER','expressiontypes',1,'p_expressiontypes','forthYacc.py',152),
  ('function_dot -> DOT','function_dot',1,'p_function_dot','forthYacc.py',168),
  ('arithmetic_expression -> statement statement arithmetic_op','arithmetic_expression',3,'p_arithmetic_expression','forthYacc.py',183),
  ('arithmetic_op -> ADD','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',225),
  ('arithmetic_op -> MINUS','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',226),
  ('arithmetic_op -> TIMES','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',227),
  ('arithmetic_op -> DIVIDE','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',228),
  ('arithmetic_op -> MOD','arithmetic_op',1,'p_arithmetic_op','forthYacc.py',229),
  ('comparison_expression -> statement statement comparison_op','comparison_expression',3,'p_comparison_expression','forthYacc.py',233),
  ('condicinal1 -> CONDICIONAL1','condicinal1',1,'p_condicinal1','forthYacc.py',272),
  ('condicinal2 -> CONDICIONAL2','condicinal2',1,'p_condicinal2','forthYacc.py',281),
  ('2dup -> 2DUP','2dup',1,'p_2dup','forthYacc.py',290),
  ('comparison_op -> INF','comparison_op',1,'p_comparison_op','forthYacc.py',309),
  ('comparison_op -> INFEQ','comparison_op',1,'p_comparison_op','forthYacc.py',310),
  ('comparison_op -> SUP','comparison_op',1,'p_comparison_op','forthYacc.py',311),
  ('comparison_op -> SUPEQ','comparison_op',1,'p_comparison_op','forthYacc.py',312),
]
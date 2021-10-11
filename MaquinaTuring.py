"""
Tape
Cabezal (apuntador,simboloa sobreescribir,izquierda-derecha-izquierda)
Registro de estados
Tabla de transiciones
La maquina de turing tiene las caracteristicas de un Automata finito

Q = Es un conjunto de estados
    Î£ = Alfabeto conjunto de caracteres (codigo utf-8 ="\u03A3")	
    Î“ = Simbolos de la cinta
    s = Estado inicial sÏµQ
    Î´= Reglas nde transicion (Codigo utf-8 = "\u03B4")
    QxÎ£->Q Reglas de transicion
    bÏµÎ“ = es un simbolo denominado blanco, que se puede repetir 
          infinitamente en toda la cinta 
    FâŠ†Q Estado finales o de aceptacion
    
    Q = {s,q1}
    Î£ = {a}	
    Î“ = {a,b}
    s = Estado inicial q0ÏµQ
    Î´= Reglas de transicion 
    Reglas de transicion
    Q x Î£ -> Q
    ((q0,a)->q1*)
    (estado, valor) -> nuevo estado, nuevo valor, direcciÃ³n)
    (s,a)->q1,b,right
    (q1,b)->--Valido--
    "si estamos en el estado s leyendo la posiciÃ³n q1, donde hay 
    escrito el sÃ­mbolo 'a', entonces este sÃ­mbolo debe ser reemplazado 
    por el sÃ­mbolo 'b', y pasar a leer la celda siguiente, a la derecha".
    FâŠ†Q = {q1}
    
    Estructura gafica es un grafo dirigido que se conecta en los vertices 
    con:
        (lee el cabezal/
        sÃ­mbolo que escribirÃ¡ el cabezal, 
        movimiento del cabezal.)
        (s,a)->q1,b,right
        ('a',b,right)
        
"""

def turing_M (state = None, #estados de la maquina de turing
              blank = None, #simbolo blanco de el alfabeto dela cinta
              rules = [],   #reglas de transicion
              tape = [],    #cinta
              final = None,  #estado valido y/o final
              pos = 0):#posicion siguiente de la maquina de turing

    st = state
    if not tape: tape = [blank]
    if pos <0 : pos += len(tape)
    if pos >= len(tape) or pos < 0 : raise print ("Se inicializa mal la posicion")
    
    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)  #Diccionario de datos  
    """
Estado	  Simbolo lei­do	    Si­mbolo escrito	     Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)                R(dr)	         p(s1)
"""
    while True:
        print (st, '\t', end=" ")
        for i, v in enumerate(tape):
             if i==pos: print ("[%s]"%(v,),end=" ")
             else: print (v, end=" ")
        print()
        
        if st == final: break
        if (st, tape[pos]) not in rules: break
        
        (v1,dr,s1) = rules [(st, tape[pos])]
        tape[pos]=v1 #rescribe el simbolo de la cinta
    
    #movimiento del cabezal
        if dr == 'left':
            if pos > 0: pos -= 1
            else: tape.insert(0, blank)
        if dr == 'right':
            pos += 1
            if pos >= len(tape): tape.append(blank)
        st = s1

print("Maquina de turing Test")


#se puede cambiar las reglasde transicion para otra maquina de turing
turing_M (state = 'p', #estado inicial de la maquina de turing
              blank = 'b', #simbolo blanco de el alfabeto dela cinta
              tape = list("1111011111111111"),#inserta los elementos en la cinta
              final = 'q',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "p 1 x right p".split(),
                          "p 0 0 right p".split(),
                          "p b b right q".split(),
                          ]   
                         )
             )    


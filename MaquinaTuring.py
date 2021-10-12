

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

"""#Tercer maquina de turing
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
"""


"""
#Segunda Maquina
turing_M (state = 'q0', #estado inicial de la maquina de turing
              blank = 'z', #simbolo blanco de el alfabeto dela cinta
              tape = list("aaaaaaaaaa"),#inserta los elementos en la cinta
              final = 'q2',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "q0 a 1 right q0".split(),
                          "q0 b 0 right q1".split(),
                          "q1 z z right q2".split(),
                          ]   
                         )
             )    


"""



"""
#Tercer Maquina
turing_M (state = 'q0', #estado inicial de la maquina de turing
              blank = 'z', #simbolo blanco de el alfabeto dela cinta
              tape = list("aaabc"),#inserta los elementos en la cinta
              final = 'q3',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "q0 a a right q0".split(),
                          "q0 b b right q1".split(),
                          "q1 c c right q2".split(),
                          "q2 z z right q3".split(),
                          ]   
                         )
             )    
"""



#Cuarta Maquina
turing_M (state = 'q0', #estado inicial de la maquina de turing
              blank = 'z', #simbolo blanco de el alfabeto dela cinta
              tape = list("abbbcddd"),#inserta los elementos en la cinta
              final = 'q3',  #estado valido y/o final
              rules = map(tuple,#reglas de transicion
                          [
                          "q0 a a right q1".split(),
                          "q1 b b right q1".split(),
                          "q1 c c right q2".split(),
                          "q2 d d right q2".split(),
                          "q2 z z right q3".split(),
                          ]   
                         )
             ) 

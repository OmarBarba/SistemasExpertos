#Modus ponens
print("MODUS PONENS")
# Ejemplo de Modus Ponens 
condicion_1 = True
condicion_2 = True

# Primera regla: Si condicion_1 y condicion_2 son verdaderas, entonces concluimos resultado_1 es verdadero
if condicion_1 and condicion_2:
    resultado_1 = True
    print("Primera regla: Ambas condiciones son verdaderas, por lo tanto, resultado_1 es verdadero.")

# Segunda regla: Si resultado_1 es verdadero, entonces concluimos resultado_final es verdadero
if resultado_1:
    resultado_final = True
    print("Segunda regla: resultado_1 es verdadero, por lo tanto, resultado_final es verdadero.")


#Modus Tollens
print("MODUS TOLLENS")
# Ejemplo de Modus Tollens más largo
condicion_1 = True
condicion_2 = False  # Supongamos que esta condición es falsa

# Primera regla: Si condicion_1 y condicion_2 son falsas, entonces concluimos resultado_1 es falso
if not condicion_1 and not condicion_2:
    resultado_1 = False
    print("Primera regla: Ambas condiciones son falsas, por lo tanto, resultado_1 es falso.")

# Segunda regla: Si resultado_1 es verdadero, entonces concluimos resultado_final es verdadero
if resultado_1:
    resultado_final = True
    print("Segunda regla: resultado_1 es verdadero, por lo tanto, resultado_final es verdadero.")
else:
    # Aplicamos Modus Tollens: Si resultado_final es falso, entonces concluimos que resultado_1 es falso
    resultado_final = False
    print("Segunda regla: resultado_1 es falso, por lo tanto, resultado_final es falso por Modus Tollens.")

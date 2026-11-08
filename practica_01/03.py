#Calculadora de propinas
total_cuenta = 1200.40
prc_propina = 10.00
num_persona = 4

cta_prp = total_cuenta + (total_cuenta * prc_propina)
cta_ppers = cta_prp / num_persona
print(f"El monto total con propina es: S/. {cta_prp:.2f}")
print(f"Cada persona debe pagar: S/. {cta_ppers:.2f}")
if cta_ppers > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")
else:
    print(f"El monto por persona es de S/. {cta_ppers:.2f}")




salarioBase, horasExtras, bonificacion = "2355255 2 1".split()
if horasExtras.isdigit() and bonificacion.isdigit():
    salarioBase = float(salarioBase)
    horasExtras = int(horasExtras)
    bonificacion = int(bonificacion)
    if salarioBase >= 0 and horasExtras >= 0 and bonificacion >= 0:
        valorHora = salarioBase / 193
        valorHoraExtra = valorHora + valorHora * 0.29
        equivalenteBonificacion = 0
        equivalenteHorasExtra = 0
        if bonificacion == 1:
            equivalenteBonificacion = salarioBase * 0.099
        if valorHoraExtra > 0:
            equivalenteHorasExtra = valorHoraExtra * horasExtras
        salarioBase = salarioBase + equivalenteHorasExtra + equivalenteBonificacion
        salarioTotal = salarioBase
        descuentoSalud = salarioTotal * 0.06
        descuentoPension = salarioTotal * 0.03
        decuentoCompensacion = salarioTotal * 0.01
        salarioTotal -= (descuentoSalud +
                         decuentoCompensacion + descuentoPension)
        salarioBase = float(salarioBase)
        salarioBase = round(salarioBase, 1)
        salarioTotal = round(salarioTotal, 1)
        print(salarioBase, salarioTotal)

#programa para calculo de ISR

sueldo =float(input("Digite su sueldo: $ "))
isss= 0
afp= 0
if sueldo<1000:
    isss=sueldo *0.03
else:
    isss=30

afp= sueldo* 0.0725

sg=sueldo-isss-afp
isr=0

if sg>0.01 and sg<=472.00:
    isr=0
elif sg >=472.01 and sg<= 895.24:
    isr=(sg-472)*0.1+17.67

elif sg >=895.25 and sg<= 2038.10:
    isr=(sg-895.24)*0.1+60

elif sg >=2038.11:
    isr=(sg-2038.1)*0.1+288.57
else:
    isr=-1

print(f"El impuesto sobre la renta de ${sueldo:.2f} es: $ {isr:.2f}")
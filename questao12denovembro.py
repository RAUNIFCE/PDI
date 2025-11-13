salario = float(input("digite seu salario"))
salarioantigo=salario
if(salario<280.00):
  salario=salario*1.2
  print("\nsalario antigo",salarioantigo ,"\naumento:20%\nvalor aumentado:",salario-salarioantigo,"\nsalario novo",salario)
elif(salario>=280.00 and salario<700.00):
  salario=salario*1.15
  print("\nsalario antigo",salarioantigo ,"\naumento:15%\nvalor aumentado:",salario-salarioantigo,"\nsalario novo",salario)
elif(salario>=700 and salario<1500):
  salario=salario*1.1
  print("\nsalario antigo",salarioantigo ,"\naumento:10%\nvalor aumentado:",salario-salarioantigo,"\nsalario novo",salario)
elif(salario>=1500):
  salario=salario*1.05
  print("\nsalario antigo",salarioantigo ,"\naumento:5%\nvalor aumentado:",salario-salarioantigo,"\nsalario novo",salario)
  peso = float(input("digite o peso"))
frete=0.0
faixa=0
if(peso<1):
    frete=12.5
    faixa=1
elif(peso>1 and peso<5):
    frete=20.0
    faixa=2
elif(peso>5 and peso<15):
    frete=35.00
    faixa=3
elif(peso>15):
    frete=35.00+(3.00*(peso-15.00))
    faixa=4
print("peso:",peso,"\nfaixa ",faixa,"valor frete:",frete)

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

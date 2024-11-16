from conta import Cliente  
from conta import Data 
from conta import Conta  
from conta import Historico


cliente1=Cliente("Ranier","Sales","12345678-9") 
data1=Data(29,10,2003)
conta1=Conta('123-4',cliente1,120.0,1000.0,data1) 
conta2=Conta('123-5','matheus',500.0,1000.0,data1) 

#conta1.depositar(50)

#print(conta1.saldo) 

##print(conta2.saldo)

#conta1.extrato() 

#conta1.transfere_para(conta2,100)

#conta1.extrato()   

#cliente1=cliente("Ranier","Sales","12345678-9")  

#conta1.extrato()

print(conta1.titular.nome) 
print(conta1.data_abertura.dia) 




#Podemos criar	uma	Conta sem	um	Cliente	?E	um	Cliente	sem	uma	Conta? Sim, porém não poderá ultilizar nada que envolve a class cliente, e o mesmo seria ao contrário


conta1.saca(20)
print(conta1.saldo) 

print(conta1.historico)


conta1.extrato()



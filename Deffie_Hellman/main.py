import primRoot
import sympy
import random
from math import gcd as bltin_gcd

class PrimRoot:
	def __init__(self, arg):
		self.result= primRoot.primRoots(arg)[0]

class Deffie_Hellman:
	def __init__(self, arg):
		self.prange= arg    	
		self.primeN= 0			
		self.g= 0				
		self.private_A= 0		
		self.private_B= 0		
		self.public_A= 0		
		self.public_B= 0		
		self.k_A= 0				
		self.k_B= 0				

	def randomPrime(self,range):
		self.primeN = sympy.randprime(0,self.prange)
		return self.primeN
		
	def initializer(self,prime):
		objc= PrimRoot(prime)
		self.g= objc.result
		self.private_A= random.randint(0,self.primeN)
		self.private_B= random.randint(0,self.primeN)
		self.public_A= pow(self.g,self.private_A,self.primeN)
		self.public_B= pow(self.g,self.private_B,self.primeN)
		print('The Random PRIME Is: ')
		print(self.primeN)
		print('The Smallest Primitive Root Is: ')
		print(self.g)
		print('The Private Key For Alice Is: ')	
		print(self.private_A)
		print('The Private Key For Bob Is: ')
		print(self.private_B)	
		print('The Public Key For Alice Is: ')	
		print(self.public_A)
		print('The Public Key For Bob Is: ')
		print(self.public_B)	

	def verify(self):
		self.k_A= pow(self.public_B,self.private_A,self.primeN)
		self.k_B= pow(self.public_A,self.private_B,self.primeN)
		if (self.k_A == self.k_B):
			print('Verified with the value:')
			print(self.k_A)
		else:
			print('Not Verified')

if __name__ == '__main__':
    print('Enter a range for getting random prime number: ')
    random_P_range= int(input())
    obj= Deffie_Hellman(random_P_range)
    primeR= obj.randomPrime(random_P_range)
    obj.initializer(primeR)
    obj.verify()
    

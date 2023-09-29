class Matriz:
	def __init__(self):
		self.m1=[]
		self.m2=[]
		self.m3=[]
		self.m4=[]
		self.aux=[]
	def matrizNormal(self,n=1):
		if n<4:
			self.m1.append(n)
			n+=1
			self.matrizNormal(n)
		elif n<7:
			self.m2.append(n)
			n+=1
			self.matrizNormal(n)
		elif n<10:
			self.m3.append(n)
			n+=1
			self.matrizNormal(n)
		elif n<13:
			self.m4.append(n)
			n+=1
			self.matrizNormal(n)
		else:
			print(self.m1)
			print(self.m2)
			print(self.m3)
			print(self.m4)
			
	def matrizReversa(self):
		self.m1.reverse
		self.m2.reverse
		self.m3.reverse
		self.m4.reverse
		print(self.m4)
		print(self.m3)
		print(self.m2)
		print(self.m1)
		self.m1.reverse
		self.m2.reverse
		self.m3.reverse
		self.m4.reverse
		
	def caracol(self):
		if len(self.aux)>9:
			self.aux.pop()
			self.caracol()
		elif len(self.aux)>7:
			self.m2[2]=self.aux.pop()
			self.m3[2]=self.aux.pop()
			self.caracol()
		elif len(self.aux)>4:
			for j in range(0,3):
				self.m4.pop()
			for i in range(0,3):
				self.m4.append(self.aux.pop())
			self.m4.reverse()
			self.caracol()
		elif len(self.aux)>2:
			self.m3[0] = self.aux.pop()
			self.m2[0] = self.aux.pop()
			self.caracol()
		elif len(self.aux)>0:
			self.m2[1] = self.aux.pop()
			self.m3[1] = self.aux.pop()
			self.caracol()
		else:
			print(self.m1)
			print(self.m2)
			print(self.m3)
			print(self.m4)
	def ayuda(self):
		self.aux.extend(self.m1)
		self.aux.extend(self.m2)
		self.aux.extend(self.m3)
		self.aux.extend(self.m4)
		self.aux.extend(self.m4)
		self.aux.reverse()
		
matriz=Matriz()
matriz.matrizNormal()
print("\n")
matriz.matrizReversa()
print("\n")
matriz.ayuda()
matriz.caracol()

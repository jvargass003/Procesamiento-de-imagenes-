import numpy as np 
import cv2 
import math
class Operaciones():
	def Translacion(self, img, x_T,y_T):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenTraslacion = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				if(y+y_T)<alto and (x+x_T)<ancho:
					imagenTraslacion[y+y_T,x+x_T] = img[y,x]			
		cv2.imshow("Traslacion", imagenTraslacion)
		cv2.waitKey()

	def Escalado(self, img, s_x, s_y):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenEscalado = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				imagenEscalado[int(y*s_y),int(x*s_x)] = img[y,x]
		cv2.imshow("Escalado", imagenEscalado)
		cv2.waitKey()

	def Rotacion(self,img,angulo):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenRotacion = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				xr = abs(int(x * math.cos(angulo)-y*math.sin(angulo)))
				yr = abs(int(y * math.cos(angulo)+x*math.sin(angulo)))
				if xr > 0 and yr > 0 and xr < ancho and yr < alto:
					imagenRotacion[yr,xr,:] = img[y,x,:]
		cv2.imshow("Rotacion", imagenRotacion)
		cv2.waitKey()

	def RotacionPivote(self,img,angulo,xR,yR):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenRotacionP= np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				xr = abs(int(xR+((x-xR) * math.cos(angulo))-((y-yR)*math.sin(angulo))))
				yr = abs(int(yR+((y-yR) * math.cos(angulo))+((x-xR)*math.sin(angulo))))
				if xr > 0 and yr > 0 and xr < ancho and yr < alto:
					imagenRotacionP[yr,xr,:] = img[y,x,:]

		cv2.imshow("Rotacion Pivote", imagenRotacionP)
		cv2.waitKey()

	def ReflexionX(self, img):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenReflexionx= np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				xn = x * (-1)
				imagenReflexionx[y,xn,:] = img[y,x,:]
		cv2.imshow("Reflexion X", imagenReflexionx)
		cv2.waitKey()

	def ReflexionY(self,img):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenReflexiony= np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				yn = y * (-1)
				imagenReflexiony[yn,x,:] = img[y,x,:]
		cv2.imshow("ReflexionY", imagenReflexiony)
		cv2.waitKey()

	def ReflexionXY(self,img):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenReflexionXY= np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				xn = x * (-1)
				yn = y * (-1)
				imagenReflexionXY[yn,xn,:] = img[y,x,:]

		cv2.imshow("ReflexionXY", imagenReflexionXY)
		cv2.waitKey()

	def Copia(self,img):
		alto, ancho, ncolores = img.shape 
		cv2.imshow("Original", img)
		imagenCopia	= np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				imagenCopia[y,x,:] = img[y,x,:]

		cv2.imshow("Copia", imagenCopia)
		cv2.waitKey()

	def Inversion(self,img):
		alto, ancho, ncolores = img.shape  
		cv2.imshow("Original", img)
		imagenInversion= np.zeros((alto, ancho, 3), np.uint8)		
		L = [255,255,255]
		for y in range (alto):
			for x in range (ancho):
				imagenInversion[y,x,:] = L-img[y,x,:]

		cv2.imshow("Inversion", imagenInversion)
		cv2.waitKey()

	def Brillo(self,img,b):
		alto, ancho, ncolores = img.shape  
		cv2.imshow("Original", img)
		imagenBrillo= np.zeros((alto, ancho, 3), np.uint8)		
		for y in range (alto):
			for x in range (ancho):
				imagenBrillo[y,x,:] = img[y,x,:]+b

		cv2.imshow("Brillo", imagenBrillo)
		cv2.waitKey()

	def Suma(self,img1,img2):
		alto, ancho, ncolores = img1.shape 
		cv2.imshow("Original 1", img1)
		cv2.imshow("Original 2", img2)
		suma = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				suma[y,x,i] = img1[y,x,i]-img2[y,x,i]
		cv2.imshow("Suma", suma)
		cv2.waitKey()

	def Resta(self,img1,img2):
		alto, ancho, ncolores = img1.shape  
		cv2.imshow("Original 1", img1)
		cv2.imshow("Original 2", img2)
		resta = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				resta[y,x] = img1[y,x]-img2[y,x]
		cv2.imshow("Resta", resta)
		cv2.waitKey()

	def Multiplicacion(self,img1,img2):
		alto, ancho, ncolores = img1.shape  
		cv2.imshow("Original 1", img1)
		cv2.imshow("Original 2", img2)
		multiplicacion = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				multiplicacion[y,x] = img1[y,x]*img2[y,x]
		cv2.imshow("Multiplicacion", multiplicacion)
		cv2.waitKey()

	def Division(self,img1,img2):
		alto, ancho, ncolores = img1.shape  
		cv2.imshow("Original 1", img1)
		cv2.imshow("Original 2", img2)
		division = np.zeros((alto, ancho, 3), np.uint8)
		for y in range (alto):
			for x in range (ancho):
				division[y,x] = img1[y,x]/img2[y,x]
		cv2.imshow("Division", division)
		cv2.waitKey()

	def AND(self,img1,img2):
		alto, ancho, ncolores = img1.shape
		cv2.imshow("Original 1", img1)
		cv2.imshow("Original 2", img2)
		andd =  np.zeros((alto, ancho, 3), np.uint8)
		for i in range (alto):
			for j in range (ancho):
				if(img1.item(i,j,0)>0 and img1.item(i,j,1)>0 and img1.item(i,j,2)>0 and img2.item(i,j,0)>0):
					andd[i,j,0] = img1.item(i,j,0)
					andd[i,j,1] = img1.item(i,j,0)
					andd[i,j,2] = img1.item(i,j,0)
				else:
					andd[i,j,:] = 0
		cv2.imshow("AND", andd)
		cv2.waitKey()
	def OR(self,img,img2):
		cv2.imshow("Original 1", img1)
		cv2.imshow("Original 2", img2)
		arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
		for i in range(0,img.shape[0]):
			for j in range(0,img.shape[1]):
				if( img.item(i,j,0)==0 and img.item(i,j,1)==0 and img.item(i,j,2)==0 and img2.item(i,j,0)==0):
					arr[i,j,:] = 0
				if( (img.item(i,j,0)>0 or img.item(i,j,1)>0 or img.item(i,j,2)>0) and img2.item(i,j,0)==0):
					arr[i,j,0] = img.item(i, j,0)
					arr[i,j,1] = img.item(i, j,1)
					arr[i,j,2] = img.item(i, j,2)
				if( (img.item(i,j,0)==0 or img.item(i,j,1)==0 or img.item(i,j,2)==0) and img2.item(i,j,0)>0):
					arr[i,j,0] = img2.item(i, j,0)
					arr[i,j,1] = img2.item(i, j,1)
					arr[i,j,2] = img2.item(i, j,2)
				if( img.item(i,j,0)>0 and img.item(i,j,1)>0 and img.item(i,j,2)>0 and img2.item(i,j,0)>0):
					arr[i,j,0] = img2.item(i, j,0)
					arr[i,j,1] = img2.item(i, j,1)
					arr[i,j,2] = img2.item(i, j,2)
		cv2.imshow("OR", arr)
		cv2.waitKey()

	def NOT(self,img):
		cv2.imshow("Original: ", img)
		arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
		for i in range(0,img.shape[0]):
			for j in range(0,img.shape[1]):
				if( img.item(i,j,0)==0 ):
					arr[i,j,:] = 255
				else:
					arr[i,j,:] = 0   
		cv2.imshow("NOT", arr)
		cv2.waitKey()

operacion = Operaciones()
while(True):
	print("     Operaciones con imagenes")
	print("..................................")
	print("1.  Translacion")
	print("2.  Escalado")
	print("3.  Rotacion")
	print("4.  Rotación pivote")
	print("5.  Reflexión x")
	print("6.  Reflexión y")
	print("7.  Reflexión xy")
	print("8.  Copia")
	print("9.  Inversión")
	print("10. Brillo")
	print("11. Suma")
	print("12. Resta")
	print("13. Multiplicación")
	print("14. División")
	print("15. AND")
	print("16. OR")
	print("17. NOT")
	print("0.  Salir")
	opcion = int(input("Ingresa una opcion: "))
	
	if opcion == 0:
		exit()
	
	elif opcion == 1:
		print("  			 Trasnlacion")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		x_T = int(input("Ingrese nueva posicion en X: "))
		y_T = int(input("Ingrese nueva posicion en Y: "))
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.Translacion(img,x_T,y_T)
	
	elif opcion == 2:
		print("  			 Escalado")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		s_x = int(input("Ingrese s_X: "))
		s_y = int(input("Ingrese s_Y: "))
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.Translacion(img,s_x,s_y)

	elif opcion == 3:
		print("  			  Rotacion")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		angulo = int(input("Angulo (grados): "))
		angulo = (angulo*math.pi)/180
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.Rotacion(img,angulo)
	
	elif opcion == 4:
		print("  			 Rotacion Pivote")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		angulo = int(input("Angulo (grados): "))
		xR = int(input("Pivote en x: "))
		yR = int(input("Pivote en y: "))
		angulo = (angulo*math.pi)/180
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.RotacionPivote(img,angulo,xR,yR)

	elif opcion == 5:
		print("  			 Reflexion X")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.ReflexionX(img)

	elif opcion == 6:
		print("  			 Reflexion Y")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.ReflexionY(img)

	elif opcion == 7:
		print("  			 Reflexion XY")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.ReflexionXY(img)

	elif opcion == 8:
		print("  			 Copia")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.Copia(img)

	elif opcion == 9:
		print("  			 Inversion")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.Inversion(img)

	elif opcion == 10:
		print("  			 Brillo")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		b = int(input("Ingrese el valor de brillo (0 a 255): "))
		while (True):
			if(b<=255):
				break
			b = int(input("INVALIDO. Ingrese el valor de brillo (0 a 255): "))
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.Brillo(img,b)

	elif opcion == 11:
		print("  			 Suma")
		print(".........................................")
		nomImg1 = input("Ingrese el nombre de la imagen: ")
		nomImg2 = input("Ingrese el nombre de la imagen: ")
		img1 = cv2.imread("./"+nomImg1)
		img2 = cv2.imread("./"+nomImg2)
		img1 = cv2.resize(img1,(600,500))
		img2 = cv2.resize(img2,(600,500))
		operacion.Suma(img1,img2)

	elif opcion == 12:
		print("  			 Resta")
		print(".........................................")
		nomImg1 = input("Ingrese el nombre de la imagen: ")
		nomImg2 = input("Ingrese el nombre de la imagen: ")
		img1 = cv2.imread("./"+nomImg1)
		img2 = cv2.imread("./"+nomImg2)
		img1 = cv2.resize(img1,(600,500))
		img2 = cv2.resize(img2,(600,500))
		operacion.Resta(img1,img2)

	elif opcion == 13:
		print("  			 Multiplicacion")
		print(".........................................")
		nomImg1 = input("Ingrese el nombre de la imagen: ")
		nomImg2 = input("Ingrese el nombre de la imagen: ")
		img1 = cv2.imread("./"+nomImg1)
		img2 = cv2.imread("./"+nomImg2)
		img1 = cv2.resize(img1,(600,500))
		img2 = cv2.resize(img2,(600,500))
		operacion.Multiplicacion(img1,img2)

	elif opcion == 14:
		print("  			 Division")
		print(".........................................")
		nomImg1 = input("Ingrese el nombre de la imagen: ")
		nomImg2 = input("Ingrese el nombre de la imagen: ")
		img1 = cv2.imread("./"+nomImg1)
		img2 = cv2.imread("./"+nomImg2)
		img1 = cv2.resize(img1,(600,500))
		img2 = cv2.resize(img2,(600,500))
		operacion.Division(img1,img2)

	elif opcion == 15:
		print("  			 AND")
		print(".........................................")
		nomImg1 = input("Ingrese el nombre de la imagen: ")
		nomImg2 = input("Ingrese el nombre de la imagen: ")
		img1 = cv2.imread("./"+nomImg1)
		img2 = cv2.imread("./"+nomImg2)
		img1 = cv2.resize(img1,(600,500))
		img2 = cv2.resize(img2,(600,500))
		operacion.AND(img1,img2)

	elif opcion == 16:
		print("  			 OR")
		print(".........................................")
		nomImg1 = input("Ingrese el nombre de la imagen: ")
		nomImg2 = input("Ingrese el nombre de la imagen: ")
		img1 = cv2.imread("./"+nomImg1)
		img2 = cv2.imread("./"+nomImg2)
		img1 = cv2.resize(img1,(600,500))
		img2 = cv2.resize(img2,(600,500))			
		operacion.OR(img1,img2)

	elif opcion == 17:
		print("  			 NOT")
		print(".........................................")
		nomImg = input("Ingrese el nombre de la imagen: ")
		img = cv2.imread("./"+nomImg)
		img = cv2.resize(img,(600,500))
		operacion.NOT(img)
	
import RPi.GPIO as GPIO
import time
pin1=3
pin2=8
GPIO.setmode (GPIO.BOARD)
GPIO.setup (pin1,GPIO.OUT)
GPIO.setup (pin2,GPIO.OUT)
class Alarma:
    def menu(self):
      opc= input('''                                   Señales de ingreso
      ######### ALARMA #########                        ######### BOMBA DE RIEGO #########
      
      pin11: si se detecta GAS                          pin19: si la tierra está seca
      pin13: si se detecta HUMO.                        pin21: si hay restricciones en el riego (es verano)
      pin15: si la temperatura es superior a 45ºC       pin23: si es de día
      pin16: si la temperatura es superior a 60ºC       pin24: si el depósito de agua está vacío
      
      ''')
      return opc
    
    def llama_pin(self,pin1):
      print("Alarma activada")
      for i in range(0,10):
        GPIO.setup (3,GPIO.OUT)
        GPIO.output(3,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(3,GPIO.LOW)
        time.sleep(0.5)
        GPIO.cleanup()
       
    def llama_pin2(self,pin2):
      print("Bomba activada")
      for i in range(0,10):
        GPIO.setup (8,GPIO.OUT)
        GPIO.output(8,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(8,GPIO.LOW)
        time.sleep(0.5)
        GPIO.cleanup() 
              
    def opcion(self,opc):
      if GPIO.input(16)==GPIO.HIGH:
        Alarma.llama_pin (self,pin1)
      elif GPIO.input(15)==GPIO.HIGH and GPIO.input(13)==GPIO.HIGH or  GPIO.input(15)==GPIO.HIGH and GPIO.input(11)==GPIO.HIGH or GPIO.input(15)==GPIO.HIGH and GPIO.input(11)==GPIO.HIGH and GPIO.input(13)==GPIO.HIGH:
        Alarma.llama_pin (self,pin1)
      elif GPIO.input(11)==GPIO.HIGH and GPIO.input(12)==GPIO.HIGH:
        Alarma.llama_pin (self,pin1)
      else:
        print("Alarma desactivada")
      
    def opcion1(self,opc):
      if  GPIO.input(21)==GPIO.HIGH and GPIO.input(23)==GPIO.LOW and GPIO.input(24)==GPIO.LOW :
        Alarma.llama_pin2(self,pin2)
      elif GPIO.input(23)==GPIO.HIGH and GPIO.input(19)==GPIO.HIGH  and GPIO.input(21)==GPIO.LOW and GPIO.input(24)==GPIO.LOW or GPIO.input(24)==GPIO.LOW and GPIO.input(21)==GPIO.LOW and GPIO.input(23)==GPIO.LOW and GPIO.input(19)==GPIO.HIGH :
        Alarma.llama_pin2(self,pin2)
      else:
        print("Bomba desactivada") 
GPIO.input(35)==GPIO.LOW       
while True: 
  while GPIO.input(35)==GPIO.LOW:
    alarma1=Alarma()
    opcion2=alarma1.menu()
    encender=alarma1.opcion(opcion2)
    encender=alarma1.opcion1(opcion2)
    print("Si desea volver a seleccionar los pines presione OK, caso contrario seleccione el PIN 35")
    input(GPIO.input(35))
    if GPIO.input(35)==GPIO.HIGH:
      print("El programa a finalizado")
      break

  

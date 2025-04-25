class Motor:
    def __init__(self):
        self.encendido = False
        self.temperatura = 0
    
    def encender(self):
        self.encendido = True
        print("Motor encendido")
    
    def apagar(self):
        self.encendido = False
        print("Motor apagado")
    
    def estado_actual(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"Estado del motor: {estado}")
        print(f"Temperatura actual: {self.temperatura}°C")
    
    def establecer_temperatura(self, temp):
        self.temperatura = temp
        print(f"Temperatura actualizada a: {self.temperatura}°C")
        self.verificar_temperatura()
    
    def verificar_temperatura(self):
        if self.temperatura > 80 and self.encendido:
            print("¡ALERTA! Temperatura crítica detectada")
            self.apagar()
            return True
        return False

def sistema_control():
    motor = Motor()
    
    while True:
        print("\n=== SISTEMA DE CONTROL INDUSTRIAL ===")
        print("1. Encender motor")
        print("2. Apagar motor")
        print("3. Ver estado del motor")
        print("4. Actualizar temperatura")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            motor.encender()
        elif opcion == "2":
            motor.apagar()
        elif opcion == "3":
            motor.estado_actual()
        elif opcion == "4":
            try:
                temp = float(input("Ingrese la nueva temperatura (°C): "))
                motor.establecer_temperatura(temp)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido")
        elif opcion == "5":
            print("Saliendo del sistema de control")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    sistema_control()
    
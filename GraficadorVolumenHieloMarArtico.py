import pandas as pd
import matplotlib.pyplot as plt

class GraficadorVolumenHieloMarArtico:
    def __init__(self, archivo_csv):
        self.datos = pd.read_csv(archivo_csv, delimiter=';')
        self.año = self.datos['year']
        self.meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.meses_esp = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    def graficar_por_mes(self):       
        while True:          
            for i, mes in enumerate(self.meses_esp, start=1):
                if (i - 1) % 4 == 0:
                    print()
                if i < 10:
                    print(f" {i}. {mes.rjust(3)}", end="\t\t")
                else:
                    print(f"{i}. {mes.rjust(3)}", end="\t\t")   
            print("\n")
            n_mes = input("Ingrese un número de1 1 al 12 de acuerdo al orden de meses: ")            
            try:
                n_mes= int(n_mes)
                if 1<= n_mes<= 12:
                    break
                else:
                    print("Por favor, ingrese un número dentro del rango válido.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")

        mes_seleccionado=self.meses[n_mes-1]
        mes_seleccionado_esp=self.meses_esp[n_mes-1]
        volumen = self.datos[mes_seleccionado]
        plt.plot(self.año, volumen, label=str(mes_seleccionado_esp))
        plt.xlabel('Año')
        plt.ylabel('Volumen (1000 km^3)')
        plt.title(f'Volumen Histórico de Hielo del Mar Ártico en el mes de {mes_seleccionado_esp}')
        plt.legend()
        plt.show()
    
    def graficar_por_año(self):
        while True:
            año_seleccionado = input("Ingrese el año (1979-2023): ")
            try:
                año_seleccionado = int(año_seleccionado)
                if 1979 <= año_seleccionado <= 2023:
                    break
                else:
                    print("Por favor, ingrese un año dentro del rango válido.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un año válido.")

        volumen = self.datos.loc[self.año == año_seleccionado].squeeze()[1:]
        plt.plot(self.meses, volumen, label=str(año_seleccionado))
        plt.xlabel('Mes')
        plt.ylabel('Volumen (1000 km^3)')
        plt.title(f'Volumen de Hielo del Mar Ártico - Año {año_seleccionado}')
        plt.legend()
        plt.show()

    def graficar_todos_los_datos_por_meses(self):
        for mes in self.meses:
            volumen = self.datos[mes]
            
            plt.plot(self.año, volumen, label=mes)

        plt.xlabel('Año')
        plt.ylabel('Volumen (1000 km^3)')
        plt.title('Volumen de Hielo del Mar Ártico - Todos los Datos')
        plt.legend()
        plt.show()

    def graficar_todos_los_datos_continuamente(self):
        volumen = self.datos.iloc[:, 1:].values.flatten()
        meses_totales = []
        for año in self.año:
            for mes in self.meses:
                meses_totales.append(mes + ' ' + str(año))
        
        plt.plot(meses_totales, volumen)
        plt.xlabel('')
        plt.ylabel('Volumen (1000 km^3)')
        plt.title('Volumen Historico de Hielo del Mar Ártico')
        # plt.xticks([])
        plt.legend()
        plt.show()

# Uso
archivo_csv = 'CSV/DS_PIOMAS_monthly_Current_Arctic_Sea_Ice_Volume.csv'
graficador = GraficadorVolumenHieloMarArtico(archivo_csv)

print("Seleccione una opción:")
print("1. Graficar por mes")
print("2. Graficar por año")
print("3. Graficar todos los datos por meses")
print("4. Graficar todos los datos continuamente")
opcion = int(input("Ingrese el número de opción: "))


def main():
    if opcion == 1:
        graficador.graficar_por_mes()
    elif opcion == 2:
        graficador.graficar_por_año()
    elif opcion == 3:
        graficador.graficar_todos_los_datos_por_meses()
    elif opcion == 4:
        graficador.graficar_todos_los_datos_continuamente()
    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()


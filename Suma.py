#una funcion que use libreia panda
import pandas as pd

def suma():
    #creamos un diccionario

    data = {'Nombre':['Juan','Ana','Pedro','Pablo'],
            'Edad':[23,78,22,19],
            'Genero':['M','F','M','M'],
            'Calificaciones':[89,78,45,60]}
    
    #Convertimos el diccionario en un DataFrame
    df = pd.DataFrame(data)
    
    print()  # Esta línea esta en blanco
    print(df)
    print("\n- La suma de las calificaciones es: ", df['Calificaciones'].sum())
    print("- El promedio de las calificaciones es: ", df['Calificaciones'].mean())
    print("- Se cuenta con", df['Genero'].str.contains('M').sum(),"hombres en el grupo")
    print("- Se cuenta con", df['Genero'].str.contains('F').sum(),"mujer en el grupo")
    print() # Esta línea esta en blanco
# Llamada a la función suma
suma()
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Carrera, Profesor

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def poblar_profesores():
    """Puebla la tabla de Profesores desde el archivo JSON"""
    
    # Ruta del archivo JSON
    ruta_json = "data/datos_universidad/datos/profesores.json"
    
    try:
        # Leer el archivo JSON
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            profesores_data = json.load(archivo)
        
        # Verificar si hay datos para insertar
        if not profesores_data:
            print("No hay datos en el archivo JSON de profesores.")
            return
        
        # Insertar cada profesor
        for profesor_data in profesores_data:
            # Buscar la carrera por nombre
            carrera = session.query(Carrera).filter_by(
                nombre=profesor_data['carrera']
            ).first()
            
            if not carrera:
                print(f"Carrera '{profesor_data['carrera']}' no encontrada. Se omitirá profesor '{profesor_data['nombres']} {profesor_data['apellidos']}'.")
                continue
            
            # Verificar si el profesor ya existe
            profesor_existente = session.query(Profesor).filter_by(
                correo=profesor_data['correo']
            ).first()
            
            if profesor_existente:
                print(f"Profesor con correo '{profesor_data['correo']}' ya existe. Se omitirá.")
                continue
            
            # Crear nuevo registro
            nuevo_profesor = Profesor(
                nombre=profesor_data['nombres'],
                apellido=profesor_data['apellidos'],
                correo=profesor_data['correo'],
                especialidad=profesor_data['especialidad'],
                carrera_id=carrera.id
            )
            
            session.add(nuevo_profesor)
            print(f"Agregado profesor: {profesor_data['nombres']} {profesor_data['apellidos']} (Carrera: {profesor_data['carrera']})")
        
        # Confirmar cambios
        session.commit()
        print(f"\n{len(profesores_data)} Profesores poblados exitosamente!")
        
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {ruta_json}")
        session.rollback()
    except KeyError as e:
        print(f"Error: Campo faltante en JSON: {e}")
        session.rollback()
    except Exception as e:
        print(f"Error al poblar profesores: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    print("=" * 50)
    print("POBLANDO TABLA: PROFESORES")
    print("=" * 50)
    poblar_profesores()

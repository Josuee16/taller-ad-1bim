import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def poblar_carreras():
    """Puebla la tabla de Carreras desde el archivo JSON"""
    
    # Ruta del archivo JSON
    ruta_json = "data/datos_universidad/datos/carreras.json"
    
    try:
        # Leer el archivo JSON
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            carreras_data = json.load(archivo)
        
        # Verificar si hay datos para insertar
        if not carreras_data:
            print("No hay datos en el archivo JSON de carreras.")
            return
        
        # Insertar cada carrera
        for carrera_data in carreras_data:
            # Buscar la facultad por nombre
            facultad = session.query(Facultad).filter_by(
                nombre=carrera_data['facultad']
            ).first()
            
            if not facultad:
                print(f"Facultad '{carrera_data['facultad']}' no encontrada. Se omitirá carrera '{carrera_data['nombre']}'.")
                continue
            
            # Verificar si la carrera ya existe
            carrera_existente = session.query(Carrera).filter_by(
                nombre=carrera_data['nombre']
            ).first()
            
            if carrera_existente:
                print(f"Carrera '{carrera_data['nombre']}' ya existe. Se omitirá.")
                continue
            
            # Crear nuevo registro
            nueva_carrera = Carrera(
                nombre=carrera_data['nombre'],
                codigo=carrera_data['codigo'],
                facultad_id=facultad.id
            )
            
            session.add(nueva_carrera)
            print(f"Agregada carrera: {carrera_data['nombre']} (Facultad: {carrera_data['facultad']})")
        
        # Confirmar cambios
        session.commit()
        print(f"\n{len(carreras_data)} Carreras pobladas exitosamente!")
        
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {ruta_json}")
        session.rollback()
    except KeyError as e:
        print(f"Error: Campo faltante en JSON: {e}")
        session.rollback()
    except Exception as e:
        print(f"Error al poblar carreras: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    print("=" * 50)
    print("POBLANDO TABLA: CARRERAS")
    print("=" * 50)
    poblar_carreras()

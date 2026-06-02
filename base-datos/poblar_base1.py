import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def poblar_facultades():
    """Puebla la tabla de Facultades desde el archivo JSON"""
    
    # Ruta del archivo JSON
    ruta_json = "data/datos_universidad/datos/facultades.json"
    
    try:
        # Leer el archivo JSON
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            facultades_data = json.load(archivo)
        
        # Verificar si hay datos para insertar
        if not facultades_data:
            print("No hay datos en el archivo JSON de facultades.")
            return
        
        # Insertar cada facultad
        for facultad_data in facultades_data:
            # Verificar si la facultad ya existe
            facultad_existente = session.query(Facultad).filter_by(
                nombre=facultad_data['nombre']
            ).first()
            
            if facultad_existente:
                print(f"Facultad '{facultad_data['nombre']}' ya existe. Se omitirá.")
                continue
            
            # Crear nuevo registro
            nueva_facultad = Facultad(
                nombre=facultad_data['nombre'],
                ubicacion=facultad_data['ubicacion'],
                decano=facultad_data['decano']
            )
            
            session.add(nueva_facultad)
            print(f"Agregada facultad: {facultad_data['nombre']}")
        
        # Confirmar cambios
        session.commit()
        print(f"\n{len(facultades_data)} Facultades pobladas exitosamente!")
        
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {ruta_json}")
        session.rollback()
    except KeyError as e:
        print(f"Error: Campo faltante en JSON: {e}")
        session.rollback()
    except Exception as e:
        print(f"Error al poblar facultades: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    print("=" * 50)
    print("POBLANDO TABLA: FACULTADES")
    print("=" * 50)
    poblar_facultades()

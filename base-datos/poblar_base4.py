import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def poblar_recursos_academicos():
    """Puebla la tabla de Recursos Académicos desde el archivo JSON"""
    
    # Ruta del archivo JSON
    ruta_json = "data/datos_universidad/datos/recursos_academicos.json"
    
    try:
        # Leer el archivo JSON
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            recursos_data = json.load(archivo)
        
        # Verificar si hay datos para insertar
        if not recursos_data:
            print("No hay datos en el archivo JSON de recursos académicos.")
            return
        
        # Insertar cada recurso
        for recurso_data in recursos_data:
            # Buscar el profesor por nombre completo (nombre + apellido)
            nombre_profesor = recurso_data['profesor']
            profesor = session.query(Profesor).filter(
                (Profesor.nombre + ' ' + Profesor.apellido) == nombre_profesor
            ).first()
            
            if not profesor:
                print(f"Profesor '{nombre_profesor}' no encontrado. Se omitirá recurso '{recurso_data['titulo']}'.")
                continue
            
            # Verificar si el recurso ya existe
            recurso_existente = session.query(RecursoAcademico).filter_by(
                titulo=recurso_data['titulo']
            ).first()
            
            if recurso_existente:
                print(f"Recurso '{recurso_data['titulo']}' ya existe. Se omitirá.")
                continue
            
            # Convertir fecha_publicacion de string a datetime
            fecha_pub = datetime.strptime(recurso_data['fecha_publicacion'], '%Y-%m-%d').date()
            
            # Crear nuevo registro
            nuevo_recurso = RecursoAcademico(
                titulo=recurso_data['titulo'],
                tipo_recurso=recurso_data['tipo'],
                fecha_publicacion=fecha_pub,
                url=recurso_data['url'],
                profesor_id=profesor.id
            )
            
            session.add(nuevo_recurso)
            print(f"Agregado recurso: {recurso_data['titulo']} (Tipo: {recurso_data['tipo']}, Profesor: {nombre_profesor})")
        
        # Confirmar cambios
        session.commit()
        print(f"\n{len(recursos_data)} Recursos Académicos poblados exitosamente!")
        
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {ruta_json}")
        session.rollback()
    except KeyError as e:
        print(f"Error: Campo faltante en JSON: {e}")
        session.rollback()
    except ValueError as e:
        print(f"Error al procesar fecha: {e}")
        session.rollback()
    except Exception as e:
        print(f"Error al poblar recursos académicos: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    print("=" * 50)
    print("POBLANDO TABLA: RECURSOS ACADÉMICOS")
    print("=" * 50)
    poblar_recursos_academicos()

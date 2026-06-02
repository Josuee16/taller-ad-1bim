"""
Consulta ALL - Obtener todos los registros de una entidad
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def mostrar_facultades():
    """Mostrar todas las facultades"""
    print("\n" + "="*60)
    print("TODAS LAS FACULTADES")
    print("="*60)
    
    facultades = session.query(Facultad).all()
    
    if not facultades:
        print("No hay facultades registradas.")
        return
    
    for fac in facultades:
        print(f"ID: {fac.id}")
        print(f"  Nombre: {fac.nombre}")
        print(f"  Ubicación: {fac.ubicacion}")
        print(f"  Decano: {fac.decano}")
        print()

def mostrar_carreras():
    """Mostrar todas las carreras"""
    print("\n" + "="*60)
    print("TODAS LAS CARRERAS")
    print("="*60)
    
    carreras = session.query(Carrera).all()
    
    if not carreras:
        print("No hay carreras registradas.")
        return
    
    for car in carreras:
        print(f"ID: {car.id}")
        print(f"  Nombre: {car.nombre}")
        print(f"  Código: {car.codigo}")
        print(f"  Facultad ID: {car.facultad_id}")
        print()

def mostrar_profesores():
    """Mostrar todos los profesores"""
    print("\n" + "="*60)
    print("TODOS LOS PROFESORES")
    print("="*60)
    
    profesores = session.query(Profesor).all()
    
    if not profesores:
        print("No hay profesores registrados.")
        return
    
    for prof in profesores:
        print(f"ID: {prof.id}")
        print(f"  Nombre: {prof.nombre} {prof.apellido}")
        print(f"  Correo: {prof.correo}")
        print(f"  Especialidad: {prof.especialidad}")
        print(f"  Carrera ID: {prof.carrera_id}")
        print()

def mostrar_recursos():
    """Mostrar todos los recursos académicos"""
    print("\n" + "="*60)
    print("TODOS LOS RECURSOS ACADÉMICOS")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).all()
    
    if not recursos:
        print("No hay recursos académicos registrados.")
        return
    
    for rec in recursos:
        print(f"ID: {rec.id}")
        print(f"  Título: {rec.titulo}")
        print(f"  Tipo: {rec.tipo_recurso}")
        print(f"  Fecha Publicación: {rec.fecha_publicacion}")
        print(f"  URL: {rec.url}")
        print(f"  Profesor ID: {rec.profesor_id}")
        print()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CONSULTAS CON .all() - OBTENER TODOS LOS REGISTROS")
    print("="*60)
    
    mostrar_facultades()
    mostrar_carreras()
    mostrar_profesores()
    mostrar_recursos()
    
    print("\nConsultas completadas\n")
    session.close()

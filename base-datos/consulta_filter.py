"""
Consulta FILTER - Filtrar registros con condiciones específicas
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def filtrar_facultad_ingenieria():
    """Filtrar facultad de ingeniería"""
    print("\n" + "="*60)
    print("FACULTAD DE INGENIERÍA (FILTER)")
    print("="*60)
    
    facultad = session.query(Facultad).filter(
        Facultad.nombre == "Facultad de Ingeniería"
    ).first()
    
    if facultad:
        print(f"Nombre: {facultad.nombre}")
        print(f"Ubicación: {facultad.ubicacion}")
        print(f"Decano: {facultad.decano}")
    else:
        print("Facultad no encontrada")

def filtrar_carreras_ingenieria():
    """Filtrar carreras que contienen 'Ingeniería' en el nombre"""
    print("\n" + "="*60)
    print("CARRERAS QUE CONTIENEN 'INGENIERÍA' (FILTER)")
    print("="*60)
    
    carreras = session.query(Carrera).filter(
        Carrera.nombre.like('%Ingeniería%')
    ).all()
    
    if carreras:
        for car in carreras:
            print(f"  • {car.nombre} (Código: {car.codigo})")
    else:
        print("No se encontraron carreras")

def filtrar_profesores_por_especialidad():
    """Filtrar profesores con especialidad en Bases de Datos"""
    print("\n" + "="*60)
    print("PROFESORES ESPECIALIZADOS EN 'BASES DE DATOS' (FILTER)")
    print("="*60)
    
    profesores = session.query(Profesor).filter(
        Profesor.especialidad == "Bases de Datos"
    ).all()
    
    if profesores:
        for prof in profesores:
            print(f"  • {prof.nombre} {prof.apellido}")
            print(f"    Especialidad: {prof.especialidad}")
            print(f"    Correo: {prof.correo}")
    else:
        print("No se encontraron profesores")

def filtrar_recursos_por_tipo():
    """Filtrar recursos académicos de tipo 'Libro'"""
    print("\n" + "="*60)
    print("RECURSOS DE TIPO 'LIBRO' (FILTER)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).filter(
        RecursoAcademico.tipo_recurso == "Libro"
    ).all()
    
    if recursos:
        print(f"Total de libros: {len(recursos)}")
        for rec in recursos:
            print(f"  • {rec.titulo}")
            print(f"    URL: {rec.url}")
    else:
        print("No se encontraron recursos de tipo Libro")

def filtrar_recursos_por_url():
    """Filtrar recursos que contengan 'sql' en la URL"""
    print("\n" + "="*60)
    print("RECURSOS CON 'sql' EN LA URL (FILTER)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).filter(
        RecursoAcademico.url.like('%sql%')
    ).all()
    
    if recursos:
        for rec in recursos:
            print(f"  • {rec.titulo}")
            print(f"    URL: {rec.url}")
    else:
        print("No se encontraron recursos")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CONSULTAS CON .filter() - FILTRAR REGISTROS")
    print("="*60)
    
    filtrar_facultad_ingenieria()
    filtrar_carreras_ingenieria()
    filtrar_profesores_por_especialidad()
    filtrar_recursos_por_tipo()
    filtrar_recursos_por_url()
    
    print("\nConsultas completadas\n")
    session.close()

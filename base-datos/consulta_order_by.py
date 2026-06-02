"""
Consulta ORDER_BY - Ordenar resultados
"""

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def ordenar_profesores_por_nombre():
    """Ordenar profesores alfabéticamente por nombre"""
    print("\n" + "="*60)
    print("PROFESORES ORDENADOS ALFABÉTICAMENTE (ORDER_BY)")
    print("="*60)
    
    profesores = session.query(Profesor).order_by(Profesor.nombre).all()
    
    if profesores:
        for i, prof in enumerate(profesores, 1):
            print(f"{i:2d}. {prof.nombre} {prof.apellido}")
    else:
        print("No hay profesores registrados")

def ordenar_carreras_por_codigo():
    """Ordenar carreras por código (descendente)"""
    print("\n" + "="*60)
    print("CARRERAS ORDENADAS POR CÓDIGO (DESCENDENTE)")
    print("="*60)
    
    carreras = session.query(Carrera).order_by(desc(Carrera.codigo)).all()
    
    if carreras:
        for i, car in enumerate(carreras, 1):
            print(f"{i:2d}. {car.nombre} (Código: {car.codigo})")
    else:
        print("No hay carreras registradas")

def ordenar_recursos_por_fecha():
    """Ordenar recursos académicos por fecha de publicación (más recientes primero)"""
    print("\n" + "="*60)
    print("RECURSOS ORDENADOS POR FECHA (MÁS RECIENTES PRIMERO)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).order_by(
        desc(RecursoAcademico.fecha_publicacion)
    ).all()
    
    if recursos:
        for i, rec in enumerate(recursos, 1):
            print(f"{i:2d}. {rec.titulo}")
            print(f"    Fecha: {rec.fecha_publicacion}")
    else:
        print("No hay recursos registrados")

def ordenar_facultades_por_nombre():
    """Ordenar facultades por nombre (A-Z)"""
    print("\n" + "="*60)
    print("FACULTADES ORDENADAS POR NOMBRE (A-Z)")
    print("="*60)
    
    facultades = session.query(Facultad).order_by(Facultad.nombre).all()
    
    if facultades:
        for i, fac in enumerate(facultades, 1):
            print(f"{i}. {fac.nombre}")
    else:
        print("No hay facultades registradas")

def ordenar_profesores_por_apellido_descendente():
    """Ordenar profesores por apellido (Z-A)"""
    print("\n" + "="*60)
    print("PROFESORES ORDENADOS POR APELLIDO (Z-A)")
    print("="*60)
    
    profesores = session.query(Profesor).order_by(
        desc(Profesor.apellido)
    ).all()
    
    if profesores:
        for i, prof in enumerate(profesores, 1):
            print(f"{i:2d}. {prof.apellido}, {prof.nombre}")
    else:
        print("No hay profesores registrados")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CONSULTAS CON .order_by() - ORDENAR RESULTADOS")
    print("="*60)
    
    ordenar_profesores_por_nombre()
    ordenar_carreras_por_codigo()
    ordenar_recursos_por_fecha()
    ordenar_facultades_por_nombre()
    ordenar_profesores_por_apellido_descendente()
    
    print("\nConsultas completadas\n")
    session.close()

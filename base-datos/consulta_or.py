"""
Consulta OR - Usar operador OR en las condiciones
"""

from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def profesores_ingenieria_o_economia():
    """Encontrar profesores que enseñan en carreras de Ingeniería O Economía"""
    print("\n" + "="*60)
    print("PROFESORES DE INGENIERÍA O ECONOMÍA (OR)")
    print("="*60)
    
    # Primero obtener las carreras de Ingeniería o Economía
    carreras = session.query(Carrera).filter(
        or_(
            Carrera.nombre.like('%Ingeniería%'),
            Carrera.nombre.like('%Economía%')
        )
    ).all()
    
    # Luego obtener profesores de esas carreras
    carrera_ids = [car.id for car in carreras]
    profesores = session.query(Profesor).filter(
        Profesor.carrera_id.in_(carrera_ids)
    ).all()
    
    if profesores:
        print(f"Total de profesores encontrados: {len(profesores)}\n")
        for prof in profesores:
            carrera = session.query(Carrera).filter_by(id=prof.carrera_id).first()
            print(f"  • {prof.nombre} {prof.apellido}")
            print(f"    Carrera: {carrera.nombre}")
            print(f"    Especialidad: {prof.especialidad}")
    else:
        print("No se encontraron profesores")

def recursos_libros_o_guias():
    """Encontrar recursos que sean de tipo Libro O Guía"""
    print("\n" + "="*60)
    print("RECURSOS DE TIPO LIBRO O GUÍA (OR)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).filter(
        or_(
            RecursoAcademico.tipo_recurso == "Libro",
            RecursoAcademico.tipo_recurso == "Guia"
        )
    ).all()
    
    if recursos:
        print(f"Total de recursos encontrados: {len(recursos)}\n")
        for rec in recursos:
            print(f"  • {rec.titulo}")
            print(f"    Tipo: {rec.tipo_recurso}")
    else:
        print("No se encontraron recursos")

def facultades_ingenieria_o_salud():
    """Encontrar facultades de Ingeniería O Salud"""
    print("\n" + "="*60)
    print("FACULTADES DE INGENIERÍA O SALUD (OR)")
    print("="*60)
    
    facultades = session.query(Facultad).filter(
        or_(
            Facultad.nombre.like('%Ingeniería%'),
            Facultad.nombre.like('%Salud%')
        )
    ).all()
    
    if facultades:
        print(f"Total de facultades encontradas: {len(facultades)}\n")
        for fac in facultades:
            print(f"  • {fac.nombre}")
            print(f"    Ubicación: {fac.ubicacion}")
            print(f"    Decano: {fac.decano}")
    else:
        print("No se encontraron facultades")

def profesores_nombres_especificos():
    """Encontrar profesores con nombres Ana O Pedro"""
    print("\n" + "="*60)
    print("PROFESORES CON NOMBRE ANA O PEDRO (OR)")
    print("="*60)
    
    profesores = session.query(Profesor).filter(
        or_(
            Profesor.nombre == "Ana",
            Profesor.nombre == "Pedro"
        )
    ).all()
    
    if profesores:
        print(f"Total de profesores encontrados: {len(profesores)}\n")
        for prof in profesores:
            print(f"  • {prof.nombre} {prof.apellido}")
            print(f"    Correo: {prof.correo}")
    else:
        print("No se encontraron profesores")

def recursos_url_sql_o_ml():
    """Encontrar recursos con 'sql' O 'ml' en la URL"""
    print("\n" + "="*60)
    print("RECURSOS CON 'sql' O 'ml' EN LA URL (OR)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).filter(
        or_(
            RecursoAcademico.url.like('%sql%'),
            RecursoAcademico.url.like('%ml%')
        )
    ).all()
    
    if recursos:
        print(f"Total de recursos encontrados: {len(recursos)}\n")
        for rec in recursos:
            print(f"  • {rec.titulo}")
            print(f"    URL: {rec.url}")
    else:
        print("No se encontraron recursos")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CONSULTAS CON OR - CONDICIONES ALTERNATIVAS")
    print("="*60)
    
    profesores_ingenieria_o_economia()
    recursos_libros_o_guias()
    facultades_ingenieria_o_salud()
    profesores_nombres_especificos()
    recursos_url_sql_o_ml()
    
    print("\nConsultas completadas\n")
    session.close()

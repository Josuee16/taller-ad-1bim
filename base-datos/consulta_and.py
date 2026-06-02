"""
Consulta AND - Usar operador AND en las condiciones
"""

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()

def profesores_ingenieria_y_bases_datos():
    """Encontrar profesores que enseñen en Ingeniería Y se especialicen en Bases de Datos"""
    print("\n" + "="*60)
    print("PROFESORES DE INGENIERÍA CON ESPECIALIDAD EN BASES DE DATOS (AND)")
    print("="*60)
    
    # Obtener profesores con especialidad en Bases de Datos
    profesores = session.query(Profesor).filter(
        and_(
            Profesor.especialidad == "Bases de Datos",
            Profesor.carrera_id.in_(
                session.query(Carrera.id).filter(
                    Carrera.nombre.like('%Ingeniería%')
                )
            )
        )
    ).all()
    
    if profesores:
        print(f"Total de profesores encontrados: {len(profesores)}\n")
        for prof in profesores:
            carrera = session.query(Carrera).filter_by(id=prof.carrera_id).first()
            print(f"  • {prof.nombre} {prof.apellido}")
            print(f"    Correo: {prof.correo}")
            print(f"    Carrera: {carrera.nombre}")
            print(f"    Especialidad: {prof.especialidad}")
    else:
        print("No se encontraron profesores")

def recursos_libro_y_sql():
    """Encontrar recursos que sean de tipo Libro Y contengan 'sql' en la URL"""
    print("\n" + "="*60)
    print("RECURSOS QUE SON LIBRO Y CONTIENEN 'sql' EN LA URL (AND)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).filter(
        and_(
            RecursoAcademico.tipo_recurso == "Libro",
            RecursoAcademico.url.like('%sql%')
        )
    ).all()
    
    if recursos:
        print(f"Total de recursos encontrados: {len(recursos)}\n")
        for rec in recursos:
            print(f"  • {rec.titulo}")
            print(f"    Tipo: {rec.tipo_recurso}")
            print(f"    URL: {rec.url}")
    else:
        print("No se encontraron recursos")

def carreras_ingenieria_y_edificio_a():
    """Encontrar carreras de Ingeniería Y ubicadas en Edificio A"""
    print("\n" + "="*60)
    print("CARRERAS DE INGENIERÍA UBICADAS EN EDIFICIO A (AND)")
    print("="*60)
    
    # Obtener facultades ubicadas en Edificio A
    facultades_edificio_a = session.query(Facultad.id).filter(
        Facultad.ubicacion == "Edificio A"
    ).all()
    
    facultad_ids = [f.id for f in facultades_edificio_a]
    
    # Obtener carreras de Ingeniería en esas facultades
    carreras = session.query(Carrera).filter(
        and_(
            Carrera.nombre.like('%Ingeniería%'),
            Carrera.facultad_id.in_(facultad_ids)
        )
    ).all()
    
    if carreras:
        print(f"Total de carreras encontradas: {len(carreras)}\n")
        for car in carreras:
            facultad = session.query(Facultad).filter_by(id=car.facultad_id).first()
            print(f"  • {car.nombre}")
            print(f"    Código: {car.codigo}")
            print(f"    Facultad: {facultad.nombre} ({facultad.ubicacion})")
    else:
        print("No se encontraron carreras")

def recursos_video_y_aria():
    """Encontrar recursos de tipo Video Y con 'aria' en alguna parte (aria = tema académico)"""
    print("\n" + "="*60)
    print("RECURSOS DE TIPO VIDEO Y QUE CONTENGAN 'aria' EN EL TÍTULO (AND)")
    print("="*60)
    
    recursos = session.query(RecursoAcademico).filter(
        and_(
            RecursoAcademico.tipo_recurso == "Video",
            RecursoAcademico.titulo.like('%aria%')
        )
    ).all()
    
    if recursos:
        print(f"Total de recursos encontrados: {len(recursos)}\n")
        for rec in recursos:
            print(f"  • {rec.titulo}")
            print(f"    Tipo: {rec.tipo_recurso}")
    else:
        print("No se encontraron recursos")

def profesores_correo_educacion_y_didactica():
    """Encontrar profesores en carreras de Educación Y con especialidad en Didáctica"""
    print("\n" + "="*60)
    print("PROFESORES DE EDUCACIÓN CON ESPECIALIDAD EN DIDÁCTICA (AND)")
    print("="*60)
    
    profesores = session.query(Profesor).filter(
        and_(
            Profesor.especialidad.like('%Didáctica%'),
            Profesor.carrera_id.in_(
                session.query(Carrera.id).filter(
                    Carrera.nombre.like('%Educación%')
                )
            )
        )
    ).all()
    
    if profesores:
        print(f"Total de profesores encontrados: {len(profesores)}\n")
        for prof in profesores:
            carrera = session.query(Carrera).filter_by(id=prof.carrera_id).first()
            print(f"  • {prof.nombre} {prof.apellido}")
            print(f"    Correo: {prof.correo}")
            print(f"    Carrera: {carrera.nombre}")
            print(f"    Especialidad: {prof.especialidad}")
    else:
        print("No se encontraron profesores")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CONSULTAS CON AND - MÚLTIPLES CONDICIONES")
    print("="*60)
    
    profesores_ingenieria_y_bases_datos()
    recursos_libro_y_sql()
    carreras_ingenieria_y_edificio_a()
    recursos_video_y_aria()
    profesores_correo_educacion_y_didactica()
    
    print("\nConsultas completadas\n")
    session.close()

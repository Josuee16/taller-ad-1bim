"""
Consulta personalizada - Presentar recursos académicos de una facultad específica
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import CADENA_CONEXION
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

# Crear conexión y sesión
engine = create_engine(CADENA_CONEXION)
Session = sessionmaker(bind=engine)
session = Session()


def recursos_de_facultad(nombre_facultad):
    """Presentar recursos académicos vinculados a una facultad específica."""
    print("\n" + "="*60)
    print(f"RECURSOS ACADÉMICOS DE LA FACULTAD: {nombre_facultad}")
    print("="*60)

    facultad = session.query(Facultad).filter(
        Facultad.nombre == nombre_facultad
    ).first()

    if not facultad:
        print(f"Facultad '{nombre_facultad}' no encontrada")
        return

    recursos = session.query(RecursoAcademico).join(RecursoAcademico.profesor).join(Profesor.carrera).filter(
        Carrera.facultad_id == facultad.id
    ).all()

    if not recursos:
        print(f"No se encontraron recursos académicos para la facultad '{nombre_facultad}'")
        return

    print(f"Facultad: {facultad.nombre}")
    print(f"Ubicación: {facultad.ubicacion}")
    print(f"Decano: {facultad.decano}")
    print(f"Total de recursos encontrados: {len(recursos)}\n")

    for rec in recursos:
        profesor = rec.profesor
        carrera = profesor.carrera if profesor else None
        print(f"  • {rec.titulo}")
        print(f"    Tipo: {rec.tipo_recurso}")
        print(f"    Fecha de publicación: {rec.fecha_publicacion}")
        print(f"    URL: {rec.url}")
        if profesor:
            print(f"    Profesor: {profesor.nombre} {profesor.apellido}")
        if carrera:
            print(f"    Carrera: {carrera.nombre}")
        print()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("CONSULTA NUEVA - RECURSOS ACADÉMICOS POR FACULTAD")
    print("="*60)

    recursos_de_facultad("Facultad de Ingeniería")

    print("\nConsultas completadas\n")
    session.close()

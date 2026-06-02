from sqlalchemy import *
from sqlalchemy.orm import *

from configuracion import CADENA_CONEXION

engine = create_engine(CADENA_CONEXION)

Base = declarative_base()

class Facultad(Base):
    __tablename__ = "facultades"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    ubicacion = Column(String(50), nullable=False)
    decano = Column(String(50), nullable=False)

    carrera = relationship("Carrera", back_populates="facultad")
    
    def __repr__(self):
        return f"<Facultad(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}', decano='{self.decano}')>"


class Carrera(Base):
    __tablename__ = "carreras"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(150))
    codigo = Column(String(30))

    facultad_id = Column(Integer, ForeignKey("facultades.id"))

    facultad = relationship("Facultad", back_populates="carrera") 

    profesores = relationship("Profesor", back_populates="carrera")
    
    def __repr__(self):
        return f"<Carrera(id={self.id}, nombre='{self.nombre}', codigo='{self.codigo}', facultad_id={self.facultad_id})>"

class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(100), nullable=False)
    especialidad = Column(String(200), nullable=False)

    carrera_id = Column(Integer, ForeignKey("carreras.id"))

    carrera = relationship("Carrera", back_populates="profesores")
    
    recuros = relationship("RecursoAcademico", back_populates="profesor")
    
    def __repr__(self):
        return f"<Profesor(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}', correo='{self.correo}', especialidad='{self.especialidad}', carrera_id={self.carrera_id})>"

class RecursoAcademico(Base):
    __tablename__ = "recursos_academicos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    tipo_recurso = Column(String(50), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    url = Column(String(200))

    
    def __repr__(self):
        return f"<RecursoAcademico(id={self.id}, titulo='{self.titulo}', tipo_recurso='{self.tipo_recurso}', fecha_publicacion={self.fecha_publicacion}, url='{self.url}', profesor_id={self.profesor_id})>"
    profesor_id = Column(Integer, ForeignKey("profesores.id"))

    profesor = relationship("Profesor", back_populates="recuros")


Base.metadata.create_all(engine)

print("Base creada correctamente")
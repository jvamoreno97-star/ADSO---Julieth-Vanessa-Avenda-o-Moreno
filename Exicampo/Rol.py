class Rol:
    def __init__(self, id_rol, nombre_rol, descripcion, estado):
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.descripcion = descripcion
        self.estado = estado

    def datos_rol(self):
        return (f"Rol: {self.nombre_rol} - Descripción: {self.descripcion}")
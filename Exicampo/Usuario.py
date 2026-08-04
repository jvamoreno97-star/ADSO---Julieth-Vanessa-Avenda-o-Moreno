class Usuario:
    def __init__(self, id_usuario, nombres, apellidos, documento, correo, usuario, contraseña, estado, rol):
        self.id_usuario = id_usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.documento = documento
        self.correo = correo
        self.usuario = usuario
        self.contraseña = contraseña
        self.estado = estado
        self.rol = rol 

    def datos_usuario(self):
        return (f"Usuario: {self.usuario} - Nombre: {self.nombres} {self.apellidos} - Rol asignado: {self.rol.nombre_rol}")
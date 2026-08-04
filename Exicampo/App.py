from Rol import Rol
from Usuario import Usuario

rol_administrador = Rol(1, "Administrador", "Control total del sistema", True)

usuario1 = Usuario(
    101, 
    "Vanessa", 
    "Avendaño", 
    "123456789", 
    "vanessa@gmail.com", 
    "vavendano", 
    "clave123", 
    True, 
    rol_administrador
)

print(usuario1.datos_usuario())
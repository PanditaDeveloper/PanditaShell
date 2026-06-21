usuarios = [
    {"username": "pandita_dev", "rol": "admin", "activo": True},
    {"username": "anonymous_99", "rol": "guest", "activo": True},
    {"username": "boss_panda", "rol": "admin", "activo": False},
    {"username": "coffee_lover", "rol": "developer", "activo": True},
    {"username": "scripter_pro", "rol": "admin", "activo": True}
]

usuarios_activos = [
    usuario["username"] for usuario in usuarios
    if usuario["rol"] == "admin" and usuario["activo"]
]

for activos in usuarios_activos:
    print(activos)

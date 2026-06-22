servicios = ["Auth-API", "Database-Cluster", "Frontend-Nginx", "Cache-Redis"]
direcciones_ip = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40"]
estados_salud = ["ONLINE", "MAINTENANCE", "ONLINE", "CRITICAL"]

print("==================================================")
print("🖥️  MONITOR DE INFRAESTRUCTURA - PANDITA CORE")
print("==================================================\n")

# 🌟 COMBINACIÓN MAESTRA:
# 1. 'zip' une las tres listas en un solo flujo.
# 2. 'enumerate' envuelve ese flujo para darnos un número de Rack (ID) empezando en 1.
for id_rack, (servicio, ip, estado) in enumerate(zip(servicios, direcciones_ip, estados_salud), start=1):
    
    # Operador ternario para darle color visual al estado
    if estado == "ONLINE":
        color_status = f"\033[32m{estado}\033[0m"   # Verde
    elif estado == "MAINTENANCE":
        color_status = f"\033[33m{estado}\033[0m"  # Amarillo
    else:
        color_status = f"\033[31m{estado}\033[0m"  # Rojo
        
    print(f"[Rack #{id_rack}] 🚀 Nodo: {servicio:<18} | IP: {ip:<13} | Estado: {color_status}")

print("\n==================================================")

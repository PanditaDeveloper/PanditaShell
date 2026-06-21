procesos_sistema = [
    ("nvim.exe", 45, "running"),
    ("chrome.exe", 850, "running"),
    ("powershell.exe", 120, "running"),
    ("python.exe", 310, "running"),
    ("discord.exe", 95, "suspended"),
    ("svchost.exe", 15, "running")
]

print("==================================================")
print("🔍 FILTRADO DE PROCESOS CRÍTICOS (> 100MB RAM)")
print("==================================================")

procesos_pesados = [
        f"🚨 Alerta: {nombre} consumiendo {ram}MB"
        for nombre, ram, estado in procesos_sistema
        if ram > 100 and estado == "running"
]

for alerta in procesos_pesados:
    print(alerta)

print("==================================================")

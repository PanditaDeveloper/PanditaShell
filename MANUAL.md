# 🐼 Manual de Referencia de PanditaShell (Mi "Man Page" Personal)

Bienvenido a tu bitácora y manual de comandos personalizado. Este archivo está diseñado en formato Markdown (`.md`) para que Neovim renderice la sintaxis con colores hermosos gracias a tu nuevo tema *Tokyo Night*. Puedes usarlo como tu propia página de ayuda (`man`) para repasar atajos, comandos de consola, flujos de Git y desarrollo en Python.

---

## 💻 1. El Shell: PowerShell 7 y Navegación

La consola es tu centro de operaciones. Aquí tienes los comandos y superpoderes que hemos configurado y aprendido.

### 📌 Comandos de Navegación Básica
| Comando | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| `pwd` | *Print Working Directory*. Muestra la ruta exacta donde estás parado. | `pwd` |
| `ls` o `dir` | Lista los archivos y carpetas del directorio actual. | `ls` |
| `ll` | Alias personalizado para ver detalles completos de los archivos. | `ll` |
| `cd <ruta>` | *Change Directory*. Muévete a otra carpeta. | `cd Documents\proyectos` |
| `cd ..` | Retrocede una carpeta hacia arriba en el árbol de directorios. | `cd ..` |
| `cd ~` | Te lleva directo a tu carpeta raíz de usuario (`C:\Users\TuUsuario`). | `cd ~` |
| `cls` | Alias personalizado que limpia la pantalla y vuelve a dibujar tu banner de inicio. | `cls` |

### 📌 Gestión de Archivos desde Consola
* **Crear Carpeta:** `mkdir <nombre>` (Ej: `mkdir scripts-python`)
* **Crear Archivo Vacío:** `New-Item <archivo.ext>` (Ej: `New-Item README.md`)
* **Forzar Estructuras:** `New-Item -Path $PROFILE -ItemType File -Force` (Crea carpetas contenedoras y el archivo si no existen).
* **Mover Elementos:** `Move-Item <origen> <destino>` (Ej: `Move-Item ..\organizador.py .\scripts-python\`)
* **Copiar Elementos:** `Copy-Item <origen> <destino>` (Ej: `Copy-Item $PROFILE .\configuraciones\`)

### ⚡ Trucos de Productividad en Consola
* **El Tabulador (`Tab`):** Escribe el inicio de un comando o ruta y presiona `Tab` para que la consola lo complete automáticamente.
* **Flecha Derecha (->):** Acepta la predicción gris del historial predictivo que configuramos.
* **Buscar en Historial (`Ctrl + R`):** Presiona este atajo y empieza a escribir un comando viejo; la consola lo buscará al instante.

---

## 📝 2. El Editor: Neovim (Atajos de Teclado)

Neovim no usa el mouse de forma nativa; todo se controla mediante **Modos** y combinaciones de teclas. Recuerda tu alias maestro: escribir **`v <archivo>`** o **`v .`** abre Neovim al instante.

### 🔄 Los Modos de Neovim
1. **Modo Normal (Por Defecto):** Sirve para moverte, borrar, copiar y ejecutar comandos. Entras aquí presionando la tecla `Esc`.
2. **Modo Inserto (Escribir):** Sirve para redactar código. Entras desde el Modo Normal presionando la tecla `i`. Verás `-- INSERT --` abajo.
3. **Modo Comando (Acciones del Editor):** Sirve para guardar, salir y configurar. Entras desde el Modo Normal escribiendo `:` (dos puntos).

### 🚀 Movimiento y Edición Rápida (Modo Normal)
* `h`, `j`, `k`, `l` : Movimiento básico (Izquierda, Abajo, Arriba, Derecha).
* `w` / `b` : Salta a la siguiente palabra / Regresa a la palabra anterior.
* `0` / `$` : Salta al inicio / final absoluto de la línea actual.
* `x` : Borra la letra exacta sobre la que está el cursor.
* `dd` : Borra (corta) la línea completa actual.
* `o` : Abre una línea en blanco debajo y entra en Modo Inserto.

### 📂 Navegación Ninja y Explorador de Archivos (Netrw)
| Comando | Descripción |
| :--- | :--- |
| `v .` | Abre Neovim inicializando el explorador en la carpeta actual. |
| `Ctrl + n` | Abre o cierra el panel del explorador de archivos lateral. |
| `Ctrl + w` luego `l` | Salta del explorador izquierdo hacia el editor de código derecho. |
| `Ctrl + w` luego `h` | Regresa el cursor del editor de código al explorador izquierdo. |
| `Enter` (en Netrw) | Abre la carpeta seleccionada o carga el archivo en el editor. |
| `%` (en Netrw) | Crea un nuevo archivo dentro de la carpeta seleccionada. |
| `d` (en Netrw) | Crea una nueva carpeta en el directorio actual. |
| `R` / `D` (en Netrw) | Renombra / Elimina el archivo o carpeta seleccionado. |

### 💾 Comandos de Archivo (Modo Comando `:`)
* `:w` : Guarda los cambios (*Write*).
* `:q` : Cierra el archivo actual (*Quit*).
* `:wq` : Guarda los cambios y cierra el editor de un solo golpe.
* `:q!` : Fuerza el cierre del editor **sin guardar** los cambios realizados.

---

## 🧠 3. Neovim Inteligente: LSP y Automatizaciones

Tu entorno cuenta con el instalador de servidores **Mason**, un motor de autocompletado flotante (**nvim-cmp**) y un sistema de auto-cierre de caracteres (**nvim-autopairs**).

### ⚡ Atajos de Inteligencia Artificial e IDE
* `K` (Mayúscula) : Muestra una ventana flotante con la documentación oficial de la función que pisas.
* `gd` : *Go to Definition*. Salta al archivo y línea exacta donde nació la variable o función.
* **`F5` (Atajo Maestro Pandita):** Guarda el archivo automáticamente, divide la pantalla y ejecuta el script de Python.
* **`Tab` / `Shift + Tab`** : Navega hacia abajo / arriba en el menú flotante de sugerencias de código.
* **`Enter`** : Confirma la sugerencia del menú y auto-rellena el código por ti.

> ⚙️ **Nota de Arquitectura:** El entorno está configurado con la sintaxis nativa moderna `vim.lsp.enable('pyright')`, garantizando velocidad máxima y compatibilidad con versiones de Neovim 0.11 o superiores.

---

## 🐙 4. Control de Versiones: Git Basado en Consola

Tu prompt en la terminal te avisa en qué rama estás parado y cambia a **Rojo con un asterisco (`*`)** si tienes cambios pendientes, o a **Verde** si todo está guardado.

### 📐 Flujo de Trabajo Diario en Git
1. **Inicializar proyecto:** `git init` (Solo una vez por carpeta).
2. **Preparar archivos:** `git add .` (El punto agrega absolutamente todos los cambios).
3. **Confirmar cambios:** `git commit -m "Mensaje descriptivo"` (Guarda la foto localmente).
4. **Subir a GitHub:** `git push origin main` (Respalda en la nube).

### 🧩 Alias Útiles de Git (Forzados en tu Perfil)
* `gs` : Abre el estado rápido de Git (`git status`).
* `gc "mensaje"` : Hace un commit rápido ahorrando comandos (`git commit -m`).
* `gp` : Sube los cambios rápidamente a la nube (`git push`).

---

## 🐍 5. El Lenguaje: Python para Automatización

### 📝 Estructura y Librerías del Sistema
* `import os` / `import shutil` : Interacción avanzada con el sistema de archivos de Windows.
* `input("Texto: ")` : Captura datos del usuario por teclado (siempre entran en formato Texto).
* `int(variable)` : *Type Casting*. Convierte un texto numérico en un entero real para cálculos matemáticos.

### 🔄 Control de Flujos y Bucles
* **Bucle `for in range(inicio, fin)`** : Bucle controlado que itera un número determinado de veces.
* **Bucle `while <condicion>:`** : Repite un bloque de código mientras la condición booleana sea verdadera.
* **`break`** : Rompe y aborta de forma inmediata la ejecución de cualquier bucle.

### ⚠️ Gestión Profesional de Errores
Estructura robusta de 4 bloques para evitar que el software explote ante fallos imprevistos:
```python
try:
    # Código bajo monitoreo que puede lanzar excepciones
    resultado = 10 / int(input("Divide entre: "))
except ZeroDivisionError:
    # Se ejecuta solo si se intentó dividir entre cero
    print("❌ ¡No puedes dividir entre cero!")
except ValueError:
    # Se ejecuta si el usuario escribió letras en vez de números
    print("❌ ¡Debes ingresar un número entero válido!")
else:
    # Se ejecuta ÚNICAMENTE si el bloque TRY fue 100% exitoso
    print(f"✅ Operación realizada con éxito. Resultado: {resultado}")
finally:
    # Se ejecuta SIEMPRE, haya ocurrido un error o no (Limpieza de memoria/auditoría)
    print("🧹 Ciclo de ejecución finalizado.")

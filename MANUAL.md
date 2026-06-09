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
* **El Tabulador (`Tab`):** Escribe el inicio de un comando o ruta y presiona `Tab` para que la consola lo complete mágicamente.
* **Flecha Derecha ($ightarrow$):** Acepta la predicción gris del historial predictivo que configuramos.
* **Buscar en Historial (`Ctrl + R`):** Presiona este atajo y empieza a escribir un comando viejo; la consola lo buscará al instante.

---

## 📝 2. El Editor: Neovim (Atajos de Teclado)

Neovim no usa el mouse de forma nativa; todo se controla mediante **Modos** y combinaciones de teclas. Recuerda tu alias maestro: escribir **`v <archivo>`** abre Neovim al instante.

### 🔄 Los Modos de Neovim
1.  **Modo Normal (Por Defecto):** Sirve para moverte, borrar, copiar y ejecutar comandos. Entras aquí presionando la tecla `Esc`.
2.  **Modo Inserto (Escribir):** Sirve para redactar código. Entras desde el Modo Normal presionando la tecla `i`. Verás `-- INSERT --` abajo.
3.  **Modo Comando (Acciones del Editor):** Sirve para guardar, salir y configurar. Entras desde el Modo Normal escribiendo `:` (dos puntos).

### 🚀 Movimiento Avanzado (Modo Normal)
Deja de usar las flechas del teclado. Tus manos deben descansar en la fila central:
* `h` : Mueve el cursor a la **izquierda**.
* `j` : Mueve el cursor hacia **abajo**.
* `k` : Mueve el cursor hacia **arriba**.
* `l` : Mueve el cursor a la **derecha**.
* `w` : Salta a la siguiente **palabra** (*Word*).
* `b` : Regresa a la **palabra anterior** (*Back*).
* `0` : Salta al **inicio absoluto** de la línea.
* `$` : Salta al **final absoluto** de la línea.

### ✂️ Edición Rápida (Modo Normal)
* `x` : Borra la letra exacta sobre la que está el cursor.
* `dd` : Borra (corta) la línea completa actual.
* `o` : Abre una línea en blanco **debajo** de tu posición actual y entra en Modo Inserto.

### 💾 Comandos de Archivo (Modo Comando `:`)
* `:w` : Guarda los cambios (*Write*).
* `:q` : Cierra el archivo actual (*Quit*).
* `:wq` : Guarda los cambios y cierra el archivo de un solo golpe.
* `:q!` : Fuerza el cierre del editor **sin guardar** los cambios realizados.

---

## 🧠 3. Neovim Inteligente: LSP y Atajos Profesionales

Gracias a **Mason** y al Language Server Protocol (LSP), Neovim analiza tu código en tiempo real utilizando el motor de Microsoft para Python (`pyright`).

### 🛠️ Comandos Internos de Plugins
* `:Lazy` : Abre la interfaz gráfica de tu gestor de plugins para ver actualizaciones o cargas.
* `:Mason` : Abre la tienda interna de LSPs. Desde ahí instalas, actualizas o remueves soportes de lenguajes presionando `i`.

### ⚡ Atajos de Inteligencia Artificial (Modo Normal)
* `K` (Mayúscula) : Muestra una ventana flotante con la **documentación oficial** de la función o módulo que tu cursor esté pisando.
* `gd` : *Go to Definition*. Salta directamente al archivo y línea exacta donde se definió la variable o función.
* **`F5` (Atajo Maestro Pandita):** Guarda tu archivo automáticamente, divide la pantalla horizontalmente y **ejecuta tu script de Python** en una consola interna. Escribe `exit` en esa consola para cerrarla.

---

## 🐙 4. Control de Versiones: Git Basado en Consola

Tu prompt en la terminal ahora es inteligente. Te avisa en qué rama estás parado y cambia a **Rojo con un asterisco (`*`)** si hay cambios pendientes, o a **Verde** si todo está guardado.

### 📐 Flujo de Trabajo Diario en Git
1.  **Inicializar proyecto:** Solo se hace una vez por carpeta.
    ```powershell
    git init
    ```
2.  **Preparar archivos (Tomar foto):** Selecciona qué cambios vas a guardar.
    ```powershell
    git add .   # El punto agrega TODOS los archivos de la carpeta
    git add nombre_archivo.py  # Agrega solo ese archivo específico
    ```
3.  **Hacer Commit (Confirmar foto):** Guarda los archivos localmente con un mensaje de qué hiciste.
    ```powershell
    git commit -m "Explicación breve de los cambios o mejoras"
    ```
4.  **Subir a GitHub (Respaldar en la Nube):**
    ```powershell
    git push origin main
    ```

### 🧩 Alias Útiles de Git creados en tu perfil
* `gs` : Abre el estado rápido de Git (`git status`).
* `gc "mensaje"` : Hace un commit rápido sin escribir todo el comando (`git commit -m`).
* `gp` : Sube los cambios rápidamente a la nube (`git push`).

---

## 🐍 5. El Lenguaje: Python para Automatización

Python es limpio, no requiere compilación pesada y es ideal para el rendimiento de tu laptop (8 GB RAM).

### 📝 Estructura Básica de Scripts Aprendida
En nuestro primer proyecto (`organizador.py`), dominamos librerías del sistema operativo:
* `import os` : Permite hablar con Windows (crear carpetas, listar archivos, verificar rutas).
* `import shutil` : Permite manipular archivos a bajo nivel (mover, copiar, borrar de raíz).
* `os.path.join()` : Une carpetas de forma segura sin importar si Windows usa barras `\` o Linux usa `/`.
* `os.path.splitext()` : Separa mágicamente el nombre de un archivo de su extensión (Ej: `foto.png` -> `foto` y `.png`).

---

*Manual creado con dedicación para @PanditaDeveloper. Puedes editar este archivo desde Neovim con `v MANUAL.md` y agregar nuevas secciones a medida que vayamos desbloqueando tecnologías (como Go o SQL).*

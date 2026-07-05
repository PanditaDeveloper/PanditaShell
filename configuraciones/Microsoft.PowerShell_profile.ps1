# --- ROTULO DE BIENVENIDA (PANDITA DEV) ---
$asciiArt = @"
██████╗  █████╗ ███╗   ██╗██████╗ ██╗████████╗ █████╗ 
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██║╚══██╔══╝██╔══██╗
██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║   ███████║
██╔═══╝ ██╔══██║██║╚██╗██║██║  ██║██║   ██║   ██╔══██║
██║     ██║  ██║██║ ╚████║██████╔╝██║   ██║   ██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝
                    ╺┳┓┏━╸╻ ╻
                     ┃┃┣╸ ┃┏┛
                    ╺┻┛┗━╸┗┛ 
"@

function Center-AsciiArtBlock {
    param (
        [string]$AsciiText,
        [string]$Color = "Cyan"
    )

    $consoleWidth = (Get-Host).UI.RawUI.BufferSize.Width
    $lines = $AsciiText -split "`n"
    $maxLineWidth = ($lines | Measure-Object -Maximum -Property Length).Maximum

    foreach ($line in $lines) {
        $padding = ($consoleWidth - $maxLineWidth) / 2
        # Evitar errores si la consola es muy estrecha
        if ($padding -lt 0) { $padding = 0 }
        Write-Host (" " * $padding + $line) -ForegroundColor $Color
    }
}

Center-AsciiArtBlock -AsciiText $asciiArt -Color Cyan

# --- FUNCION PARA CENTRAR TEXTO ---
function Center-Text {
    param (
        [string]$Text,
        [string]$Color = "White"
    )
    $consoleWidth = (Get-Host).UI.RawUI.BufferSize.Width
    $padding = ($consoleWidth - $Text.Length) / 2
    if ($padding -lt 0) { $padding = 0 }
    Write-Host (" " * $padding + $Text) -ForegroundColor $Color
}

# --- INFORMACIÓN PRINCIPAL ---
Center-Text -Text "Bienvenido a tu entorno de desarrollo, Cristobal 🚀" -Color Yellow
Center-Text -Text "Hoy es: $(Get-Date -Format 'dddd, dd MMMM yyyy HH:mm')" -Color Green
Write-Host ""

# --- INFO DEL SISTEMA EN TABLA MEJORADA ---
function Draw-Centered-Table {
    param(
        [string]$Title,
        [Hashtable]$Data
    )

    $consoleWidth = (Get-Host).UI.RawUI.BufferSize.Width
    $tableWidth = [int]($consoleWidth * 0.8)
    if ($tableWidth -lt 80) { $tableWidth = 80 }

    # DIBUJAR BORDES SUPERIORES
    $borderTop = "╔" + ("═" * ($tableWidth - 2)) + "╗"
    Center-Text -Text $borderTop -Color Cyan

    # DIBUJAR TÍTULO
    $titlePadded = (" " * [int](($tableWidth - 2 - $Title.Length) / 2)) + $Title
    $titleLine = "║" + $titlePadded + (" " * ($tableWidth - 2 - $titlePadded.Length)) + "║"
    Center-Text -Text $titleLine -Color Cyan

    # CALCULAR ANCHOS DE COLUMNA
    $dataKeys = $Data.Keys | Sort-Object
    $maxLabelLength = ($dataKeys | Measure-Object -Maximum -Property Length).Maximum
    $labelColWidth = $maxLabelLength + 2
    $valueColWidth = $tableWidth - $labelColWidth - 3

    # DIBUJAR SEPARADOR
    $separator = "╠" + ("═" * ($labelColWidth - 1)) + "╦" + ("═" * ($valueColWidth + 1)) + "╣"
    Center-Text -Text $separator -Color Cyan

    # DIBUJAR DATOS
    foreach ($key in $dataKeys) {
        $value = $Data[$key]
        $labelPadded = " " + $key.PadRight($labelColWidth - 2, " ")
        $valuePadded = " " + $value.PadRight($valueColWidth, " ")
        $row = "║" + $labelPadded + "║" + $valuePadded + "║"
        Center-Text -Text $row -Color Cyan
    }

    # DIBUJAR BORDES INFERIORES
    $borderBottom = "╚" + ("═" * ($tableWidth - 2)) + "╝"
    Center-Text -Text $borderBottom -Color Cyan
    Write-Host ""
}

# --- USO DE LA FUNCIÓN PARA DIBUJAR LA TABLA ---
# Cambié $env:COMPUTERNAME por una validación más limpia y usé [ordered] para fijar el orden.
$systemInfo = [ordered]@{
    "Usuario" = "Cristobal (Pandita Triste)"
    "PC" = "$env:COMPUTERNAME"
    "Versión de PowerShell" = "v$($PSVersionTable.PSVersion.Major).$($PSVersionTable.PSVersion.Minor)"
    "Editor Principal" = "Neovim"
}

Draw-Centered-Table -Title "Información del sistema" -Data $systemInfo

# --- PROMPT PERSONALIZADO CON SOPORTE GIT DINÁMICO ---
function prompt {
    $currentPath = (Get-Location).Path
    Write-Host ("PS " + $currentPath) -ForegroundColor Cyan -NoNewline

    # Lógica para detectar Git dinámicamente
    if (Get-Command git -ErrorAction SilentlyContinue) {
        $isGitRepo = git rev-parse --is-inside-work-tree 2>$null
        if ($isGitRepo -eq 'true') {
            # Obtener la rama actual
            $branch = git branch --show-current 2>$null
            # Verificar si hay cambios sin commitear
            $status = git status --porcelain 2>$null
            
            if ($status) {
                # Si hay cambios, se muestra en rojo con un asterisco
                Write-Host " [Git: $branch *]" -ForegroundColor Red -NoNewline
            } else {
                # Si está limpio, se muestra en verde
                Write-Host " [Git: $branch]" -ForegroundColor Green -NoNewline
            }
        }
    }
    
    # Salto de línea para que el cursor quede abajo, más limpio para comandos largos
    Write-Host ""
    Write-Host "> " -ForegroundColor Yellow -NoNewline
    return " "
}

# --- ALIAS ÚTILES Y DETECCIÓN DE GIT ---
Set-Alias ll Get-ChildItem -Force
Set-Alias v nvim -Force
Set-Alias python3 python -Force

# PowerShell reserva gs, gc y gp de forma nativa. Usamos funciones intermedias y forzamos el alias:
function Watch-GitStatus { git status }
function Do-GitCommit { git commit -m "$args" }
function Do-GitPush { git push }

Set-Alias gs Watch-GitStatus -Force
Set-Alias gc Do-GitCommit -Force
Set-Alias gp Do-GitPush -Force

# --- AUTOCOMPLETADO Y PREDICTIVO ---
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle ListView

# --- LIMPIAR PANTALLA Y MOSTRAR PERFIL ---
function Clean-Screen-And-Show-Profile {
    Clear-Host
    & $PROFILE
}

Set-Alias cls Clean-Screen-And-Show-Profile -Force

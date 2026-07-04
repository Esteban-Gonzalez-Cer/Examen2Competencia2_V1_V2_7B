#README

Este proyecto contiene 2 analizadores léxicos (lexers) independientes, construidos mediante **ANTLR4** y programados con **Python 3**. Su objetivo principal es analizar gramáticas léxicas básicas y tokenizar cadenas de entrada, imprimiendo la información detallada de cada token reconocido.

## Descripción

Contiene los ejercicios del examen para la materia de **Lenguajes y Autómatas II**. Cada carpeta contiene una gramática definida en un archivo `.g4`, el analizador generado para Python 3 y un script interactivo para realizar las pruebas de tokenización. Las gramáticas están diseñadas para reconocer desde expresiones numéricas simples y asignaciones de variables, hasta comandos de impresión, estructuras condicionales y operadores de comparación.

## Tecnologías utilizadas

- Python 3.x
- ANTLR4 (Parser Generator v4.13.2)
- Java JDK 21+ (necesario para compilar gramáticas de ANTLR4)
- Git

## Requisitos previos

Para poder ejecutar o modificar los analizadores, asegúrese de tener instalado en su sistema:
- **Java JDK 21** o superior (para ejecutar el generador de ANTLR).
- **Python 3.10** o superior.
- **Visual Studio Code** (o cualquier otro editor de código).
- **Git** (para la gestión de versiones).

## Instalación

1. Clonar el repositorio desde GitHub:
   ```bash
   git clone https://github.com/Esteban-Gonzalez-Cer/Examen2Competencia2_V1_V2_7B.git
   ```


## Configuración

Si desea compilar o modificar los archivos de gramática (`.g4`), debe tener configurado ANTLR4 en su entorno:

- **En macOS (con Homebrew):**
  ```bash
  brew install antlr
  ```
- **En Windows:**
  Asegurarse de descargar la herramienta `antlr-4.13.2-complete.jar` y configurar la variable de entorno `CLASSPATH` de Java, agregando un alias o script para facilitar su ejecución desde la consola.

## Ejecución del proyecto

Cada uno de los 10 programas cuenta con un entorno virtual de Python preconfigurado (`venv`) con la librería runtime correspondiente para evitar problemas de dependencias globales.

Para probar cualquiera de los analizadores léxicos:

1. Ingrese a la carpeta del programa deseado (por ejemplo, `PROGRAMA_1`):
   ```bash
   cd PROGRAMA_1
   ```
2. Active el entorno virtual de Python:
   - **En macOS y Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **En Windows (CMD):**
     ```cmd
     venv\Scripts\activate.bat
     ```
   - **En Windows (PowerShell):**
     ```powershell
     venv\Scripts\Activate.ps1
     ```
3. Inicie el script interactivo:
   Para el programa 1:
     ```bash
     python main.py
     Indicar la dirección del archivo
     ```
     Para el programa 3:
     ```bash
     streamlit run app.py
     ```
   
   ```
4. Desactive el entorno virtual al finalizar las pruebas:
   ```bash
   deactivate
   ```


Cada una de las carpetas de los programas contiene:
- `Expr.g4`: Especificación de gramática y reglas léxicas de ANTLR4.
- `ExprLexer.py` / `ExprParser.py` / `.tokens`: Archivos de código y metadatos generados por ANTLR4.

- `venv/`: Entorno virtual de Python con las dependencias necesarias.

## Autor

Desarrollado por:
- **Esteban Gonzalez Cervantes** ([Esteban-Gonzalez-Cer](https://github.com/Esteban-Gonzalez-Cer))


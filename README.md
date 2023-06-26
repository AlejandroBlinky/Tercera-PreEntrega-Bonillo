# Readme de aplicacion.
--Nombre de la Aplicación--
-"AppPlayground"-


--Descripción--
AppPlayground es una aplicación web que permite administrar estudiantes, cursos y profesores en un entorno educativo.


--Instalación--

1.-Asegúrate de tener Python y Django instalados en tu sistema.

2.-Clona el repositorio de la aplicación desde GitHub:
git clone https://github.com/tu-usuario/AppPlayground.git

3.-Navega al directorio del proyecto:
cd AppPlayground

4.-Instala las dependencias del proyecto:
pip install -r requirements.txt

5.-Realiza las migraciones de la base de datos:
python manage.py migrate


Inicia el servidor de desarrollo:

Copy code
python manage.py runserver
Accede a la aplicación en tu navegador web en http://localhost:8000/.

--Estructura del Proyecto--


La carpeta `AppPlayground` contiene toda la logica de la aplicacion web con sus funcionalidades.

Dentro en la carpeta `templates` se encuentran todas las plantillas de html necesarias para las paginas.

En la carpeta `static` estan todos los archivos de css, javascript, etc.

La carpeta `PlaygroundProyecto3` contiene las configuraciones principales del proyecto, y no sera utilizada.


--Uso---

1.-Accede a la página de inicio para verificar que la aplicación se carga correctamente.

2.-Explora las diferentes secciones de la aplicación, como cursos, estudiantes y profesores.

3.-Utiliza las funciones de configuración para agregar nuevos estudiantes, cursos y profesores.

4.-Utiliza las funciones de búsqueda para encontrar estudiantes, cursos o profesores específicos.
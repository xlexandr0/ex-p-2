# 🎮 Gameverse API

API REST hecha con **Django + Django REST Framework** para gestionar **Videojuegos** y **Compañías**.  
Permite realizar todas las operaciones CRUD mediante endpoints, sin usar el panel de administración.

---

## ⚙️ Instalación

```bash
git clone https://github.com/xlexandr0/ex-p-2.git
cd ex-p-2
python -m venv .venv
.venv\Scripts\activate        # En Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Servidor: http://127.0.0.1:8000/

📚 Endpoints principales
Recurso	Método	Ruta	Descripción
Videojuegos	GET	/videojuegos/	Listar videojuegos
〃	POST	/videojuegos/	Crear videojuego
〃	PUT/PATCH	/videojuegos/{id}/	Editar videojuego
〃	DELETE	/videojuegos/{id}/	Eliminar videojuego
〃	GET	/videojuegos/?search=valor	Buscar por título o género
Compañías	CRUD completo	/companias/	Gestionar compañías

🧪 Ejemplos
bash
Copiar código
# Crear compañía
curl -X POST http://127.0.0.1:8000/companias/ \
 -H "Content-Type: application/json" \
 -d '{"nombre":"SuperDev","pais":"Japón"}'

# Crear videojuego
curl -X POST http://127.0.0.1:8000/videojuegos/ \
 -H "Content-Type: application/json" \
 -d '{"titulo":"Space Quest","genero":"Aventura","anio_lanzamiento":1992,"compania":1}'

# Buscar por género
curl -X GET "http://127.0.0.1:8000/videojuegos/?search=Aventura"
🌟 Características
CRUD completo con DRF ViewSets

Filtro y búsqueda por título/género

Relación entre videojuegos y compañías

Respuesta personalizada con datos anidados (compania_detalle)

🧑‍💻 Autor: xlexandr0

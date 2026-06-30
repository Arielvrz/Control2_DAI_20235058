from flask import Flask, jsonify, request

app = Flask(__name__)

# Repositorio tempora de datos
# Esto no representa persistencia de datos
libros = {
    101: {
        "id": 101, "titulo": "Clean Code", "autor": "Robert C. Martin", "disponible": True},
    102: {
        "id": 102, "titulo": "Python Crash C", "autor": "Eric Matthes", "disponible": True},
    103: {
        "id": 103, "titulo": "Architecture Patterns", "autor": "GoF", "disponible": False}
}

if __name__ == "__main__":
    app.run(debug=True, port=5002)

@app.get('/')
def inicio():
    return jsonify(
        {
            "mensaje": "API REST de Biblioteca Universitaria",
            "version": "1.0",
            "endpoints": [
                "GET /libros", # Muestra todos los libros
                "GET /libros/<id>", # Informacion de UN libro
                "POST /libros", # Crear un nuevo libro
                "PUT /libros/<id>", # Modificar la disponibilidad
                "DELETE /libros/<id>" # Borrar un libro
            ]
        }
    )

# Obtener todos los libros
@app.get('/libros')
def obtener_libros():
    return jsonify(list(libros.values()))

# Obtener un libro por ID
@app.get('/libros/<id>')
def obtener_libro(id):
    libro = libros.get(int(id))
    if libro:
        return jsonify(libro)
    return jsonify({"mensaje": "Libro no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)

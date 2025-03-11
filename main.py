from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bookblogv1.netlify.app/"],  # Solo permite este dominio
    allow_credentials=True,
    allow_methods=["GET"],  # Métodos permitidos (GET en este caso)
    allow_headers=["*"],  # Permite todos los headers
)

# Lista de frases motivadoras con autores
motivational_quotes = [
    {"quote": "El éxito es la suma de pequeños esfuerzos repetidos día tras día.", "author": "Robert Collier"},
    {"quote": "Cree en ti mismo y todo será posible.", "author": "Anónimo"},
    {"quote": "Nunca es tarde para ser lo que podrías haber sido.", "author": "George Eliot"},
    {"quote": "El único límite para lograrlo eres tú mismo.", "author": "Anónimo"},
    {"quote": "La vida es 10% lo que te ocurre y 90% cómo reaccionas a ello.", "author": "Charles R. Swindoll"},
    {"quote": "El futuro pertenece a aquellos que creen en la belleza de sus sueños.", "author": "Eleanor Roosevelt"},
    {"quote": "No cuentes los días, haz que los días cuenten.", "author": "Muhammad Ali"},
    {"quote": "El único modo de hacer un gran trabajo es amar lo que haces.", "author": "Steve Jobs"},
    {"quote": "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.", "author": "Albert Schweitzer"},
    {"quote": "La única manera de hacer un gran trabajo es amar lo que haces.", "author": "Steve Jobs"},
    {"quote": "La mejor manera de predecir el futuro es inventarlo.", "author": "Alan Kay"}
]

@app.get("/quote")
async def get_quote():
    return random.choice(motivational_quotes)

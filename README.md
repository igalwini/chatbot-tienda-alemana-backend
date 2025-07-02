# Chatbot Tienda Alemana – Backend (FastAPI)

Este proyecto implementa un backend en **FastAPI** que expone un servicio inteligente de soporte al cliente para la Tienda Alemana. El sistema está basado en la arquitectura **RAG (Retrieval-Augmented Generation)** y permite responder preguntas frecuentes como ubicación de productos, precios y horarios de sucursales.

Internamente, utiliza:

* **LangChain** para orquestar el pipeline.
* **FAISS** como índice vectorial.
* **HuggingFace Embeddings** para representación semántica.
* **Ollama** con el modelo local `mistral` para generar respuestas.

> ⚠️ Requiere Python 3.10 o superior.

## 📁 Estructura del proyecto

```
app/
├── main.py          # Punto de entrada del servidor
├── rag_pipeline.py  # Lógica del pipeline RAG
├── models.py        # Esquemas Pydantic para input/output
├── config.py        # Configuración centralizada
vector_store/        # Índice FAISS (debe generarse desde notebooks)
requirements.txt     # Lista de dependencias
```

## ⚙️ Cómo ejecutar

1. Clonar este repositorio.
2. Crear y activar un entorno virtual.
3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```
4. Generar el índice FAISS ejecutando los notebooks en el directorio `notebooks/`.
   El archivo generado (`vector_store/`) debe copiarse a la raíz del backend.
5. Iniciar el modelo en Ollama:

   ```bash
   ollama run mistral
   ```
6. Levantar el servidor FastAPI:

   ```bash
   uvicorn app.main:app --reload
   ```

## 📡 API disponible

### `POST /ask`

* **Request JSON**

```json
{ "question": "¿Dónde está el arroz de 1kg?" }
```

* **Response JSON**

```json
{ "answer": "El arroz de 1kg se encuentra en la góndola 5, sección Almacén." }
```

## 🧪 Ejemplo con `curl`

```bash
curl -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "¿Qué productos hay en la góndola 2?"}'
```

---

> 📌 **Importante:** El backend no funcionará si no se incluye el directorio `vector_store/` generado desde los notebooks, ni si el modelo `mistral` no está corriendo en Ollama.

---

## 📦 requirements.txt

```txt
fastapi
uvicorn
langchain
langchain-community
langchain-huggingface
langchain-ollama
sentence-transformers
faiss-cpu
pydantic
tiktoken
```

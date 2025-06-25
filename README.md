# Chatbot Tienda Alemana Backend

Este proyecto implementa un backend en **FastAPI** para exponer un sistema de soporte automatizado de la Tienda Alemana. Utiliza un pipeline RAG construido con LangChain, embeddings de `sentence-transformers` y un índice FAISS para recuperar información relevante. El modelo de lenguaje se ejecuta localmente mediante Ollama con el modelo `mistral`.

## Estructura

```
app/
├── main.py          # Punto de entrada del servidor
├── rag_pipeline.py  # Carga del FAISS y generación de respuestas
├── models.py        # Esquemas Pydantic
└── config.py        # Configuración
vector_store/        # Índice FAISS previamente generado (no incluido)
requirements.txt     # Dependencias
```

## Uso

1. Crear un entorno virtual y activar.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Hacer solicitudes POST a `http://localhost:8000/ask` con un cuerpo JSON:
   ```json
   { "question": "¿Dónde está el arroz de 1kg?" }
   ```

El servicio responderá con una cadena generada por el modelo.

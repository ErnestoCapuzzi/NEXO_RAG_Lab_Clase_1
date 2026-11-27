# NEXO / RAG LAB

**Módulo 1 · Clase 1: Estrategias de Segmentación Avanzada**

Una experiencia educativa e interactiva basada en el material de clase del curso *Desarrollo de Aplicaciones de Inteligencia Artificial con RAG y Arquitectura de Agentes*. Es un proyecto de estudio independiente, no una página oficial de la UTN ni del docente.

## Abrir el sitio

1. Descomprimí el ZIP en cualquier carpeta.
2. Hacé doble clic en `index.html`.
3. Listo. No necesitás Node, React, npm, conexión a internet ni claves API.

También podés abrirlo desde VS Code con Live Server si preferís trabajar en un servidor local. Para publicarlo en GitHub Pages, subí `index.html`, `styles.css`, `app.js` y `assets/` a la raíz del repositorio y activá Pages desde Settings > Pages.

## Qué incluye

- **Introducción a RAG**: documento → chunks → embeddings → recuperación → respuesta.
- **Chunking ciego**: laboratorio con tamaño de corte ajustable y texto editable.
- **Chunking recursivo**: separadores jerárquicos, `chunk_size` y `chunk_overlap`, código Python auténtico.
- **Chunking semántico**: visualización de similitudes entre oraciones con valores ilustrativos y umbral de demostración.
- **Parent-Document Retrieval**: simulación visual de relación hijo → padre con tres casos.
- **Problemas de los documentos reales**: tablas, doble columna, ruido y metadatos.
- **Comparación de estrategias**: casos de uso y criterios de elección.
- **Desafío final**: 8 preguntas con corrección explicada, puntaje y mejor marca local.
- **Story Studio**: 5 temas y exportador PNG de 1080 × 1920 píxeles para Instagram, más texto sugerido para copiar.

## Qué es una simulación y qué es real

Los laboratorios web usan JavaScript local y fueron diseñados para **aprender conceptos**. No ejecutan LangChain, LlamaIndex, embeddings ni bases vectoriales. El laboratorio recursivo aproxima la jerarquía y el solapamiento, pero no pretende reproducir byte a byte el algoritmo de una versión particular de LangChain. El laboratorio semántico usa valores de similitud predeterminados, **no embeddings reales**. Parent-Document Retrieval se ejemplifica con consultas fijas, no con un retriever real. Los ejemplos y su alcance aparecen identificados en la interfaz.

El archivo **`ejemplos/comparacion_real.py`** sí ejecuta las bibliotecas Python instaladas en el entorno de la diplomatura:

```powershell
# Desde la carpeta diplomatura-ia, con .venv creado e instalado:
python -m pip install langchain-text-splitters llama-index-core
python ejemplos\comparacion_real.py
```

Si tenés NEXO RAG Lab en otra carpeta, copiá `ejemplos/comparacion_real.py` dentro de la carpeta `diplomatura-ia/ejemplos/` para ejecutarlo así. En vez de copiarlo, también podés ejecutar `python` sobre su ruta completa.

`RecursiveCharacterTextSplitter` usa caracteres por defecto, mientras que `SentenceSplitter` de LlamaIndex usa tokens. No comparar `chunk_size` en ambas clases como si fuesen unidades iguales.

## Contenido de la fuente

Basado en las 32 páginas aportadas del archivo “Módulo 1 - Clase 1-Estrategias de Segmentación Avanzada (1).pdf”. Temas centrales: limitaciones del RAG estándar; fragmentación ciega; chunking recursivo y semántico; embeddings y similitud coseno; Parent-Document Retrieval; impacto de tablas, columnas y ruido; preprocesamiento; comparación de estrategias; transición a bases vectoriales.

Los textos fueron parafraseados, reordenados y ampliados pedagógicamente. No se reprodujeron logos ni fotografías de la presentación. Algunas afirmaciones cuantitativas de la clase se presentan como pautas generales, no como leyes universales.

## Arquitectura

```text
NEXO_RAG_Lab_Clase_1/
├── index.html                # estructura y accesibilidad
├── styles.css                # sistema visual responsive
├── app.js                    # estado, rutas, laboratorios y exportación
├── assets/
│   └── favicon.svg
├── ejemplos/
│   └── comparacion_real.py   # ejercicio real en Python
└── README.md
```

El progreso del recorrido y la mejor nota se almacenan en `localStorage`, en el navegador que utilizás. No hay backend ni recopilación de datos. El sitio funciona offline.

## Próxima iteración sugerida

Para expandirlo a una plataforma con varios módulos: migrar a React/Vite con componentes desacoplados, agregar tests automatizados, contenidos en archivos JSON/MDX, backend opcional para ejercicios reales con embeddings, y un editor de documentos. El alcance actual prioriza aprendizaje claro, uso inmediato y compatibilidad sin instalar nada.

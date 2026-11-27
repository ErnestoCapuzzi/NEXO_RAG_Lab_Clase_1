"""Ejercicio real de la clase 1, requiere langchain-text-splitters y llama-index-core.
Ejecutar con el Python del entorno de la diplomatura:
  .\.venv\Scripts\python.exe ejemplos\comparacion_real.py
"""
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llama_index.core.node_parser import SentenceSplitter

texto = (
    "## Política de devoluciones\n\n"
    "Se aceptan devoluciones hasta 30 días después de la compra. "
    "Es obligatorio presentar el comprobante de pago.\n\n"
    "## Excepciones\n\n"
    "Los productos personalizados no admiten devolución, "
    "salvo que tengan un defecto de fabricación.\n\n"
) * 6

langchain_splitter = RecursiveCharacterTextSplitter(
    chunk_size=220,
    chunk_overlap=35,
    separators=["\n\n", "\n", " ", ""],
)
llama_splitter = SentenceSplitter(chunk_size=120, chunk_overlap=20)

for nombre, fragmentos in [
    ("LANGCHAIN · caracteres", langchain_splitter.split_text(texto)),
    ("LLAMAINDEX · tokens", llama_splitter.split_text(texto)),
]:
    print(f"\n{'=' * 60}\n{nombre}: {len(fragmentos)} chunks")
    for i, fragmento in enumerate(fragmentos, 1):
        print(f"\nCHUNK {i} · {len(fragmento)} caracteres\n{fragmento}")

print("\nATENCIÓN: Los chunk_size no usan las mismas unidades.")

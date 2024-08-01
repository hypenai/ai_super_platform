import pandas as pd

def process_large_dataset(file_path):
    chunk_size = 10000
    chunks = pd.read_csv(file_path, chunksize=chunk_size)
    for chunk in chunks:
        yield process_chunk(chunk)

def process_chunk(chunk):
    return chunk.apply(lambda x: x * 2)

print("Memory-efficient data processing module initialized.")

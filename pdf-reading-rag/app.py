from loader import load_pdf
from splitter import split_documents

if __name__ == "__main__":
    docs = load_pdf("sample.pdf")
    chunks = split_documents(docs)

    print(f"Pages: {len(docs)}")
    print(f"Chunks: {len(chunks)}\n")

    print("First chunk:\n")
    print(chunks[0].page_content)

    print("\nMetadata:", chunks[0].metadata)
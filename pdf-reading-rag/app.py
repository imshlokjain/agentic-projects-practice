from loader import load_pdf

if __name__ == "__main__":
    docs = load_pdf("sample.pdf")

    print(f"Loaded {len(docs)} documents\n")

    print("First document preview:\n")
    print(docs[0].page_content[:500])
    print("\nMetadata:", docs[0].metadata)

for i, doc in enumerate(docs[:3]):
    print(f"\n--- Document {i} ---")
    print(doc.page_content[:200])
    print(doc.metadata)
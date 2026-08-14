def format_sources(documents):
    sources = []

    for doc in documents:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", None)

        if page is not None:
            page_number = page + 1
            source_text = f"{source}, page {page_number}"
        else:
            source_text = source

        if source_text not in sources:
            sources.append(source_text)

    return sources
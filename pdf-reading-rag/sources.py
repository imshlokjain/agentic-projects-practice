from pathlib import Path


def format_sources(documents):

    sources = []

    for doc in documents:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page_label = doc.metadata.get(
            "page_label"
        )

        source_name = Path(source).name

        if page_label is not None:
            source_text = (
                f"{source_name}, page {page_label}"
            )
        else:
            page = doc.metadata.get("page")

            if page is not None:
                source_text = (
                    f"{source_name}, page {page + 1}"
                )
            else:
                source_text = source_name

        if source_text not in sources:
            sources.append(source_text)

    return sources
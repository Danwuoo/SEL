"""Quick manual check for the semantic retriever."""

from sel.rat import SemanticRetriever

if __name__ == "__main__":
    retriever = SemanticRetriever()
    retriever.index_documents(["hello world", "foo bar"])
    print(retriever.query("hello", top_k=1))


from query import query_rag_pipeline

print("=" * 50)
print("Document QA Bot")
print("=" * 50)

while True:

    question = input(
        "\nAsk Question (or type exit): "
    )

    if question.lower() == "exit":
        break

    answer = query_rag_pipeline(question)

    print("\nAnswer:")
    print(answer)
T = int(input())
for case_num in range(1, T + 1):

    pages = []


    for _ in range(10):
        url, relevance = input().split()
        relevance = int(relevance)
        pages.append((url, relevance))


    max_relevance = max(p[1] for p in pages)


    print(f"Case #{case_num}:")
    for url, relevance in pages:
        if relevance == max_relevance:
            print(url)

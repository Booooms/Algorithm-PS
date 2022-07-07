t = int(input())
for i in range(t):
    sentences = list(input().split())
    reverse_sentences = []
    for sentence in sentences:
        reverse_sentences.append(sentence[::-1])
        print(reverse_sentences)
    print(" ".join(reverse_sentences))
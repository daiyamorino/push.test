def main():
    a, b = map(int, input().split())
    answer=3 #最大三日間参加できない
    for c in range(23,26):
        
        if a<=c<=b:
            answer-=1
    print(answer)


if __name__ == "__main__":
    main()



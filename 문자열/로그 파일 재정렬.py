'''
파이썬 인터뷰
리스트안에 문자열을 주어진 조건에 따라 재정렬하는 문제
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그(문자열의 2번째)가 숫자 로그보다 앞에온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
'''

logs = ["digi1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
letters, digits = [], []

for i in logs:
    if i.split()[1].isdigit():
        digits.append(i)
    else:
        letters.append(i)

letters.sort(key= lambda x: (x.split()[1:], x.split()[0]))
print(letters + digits)
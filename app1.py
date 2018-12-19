"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
iu_list = list(iu_score.values())
iu_sum = 0
for i in iu_list:
    iu_sum += i 
iu_mean = iu_sum/len(iu_list)

print("평균: %d\n"%iu_mean)


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.

dicts = {}
for c in score:
    sscore = list(score[c].values())
    dicts[c] = sum(sscore)/len(sscore)
    
for k in dicts:
    print("%s: %d"%(k, dicts[k]))

print("\n")

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
dict1 = {}
for key in city:
    dict1[key] = sum(city[key]) / len(city[key])

for k in dict1:
    print("%s: %d"%(k, dict1[k]))

print("\n")


# 답변 코드는 아래에 작성해주세요.


dict2 = {}
dict3 = {}
for key in city:
    maxv = city[key][0]
    maxc = key
    for v in city[key]:
        if v > maxv:
            maxv = v
            maxc = key
    dict2[key] = maxv
    dict3["가장 더운 곳"] = dict2
    
    minv = city[key][0]
    minc = key
    for v in city[key]:
        if v < minv:
            minv = v
            minc = key
    dict2[key] = minv        
    dict3["가장 추운 곳"] = dict2
    
for k in dict3:
    print("{}: {}({}도)".format(k, dict3[k].items))

print("\n")


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.

if 2 in city["서울"]:
    print("yes")
else:
    print("no")
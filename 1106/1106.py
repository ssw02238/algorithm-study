import sys
import math
def input():
    return sys.stdin.readline().rstrip()
MIN, MAX = map(int, input().split())
last = int(math.floor(math.sqrt(MAX)))

# 마지막 후보 제곱수, MAX보다 작은 last*last ''' MIN 부터 MAX까지 아리스토 체를 구현한다.
#  res[0] == res[MIN] 이걸 의미하게 하기 위해 넣어줄 떄 res[n-MIN] 을 해준다.
# ''' res = [True for i in range(MAX-MIN+1)] for i in range(2, last+1): zegop = i * i mok = MIN // zegop # 몫을 1씩 높여주며 걸러준다.
#  while True: nxt = mok * zegop # 걸러질 수 (제곱수의 합성수) if nxt < MIN: mok += 1 continue if nxt > MAX: break res[nxt - MIN] = False
#  mok += 1 cnt = 0 for r in res: if r: cnt+= 1 print(cnt)


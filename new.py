def solve(p,k):
   n = len(p)
   hm = dict()
   for t in p:
       if t%k in hm:hm[t%k] += 1
       else:hm[t%k] = 1
   rem = res = 0
   for key in hm:
       res = max(res,hm[key])
       if res == hm[key]:rem = key

   print(res)
   for t in p:
       if t%k == rem:print(t)
   return
n,k = list(map(int,(input().split())))
p = [-1 for i in range(n)]
for q in range(n):
   p[q] = int(input())
p.sort()
solve(p,k)
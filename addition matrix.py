a=[[1,2],
  [5,3]]
b=[[2,3],
  [4,1]]
c[5][5]=int(input())
for i in range(len(a)):
   for j in range(len(b)):
      c[i][j]=a[i][j]+b[i][j]
for i in c:
   print(c[i][j])
   

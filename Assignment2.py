fluctuation_indices = [] # List to store the fluctuation indices.
x = 15
for i in range(5, 25 + 1):
  r = i/10
  N = 50
  tseries = [] # List to store the time series of the specific r.
  for j in range(x):
    N = N * r
    tseries.append(N)
  mean = sum(tseries)/len(tseries)
  A = [abs(tseries[i + 1] - tseries[i]) for i in range(len(tseries) - 1)]
  fi = sum(A) / (mean * x)  
  fluctuation_indices.append(fi)
  print(f"{r}: {fi}")

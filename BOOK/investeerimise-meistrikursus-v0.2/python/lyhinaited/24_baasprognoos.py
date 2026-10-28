# Regressioon versus naiivne prognoos
from statistics import mean
x_train=[-2,-1,1,2]
y_train=[-.02,-.01,.01,.02]
b=sum(x*y for x,y in zip(x_train,y_train))/sum(x*x for x in x_train)
x_test,y_test=[-3,3],[-.025,.025]
mse_model=mean((b*x-y)**2 for x,y in zip(x_test,y_test))
mse_naive=mean(y*y for y in y_test)
print(f"Mudeli MSE: {mse_model:.6f}; nullprognoosi MSE: {mse_naive:.6f}")

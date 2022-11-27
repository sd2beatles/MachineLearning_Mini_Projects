#1. What is the difference ordianry leaste square and MLE?


![image](https://user-images.githubusercontent.com/53164959/204120864-8ac627d5-fda8-4f55-a524-2e8d65429e62.png)

The ordinary least square is concerned with finding the least minimum value of loss from the prediction. The minimum loss here refers to the sum of the distance between actual values and predicted ones that the model equation generates. The most important here is that the model simulates a lot of linear lines, computes the sum of squares of errors(or residuals), and picks the one that best fits with the lower sum of squared residuals. 

MLE, on the other hand, finds the optimal values of intercept and slope of the line that best maximize the likelihood. The most distinct characteristic of mle is that the distribution we choose should reflect the distribution of the data point around the line. Let's assume we are using a normal distribution for our input data. The height of the curve will be higher if the observation is located closer to the central measures (i.e., the mean of the distribution), which are the points lying on the estimated line. We first compute the likelihood of the difference between the actual and each predicted one and compute the joint product of them. 

  By trying out changing the different levels of parameters of linear regression (i.e., weight and biases) with given distribution, we will pick the parameters that lead to the highest joint products of likelihood. These are what are so-called maximum likelihood estimators. 

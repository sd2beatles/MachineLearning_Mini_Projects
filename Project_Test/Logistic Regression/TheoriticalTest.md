## 1.  Can you tell me what is the major difference between the frequentists and bayesian approach?

Frequentists treat an unknown static as a constant from the whole population.Then,they draw conclusions from sample data by looking at the relative frequency of multiple trials.

Their ultimate goal is to find the parameters (i.e., unknown statistics) to maximize the posterior probability,that is, the probability of parameters given a dataset. Bayesian has many distinct features compared to the frequentist approach.

First) They believe that the parameters are not constant but random variable. That is, it follows a distribution and all the prior knowledge of paramters is relfecte to the distribution so called prior distribution. The prior distribution,therefore, provides knowledge about parameters before seeing the data.

Second) Bayesian dynamically updates our posterior probability through prior distriubtion whenever we have more data to come. The mechansim behind it is that the old posterior probabilty becomes the new prior probability since it represents the new prior probability of our belief.

Third) Bayeisan is also concerend with the uncertainty related to the future events. Therefore,the chance of overfitting problem is relatively smaller compared to frequetists. It says that explaining the current events is not enough ,but future events.

Forth) The choice of prior distribution is not fixed, but arbitrary. This is really a subjective issue. Overall, we will find the parmeters to maximze the posterior probability. The process is called MAP(Maximum a posteriori).

## 2. Is a logistic regression a generative or a descriptive classifier?Why?
<Related Question: How does maximum likelihood estimation play in the estimation of parameters?>
![image](https://user-images.githubusercontent.com/53164959/204186231-bc5c93bc-24fd-4cb0-bca7-ad3bc536319d.png)



 Logistic regression is a typical example of a descriptive classifier that is commonly used in supervised learning. They will learn the boundary between classes in a dataset.  The most distinct feature of the logistic regression is to find the estimators directly from training data based on the likelhood.  Let me explain briefly about it.  We first assume the distribution with a parameter. In the case of logistic regression, we will take the Bernoulli distribution We can estimate the probability of each data for the given distribution and compute the product of all the corresponding probabilities. We label it as likelihood. The ones that generate the maximum likelihood are the parameters we are looking for.
 
 From this point, logitic regression find estimators directly from data poitns. Another thing I want to mention the logistic regression ,as most discriptive models do, does not genearte the new data set beacuse there is no separate probability of the distribution about the data.Therefore, their ultimate goal is to separate one class from another. 

If we have some outliers present in the dataset, then discriminative models work better compared to generative models i.e, discriminative models are more robust to outliers. However, there is one major drawback of these models is the misclassification problem, i.e., wrongly classifying a data point.
 
[url] https://www.analyticsvidhya.com/blog/2021/07/deep-understanding-of-discriminative-and-generative-models-in-machine-learning/


## 3. Why people call logisitc regresssion not logistic classification?


We all know that logistic regression uses a sigmoid function to generate a value in a range between 0 and 1. Before the function, we should compute odds as the ratio of the success rate to the loss and place the log on it. These log odds are linear transformation of weights and data, which is why the name comes after regression. 


## 3.  Can you use logistic regression for classification between more than two classes?

Yest,it is possible to use logistic regression for classification between more than two classes. We cannot simply
implement without modifications to the vanilla logistic regression model. The multimodel logistic regression can
be implemented using a generalization of the sigmoid,called softmax fucntion. Assuming that we have classes, the 
softmax assigns each class with a value in a range between 0 and 1. Unlike the sigmoid function, the softmax guarantees that the sum of all values is equal to 1. 


## 4. Why odds are used in the logistic regresesion?


The odds are the expected number of successes per failure, it can take any value from 0 to infinity. The log can map the values of odds to any value in a range between negative infinity and positive infinity, which can not allow the linear model to make an impossible prediction.  However, in the case of log probability, we need to make sure of complicated multi-dimensional constraints on the regression coefficients since the probability must not exceed one. Without the constraints, we will see some probabilities greater than 1, which is a clear violation of the rule. Also, the linear model  without the contraints generates the wrong prediciton since the probablities must remain within a range betwen 0 and 1 while this is not an issue with an odds-ratio.


## 5. Given a fair die,what are the oods of occurence of odd numbers?

Given fair die, what are the odds of occurrence of odd numbers?

The odds of occurrence of odd numbers is 1. 

There are three odd and three even numbers in a fair die, and therefore, the probability of occurrence of odd numbers is 3/6 or 0.5. Similarly, the odds of occurrence of numbers that are not odd is 0.5. Since odds is the ratio of the probability of success and that of failure, 

Odds = 0.5/0.5=1.


## 6. Why can't we use the mean square error cost function used in linear regression for logistic regression?

If we use mean square error in logistic regression, the resultant cost function will be non-convex, i.e., a function with many local minima, owing to the presence of the sigmoid function in h(x). As a result, an attempt to find the parameters using gradient descent may fail to optimize cost function properly. It may end up choosing a local minima instead of the actual global minima.


## 7.How many binary classifiers would you need to implement one-vs-all for three classes? How does it work?

You would need three binary classifiers to implement one-vs-all for three classes since the number of binary classifiers is precisely equal to the number of classes with this approach. If you have three classes given by y=1, y=2, and y=3, then the three classifiers in the one-vs-all approach would consist of h(1)(x), which classifies the test cases as 1 or not 1, h(2)(x) which classifies the test cases as 2 or not 2 and so on. You can then take the results together to arrive at the correct classification. For example, with three categories, Cats, Dogs, and Rabbits, to implement the one-vs-all approach, we need to make the following comparisons:

    Binary Classification Problem 1: Cats vs. Dogs, Rabbits (or not Cats)

    Binary Classification Problem 2: Dogs vs. Cats, Rabbits (or not Dogs)

    Binary Classification Problem 3: Rabbits vs. Cats, Dogs (or not Rabbits)


# 8. is the Wald Test useful in logistic regression but not in linear regression? 

The Wald test, also known as the Wald Chi-Squared Test, is a method to find whether the independent variables in a model are of significance. The significance of variables is decided by whether they contribute to the predictions or not. The variables that add no value to the model can therefore be deleted without risking severe adverse effects to the model. The Wald test is unnecessary in linear regression because it is easy to compare a more complicated model to a simpler model to check the influence of the added independent variables. After all, we can use the R2 value to make this comparison. However, this is not possible with logistic regression as we use Maximum Likelihood Estimate, which uses the previously mentioned method infeasible. The Wald test can be used for many different models, including those with binary variables or continuous variables, and has the added advantage that it only requires estimating one model.



# 1. What do you mean by Random Forest Algorithm?

Random forest algorithm is one typical type of ensembling method that contains several decision trees and the overall performance is based on either averaging or majority voting of all the results learners in the forest generate. 

# 2.  Why is Random Forest Algorithm popular?

There are many advantages to the use of the random forest. 

First, they can serve many different roles to generate business solutions for many given cases. The model itself can be used for regression, classification, and even clustering.  Often, due to its versatility, many practitioners rely on these algorithms for answering their business cases.

Another thing I want to say is unlike many traditional machine learning algorithms, the random forest does not require too many assumptions to follow. That is, this flexibility gives less change in the preparation of data and helps to save a lot of time on it. In dealing with the regression case, the linear regression model ensures that 


homogeneity (each point is located from the line with relatively an equal distance whereas heterogeneity(헤럴러저네이티) refers to the case where points are varying the distance from the predicted line.

Homoskedasticity variance of errors is within the specified range or has a similar scatter regardless of the value of the input.

auto-correlation not permitted: Errors are not correlated to each other

Errors are following the normal distribution. 

One last thing is that the model does not require feature scaling such as mapping the values into a range with minimum and maxim values or making the data follow the standard normal distribution. None of the extra work is necessary since the model is not sensitive to the variance of data itself. 

# 3. What do you mean by bagging?

The single-decision algorithms suffer from higher variance since they are heavily affected by training data in the construction process. The variance here refers to any errors in prediction coming from a change in data. Because the model is highly sensitive to changes in data, the best performance when training a model is not guaranteed on other unseen data.

To minimize the variation of our prediction, we could group many single weak learners modeled on the different sub-samples of the same data set. (i.e) bootstrapping with replacement is best used among practitioners.
The bagging, that is, is a process of grouping many predictive modes running on multiple subsets of the original data set to achieve better accuracy and model stability. 


# 4. Explain the working of the Random Forest Algorithm.


Explain the working of the Random Forest Algorithm.

We can make a good guess from the name itself. The forest indicates that we should select the number of single trees involved in the group. 

We move to select the k features from the total number of features. Not all features must be used in training, thereby allowing for a fast training time. The selected features are less than the total number, and among the features, we will find the best split. Then, splitting the node into daughter nodes will be followed. Repeat these steps until the pre-assigned number of terminal nodes has been reached. This is how we construct a single decision model and the same procedures apply to the rest of the trees.


# 5.What is the bias and variance trade off?




Errors can be decomposed into two different parts; bias and variance. 



The total predict
1)Bias is often thought of as the number of assumptions your model makes against the problems you trying to frame. That is, the more assumptions you have, the higher bias is going to be on your model. 

The typical example with higher bias is linear regression and users must ensure that all the assumptions must be met, otherwise the predictive power would not be so much as impressive as she or he thought it would be. Mostly, linear regression suffers from higher bias.


2) Variance refers to the sensitivity of our model to the training dataset. 

Variance measures how much the output would change if we change the training dataset with the same problem objective. 
If the case is higher variance, the output of the model will change dramatically whenever we change our training dataset, which leads to an overfitting problem. (Higher variance = overfitting).  Generally speaking, models with higher flexibility tend to have higher variance like decision trees. If you do not impose any restriction, the tree model will split the node into daughter nodes, eventually, branch up to fit every single data point in the extreme case. The model will perform pretty well on the training dataset but fails to give the same performance as we have seen on the training. 

In evaluating bias and variance, we always think of the trade-off between bias and variance. If we relax the assumptions of our model, then we expect lower bias but higher variance as mentioned, and vice versa. This trade-off encourages us to find the most optimal point based on the number of experiments. 


# 6. Why do we prefer a Forest (collection of Trees) rather than a single Tree?

Compared to the single tree, random forests take much longer to construct trees and obtain outcomes since they involve many trees in the group. Also, in terms of interpreting the results and identifying the types of features that contribute most to the prediction power, the single decision tree is superior over random forests. Despite its all merits, single decision trees will suffer from overfitting problems. (i.e., how dramatically output models change if we change the training data.) The decision trees have more possibility of overfitting while random forest limits its exposure to it. 


#7. What do you mean by Bootstrap Sample?


# 6.rove that in the Bagging method only about 63% of the total original examples (total training set) appear in any of sampled bootstrap datasets. Provide proper justification.



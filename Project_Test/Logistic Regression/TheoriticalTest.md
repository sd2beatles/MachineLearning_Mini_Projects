#1.  Can you tell me what is the major difference between the frequentists and bayesian approach?

Frequentists treat an unknown static as a constant from the whole population.Then,they draw conclusions from sample data by looking at the relative frequency of multiple trials.

Their ultimate goal is to find the parameters (i.e., unknown statistics) to maximize the posterior probability,that is, the probability of parameters given a dataset. Bayesian has many distinct features compared to the frequentist approach.

First) They believe that the parameters are not constant but random variable. That is, it follows a distribution and all the prior knowledge of paramters is relfecte to the distribution so called prior distribution. The prior distribution,therefore, provides knowledge about parameters before seeing the data.

Second) Bayesian dynamically updates our posterior probability through prior distriubtion whenever we have more data to come. The mechansim behind it is that the old posterior probabilty becomes the new prior probability since it represents the new prior probability of our belief.

Third) Bayeisan is also concerend with the uncertainty related to the future events. Therefore,the chance of overfitting problem is relatively smaller compared to frequetists. It says that explaining the current events is not enough ,but future events.

Forth) The choice of prior distribution is not fixed, but arbitrary. This is really a subjective issue. Overall, we will find the parmeters to maximze the posterior probability. The process is called MAP(Maximum a posteriori).

#2.
https://www.analyticsvidhya.com/blog/2021/07/deep-understanding-of-discriminative-and-generative-models-in-machine-learning/

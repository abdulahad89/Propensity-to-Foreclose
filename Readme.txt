MAKING A DATASET
Using all the the datsets provided i merged train dataset,Customers dataset and LMS dataset to create a final train dataset
i.e.(data)
Similarly for test dataset (test)

ANALYSIS
I did some analysis like the missing values,unique values counts and the columns having 0 values.
I dropped the missing values as it was not easy to find all thousands of missing values.ALso the count of missing values
was much less as compared to whole dataset.
I dropped dates given in the datasets

As the number of features was around 50 so i tried to reduce it using the correlation of features.
I found out the correlation matrix and plot it on a heatmap tobetter find the correlation of each fetaure with all others.
I dropped one of the feature having higher correltaion with other.
Above process reduced the number of features to 36 features.
So we created a different dataset "tr1" using these 36 features.

MODELLING
After reducing the feature we standardise the whole dataset tobring it on a similar scale so as to make our modelling 
more accurate.

USING PCA FOR FEATURE REDUCTION
We still need to reduce our features to make computation easier and avoid overfitting.Excess features can also affect our 
prediction.

TOOLS USED 
For whole code i used python 3.7
I used pandas library for data manipulation.
Seaborn and matplotlib for plotting.
Scikit learn for preprocessing, modelling and PCA.
So there was a need to find features which explains the highest variance or data in our dataset.
So i used Principal component analysis iteratively for different number of components.
I found out that the optimum number of component for this was n=15 which explained almost 86% of our dataset.

LOGISTIC REGRESSION
I used simple logistic regression for training.
After training i applied it to our test dataset(test) for prediction and probability of prediction.

Then i combined respective agreement id with their respective prediction probaility.
There were agreement id which were repeating so i took the average probability for that respective id. 

There were some agreement ids whose data was not give so i merged it with our final prediction dataset (predict_tr2) and 
fill the value of those with 0.01 for less error.
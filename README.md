The script in this repo can be safely run assuming you have done pip install requirements.txt

summarize.py was going to dp more but then I realized it would be overkill so all it does it retrieve the files for local use
exploration.ipynb contains the meat of the assignment

Questions
1 - Please provide a general description of the data. This may involve descriptive statistics, graphs, or other presentation methods of your choice.

There are summary statistics and misc. in the jupiter notebook but I am a visual person, as are most humans so here is a link to a Google Data Studio dashboard that highlights some of what I found interesting about the data - both before and after cleaning
Note: I cleaned the data in Excel because my python workflow is a bit dated and I was short on time. I clean data by code all the time, I just have been using Node lately to do it and that was not appropriate here.
Go here for more data summaries: https://datastudio.google.com/reporting/f5143016-ab37-40ba-b6f9-26370c33bee5

2 - Please create a linear regression model which estimates the prior_month_paid as a function of some (or
all) of the attributes contained in the file.

Simple backwards elimination model shown in the jupiter notebook.
'prior_month_paid ~ C(industry_simple) + C(geo_clean)'

Preferred browser was dropped because it didn't add anything to the effectiveness of the model. This was actually surprising because in my experience browser is often a proxy for other things like age or income which usually influence EVERYTHING so either in this data set browser is not a good proxy or age and income don't matter. Worthy of further investigation in a real data set.
Geo_clean just simplifies names and best I could
Industry simple treats all missing and unknown values the same way - I had previously tested keeping them different because I have much experience classifying nulls and treating them in specific ways depending on their source. Often where a null is introduced changes how it should be modelled
I could have looked at interaction effects, but in this project it didn't seem worthwhile

3 - Please provide an inferential interpretation of the results of your regression model.
In a lot of ways, this data seems... simplified. That is probably because it has been faked in some way but it is worth noting that several variables did not behave as I expected

OLS Regression Results (highlights)
Dep. Variable:	prior_month_paid
R-squared:	0.916 - this is good. Too good, really, but it is hard to say with mock data I am not familiar with.
Method:	Least Squares	F-statistic:	5.259e+04 - also very low

I am very suspicious of all models by nature. Often people will overfit a model, fail to test for multicolinearity, or simply swear the insane variables really really really matter to the prediction of the result. We called that the phase of the moon problem in school. The phase of the moon did not actually cause your customers to pay you more money but random chance has made it relevant to your model.
This model seems too good to be true. Let's test!

4 - Please run your model against the training data set, and describe it’s performance.
Overall the performance was in line with expectations. We'd expect this model to be around 90% accurate and it is. The test set appears similar to the training set from the perspective of this model, which is good.

5 - What would your recommended next steps for the business be?
First, data hygiene! I don't like making assumptions about the source of my data. healthcare == health care is ok, probably, but I can easily conceive of a process where only one person keys in "health care" and something unusual about that person causes it to jump out in a model. These thingsa re 100% worth hunting down. Even if they can't be fixed they need to be understood
Specifically, industry was especially messy. In this case the missings and unknowns seemed similar but relying on that assumption is, in my opinion, terrible data science
Second, this model is particular interesting with regards to GEO. The coefficients for US versus the rest of the world were very different but the rest of the world could not be simplified without compromising the model. However it is very common for an American centric business to do exactly that (assume other countries are either like-USA or unlike-USA). Exploring nuances in the global market could be a very lucrative research task
Third, this data is notable for the absence of TIME. Obviously time series analysis is a whole different beast, but since FUTURE cash flows are of the most interest to the business, the next step would be to understand this data in terms of time.
Finally there is an interesting inverse relationship between session time and prior month paid when looked at by industry. There may be opportunities to look into the causes of long sessions times. Are potential customers outside of marketing agencies finding what they need quickly enough or are they getting frustrated?

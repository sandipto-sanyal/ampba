#Let us work with some Social media data
#Goal is to understand user behavior one variable at a time

data <- read.csv("social_data.csv")
#What does names do?
names(data)
str(data)

#We will make use of ggplot 2 package. Used for visualizations.
install.packages("ggplot2")
library("ggplot2")

#Use qplot function to plot a histogram. For example, let us plot 
# date of birth by day.
#What do you expect to find?
qplot(x=dob_day,data=data)


#What does this code do? 
#What insights can you derive?
qplot(x=dob_day,data=data) + facet_wrap(~dob_month,ncol=3)


#Create a histogram of friend count
qplot(x=friend_count, data=data)
#What do you find?

#Let us limit count and then see
qplot(x=friend_count, data=data, xlim=c(0,1000))


#Let us look at friend count by gender
qplot(x=friend_count, data=data, binwidth=25) + 
  scale_x_continuous(limits=c(0,1000),breaks=seq(0,1000,50))+
  facet_wrap(~gender)

#Let us omit NA values
qplot(x=friend_count, data=subset(data,!is.na(gender)), binwidth=25) + 
  scale_x_continuous(limits=c(0,1000),breaks=seq(0,1000,50))+
  facet_wrap(~gender)
#By looking at above plots can you tell which gender has more friends 
#on average?

#Which gender has more friends by average? Is median better than mean?
#Long tailed data. Median is better measure than mean.
table(data$gender)
by(data$friend_count, data$gender, summary)


#Since how long people are using FB?
qplot(x=tenure, data=data, binwidth=30)
#Create in years
qplot(x=tenure/365, data=data, binwidth=1)


#What can we say about ages? What is min age?
qplot(x=age, data=data, binwidth=1)
summary(data$age)

#Let us transform some data. What about friend count variable? It is long tail variable.
#These are over dispersed data. We transform them so that their tail is 
# shortened
qplot(x=friend_count,data=data)
summary(data$friend_count)

summary(log(data$friend_count))
#What is going on?


summary(log(data$friend_count+1))

#another kind of transformation
summary(sqrt(data$friend_count))

qplot(x=friend_count,data=data)

qplot(x=log(friend_count+1),data=data)

#Let us create multiple histograms on one plot
install.packages('gridExtra')
library(gridExtra)

a<-qplot(x=friend_count,data=data)
b<-qplot(x=log(friend_count+1),data=data)
c<-qplot(x=sqrt(friend_count),data=data)

grid.arrange(a,b,c,ncol=1)
#What can we say about these?


#Let us now look at likes. How would this help your business?
by(data$www_likes,data$gender,sum)


#Box plot. How does it look? How many outliers are there?
qplot(x=gender, y=friend_count, data=subset(data,!is.na(gender)),geom='boxplot')


qplot(x=gender, y=friend_count, data=subset(data,!is.na(gender)),geom='boxplot',ylim=c(0,1000))

qplot(x=gender, y=friend_count, data=subset(data,!is.na(gender)),geom='boxplot')+
  coord_cartesian(ylim=c(0,1000))
#Differences between the above two commands?

#Let us now look at who initiates more friend requests
qplot(x=gender, y=friendships_initiated, data=subset(data,!is.na(gender)),geom='boxplot')+
  coord_cartesian(ylim=c(0,1000))

by(data$friendships_initiated, data$gender, summary)


#What about mobile devices?
summary(data$mobile_likes)
#What percentage of people use mobile devices?
summary(data$mobile_likes>0)

#Exercise: Repeat the same set of commands for sets of first 100, 1000, 
#10,000, and 50,000 observations and report your general observations.

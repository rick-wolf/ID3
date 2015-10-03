setwd("Documents/ID3/")
df = read.csv("heart_results_part2.csv")


theme_set(theme_gray(base_size = 18))
ggplot(df, aes(x=samplePercentage, y=Accuracy, fill='red')) + geom_bar(stat='identity') +
  coord_cartesian(ylim=c(0,100)) + geom_errorbar(aes(ymin=Min, ymax=Max)) + xlab("Percentage of Training Set") +
  ggtitle('Heart Disease Data: 5%, 10%, 20%, 50%, 100%, \n Error Bars are min and max')


df = read.csv("diabetes_results_part2.csv")

theme_set(theme_gray(base_size = 18))
ggplot(df, aes(x=samplePercentage, y=Accuracy, fill='red')) + geom_bar(stat='identity') +
  coord_cartesian(ylim=c(0,100)) + geom_errorbar(aes(ymin=Min, ymax=Max)) + xlab("Percentage of Training Set") +
  ggtitle('Diabetes Data: 5%, 10%, 20%, 50%, 100%, \n Error Bars are min and max')

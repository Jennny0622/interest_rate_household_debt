library(readr)
library(ggplot2)

df<- read_csv("/Users/jenny/Desktop/project/data/cash_rate_recent.csv")

#cash rate trend per quarter
ggplot(df, aes(x=quarter, y=cash_rate, group =1)) + geom_line() + geom_point() + labs(title = "Quarterly Cash Rate (2015-2025)", x= 'Quarter', y="Cash Rate(%)") + theme_minimal() + theme(plot.title = element_text(hjust=0.5), axis.text.x=element_text(angle=45, hjust=1))
  
ggplot(df, aes(x=quarter, y=rate_change)) + geom_col() + geom_hline(yintercept = 0) + labs(title = "Quarterly Rate Change (2015-2025)", x = 'Quarter', y='Change in cash rate') + theme_minimal() + theme(plot.title = element_text(hjust=0.5), axis.text.x=element_text(hjust=1, angle = 45))

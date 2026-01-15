library(tidyverse)
library(readr)
library(dplyr)
household <- read_csv("/Users/jenny/Desktop/project/data/analysis_df.csv")
cash <- read_csv("/Users/jenny/Desktop/project/data/cash_rate_recent.csv")

colnames(household)
colnames(cash)

cash<- cash %>% rename(Quarter = quarter)
df <- household %>%left_join(cash, by = "Quarter")

df <- df %>%
  mutate(
    Quarter = factor(Quarter, levels = unique(Quarter)),
    `Cash rate` = as.numeric(`Cash rate`)
  )

df <- df %>%
  mutate(
    cash_rate_clean = as.numeric(gsub("%", "", cash_rate))
  )
#summary(df$`Cash rate`)
#summary(df$cash_rate)
#summary(df$cash_rate_clean)

ggplot(df, aes(x = Quarter)) +
  geom_line(
    aes(
      y = `Household debt to income`,
      colour = "Debt-to-income",
      group = 1
    ),
    linewidth = 1
  ) +
  geom_line(
    aes(
      y = cash_rate_clean * 50,
      colour = "Cash rate",
      group = 1
    ),
    linetype = "dashed",
    linewidth = 1
  ) +
  scale_y_continuous(
    name = "Household debt-to-income ratio",
    sec.axis = sec_axis(~./50, name = "Cash rate (%)")
  ) +
  scale_colour_manual(
    values = c(
      "Debt-to-income" = "black",
      "Cash rate" = "red"
    )
  ) +
  labs(
    title = "Household Debt-to-Income Ratio and Cash Rate Changes in Australia (2015–2025)",
    x = "Quarter",
    colour = ""
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )



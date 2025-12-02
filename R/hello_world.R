# hello_world.R

print("hello world")
print("test1")

print("test2")

print("test3")

y <- c(1, 2, 3)
print(y)
R.home()

log(10)

x = c(1, 2)

z <- c("a", "b", "c")


# =============================================================

# spreadsheet1 <- read_excel("spreadsheet/location.xlsx")

patient_CGVs <- read.csv("/home/user/git/githubSifr01/captimed/glooko_web_scraping/model/1_scraper_pipeline/scrape_05AUG2025/3_standardized_CSVs/05-004_2024-04-23_to_2025-03-11.csv")
View(patient_CGVs)

mean(patient_CGVs$PCSTRESN)

print(unique(patient_CGVs$STUDYID))
print(unique(patient_CGVs$SITEID))
print(unique(patient_CGVs$USUBJID))
print(unique(patient_CGVs$PCSTRESU))
print(unique(patient_CGVs$PCSPID))

library(dplyr)
glimpse(patient_CGVs)
filter(patient_CGVs, PCSTRESN <= 20)

PCSTRESN_times_ten <- patient_CGVs %>%
    mutate(PCSTRESN_times_ten = PCSTRESN * 10)


library(ggplot2)    # Part of the tidyverse package

# Plot a graph:
ggplot(patient_CGVs, aes(x=PCSTRESN)) +
    geom_histogram() +
    # geom_freqpoly() +
    labs(x = "CGVs in mg/dL")

ggplot(patient_CGVs, aes(x=PCSTRESN)) +
    geom_histogram() +
    geom_freqpoly() +
    labs(x = "CGVs in mg/dL")
# Note: for loop solution was just too slow. Modified code to add 2 other solutions.
# For PART 1, there are 2 solutions below
    # 1st solution is fastest and uses stringr::sr_count function
    # 2nd solution is a bit slower but is base R gregexpr function
# For Part 2

# Libraries
library(readr)
library(stringr)
library(dplyr)
library(bench)
# Setwd
#setwd("Desktop/ProgrammingProjects/AdventOfCode-local/AdventOfCode/Puzzles/Week1/")


######  PART 1  #####

stringInput <- read_file("PuzzleString.txt")
# Solution 1
print(paste0("PART 2: Entered the basement at ",str_count(stringInput,"\\(") - str_count(stringInput,"\\)")))
#Solution 2
print(paste0("PART 2: Entered the basement at ",
             sum(gregexpr("(",stringInput, fixed=TRUE)[[1]] > 0) - sum(gregexpr(")",stringInput, fixed=TRUE)[[1]] > 0)))

bench::mark(
iterations = 100,
check = FALSE,
solution1 = {
print(paste0("PART 2: Entered the basement at ",str_count(stringInput,"\\(") - str_count(stringInput,"\\)")))},
solution2 = {
  print(paste0("PART 2: Entered the basement at ",
               sum(gregexpr("(", 
                            stringInput, fixed=TRUE)[[1]] > 0) - sum(gregexpr(")", 
                                                                              stringInput, fixed=TRUE)[[1]] > 0)))
}

)




######  PART 2  #####



# Part2

# When does santa first enter the basement? (floor <0)
# Libraries
library(readr)

# Setwd

start <- Sys.time()
stringInput <- read_file("PuzzleString.txt")
start.time <- Sys.time()
floor = 0
for(i in 1:nchar(as.character(stringInput))){
  upOrDown <- ifelse(substring(stringInput,i,i) == "(", 
                     1, - 1)
  floor <- floor + upOrDown
  if(floor <0){break}
}
print(paste0("PART 2: Entered the basement at ",i))
print(paste0("Final time: ",Sys.time()-start.time, " seconds"))



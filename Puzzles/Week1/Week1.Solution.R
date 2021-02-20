# Libraries
library(readr)

# Setwd
setwd("Desktop/ProgrammingProjects/AdventOfCode-local/AdventOfCode/Puzzles/Week1/")

start <- Sys.time()
stringInput <- read_file("PuzzleString.txt")
floor = 0
for(i in 1:nchar(as.character(stringInput))){
  upOrDown <- ifelse(substring(stringInput,i,i) == "(", 
         1, - 1)
  floor <- floor + upOrDown
}
print(paste0("PART 1: finished on floor ",floor))
print(paste0("Final time: ",Sys.time()-start, " seconds"))

# Part2

# When does santa first enter the basement? (floor <0)
# Libraries
library(readr)

# Setwd

start <- Sys.time()
stringInput <- read_file("PuzzleString.txt")
floor = 0
for(i in 1:nchar(as.character(stringInput))){
  upOrDown <- ifelse(substring(stringInput,i,i) == "(", 
                     1, - 1)
  floor <- floor + upOrDown
  if(floor <0){break}
}
print(paste0("PART 2: Entered the basement at ",i))
print(paste0("Final time: ",Sys.time()-start, " seconds"))


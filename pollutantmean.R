pollutantmean <- function( directory, pollutant, id=1:332) {
    allFiles <- list.files(path = directory, full.names = TRUE)
    dataset <- data.frame()
    for (i in id) {
        dataset <- rbind(dataset, read.csv(allFiles[i]))
    }
    if (pollutant == 'sulfate') {
        mean(dataset$sulfate, na.rm = TRUE)
    } else if (pollutant == 'nitrate') {
        mean(dataset$nitrate, na.rm = TRUE)
    }
    
}
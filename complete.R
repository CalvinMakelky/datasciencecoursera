complete <- function(directory, id=332) {
    allfiles <- list.files(path=directory, full.names=TRUE)
    dataset <- data.frame()
    completeCases <- data.frame()
    for ( i in id) {
        dataset <- (read.csv(allfiles[i], header=TRUE))
        nobs <- sum(complete.cases(dataset))
        completeCases <- rbind(completeCases, data.frame(i,nobs))
    }
    completeCases
}
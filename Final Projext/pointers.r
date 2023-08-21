# x <- c(20, 40, 10, 30, 50)
# y <- sort(x)
# print(y)
# print(x)

# x <- c(20, 40, 10, 30, 50)
# x <- sort(x)
# print(x)

mult_two <- function(lst){
  lst$x <- lst$x * 2
  lst$y <- lst$y * 2
  lst$z <- lst$z * 2
  return(lst)
}

xyzlst <- list()
xyzlst$x <- 1
xyzlst$y <- 2
xyzlst$z <- 3
xyzlst <- mult_two(xyzlst)

print(xyzlst$x)
print(xyzlst$y)
print(xyzlst$z)
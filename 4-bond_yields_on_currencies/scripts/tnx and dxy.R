library(readr)
data_curr <- read_csv("C:/Users/okiki/Desktop/TimeSeries/bond yiels on currencies/data.csv")
View(data_curr)

library(tidyverse)
ggplot(data_curr, aes(x=data_curr$Date, y = data_curr$TNX)) + geom_line()
ggplot(data_curr, aes(x=data_curr$Date, y = data_curr$DXY)) + geom_line()

ggplot(data_curr) + geom_line(aes(x=data_curr$Date, y = data_curr$DXY)) +
  geom_line(aes(x=data_curr$Date, y = data_curr$TNX))
       
p <- ggplot(data_curr,aes(x=TNX, y = DXY))+ geom_point() +geom_smooth(method = lm )+ scale_x_log10() + scale_y_log10()
p + ggtitle("Scatter Plot of Dollar Index and Ten Year Bond Prices") + xlab("Ten Year Bond Prices") + ylab("Dollar Index") 


## Test for Stationarity
library(tseries)
## test for stationarity
adf.test(data_curr$TNX)
adf.test(data_curr$DXY)

acf(data_curr$TNX, main = "Correlogram of TNX", lag.max = 30)
acf(data_curr$DXY, main = "Correlogram of DXY", lag.max = 30)

##Detrending non-stationary data
us_tnx <- diff(data_curr$TNX, differences = 1)
us_dxy <- diff(data_curr$DXY, differences = 1)

## test for stationarity
adf.test(us_tnx)
adf.test(us_dxy)


p <- ggplot()+ geom_point(aes(x=us_tnx, y = us_dxy)) + geom_smooth(method=lm, se=FALSE)
p + ggtitle("Scatter Plot of Dollar Index Returns and Ten Year Bond Yields") + xlab("Ten Year Bond Yields") + ylab("Dollar Index Returns") 

autoplot(ts(us_dxy))+ylab("") +ggtitle("DXY I(1)")
autoplot(ts(us_tnx))+ylab("")+ ggtitle("TNX I(1)")

##ACF TNX
acf(us_tnx, main = "Correlogram of TNX I(1)", lag.max = 30)
pacf(us_tnx, main = "Partial Correlogram of Ten Year Bond Yields", lag.max = 30)


##ACF DXY
acf(us_dxy, main = "Correlogram of DXY I(1)", lag.max = 30)
pacf(us_dxy, main = "Partial Correlogram of % Change in Dolla Index", lag.max = 30)


#correlation of lags 
Box.test(us_tnx, lag = 10, type = c("Ljung-Box"))
Box.test(us_dxy, lag = 10, type = c("Ljung-Box"))



#correlation of error terms
modelb1<-lm(us_dxy~us_tnx)
summary(modelb1)
Box.test(resid(modelb1), lag = 10, type = c("Ljung-Box"))


# running auto arima
library(forecast)
modeltnx_us<-auto.arima(data_curr$TNX)
summary(modeltnx_us)

modeldxy_us<-auto.arima(data_curr$DXY)
summary(modeldxy_us)

library(lmtest)
coeftest(modeltnx_us)             ## Using the z-statistic and the p-values, you can interpret the statistical significance
coeftest(modeldxy_us)  

Box.test(residuals(modeltnx_us), lag = 30, type = c("Ljung-Box"))
Box.test(residuals(modeldxy_us), lag = 30, type = c("Ljung-Box"))


library(vars)
tnx_us <- ts(scale(data_curr$TNX))
dxy_us <- ts(scale(data_curr$DXY))

autoplot(cbind(tnx_us,dxy_us)) +ggtitle(" Dollar Index and Ten Year Bond Yields")

DATAtnxdxy <- ts(cbind(us_tnx,us_dxy))
VARselect(y=DATAtnxdxy, lag.max = 8, type = "const")       ##VARSelect allows you to select the optimal number of lags
var<- VAR(y=DATAtnxdxy, p=2, type = c("const"), ic = "SC")
summary(var)


jotest=ca.jo(DATAtnxdxy,type = "trace", ecdet = "none", K = 8)
coeftest(jotest)
summary(jotest)

#The long run equilibrium equation is given by output under beta
benson$beta

tnx_us2 <- ts(data_curr$TNX)
dxy_us2 <- ts(data_curr$DXY)

gra_tnx <- causality(var, cause = 'us_tnx')
gra_tnx

gra_dxy <- causality(var, cause = 'us_tnx')
gra_dxy

imp_tnx <- irf(var , impulse = 'us_dxy', response = 'us_tnx', n.ahead = 10, boot = TRUE)
plot(imp_tnx, ylab='TNX', main = "Shock from Dollar Index")

imp_dxy <- irf(var , impulse = 'us_tnx', response = 'us_dxy', n.ahead = 10, boot = TRUE)
plot(imp_dxy, ylab='TNX', main = "Shock from Ten Year Bond Yield")

forecasttnx <- predict(var, n.ahead = 500, ci = 0.95)
fanchart(forecasttnx, names="tnx_us")
forecastdxy <- predict(var, n.ahead = 500, ci = 0.95)
fanchart(forecastdxy, names="dxy_us")








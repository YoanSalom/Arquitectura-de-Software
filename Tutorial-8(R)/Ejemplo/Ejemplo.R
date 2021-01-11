vector= c(1,2,3,4,5,6,7,8)
#media:
  median(vector)
#mediana:
  mean(vector)
#minimo:
  min(vector)
#maximo:
  max(vector)
#cuartiles:
  quantile(vector)
#resumen de datos(muestra todos los datos anteriores):
  summary(vector)
#varianza:
  var(vector)
#desviacion estandar:
  sd(vector)
x <- rnorm(100)
y <- x + rnorm(100)
plot(x,y)
plot(x, y, main = "Gráfico de puntos")
hist(x, main = "Grafico de barras de X")
hist(x, main = "Grafico de barras de Y")
c=data.frame(x,y) 
#data frame agrupa enlos datos en sus filas correspondientes

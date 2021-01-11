R es un entorno y lenguaje de programación con un enfoque al análisis estadístico, este fue muy utlizado en el mismo ramo de Estadistica, usando archvos csv. o xls. 
ya que permite usar los datos  de estos para trabajar con ellos.

"R nació como una reimplementación de software libre del lenguaje S, adicionado con soporte para ámbito estático.
Este lenguaje es unos de los mas utilizados en la investigacion cientifica ya que con sus diferentes bibliotecas puedes solucionar diferentes
problemas matematicos de analisis estadisticos , apoyando a los diferentes campos que lo utilizan como puede ser el de investigacion biomedica,
bioinformatica , matematicas financieras entre otros".

Se descarga en ://www.r-project.org (Lo utilize en windows,por unos problemas de espacio en ubuntu)

Si gusta de usar este programa para estudios de estadistica recomiendo el uso de rstudio ,requiere el r anterior, ya que es mas 
facil y ordenado de programar:

Se descarga en : https://rstudio.com/products/rstudio/download/#download


 

*Ejemplo Trabajo con datos agrupados (Trabajo en consola)

R nos permite tener una lectura grandes cantidades de datos agrupados en poco tiempo , por ejemplo en R puedes hacer un calculo de
 la medición de la mediana, desviacion estandar, minimo y maximo de un dato agrupado de tamaño N. 

Crearemos el dato agrupado vector el cual se crea de la manera

vector= c(1,2,3,4,5,6,7,8)

en el cual se crea un vector numerico con los numeros contenidos dentro del parentesis.

Al tener creado el vector numerico con R a este se le calcular la mediana ,desviacion estandar , minimo , maximo entre otros de manera
facil con los diferentes comandos que nos permite utilizar R , siendo asi estos se calculan de la manera:

media:
	median(vector)
mediana:
	mean(vector)
minimo:
	min(vector)
maximo:
	max(vector)

entregandonos directamente estos valores en la consola:

tambien nos permite calcular los cuartiles ,resumen de todo lo anteriror,la varianza y la desviacion del vector de esta forma:

cuartiles:
	quantile(lista)
resumen:
	summary(lista)
varianza:
	var(lista)
desviacion estandar:
	sd(lista)

La función plot en R permite crear un gráfico pasando dos vectores (de la misma longitud), un data frame, una matriz o incluso otros objetos.

Por ejemplo simularemos dos variables normales aleatorias llamadas x e y de la manera (Trabajo en consola):

	# Generamos datos de ejemplo 
	# Se crean 100 datos aleatorios
	x <- rnorm(100)
	y <- rnorm(100)

Al utilizar el comando plot de la forma plot(x,y) se generara un grafico con el diagrama de puntos de los vectores x e y
al utilizar plot(x, y, main = "Gráfico de puntos") se nos generara el mismo grafico pero con el titulo Grafico de puntos.
Al utilizar el comnado hist de la forma hist(x)o hist(y)se crea un grafico de barras con los datos aleatorios.
Al utilizar data.frame(x,y) crea 2 columnas con los datos produciodos aleatoriamente
igualemnte que plot al utilizar, hist(x, y, main = "Gráfico de barras") se nos generara el mismo grafico pero con el titulo Grafico de barras. 




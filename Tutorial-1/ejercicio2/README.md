#Uso:

Se debe buildear con:
`docker-compose build `(en la carpeta compose)
esto se hace para crear una imagen para correrla donde sea de forma segura ya que solo usa el token OAut2 del bot

Luego, se ejecuta con:

`docker-compose up`
Y luego dockerizamos la aplicacion,creando la imagen:
`docker build revys/ -t (nombre de imagen del repositorio)`

![Header](/blog/images/The_Ebikes_Update_ES.webp){.header_image}
# La actualización de e-bikes {.blog_entry_title}

Llego un poco en el tiempo de descuento, pero ya puedo volver a decir que esta API vuelve a estar al día con la serie. La South API da la bienvenida a South America con los brazos abiertos y la mano en el pecho.

Esta actualización es muy pequeña porque no quería que se me juntaran el episodio 1 con el 2, por lo que creo que lo mejor ha sido retrasar la actualización de personajes para la siguiente versión, la 0.9, y de paso incluir alguna que otra "sorpresa". Pero esta entrada del blog va sobre la versión 0.8, así que ¡al lío!
{.blog_intro}

## Añadidos a la API {.blog_title}

### Nuevos personajes {.blog_subtitle}

Se ha añadido el personaje 1049, [el dependiente de la tienda de e-bikes](/api/characters/1049).

### Nuevo episodio {.blog_subtitle}

Se ha añadido el episodio 332 de la serie: "[South American Biker Gangs](/api/episodes/332)".

## Cambios en la API {.blog_title}

### Nuevo campo: ¿Tiene entrada en el sitio web? {.blog_subtitle}

Mientras desarrollaba la API me he encontrado con el "problema" de que este es el primer episodio que no está como tal en la web de South America Studios (South Park Studios). Es algo que me extraña y que no me ha pasado en ningún momento mientras desarrollaba la API. En vista de que pueda seguir pasando a futuro, he creado un nuevo campo en la tabla de episodios de la base de datos para especificar si ese episodio tiene entrada en la web, ya que era lo que estaba usando antes como referencia para los episodios. Si de cara a futuras actualizaciones añaden la entrada en la web, actualizaré el registro de ese episodio, aunque mi intención es dejar el campo por si acaso.

## Reflexión del desarrollador {.blog_title}

Aunque puede parecer una actualización pequeña (y lo es), reconozco que estoy un poco vago. Gran parte del tiempo lo he pasado pensando qué hacer con la API de cara a esta nueva temporada: si me gustaría terminar ya la base de datos de personajes o añadir nuevos endpoints interesantes. Mi idea original era cambiarle el nombre entero a la API y hacer que deje de llamarse "South Park API" para pasar a ser "South America API". Aunque podía resultar tremendamente confuso, mi idea con esta API ha sido siempre estar lo más actualizado posible con la serie, y eso incluye estos cambios. Sin embargo, ponerme a cambiar nombres, descripciones e incluso entradas antiguas del blog hubiese sido demasiado drástico; además, tendría que ponerme a revisar qué capítulos han cambiado la sinopsis y cuáles no para actualizar los registros uno a uno, por lo que esa opción queda totalmente descartada (Las palabras South Park apaerce 347 veces en toda la API, contando esa ultima).

La siguiente actualización será el episodio 333 de la serie, que de momento no tiene ni sinopsis ni tráiler (me pregunto de qué irá...). Junto con eso, espero que me dé tiempo a terminar los personajes cuyo nombre empieza por L y el nuevo endpoint que estoy preparando. Debería salir a mediados de la semana que viene; lo ideal sería que saliera antes de la emisión del siguiente episodio, pero dependerá de cuándo la termine. Aunque me está costando encontrar motivación para seguir con la API y se me está haciendo pesado, espero que se me haga más ameno con el tiempo.

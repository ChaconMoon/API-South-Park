![Header](/blog/images/The_F_Update_ES.webp){.header_image}
# Actualización de la Fuerza del Azar {.blog_entry_title}

¡Bienvenid@ al blog de desarrollo de la versión 0.3 de la API! En esta actualización se han añadido los personajes de la serie cuyo nombre empieza por F y la posibilidad de obtener resultados aleatorios en cada endpoint.
{.blog_intro}

## Nuevos Endpoints {.blog_title}

Ahora, todos los endpoints de la API cuentan con una opción para obtener un registro aleatorio bajo diferentes condiciones.

- [Personaje aleatorio](/api/characters/random) `/api/characters/random`
- [Personaje aleatorio (excluyendo invitados famosos)](/api/characters/random?exclude_famous_guests=true) `/api/characters/random?exclude_famous_guests=true`

Todos estos endpoints siguen la estructura: `api/'categoria'/random`. En el caso de los alter egos, la categoría es `alteregos`.

Puedes ver más detalles en el [changelog](/changelog/Version_0.3).

Estos endpoints están pensados para ser utilizados en bots o programas que requieran obtener resultados aleatorios, facilitando mucho su desarrollo.

## Nuevos personajes en la base de datos {.blog_title}

Se han añadido todos los personajes de la serie cuyo nombre empieza por F: desde [ID 697](/api/characters/697) hasta [ID 741](/api/characters/741).

## Cambios en las respuestas de la API {.blog_title}

Debido a los nuevos filtros para personajes aleatorios, he establecido criterios claros sobre qué es y qué no es un invitado famoso. En resumen: "Cualquier personaje que no haya tenido protagonismo en la serie y sea una persona o entidad real o ficticia será considerado un invitado, excluyendo a aquellos que han tenido desarrollo propio o que South Park ha reinterpretado de otra forma".

*En el futuro se revisarán los personajes que cumplan estos criterios y se les asignará el valor correspondiente.*

También se han corregido errores tipográficos en las palabras "AVAILABLE" y "CENSORED".

Además, se han añadido las fotos que faltaban en todas las familias.

## Nota del desarrollador {.blog_title}

Personalmente, considero que esta es una de las actualizaciones más importantes para la API, principalmente porque uno de los usos que me gustaría fomentar es la creación de bots que soliciten personajes aleatorios para juegos en Discord o Twitter. Yo mismo tengo la idea de desarrollar un bot para probar la API y, gracias a esta actualización, podré hacerlo.

La próxima actualización debería incluir el siguiente episodio de la serie, los personajes cuyo nombre empieza por G y alguna novedad más.

Para terminar: si estás leyendo esto, quiero contarte que la API ahora tiene cuenta oficial de Twitter, donde se publicarán avances y curiosidades sobre el desarrollo. ¡Te invito a seguirme allí!: [@SouthParkAPI](https://x.com/SouthParkAPI)
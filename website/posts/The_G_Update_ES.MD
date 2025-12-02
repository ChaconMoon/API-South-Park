![Header](/blog/images/The_G_Update_ES.webp){.header_image}
# Actualización de grupos {.blog_entry_title}

Presento la actualización 0.4 de la API, que introduce el episodio 330, nuevos personajes cuyos nombres empiezan con la letra 'G' y la creación del endpoint de grupos.
{.blog_intro}

## Nuevo Endpoint de Grupos {.blog_title}

Esta actualización introduce un nuevo endpoint dedicado a los grupos, permitiendo obtener un grupo específico por su ID o uno de forma aleatoria.

- [Obtener un grupo por ID](/api/groups/1): `/api/groups/1`
- [Obtener un grupo aleatorio](/api/groups/random): `/api/groups/random`

Es importante destacar que no todos los grupos listan miembros individuales. Algunos, como el de [los niños afganos](/api/groups/14), son tratados como una entidad única. Los personajes que componen estos grupos se añadirán a la base de datos más adelante, una vez completado el listado alfabético principal. Su inclusión dependerá de si es posible obtener una imagen individual y un nombre. En caso de no tener un nombre oficial, se les asignará uno genérico (ej: "Niño afgano parecido a Kyle").

## Actualizaciones de la Base de Datos {.blog_title}

- Se han añadido todos los personajes de la serie cuyo nombre empieza por G: [ID 742](/api/characters/742) -> [ID 796](/api/characters/796).

- Se han añadido 4 nuevas familias, incuyendo corregir el error por el que faltaba la familia Trump. [ID 74](/api/families/74) -> [ID 78](/api/families/78)

## Nuevo Episodio: Temporada 28 EP 4 'Turkey Trot" {.blog_title}

- Se ha añadido el episodio [330](/api/episodes/330) de la serie.

- Este episodio no introduce ningún nuevo personaje que deba ser incluido por order alfabetico, el nuevo personaje que introduce sera añadido a la API cuando le corresponda por orden alfabetico.

## Cambios en las Respuestas de la API {.blog_title}

- El campo `family` en la respuesta de los personajes ahora devuelve un objeto con el nombre y una URL directa al endpoint de la familia. Este cambio busca mejorar la consistencia con otros campos, como las canciones en los álbumes, y minimizar el número de peticiones necesarias para obtener la información completa de un personaje.
- Se ha eliminado temporalmente el campo `group` de los personajes. Este campo será reestructurado en una futura actualización para que su funcionamiento sea consistente con el del campo `family`.

# Notas del Desarrollador {.blog_entry_title}

Esta es la primera de una serie de actualizaciones de 'paridad', enfocadas en hacer más consistentes tanto la base de datos como las respuestas de la API. Aunque será un proceso largo, estoy convencido de que facilitará un desarrollo más fluido a futuro.

Es probable que la próxima semana no haya una nueva actualización para disponer de más tiempo de desarrollo. Mi objetivo es lanzar la siguiente versión coincidiendo con el final de la temporada actual.
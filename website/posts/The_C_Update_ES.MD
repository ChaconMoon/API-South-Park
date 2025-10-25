![Header](/blog/images/C_Update_ES.webp){.header_image}
# La actualización C {.blog_entry_title}

Esta es la primera actualización de datos tras la creación de la web, la actualización C (No sé cómo llamar a las actualizaciones de personajes, de momento se queda con la inicial hasta que se me ocurra algo mejor.) 
{.blog_intro}

El principal cambio que trae esta actualización es la adición de todos los personajes de la serie de televisión cuyo nombre empieza por C. Esto excluye de momento a la película y especiales de Paramount Plus, se añadirán en una actualización futura, aunque personajes que hayan aparecido en la serie tras la película o un especial sí aparecerán.

## Principales cambios de la actualización {.blog_title}

- Adición de los personajes de la serie cuyo nombre empieza por C
- Cambio en las miniaturas del blog de desarrollo. Ahora muestran su título en la miniatura, como en este caso.

![Thumbnail Example](/blog/images/C_Update_ES.webp){.body_image}

- Reordenamiento de los artículos del blog de desarrollo, antes estaban de antiguo a nuevo y ahora de nuevo a antiguo.

La API tiene un Easter Egg en el ID 210, es el ID entre los personajes de la serie con familia y los personajes por orden alfabetico, sirve de separador. Este Easter Egg antes era el personaje "Carlos" pero su id se ha cambiado al que le correspondia por orden albabetico [ID: 444](/api/characters/444) Ahora este Easter Egg es el personaje Charlie Brown, quien tiene ahora el [ID: 210](/api/characters/210)

## Corrección de errores {.blog_title}

### Errores en la base de datos {.blog_subtitle}

Se han actualizado los siguientes registros de personajes que no tenían imagen:

- [Shelly Marsh ID: 17](/api/characters/17)

- [Murray Broflovski ID: 23](/api/characters/23)

- [Alexandra Cartman ID: 36](/api/characters/36)

- [Karen McCormick ID: 50](/api/characters/50)

- [Thomas Tucker ID: 56](/api/characters/56)

- [Barney ID: 68](/api/characters/68)

- [Mrs. Anderson ID: 76](/api/characters/76)

- [Chad Handler ID: 120](/api/characters/120)

- [Louis Handler ID: 121](/api/characters/121)

- [Alexis Testaburger ID: 190](/api/characters/190)

- [Satan ID: 193](/api/characters/193)

- [Ali Khamenei ID: 239](/api/characters/239)

- [Barack Hussein Obama II ID: 283](/api/characters/283)

- [Bloods (Gang) ID: 346](/api/characters/346)

- [Brad Morgan ID: 380](/api/characters/380)

### Se han corregido los siguientes registros de alteregos que no tenían imagen {.blog_subtitle}

- [Shielmaiden Wendy -> Character: 188, AlterEgo: 2](/api/characters/188/alteregos/2)

- [Fastpass -> Character: 199, AlterEgo: 5](/api/characters/199/alteregos/5)

### Correcciones de errores tipográficos {.blog_subtitle}

- Se ha reemplazado la palabra española "serie" por "show" en todo el proyecto.

### Errores en el sitio web {.blog_subtitle}

- Se ha corregido el error por el cual la página de error 404 devolvía un código de respuesta 200.

## Tests añadidos {.blog_title}

- Se ha añadido un test que comprueba todas las imágenes existentes de los personajes
- Se ha añadido un test que comprueba las imágenes existentes de los alteregos




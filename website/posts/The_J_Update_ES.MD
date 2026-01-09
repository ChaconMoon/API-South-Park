![Header](/blog/images/The_J_Update_ES.webp){.header_image}
# La Actualización J {.blog_entry_title}
Bienvenidos a la primera actualización del año 2026, la actualización J o versión 0.6. Esta actualización trae todos los personajes cuyo nombre empieza por J, un nuevo endpoint relacionado con Butters y cambios en el procesamiento de imágenes.
{.blog_intro}

## Añadidos a la API {.blog_title}

### Nuevos personajes {.blog_subtitle}
La principal novedad de esta actualización son todos los personajes del juego cuyo nombre empieza por J: desde el Personaje 869 [J.J Abrams] [/api/characters/869](/api/characters/869) hasta [Justin Trudeau] [/api/characters/997](/api/characters/997). Ya estamos a punto de llegar a los 1000 personajes en la API; llevo más de la mitad del progreso, puede que termine pronto. Jeje.

### Nuevo Endpoint (Castigos de Butters) {.blog_subtitle}
Se ha añadido un nuevo endpoint 'butterspunishments', que contiene un listado de los castigos que ha sufrido Butters a lo largo de la serie. Aunque puede que se me haya pasado alguno, si es así lo añadiré.

Por ejemplo:

- [/api/butterspunishments/1](/api/butterspunishments/1) Butters es castigado por hacer una cara en la foto escolar.
- [/api/butterspunishments/15](/api/butterspunishments/15) Butters es castigado por hacerle un chupón a Cartman.

Este endpoint puede devolver metadatos, pero aún no puede mostrar el listado completo.

### Cambios en el procesamiento de imágenes (Episodios y Familias) {.blog_subtitle}

Se ha cambiado la forma en que se devuelven las imágenes de las familias y los episodios. Los enlaces de las categorías ahora tienen un formato similar a este:

- [/api/episodes/1/thumbnail](/api/episodes/1/thumbnail) Imágenes de los episodios.
- [/api/episodes/1/thumbnail](/api/episodes/1/thumbnail) Imagen 1 de la familia 1.

Ahora, en lugar de acceder directamente al fichero dentro del servidor, el archivo se genera y se modifica antes de ser enviado, permitiendo enviar alteraciones por parámetros.

- [/api/families/1/image/1?size=large](/api/families/1/image/1?size=large) Tamaño grande 1280 x 720.
- [/api/families/1/image/1?size=medium](/api/families/1/image/1?size=medium) Tamaño mediano 960 x 540.
- [/api/families/1/image/1?size=small](/api/families/1/image/1?size=small) Tamaño pequeño 640 x 480.

Los mismos tamaños se aplican a las miniaturas de los vídeos. Si no se especifica nada o se pone '?size=original', se recupera la imagen original en 1920 x 1080.

Estoy considerando añadir un tamaño aún más pequeño.

Este cambio está ahora mismo en fase experimental; no ha reemplazado a los enlaces antiguos, que seguirán funcionando hasta que esto abandone la fase experimental. No obstante, ya no son visibles en la respuesta.

El objetivo de sacarlo de forma experimental es poder evaluar si es factible un cambio así, y si el coste de procesamiento de imágenes en el servidor compensa la reducción de ancho de banda.

Además, ahora las imágenes se envían mediante streaming de bytes, por lo que es posible cargarlas de forma "lazy", permitiendo que la sección se cargue mientras se descarga la imagen.

De hecho, este cambio ya está aplicado en el sitio web y podéis ver cómo las imágenes de las familias y los episodios cargan poco a poco y usan la resolución "small".

En las siguientes actualizaciones se irá implementando en el resto de endpoints mientras lo optimizo y evalúo su fiabilidad.

La próxima actualización saldrá la semana que viene; será una mini-versión, en lugar de la versión 0.7 será la versión 0.6.5. Esta actualización consistirá en un nuevo endpoint y la incorporación de una nueva tabla a la API.

Próximamente más novedades.

¡Les deseo un muy buen inicio de año!
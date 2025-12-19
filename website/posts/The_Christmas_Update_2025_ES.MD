![Header](/blog/images/Christmas_Update_2025_ES.webp){.header_image}
# Actualización Navideña (2025) {.blog_entry_title}

Felices fiestas, o feliz día, es posible que veas esto después de Navidad. Esta es la actualización navideña de 2025, ya doy por hecho que va a haber una en 2026, ojalá. Mantener esta API un año sería un gran logro para mí y bueno, va a ser la última actualización del año y la última de la temporada 28. Creo que, aun habiendo tardado 2 semanas, será una actualización bastante completa.
{.blog_intro}

## Actualizaciones de los endpoints en la API. {.blog_title}

Ahora todos los endpoints, excepto las canciones, tienen un endpoint para obtener todos los registros, así como limitar el número de registros y hacer búsquedas.

Por ejemplo: 

- Obtener todos los grupos `http://<tu_ip>/api/groups`
- Obtener los primeros 5 grupos `http://<tu_ip>/api/groups?limit=5`
- Obtener los 3 primeros grupos que contienen 'The' `http://<tu_ip>/api/groups?search=The&limit=3`

La razón por la que esto no se ha hecho con las canciones es que los propios álbumes contienen las canciones. Aun así, puede que lo implemente en una futura actualización.

## Actualizaciones de contenido. {.blog_title}

### Nuevo Episodio 331 (Final de la temporada 28) {.blog_subtitle}

- Se ha añadido el episodio 331 ([The Crap Out](/api/episodes/331)).

- Se ha añadido al anticristo ([el bebé de Satán](/api/characters/797)) como personaje.

Este es el primer personaje de la serie que ha muerto antes de nacer. Estaba dudando sobre si añadirlo, pero viendo que empecé esta API con la idea de que fuera el último personaje de la temporada que iba a añadir, sumado a que en Estados Unidos a un bebé que ha muerto más allá de la semana 20 de embarazo se le considera un mortinato, he querido incluirlo con la particularidad de tener 0 años.

## Actualización de personajes. {.blog_title}

- Se han añadido todos los personajes de la serie cuyo nombre empieza por H o por I: [798](/api/characters/798) -> [868](/api/characters/868).

- Se han añadido 3 nuevas familias: [79](/api/families/79) -> [81](/api/families/81).

## Actualización interna de la API. {.blog_title}

Esto no es visible para los usuarios de la API, pero internamente se ha cambiado el modo en que se hacen las consultas a la base de datos. Ahora se hacen usando un modelo ORM en lugar de consultas en crudo, lo que facilita enormemente la creación de nuevos endpoints, ya que se ha simplificado muchísimo el código. Esa es la razón por la que esta actualización ha tardado 2-3 semanas. La próxima saldrá pronto.

## Nota del desarrollador. {.blog_title}
Seguramente me tome un pequeño descanso durante el periodo navideño y empezaré 2026 con una nueva actualización de personajes. En parte, se me hace raro tener que esperar 6 meses para la siguiente actualización de episodios. Confío en haber terminado la API para entonces, o por lo menos los personajes, y de paso haber conseguido un mejor hosting. Siento que lo que más me gustaría haber conseguido en ese tiempo es un proyecto de renombre. Tengo grandes planes para este proyecto y ojalá se hagan realidad.

Felices fiestas a todos los que veáis esto y feliz 2026.
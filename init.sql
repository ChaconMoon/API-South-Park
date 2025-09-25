WARNING:  database "southpark_api" has a collation version mismatch
DETAIL:  The database was created using collation version 2.36, but the operating system provides version 2.41.
HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE southpark_api REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
--
-- PostgreSQL database dump
--

\restrict BaARXfcJBQUZEenuhCvvKECSW6Icg5YtVJjLADJfSOCHRVWWSln2Jgi0yQPc9Q2

-- Dumped from database version 15.14 (Debian 15.14-1.pgdg13+1)
-- Dumped by pg_dump version 15.14 (Debian 15.14-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: album_songs; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.album_songs (
    id integer NOT NULL,
    name text NOT NULL,
    album integer NOT NULL,
    lyrics text,
    song_url text
);


ALTER TABLE public.album_songs OWNER TO southpark;

--
-- Name: album_songs_id_seq; Type: SEQUENCE; Schema: public; Owner: southpark
--

CREATE SEQUENCE public.album_songs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.album_songs_id_seq OWNER TO southpark;

--
-- Name: album_songs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: southpark
--

ALTER SEQUENCE public.album_songs_id_seq OWNED BY public.album_songs.id;


--
-- Name: albums; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.albums (
    id integer NOT NULL,
    name text NOT NULL,
    release_date date,
    album_cover text
);


ALTER TABLE public.albums OWNER TO southpark;

--
-- Name: albums_id_seq; Type: SEQUENCE; Schema: public; Owner: southpark
--

CREATE SEQUENCE public.albums_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.albums_id_seq OWNER TO southpark;

--
-- Name: albums_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: southpark
--

ALTER SEQUENCE public.albums_id_seq OWNED BY public.albums.id;


--
-- Name: alter_ego; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.alter_ego (
    id integer NOT NULL,
    original_character integer NOT NULL,
    name text,
    images text[]
);


ALTER TABLE public.alter_ego OWNER TO southpark;

--
-- Name: characters; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.characters (
    id integer NOT NULL,
    name text NOT NULL,
    friend_group integer,
    family integer,
    birthday text,
    age integer,
    religion text[],
    first_apperance integer NOT NULL,
    images text[],
    famious_guest boolean
);


ALTER TABLE public.characters OWNER TO southpark;

--
-- Name: characters_id_seq; Type: SEQUENCE; Schema: public; Owner: southpark
--

CREATE SEQUENCE public.characters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.characters_id_seq OWNER TO southpark;

--
-- Name: characters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: southpark
--

ALTER SEQUENCE public.characters_id_seq OWNED BY public.characters.id;


--
-- Name: chinpokomon; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.chinpokomon (
    id integer NOT NULL,
    name text NOT NULL,
    image text NOT NULL
);


ALTER TABLE public.chinpokomon OWNER TO southpark;

--
-- Name: episodes; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.episodes (
    id integer NOT NULL,
    name text NOT NULL,
    season integer NOT NULL,
    episode integer NOT NULL,
    realese_date date,
    description text,
    view_on_website text,
    censured boolean DEFAULT false,
    paramount_plus_exclusive boolean DEFAULT false
);


ALTER TABLE public.episodes OWNER TO southpark;

--
-- Name: episodes_id_seq; Type: SEQUENCE; Schema: public; Owner: southpark
--

CREATE SEQUENCE public.episodes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.episodes_id_seq OWNER TO southpark;

--
-- Name: episodes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: southpark
--

ALTER SEQUENCE public.episodes_id_seq OWNED BY public.episodes.id;


--
-- Name: families; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.families (
    id integer NOT NULL,
    name text NOT NULL,
    images text[]
);


ALTER TABLE public.families OWNER TO southpark;

--
-- Name: family_id_seq; Type: SEQUENCE; Schema: public; Owner: southpark
--

CREATE SEQUENCE public.family_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.family_id_seq OWNER TO southpark;

--
-- Name: family_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: southpark
--

ALTER SEQUENCE public.family_id_seq OWNED BY public.families.id;


--
-- Name: games; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.games (
    id integer NOT NULL,
    name text NOT NULL,
    developer text,
    platforms text[],
    realese_date date,
    images text[]
);


ALTER TABLE public.games OWNER TO southpark;

--
-- Name: games_id_seq; Type: SEQUENCE; Schema: public; Owner: southpark
--

CREATE SEQUENCE public.games_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_id_seq OWNER TO southpark;

--
-- Name: games_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: southpark
--

ALTER SEQUENCE public.games_id_seq OWNED BY public.games.id;


--
-- Name: specials; Type: TABLE; Schema: public; Owner: southpark
--

CREATE TABLE public.specials (
    id integer NOT NULL,
    title text NOT NULL,
    release_date date,
    link text,
    description text
);


ALTER TABLE public.specials OWNER TO southpark;

--
-- Name: album_songs id; Type: DEFAULT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.album_songs ALTER COLUMN id SET DEFAULT nextval('public.album_songs_id_seq'::regclass);


--
-- Name: albums id; Type: DEFAULT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.albums ALTER COLUMN id SET DEFAULT nextval('public.albums_id_seq'::regclass);


--
-- Name: characters id; Type: DEFAULT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.characters ALTER COLUMN id SET DEFAULT nextval('public.characters_id_seq'::regclass);


--
-- Name: episodes id; Type: DEFAULT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.episodes ALTER COLUMN id SET DEFAULT nextval('public.episodes_id_seq'::regclass);


--
-- Name: families id; Type: DEFAULT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.families ALTER COLUMN id SET DEFAULT nextval('public.family_id_seq'::regclass);


--
-- Name: games id; Type: DEFAULT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.games ALTER COLUMN id SET DEFAULT nextval('public.games_id_seq'::regclass);


--
-- Data for Name: album_songs; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.album_songs (id, name, album, lyrics, song_url) FROM stdin;
1	South Park Theme	1	I'm goin' down to South Park, gonna have myself a time\nFriendly faces everywhere humble folks without temptations\n\nGoing down to South Park, gonna leave my woes behind\nAmple parking day or night, people spouting: Howdy, Neighbor\n\nI'm heading down to South Park, gonna see if I can unwind\nI like girls with big vagina, I like girls with big fat titties\nSo coming down to South Park, and meet some fiends' mine	https://music.youtube.com/watch?v=b7uJyw6eXzg
2	Nowhere to Run	1	Fuck that shit, you know what I'm sayin'?\nI'm a give a shout out to my niggas\nI ain't givin' a shout to no-fuckin'-body, fuck that\nBig Baby Jesus in the mother fucking house\nKnow what I'm sayin'?\nUnh, come on\nI don't walk, I stalk, livin' foul like pork\nShuttin' down underground streets of New York\nHawk is what them niggas call me, 'cause they all be\nSuckin' my dick and on my mother fucking balls, G\nI know the half, so I laugh wit' 'em\nBlood bath went I let the fuckin' rap hit 'em\nFull clip, but only half did 'em\nThat's all it took, another crook\nTaken out over a dirty look\nI bag game with niggas I leave shot dead\nYou're only taken a piss from me with hot led\nYou know my style faggot, 'cause I'm always schemin'\nIn jail, niggas holdin' a sink screamin'\nPolice, but you got no peace\nYo, was that you big man, and alot mo' grease\nAll I gets is pounds, you ain't want none of this\nBack streets are like track meets 'cause I be runnin' this\nAin't nowhere to run ('cause I be runnin' this)\nAin't nowhere to hide (come on)\nAin't nowhere to go ('cause I be runnin' this)\nReaper saved your soul (come on)\nSurroned by the colors, I see crimson, black and blue (come on)\nLocking open doors again, I'm still afraid of you\n(straight up, mother fucker)\nLight to dark, then light again, I always thought I knew (come on)\nYoung to old and young again, what's left for me to do? (straight up)\nCenter of the universe, collecting me in time (come on)\nI'm falling down upon the earth, and singing truth in rhyme (come on)\nIf I was a rolling stone, I'd roll until I'm through (come on)\nAnd if I was a garden I would bloom in black for you\n(Dirt Dog in effect)\nAin't nowhere to run ('cause I be runnin' this)\nAin't nowhere to hide (come on)\nAin't nowhere to go ('cause I be runnin' this)\nReaper saved your soul (come on)\nahhhh, yi yi yi yi (come on)\nAin't nowhere to run ('cause I be runnin' this)\nAin't nowhere to hide (come on)\nAin't nowhere to go ('cause I be runnin' this)\nReaper saved your soul (come on)\nha ha ha ha ha ha ha\nWhat you mother fuckers invented\nIs the craziest nigga that ever been invented\nha ha ha ha ha\nMost know, don't front on Ol' Dity Bastard\nha ha ha ha\nI call on Jesus\nThere's no obstacles that you have to jump\nThere's no walls that you have to climb\nThis is real, this is elementary dear\nElementary, Watson, Elementary\nahhhhh\nI ain't no pictue on your fore wall, necklace wearin' beard\nYou don't want this money till it's rich\nBuy my album, coded by Dirty, set you free\nGo against the grain, I got the p\nI know you don't recognize me now\nI dunked your tongue\nHow many lightening bulbs do it take to light up a fuck mode?\nBrothers, people, you'd better get the fuck off of me\nWe don't need it, it gets more ugly\nFools tryin' to bust their ass\nTryin' to get away from me when I said my real name\nI call myself in the niggas butthole\nAll the same, all the same, all the same\nAin't nowhere to run\nAin't nowhere to hide\nAin't nowhere to go\nReaper saved your soul\nahhh yi yi yi yi\nWhat, mother fucker?\nDon't try to psychology my shit, mother fucker\n'cause you'll never psychology it, mother fucker\nNever, never, never, mother fucker, never	https://music.youtube.com/watch?v=pSXty-BZ7kc
6	Kenny's Dead	1	This is Master P, I'm down here in South Park\nAnd I just put a million dollar reward up for any information or anybody who knows who killed Kenny, ya heard!?\n\n[Kenny's Dead] We got to ride tonight\nMy little homie, Kenny died tonight\n[That's What I Said] We got to ride tonight\nMy little homie, Kenny died tonight\n[Kenny's Dead] We got to ride tonight\nMy little homie, Kenny died tonight\n[That's what I said] We got to ride tonight\nMy little homie, Kenny died tonight\n\nKenny started messing up, hanging with the thugs\nCutting class in the fast section, ecstasy, weed and drugs\nAnd I guess that's how it is, when the ghetto's got you trapped\nBut Kenny ain't scared, he seen his pops get his neck snapped\nPeople lie and they cheat on South Park streets\nWhere the hoes chill and everybody run from the police\nBut what I liked about Kenny, he wasn't no Crip or no Blood\nAnd he mumbled when he talked, but he loved that bud..\n\n[Kenny's Dead] We got to ride tonight\nMy little homie, Kenny died tonight\n[That's What I Said] We got to ride tonight\nMy little homie, Kenny died tonight\n[Kenny's Dead] We got to ride tonight\nMy little homie, Kenny died tonight\n[That's what I said] We got to ride tonight\nMy little homie, Kenny died tonight\n\nAlotta hopeless nights chasin' nickels and dimes\nKenny rode the yellow bus to school, but at night he did crimes\n211, 187, it's like a hobby\nKenny slowed his roll, he did 3 years for a robbery\nSome say Kenny was the poorest kid on the street\nBut picture this, Kenny with about 10 Gs and a couple of keys\nServing the dope fiends, standing on the corner\nMoved and worked from New Orleans to Arizona\nBut it was a trip, Kenny I was wondering how you would die\nWould it be a car crash, a plane, a gun, or suicide?!\nHe knew one day that the rats would come\nBut he didn't know they was gonna scream 'bout it!'\nAnd hit him with a shotgun\n\n[Kenny's Dead] We got to ride tonight\nMy little homie, Kenny died tonight\n[That's What I Said] We got to ride tonight\nMy little homie, Kenny died tonight\n[Kenny's Dead] We got to ride tonight\nMy little homie, Kenny died tonight\n[That's what I said] We got to ride tonight\nMy little homie, Kenny died tonight\n\nA lot of wasted deaths\nA lot of senseless crime\nBut everybody think about what you do out there\nBecause uh, Judgment Day is for everybody\nJust remember that we can't take none of this with us\nAnd it's real out here on these streets\nI'd love to live like Kenny\nDie these days, ain't no coming back\nHombre, Master P, no limit to the world, baby\nIt don't get no realer than this	https://music.youtube.com/watch?v=eFQhSRbUYQQ
8	Will They Die 4 You	1	We did dat\nWe did dat\nWe did dat\nWe did dat\nWe did dat\nWe did dat\nWe did dat\nWe did dat\nWe did dat\n\n[Verse 1: Dum Dum]\nAin't no cappin when I'm rappin\nI'm all bout dividends\nPull up in a bigger Benz\nI know you feel adrenaline\nDon't be mad cause ya man made it\nYa ain't dedicated\nIf I'm speakin anotha language than let me translate\nit\nIt was early in the mornin\nRepos got the Volvos\nNow I'm standin at my door\nSmokin them Marlboros\nThinkin my lights be out tomorrow\nAnd I can't beg or borrow\nSo if you ainb't from our side\nIt's day one of that horror\nNow get in where I fit in\nSit down and listen\nI hate startin from the bottom but hea go the new\nmission\nWhen I'm in too deep\nI don't believe my shit stank\nNo if's, and's, or cant's to get back to my old rank\nCan I turn into a robber\nCock back revolver\nTakin what you got\nThan I'm hittin for the border\nCD's, tapes, stereos\nHere we go\nDroppin 16 in the studio\nBut ya don't hear me though\n\n[Chorus: Dum Dum and Trae]\n[Dum Dum]\nOverloaded Wells Fargo\n[Trae]\nWe did dat\n[Dum Dum]\n40,00 at the car show\n[Trae]\nWe did dat\n[Dum Dum]\nDope House Records is my studio\n[Trae]\nWe did dat\n[Dum Dum]\nHouston Hard Hittas video\n[Trae]\nWe did dat\n\n[Verse 2: Lil E aka Da Genius One]\nI think like McGiver jsu to figure things out\nI got these million dolla hands that'll outlast Boy\nScouts\nNow when I'm gone off dat drank I move slower than\nmolasses\nSmart like Urkel without the glasses\nNow undastand how da game go\nIt's the same ol same ol\nMake the crowd dangle\nThan shine like a rainbow\nTake it there\nBring it here\nCause they ain't no damn stallin\nYou put it down\nWe pick it up cause together nigga we ballin\nWe ballin all the time\nGrippin cnady\nLeavin stains\nMy roof popped up\nNow my trunk doin the same\nAnd you ask why these bitches wanna ride wit me\nCause I done did that\nBently\nStreet smarts is in me\nDa Genius baby\nI'm the nigga that approve yo credit\nI'm dat situation that get drastic if you let it\nSo if you been there and done that\nWe da niggas that did dat\nBezatines and baggets\nYellow hoes and flaggets\n\n[Chorus: Dum Dum and Trae]\n[Repeat 2x]\n\n[Verse 3:Trae]\nSpeed racer be the name destroy the rap game\nDividends and benjamins\nConstant flow on pocket change\nGot a nigga facin fame\nSmokin weedies to ease the pain\nTuck yo shit in or get put to shame\nMy whole click shine\nWe bling and blang\nH-Town chop and swang\nGrab yo bitch she feel me maan\nShe see a playa ballin givin thanks\nIf you say I did dat than I did the same\nHuh?\nWhat?\nYeah\nDope House 2000 baby\n\n[Chorus 2: Dum Dum, Lil Papa, Trae]\n[Dum Dum]\nLean harder than the Eiffel Tower\n[Trae]\nWe did dat\n[Dum Dum]\nFlip the big bird and pop my coller\n[Trae]\nWe did dat\n[Dum Dum]\nNow you know bout the Joel Cormona\n[Trae]\nWe did dat\n[Dum Dum]\nWe da shit\nDo you smell the aroma?\n[Trae]\nWe did dat\n[Lil Papa]\nSpittin game on tracks for stacks\n[Trae]\nWe did dat\n[Lil Papa]\nCan't fold my wallet cause that bitch sittin fat\n[Trae]\nWe did dat\n[Lil Papa]\nYou want ya shorty you can have her back\n[Trae]\nWe did dat\n[Lil Papa]\nCalm ya nerves and blow yaself a sack\n[Trae]\nWe did dat\n[Dum Dum]\n30,000 independently owned\n[Trae]\nWe did dat\n[Dum Dum]\nIntroduce blacks and whites to chromes\n[Trae]\nWe did dat\n[Dum Dum]\nBBBBBBOOOOOOOOYYYYYYYY!!!!\n[Trae]\nWe did dat\n[Dum Dum]\nMMMMEEESSAAGGEEE!!!!\n[Trae]\nWe did dat\n\n["we did dat" repeats til fade]	https://music.youtube.com/watch?v=Nl9ZKcQkcVQ
13	Horny	1	I'm horny all night long (x7)\n\nYou got me horny in the morning\nAnd you know uh oh\nI tried to call you\nBut I can't find the telephone\n\nI sent a message through the internet\nBut it rejected\nI wrote a letter and I sent it\nBut uh oh oh\n\nThe postage takes so long\nSo I got to sing this song\nTo let you know how I feel\nWhat's the deal baby\n\nI can't wait for you\nAnd the things you make me do\nMy heart is ringing so I'm singing\nThis song for you\n\nI'm horny, horny, horny, horny\nSo horny\nI'm horny, horny, horny\n\nI search from time to time\nBut I can't find my bedroom\nNow I got so desperate that\nI sent a rocket to the moon\n\nIn New York City, someone said\nThey saw you singing the blues\nBut it was a man from nowhere land\nThat looked like you\n\nNow we'll keep searching' on\nThis feeling's much too strong\nMy heart is ringing and I'm\nSinging this song for you\n\nI'm horny, horny, horny, horny\nSo horny\nI'm horny, horny, horny\n\nThe postage takes so long\nSo I got to sing this song\nTo let you know how I feel\nWhat's the deal baby\n\nI can't wait for you\nAnd the things you make me do\nMy heart is ringing so I'm singing\nThis song for you\n\nI'm horny, horny, horny, horny\nSo horny\nI'm horny, horny, horny	https://music.youtube.com/watch?v=nDEBgXyRIIg
16	Feel Like Makin' Love	1	Baby, when I think about you..\nI think about love.\nDarling, can't live without you..\nand your lo-mrrrrrh.\nIf I had those golden dreams\nof my yesterday..\nI would wrap you in the Heavens\nAnd feel it mrrh, mrrh, mrrh, mrrh\n[Feel like makin']\n\nFeel like makin' love..\nFeel like makin' love..\nFeel like makin' love..\nFeel like makin' love to you.\n\nBaby, If I think about you..\nI think about Love!\nDarling, If I live without you..\nI live without Love! [mrrh]\nAnd if I had the sun and the moon..\nmrrh! mgrggh! mrrrh!\nI would give you both night and day\nLove satisfying.. Feel Like, mrh, makin..\n\nFeel Like Making LOVE!\nFeel Like Making, mrgh, love.. Feel Like Making LOVE!\nFeel Like Making, mggh, mrrgh..\nFeel Like Making LOVE!\nFeel Like.. making love..\nFeel Like Making LOVE!\nFeel Like Making Love to yooou!	https://music.youtube.com/watch?v=Zb8vYRkZK0E
23	Mountain Town	2	Stan:\n\nThere's a bunch of birds in the sky,\nAnd some deers just went running by,\nOhh, the snow's pure and white on the Earth rich and brown,\nJust another Sunday morning in my quiet mountain town!\n\nThe sun is shining and the grass is green,\nUnder the three feet of the snow I mean,\nThis is a day when its hard to wear a frown!\nAll the happy people stop to say hello,\n \nMan on the Street:\n\nGet outta my way!\n\nEven though the temperature's low,\nIt's a perfect Sunday morning in my quiet, little mountain town!\n\nSharon Marsh:\n\nWell, good morning Stan.\nStan:\nMom, could I have eight dollars to see a movie?\n\nSharon:\n\nA movie?\n\nStan:\n\nYeah! It's gonna be the best movie ever! It's a foreign film from Canada.\n\nSharon:\n\nAlright, here you go. But be back for supper!\n\nStan:\n\nThanks, Mom.\n\nSharon:\n\nOh, what a picture perfect child,\nJust like Jesus he's tender and mild,\nHe'd a wear a smile while he wore a thorny crown!\nWhat an angel with a heart so sweet and sure,\nAnd a mind so open and pure,\nThank God we live in this quiet, r******, mountain town!\n\nStan:\n\nDude! Dude, wake up! Kenny, come on!\n\nKenny:\n\n(I'm Coming!)\n\nStan:\n\nKenny, the Terrance and Phillip movie is out, you wanna come?\n\nKenny:\n\n(Yeah, dude! I wanna come!)\n\nCarol McKormick:\n\nWhere do you think you're going?\n\nKenny:\n\n(I'm going to see a movie.)\n\nCarol:\n\nYou can't, you have to go to church.\n\nKenny:\n\n(But Mom, I really wanna see this movie!)\n\nCarol:\n\nWell fine, you go ahead and miss church. And then when you die and go to hell you can answer to Satan!\n\nKenny:\n\n(Okay!)\n\nStan:\n\nYou can see your breath hanging in the air,\nYou see homeless people, but you just don't care,\nIt's a sea of smiles in which we'd be glad to drown!\n\nKenny:\n\n(Don't ya know it's like a perfect winter's day,\nAnd that I'm glad I can say...)\n\nStan:\n\nThat's right!\nIt's Sunday morning in our quiet, little, white-bred, r****** mountain town!\n\nKyle:\n\nReady, Ike? Kick the baby!\n\nIke:\n\nDon't kick the baby.\n\nKyle:\n\nKick the baby!\n\nSheila Broflovski:\n\nIke! You broke another window! That's a bad baby! BAD BABY!!\n\nStan:\n\nKyle! We're going to the Terrance and Phillip movie!\n\nKyle:\n\nOh my God, dude!\n\nSheila:\n\nKyle, where are you going?\n\nKyle:\n\nUh... We're going ice skating!\n\nSheila:\n\nWell, take your little brother out with you.\n\nKyle:\n\nAww, Ma! He's not even my real brother. He's adopted!\n\nSheila:\n\nDo as I say, Kyle!\n\nKyle:\n\nOkay, okay. I'm sorry.\n\nSheila:\n\nLook at those frail and fragile boys,\nIt really gets me down,\nThe world is such a rotten place,\nAnd city life's a complete disgrace!\nThat's why I moved to this r******, meshuggeneh, quiet mountain town!\nIKE! Bad baby!\n\nAnnouncer:\n\nThis program is brought to you by Snacky S'mores…\n\nCartman:\n\nMom, somebody's at the door!\nLiane Cartman:\n\nComing, hon.\n\nCartman:\n\nEy, I can't see the TV!\n\nNews Reporter:\n\nIt's been six weeks since Saddam Hussein was killed by a pack of wild boars, and the world is still glad to be rid of him.\n\nLiane:\n\nOoh, look Eric. It's your little friends.\n\nIke:\n\nSpider-Man!\n\nCartman:\n\nWhat are you guys doing here? ... Sweet, dude! Yes! Yes!\n\nKyle/Stan/Cartman/Kenny:\n\nOff to the movies we shall go,\nWhere we learn everything that we know,\nBecause the movies teach us what our parents don't have time to say,\nAnd this movie's gonna make our lives complete,\n'Cause Terrance and Phillip are sweet,\n\nCartman:\n\nSuper sweet!\n\nAll:\n\nThank God we live in the quiet, little, r******, podunk, white-trash,\n\nKenny:\n\n(Kick ass!)\n\nAll:\n\nU- S- A-!\n\nStan:\n\nCan I have five tickets to Terrance and Phillip: Asses of Fire, please?\n\nRick:\n\nNo! 	[NOT AVAILABLE IN STREAMING SERVICES]
24	Uncle Fucka	2	Terrance:\n \nShut your fucking face, uncle fucker\nYou're a cock-sucking, ass-licking uncle fucker\nYou're an uncle fucker, yes, it's true\nNobody fucks uncles quite like you\n\nPhillip:\n\nShut your fucking face, uncle fucker\nYou're the one that fucked your uncle, uncle fucker\nYou don't eat or sleep or mow the lawn\nYou just fuck your uncle all day long\n\nPhillip:\n\nHm!\n\n\nTraffic controller:\n\nWhat's going on here?\n\nDrivers and passangers:\n\nOoh, ooh\nUncle fucker\nUncle fucker, uncle fucker\nUncle fucker\nOoh\n\nTerrance and Phillip:\n\nShut your fucking face, uncle fucker (Uncle fucker)\nYou're a boner-biting bastard, uncle fucker\n\nTerrance:\n\nYou're an uncle fucker, I must say\n\nTerrance and Phillip:\n\nWell, you fucked your uncle yesterday (Ha-ha-ha-ha)\n\nTerrance and Phillip:\n\nUncle fucker\n\nTerrance and Phillip:\n\nThat's U-N-C-L-E, fuck you!\nUncle fucker\n\nTerrance and Phillip:\n\nSuck my balls	[NOT AVAILABLE IN STREAMING SERVICES]
25	It's Easy, Mmm'kay	2	Mr. Mackey:\n\nThere are times when you get suckered in\nBy drugs and alcohol and sex with women, m'kay?\nBut it's when you do these things too much\nThat you've become an addict and must get back in touch\n\nMr. Mackey:\n\nYou can do it, it's all up to you, m'kay?\nWith a little plan, you can change your life today\nYou don't have to spend your life addicted to smack\nHomeless on the streets, giving handjobs for crack\nFollow my plan and very soon you will say\n"It's easy, m'kay?"\n\nStep one: instead of "ass," say "buns"\nLike, "Kiss my buns" or "You're a buns-hole"\nStep two: instead of "shit," say "poo"\nAs in, "Bull-poo," "Poo-head," and "This poo is cold"\nStep three: with "bitch," drop the T\n'Cause "bich" is Latin for generosity\nStep four: don't say "fuck" anymore\n'Cause "fuck" is the worst word that you can say\nSo just use the word, "m'kay"\n\nChildren:\n\nWe can do it it's all up to us, m'kay?\n\nMr. Mackey:\n\nM'kay?\n\nChildren:\n\nWith a little plan we can change our lives today\n\nMr. Mackey:\n\nYou can change today\n\nMr. Mackey and children:\nWe don't have to spend our lives shootin' up in the trash\nHomeless on the streets, giving handjobs for cash\nFollow this plan and very soon you will say\n"It's easy, m'kay?"\n\nMr. Mackey and Red:\n\nStep one: instead of "ass," say "buns"\n\nBoy 1 and girl:\n\nLike, "Kiss my buns" or "You're a buns-hole"\n\nMr. Mackey, Annie, Butters and boy 2:\n\nStep two: instead of "shit," say "poo"\n\nMr. Mackey, Kyle and boy 2:\n\nAs in, "Bull-poo," "Poo-head," and "This poo is cold"\n\nMr. Mackey and boys:\n\nStep three: with "bitch," drop the T\n\nGirls:\n\n'Cause "bich" is Latin for generosity\n\nMr. Mackey and children:\n\nStep four: don't say "fuck" anymore\n\nMr. Mackey and children:\n\n'Cause "fuck" is the worst word that you can say\n\nChildren:\n\n"Fuck" is the worst word that you can say\nWe shouldn't say "fuck", no\nWe shouldn't say "fuck," fuck no\n\nMr. Mackey:\n\nYou're cured, you can go!\n\nMr. Mackey and children:\n\nWe don't have to spend our lives shootin' up in the trash\nHomeless on the streets, giving handjobs for cash\nFollow this plan and very soon you will say\n\n\nMr. Mackey and children:\n\n"It's easy, m'kay?"\n\nChildren:\n\n"It's easy, m'kay?"\n\nMr. Mackey:\n\n"It's easy, m'kay?"\n\nChildren:\n\n"It's easy, m'kay?"\n\nMr. Mackey:\n\n"It's easy, m'kay?"\n\n\nChildren:\n\n"It's easy, m'—," "It's easy, m'—"\n"It's easy, m'kay?"\n\nMr. Mackey:\n\nHahaha, m'kay\nHahahaha, m'kay\nHaha, m'kay	[NOT AVAILABLE IN STREAMING SERVICES]
17	The Rainbow	1	Many colors in the homo rainbow\nDon't be afraid to let your colors shine\nMany colors in the homo rainbow\nShow me yours. I'm gonna show you mine\n\nIf you find a pot of gold\nEvery little thing is gonna work out fine\nIn the homo rainbow\n\nMany colors in the homo rainbow\nYou give me shade from black to yellow\nMany colors in the homo rainbow\nA warm embrace and a kind-a hello\n\nIf you find a pot of gold\nEvery little thing is gonna work out fine\nIn the homo rainbow\n\nIf you find a pot of gold\nEvery little thing is gonna work out fine\nIn the homo rainbow\nEvery single color, every walk of life\nIn & out changin, every day and night\nFrom the golden shores of Kansas, to the middle of Japan\nreach inside your soul and learn your fellow\n\nThere are many colors in the homo rainbow\nDon't be afraid to let your colors shine\nDon't be ashamed of what God made you	https://music.youtube.com/watch?v=z6TPRdkG1-4
20	Mephesto and Kevin	1	Les Claypool:\nIn 1986 the University of California Davis sought two of the all-time brightest stars: Dr. Alphonse Mephesto, and Dr. Arnie Apesacrappin. Dr. Mephesto worked hard toward his thesis. His goal was to genetically duplicate the DNA structure of asparagus so that all asparagus would grow to the same girth and length, giving asparagus a much more pleasant presentation in the world's supermarket vegetable bins.\n\nDr. Apesacrappin's goal was to genetically create the greatest musical entertainer the world had ever seen. Dr. Apesacrappin knew that if he could assemble the right elements he could theoretically build a DNA structure that would ensure his creation of talent far surpassing the average individual.\n\nAt the time, one subject of urban myth was the story that Michael Jackson, in an effort to retain his youthful look and feminine vocal characteristics, had his testicles surgically removed, thereby making him a modern day Castrato. If such a rumor were true, Michael Jackson more than likely would have some of his semen preserved before the surgery to ensure the future of his name and lineage.\n\nWord came back to Dr. Apesacrappin of a secret cold storage locker deep within the bowels of the UCLA research center, that not only contained four containers of frozen semen, but also held a pair of testicles - each was labeled with the name "Jack Michaelson".\n\nChef:\nI once heard a noise\nIn the night, the most sensual voice\nThe song of love from an angelic boy\nStuck in my head\nAnd this is what he said\n\n"I am gopher boy\nPondering reality\nI am Gopher Boy\nWho will buy my raspberries?"\n\nClaypool:\nThis had to be the seed of the King of Pop. Dr. Apesacrappin was able to use his charm and chiseled gritty features to woo a young lab technician by the name of Jennifer, who of course just happened to have the proper access needed to obtain a small vial of the precious semen.\n\nThe search for the egg was a short one. Dr. Mephesto simply ran an ad in the classifieds section of an LA Music magazine. The ad read, "Wanted: Unfertilized human eggs for genetic experiment. Donors must have musical background."\n\nWith a plethora of young eager wannabe musical starlets, willing to sell their eggs, the two doctors, after rigorous auditioning, picked and purchased. Dr. Apesacrappin felt that it would be far less complicated legally if the foetus was brought to term in the womb of a non-human. He had long since secured the services of the University Volleyball Mascot: a llama by the name of Missy.\n\nWhen the baby was ready, the child was removed via caesarean.\nIt was a healthy baby boy. He was named Kevin.\n\nChef:\nI once heard a noise\nIn the night, the most sensual voice\nThe song of love from an angelic boy\nStuck in my head\nAnd this is what he said\n\n"I am gopher boy\nPondering reality\nI am Gopher Boy\nWho will buy my raspberries?"\n\nClaypool:\nKevin was a beautiful child. Dr. Apesacrappin saw to it that Kevin was trained by the best in all aspects of performing. His voice was golden and had a sweetness to it that most males lacked. He moved with grace and was able to moonwalk by the time he was three.\n\nAs Kevin grew with his talent, Dr. Apesacrappin started noticing odd developments in his physical state. When Kevin lost his baby teeth, his secondaries came in with a vengeance; they were at least twice the size as a normal adult's and the two in front stuck nearly straight out. Also as Kevin reached his eighth year, he was the same height as he was when he was four.\n\nTo top it off, he was growing hair all over and his penis was enormous, even by adult standards. It also dawned on the doctor that even through all the years of hearing Kevin singing, he rarely spoke, often choosing to communicate through various grunts and gurgles.\n\nChef:\nI once heard a noise\nIn the night, the most sensual voice\nThe song of love from an angelic boy\nStuck in my head\nAnd this is what he said\n\n"I am gopher boy\nPondering reality\nI am Gopher Boy\nWho will buy my raspberries?"\n\nClaypool:\nOthers were noticing the changes in Kevin. Children began to tease him, they called him "Gopher Boy". One Day, a bully by the name of Big Roy started throwing bananas at him. Soon a crowd of kids were all throwing bananas. Suddenly, in a fury, Kevin rushed at Big Roy and bit three fingers off on his left hand.\n\nKevin was taken away and placed in the custody of the State. Dr. Apesacrappin's actions were found out, but because there was no legislation concerning the genetic construction of another human being, no criminal charges were brought forth.\n\nThe Medical Association's Board of Ethics stripped him of all his credentials and his reputation was ruined. In fact, his name became so synonymous with failure that for years to come, med students around the world were known to say in times of mishap, "damn, I feel just like Apesacrappin."\n\nDr. Mephesto immediately began proceedings to adopt little Kevin. Being a noted scientist and the creator of the cloned asparagus, it wasn't long before the two were legally united as father and son. They moved to Colorado, where they live in relative obscurity.\n\nKevin is still a boy of few spoken words, sticking mainly to his grunts and gurgles, but on occasion, if you listen closely, you can hear his sweet golden singing voice, ring out into the night, over the small town of South Park...\n\nKevin:\n"I am gopher boy\nPondering reality\nI am Gopher Boy\nWho will buy my raspberries?"	https://music.youtube.com/watch?v=3pctQ9tGMGk
21	Mentally Dull (Think Tank Remix)	1	Damien:\nEverybody hates me!\nMr. Mackey:\nWhy do you suppose that is?\nDamien:\nBecause I'm the son of the devil!\nMr. Mackey:\nUh huh that's a good start, why else?\n\nStan:\nDude this is pretty fucked up right here!\n\nStan:\nOh my god they killed Kenny!\nKyle:\nYou bastards!\nStan:\nOh my god they killed Kenny!\nMr. Garrison:\nWhat kind of sick weirdo are you?\nStan:\nOh my god they killed Kenny!\nKyle:\nSay something Mr. Hankey.\nMr Hankey:\nAhh!\nStan:\nOh my god they killed Kenny. Dude, Kenny is dead.\n\nChef:\nHello there children. Let me sing you a little song: I'm gonna make love to you woman.\nBarbrady:\nWell you ain't Fiona Apple, and if you ain't Fiona Apple I don't give a rat's ass.\nReporter:\nWhat would drive a man to such a disgusting act?\nWoman:\nMy god that's disgusting!\nStan:\nWhoa dude, how do you have sex with a chicken?\nBoy:\nDumb asses!\nCartman:\nOw! God damn it!\nStan:\nDude! Sick!\nMr. Hankey:\nAhhhhh!\nCartman:\nYou get your b**** ass back in the kitchen, and make me some pie!\nKyle:\nWhat the hell would you know you fat sweaty mongoloid?!?\nCartman:\nDon't call me fat buttfucker!\nKyle:\nYou're such a fat fuck Cartman, that when you walk down the street people say, God\ndammit that kid's a big fat fuck!!!\nCartman:\nHey!\nMr. Mackey:\nI mean your one screwed up little kid, do you understand?\nCartman:\nHe is a very disturbed little boy.\nLiane:\nYou want some Cheesy Poofs?\nCartman:\nYeah I want Cheesy Poofs!\nLiane:\nYou can have a eensy weensy bit can't you?\nCartman:\nWell?\nLiane:\nJust a weensy eensy woo-woo?\nCartman:\nOkay!\nLiane:\nI bought you some Cheesy Poofs and Happy Tarts.\nCartman:\nGod Damnit!\nLiane:\nJust a weensy eensy woo-woo?\n\nStan:\nOh my god they killed Kenny!\nKyle:\nYou bastards!\nStan:\nOh my god they killed Kenny!\nMr. Garrison:\nWhat kind of sick weirdo are you?\nStan:\nOh my god they killed Kenny!\nKyle:\nSay something Mr. Hankey.\nMr Hankey:\nAhh!\nStan:\nOh my god they killed Kenny. Dude, Kenny is dead.\n\nMr. Garrison:\nDumb ass, what a r*****!\nKyle:\nFatso!\nCartman:\nHey!\nStan:\nDude.\nMr. Garrison:\nDon't be such a little wuss!\nBarbrady:\nFruitcake!\nCartman:\nB****.\nWendy:\nNo, I'm not acting like a freak!\nCartman:\nWell I was standing out in a field and I had this huge satellite dish sticking out of my butt, and then there were hundreds of cows and aliens, and then I went up on the ship, and Scott Baio gave me pinkeye!\nStan:\nWhat the hell are you talking about!\nMr. Garrison:\nThere are no stupid questions, just stupid people!\nWendy:\nBarf is gross!\nCartman:\nNobody gives a rat's ass!\nPip:\nLunchy munchys umm!\nStan:\nAt least my mom isn't on the cover of Crack W**** magazine!\nCartman:\nDon't call me fat, buttfucker!\n\nStan:\nOh my god they killed Kenny!\nKyle:\nYou bastards!\nStan:\nOh my god they killed Kenny!\nStarvin' Marvin:\nYeah I want da cheesy poofs!\nStan:\nOh my god they killed Kenny!\nMr. Hankey:\nHowwwwdy-hoooo.\nStan:\nOh my god they killed Kenny. Holy Shit it's Jesus!\n\nCartman:\nYou Pigfucker!\nStan:\nDude, don't say pigfucker in front of Jesus!\nJesus:\nYay, believe in me, and ye shall find peace!\nRing Announcer:\nWearing very very black shorts... the king of all that is evil...\nTowns People:\nBarbra Streisand, Barbra Streisand!\nBarbra Streisand:\nI'm Barbra Streisand!\nChef:\nBarbra Streisand?\nLeonard Maltin:\nBarbra Streisand.\nKyle:\nKick the baby!\nIke:\nDon't kick the...\nLeonard Maltin:\nLeonard Maltin, yes.\nSidney Poitier:\nSidney Poitier.\nChef:\nSidney Poitier!?!\nStan:\nOh yeah?\nBarbra Streisand:\nPiss ass little hick!\nStan:\nYou ugly s****!\nCartman:\nDamn your black heart, Barbra Streisand!\nHey! Why don't you stop dressin' me up like a mailman, and making me dance for you, while you go and smoke crack in your bedroom and have sex with some guy I don't even know on my dad's bed!\nStan:\nThis is pretty fucked up right here!\nCartman:\nLet us remember the good times, Kenny would have wanted it that way!\n\nStan:\nOh my god they killed Kenny!\nKyle:\nYou bastards!\nStan:\nOh my god they killed Kenny!\nKyle:\nTotal weirdo freak!\nStan:\nOh my god they killed Kenny!\nStan:\nOh my god!\nKyle:\nOh my god!\nStan:\nOh my god they killed Kenny. Dude Kenny is dead!	https://music.youtube.com/watch?v=O3F1_3g3cww
22	Kyle's Mom's a Bitch	1	Well...\nKyle's mom is a bitch, she's a big fat bitch\nShe's the biggest bitch in the whole wide world\nShe's a stupid bitch, if there ever was a bitch\nShe's a bitch to all the boys and girls\n\nOn Monday she's a bitch, on Tuesday she's a bitch,\nFrom Wednesday to Saturday she's a bitch\nThen on Sunday, just to be different\nShe's a super King Kamehameha bi-atch\n\nHave you ever met my friend Kyle's mom?\nShe's the biggest bitch in the whole wide world\nShe's a mean old bitch 'cause she has stupid hair\nShe a bitch, bitch, bitch, bitch, bitch, bitch, bitch\nbitch, bitch, bitch, bitch, bitch, bitch, bitch, bitch\nShe's a stupid bitch\nKyle's mom's a bitch and she's just a dirty bitch\nKyle's mom is a bitchh, ah	https://music.youtube.com/watch?v=KqD0CfhSZjY
27	Kyle's Mom's a Bitch (Movie version)	2	Cartman: Weeellll\n\nKyle: Don't do it, Cartman!\n\nCartman: Weeellll\n\nKyle: I'm warning you!\n\nCartman: Okay, okay.\n\nKyle: I'm getting pretty sick of him, call my mom...\n\nWeeellll\nKyle's mom's a bitch, she's a big fat bitch,\nShe's the biggest bitch in the whole wide world\nShe's a stupid bitch, if there ever was a bitch,\nShe's a bitch to all the boys and girls.\n\nKyle: SHUT YOUR F**KING MOUTH, CARTMAN!\n\nOn Monday she's a bitch,\nOn Tuesday she's a bitch,\nOn Wednesday through Saturday she's a bitch\nThen on Sundays, just to be different,\nShe's a super King Kamehameha biyotch!\n\nCome on! You all know the words!\n\nHave you ever met my friend Kyle's mom?\nShe's the biggest bitch in the whole wide world.\n(La-la-la-la-la-la-la)\nShe's a mean old bitch, and she has stupid hair.\nShe's a bitch-bitch-bitch-bitch-bitch-bitch-bitch.\n\nbitch-bitch-bitch-bitch-bitch-bitch-bitch-bitch (bitch, bitch, bitch, bitch)\nShe's a stupid bitch! (WHOO!)\nKyle's mom's a bitch (Stupid bitch, because...)\nAnd she's such a dirty bitch! (...she's such a dirty bitch. bitch!)\n\nTalk to kids around the world,\nIt might go a little bit something like this:\n\n(Chinese)\n凯尔妈妈是个泼妇，她是基佬秘术大师，我只想说摸了被她变泼妇。\nKǎiěr māmā shìgè pōfù, tā shì jī lǎo mìshù dàshī, wǒ zhǐ xiǎng shuō mōle bèi tā biàn pōfù,\nKyle Mom's a bitch, She's a fat gay bitch, when I touch her she becomes a big fat bitch.\n(French)\nLa mère de Kyle est une pute, est une sacrée vieille pute, la plus grande pute du monde entier.\nKyle's Mom's a bitch, a one hell of a bitch, the biggest bitch in the whole, wide world.\n(Dutch)\nKyle's moeder is een teef, ze is een grote fout te teef ze grote teef ter ver reld, teef ter ver reld.\nKyle's Mom is a bitch, she was a big mistake of a bitch, she's the biggest bitch in the world, bitch in the world.\n(Swahili)\nMama yake Kyle ni mbwa mkubwa, ndiye ni mbwa mkubwa kuliko wote duniani hii.\nKyle's Mom's a dog, a female dog, she's the biggest bitch in whole wide world.\n\nHave you ever met my friend Kyle's mom?\nShe's the biggest bitch in the whole wide world.\n(La-la-la-la-la-la-la)\n\nShe's a mean old bitch, and she has stupid hair.\nShe's a bitch-bitch-bitch-bitch-bitch-bitch-bitch\n\nbitch-bitch-bitch-bitch-bitch-bitch-bitch-bitch.\nShe's a stupid bitch! (Uh, Cartman?)\n\nKyle's mom's a bitch\nAnd she's such a dirty bitch!\n\nI really mean it!\nKyle's mom, she's a big… fat… fucking bitch!\nBig ole fat fucking bitch, Kyle's mom!\nYeah, chaaaa!\n\nCartman: What?\n\nCartman: Oh, fuck!	[NOT AVAILABLE IN STREAMING SERVICES]
28	What Would Brian Boitano Do?	2	Stan:\n\nWhat would Brian Boitano do\nIf he was here right now,\nHe'd make a plan\nAnd he'd follow through,\nThat's what Brian Boitano'd do.\n\nKyle:\n\nWhen Brian Boitano was in the Olympics,\nSkating for the gold,\nHe did two salchows and a triple lutz\nWhile wearing a blind fold.\n\nCartman:\n\nWhen Brian Boitano was in the alps,\nFighting grizzly bears,\nHe used his magical fire breath,\nAnd saved the maidens fair.\n\nStan and Kyle:\n\nSo what would Brian Boitano do\nIf he were here today?\nI'm sure he'd kick an ass or two,\nThat's what Brian Boitano'd do.\n\nCartman:\n\nI want this V-Chip out of me,\nIt has stunted my vocabulary.\n\nKyle:\n\nAnd I just want my mom\nTo stop fighting everyone\n\nStan:\n\nFor Wendy I'll be an activist too,\n'Cause that's what Brian Boitano'd do.\n\nAll:\n\nAnd what would Brian Boitano do?\nHe'd call all the kids in town,\nAnd tell them to unite for truth\nThat's what Brian Boitano'd do.\n\nBrian Dennehy:\n\nSomeone say my name?\n\nStan:\n\nWho are you?\n\nDennehy:\n\nI'm Brian Dennehy!\n\nKyle:\n\nWhat? No, Not fuckin' Brian Dennehy!\n\nStan:\n\nYeah, get the fuck outta here!\n\nDennehy:\n\nOh. Bye-e!\n\nStan and Kyle:\n\nWhen Brian Boitano traveled through time\nTo the year 3010,\nHe fought the evil robot king\nand saved the human race again\n\nCartman:\n\nAnd when Brian Boitano built the pyramids,\nHe beat up Kublai Khan!\n\nStan and Kyle:\n\n'Cause Brian Boitano doesn't take shit...\n\nAll:\n\n...from anybody!\nSo let's all get together,\nAnd unite to stop our moms\nAnd we'll save Terrance and Phillip too,\n'Cause that's what Brian Boitano'd do!\nAnd we'll save Terrance and Phillip too,\n'Cause that's what Brian Boitano'd do!\n'Cause that's what Brian Boitano'd do!	[NOT AVAILABLE IN STREAMING SERVICES]
36	Shut Yo Face (Uncle Fucka)	2	Terrance:\n\nshut your fucking face, uncle fucka\nyou're a cock-sucking, ass-licking, uncle fucka\nyou're an uncle fucka, yes it's true\nnobody fucks uncles quite like you\n\nPhillip:\n\nshut your fucking face, uncle fucka\nyou're the one that fucked your uncle, uncle fucka\nyou don't eat or sleep or mow the lawn\njust fuck your uncle all day long\n(farting duo)\ncanadian people:\nfucka, fucka, fucka, uncle fucka, fucka!\nshut your fucking face, uncle fucka!\nyou're a boner biting bastard, uncle fucka!\nthat's u n c l e - fuck you! uncle fucka!\n(suck my balls)	[NOT AVAILABLE IN STREAMING SERVICES]
37	Riches to Rags (MMMKay)	2	Mr. Mackey:\n\nThere are times when you get suckered in\nBy drugs, and alcohol, and sex with women (mmmkay)\nBut it's when you do these things too much\nThat you've become an addict, and must get back in touch...\n\n(Mmmkay)[uhh](mmmkay)[uhh](mmmkay)[c'mon][Nappy]\n\n[Yo!]\n\n(Mmmkay)\n\nAlcohol, drugs, sex, you've become an addict (too much)\nAlcohol, drugs, sex, sex (too much)\nAlcohol, drugs, sex, you've become an addict\nAlcohol, drugs, sex, sex (too much)\n\nHe wore the finest stuff\nPlatinum chains with diamond cuts\nHawaiian slush\nCombined with wine and coconuts\nPushed a 'Lac, gator shoes\nArmani suits, shot hoops\nPlenty hoes, plenty loot\nA major nigga, a paid nigga\nKept some rich [?]\nPlus a big Benz, plus a Lex jeep\nPlus the best freaks\nPlus he jet ski in Texas\n​Flash the big cheddar\nWu-Leather, new cheddar\nGucci sweater\nSpillin' Amaretto on a black Beretta\nFor the fools who change like blue weather\nHis tailor-made Armani suits\nPlayed with Tommy boots\nPushed more Hummers than army troops\nWord to my man Dukes\nLook at him Versace'd down\nMore kids than Bobby Brown\nHad a private jet\nPlanned the odds he best\nTwo keys inside his vest\nI keep the gold chain\nAnd a cold dame\nWe drove a fast car in a slow lane\nFrom the caviar to the white cocaine\nFlick it all in the dope game\nSnort coke, push dope\nDown to cut a nigga throat\nSpent half of his summer\nCruisin' on a love boat\n\n(Mmmkay)\n\n(Chorus 1)\n[Mmmkay]{​​anyway}​​[mmm-hmm]{​​for real?}​​\n[Is that right?]{​​feel that}​​[Go'n ahead balla]{​​do ya thang}​​\n[Mmmkay]{​​anyway}​​[mmm-hmm]{​​really?}​​\n[Is that right?]{​​feel that}​​[Go ahead playa]{​​do yo thang}​​\n\nMr. Mackey:\n\nSpring break, Virginia Beach\nHad a pair of gold skis\nMo' money than Playboy\n(BK?) Nigga please!\nHe was living lavish\nDrinking cash\nWith player status\nNot the fattest chick, the baddest\nUsed to ball with Gladys Knight\nThis was just your average night\nMy dude spend a G a week\nJust to see a freak\nStrip down to her bare essentials in the Presidential Suite\nHis mental's weak\n​New York Undercover shot his brother\nIn a shootout\nHe had to move out\nAnd drop his mother in a new house\nHe had nothin' to go home to\nDefeat was on the menu\nA two time loser (oh man), deja vu\nFell in debt with Johnny Mafia\nAnd let the gun play\nHe sold his Ultima\nLeased a Hyundai\nPushin' out his mom's place\nGet caught for child support\nPoppin' corks was more important\nBench warrant, undercover informant\nThree years upstate, tough breaks\nDroppin' names, poppin' veins\nGettin' high off his own supply\nStill movin' weight, steady losin' weight\nOn the grind\nWith his life on the line	[NOT AVAILABLE IN STREAMING SERVICES]
31	Eyes of a Child	2	The eyes of a child, so innocent and pure\nA child's heart is full of song\nTake their tiny hands and lead them to the light\nAs adults, we see the pain in the world\nAnd it sometimes don't seem right\n\nBut through the eyes of a child\nThe world seems magical\nThere's a sparkle in their eyes\nThey've yet to realize the darkness in their soul.\nThe beauty of their smile\nAdventurous and wild\nLife is kinda gay, but it doesn't seem that way\nThrough the eyes of a child\n\nSo don't give up, even when the road seems long\nJust find that child inside you\nYeah, you've got to find you!\nSpread your wings and fly, to the brightest star\nIf you want, I can even get my friend Steve\nTo detail your car, for like 20 bucks\n\nBut through the eyes of a child, the world seems magical\nThere's a sparkle in their eyes\nThey've yet to realize the darkness in their soul.\nThe beauty of their smile\nAdventurous and wild\nSure, life is kinda gay, but it doesn't seem that way,\nThrough the eyes of a child\n\nGot an eye on my hand\nI've got an eye on my hand\nI've got an eye on my hand\nBut still I can't find you\nAn eye on my hand\nWhere have you gone girl?\nAn eye on my hand\nI'm coming up behind you\nEye on my hand\nDon't turn around now\n'Cause I'm right there\nI'm coming up behind you\n\nThrough the eyes of a child, the world seems magical.\nThere's a sparkle in their eyes\nWe've yet to realize the bastards they really are\nThe beauty of their smile\nAdventurous and wild\nSure, life is kinda gay, but it doesn't seem that way\nthrough the eyes of a child\n\nSure, life is kinda gay, but it doesn't seem that way,\nThrough the eyes of a child	[NOT AVAILABLE IN STREAMING SERVICES]
34	Mountain Town (Reprise)	2	Chef:\n\nEverything worked out.\nWhat a happy end!\nAmericans and Canadians are friends again.\nSo let's all join hands and knock oppression down!\n\nChoir:\n\nGood Lordy, I'm found!\n\nStan, Kyle and Cartman:\n\nDon't you know our little lives are now complete?\n\nSharon, Liane and Sheila:\n\n'Cause Terrance and Phillip are sweet.\n\nSheila:\n\nSuper sweet!\n\nAll:\n\nThank God we live in this\nquiet, little, pissant, r******,\npodunk, jerkwater, greenhorn, one-horse,\nmud-hole, peckerwood, right-wing, whistle-stop,\nhobnail, truck-drivin', old-fashioned, hayseed, inbred,\nunkempt, out-of-date, out-of-touch, white-trash,\n\nStan, Kyle, Cartman:\n\nKick-ass!\n\nAll:\n\nMountain town! 	[NOT AVAILABLE IN STREAMING SERVICES]
38	Kyle's Mom's a Bitch (Joe C. featuring Kid Rock)	2	Kid Rock:\n\nTell you 'bout Kyle's momma\nHa-ha-ha\nStraight out of Taylor: Joey C\n\nJoe C & Kid Rock:\n\nKyle's momma is a big fat bitch\nShe's the biggest bitch I know and she stinks like shit\nRemember back in the day when she was skinny? (Yeah)\nNow she's fugly, but still thinks she's pretty (Heh)\nI just laugh, and walk on past\nSayin' "Shit, god damn, that's a big fat ass!"\nFuck that slut, she's a big fat trick\nBut I still let her suck this ten-foot dick! (Ha-ha-ha)\nJoe C, I'm a crazy hit\nDown with Kid Rock and the South Park clique (Yeah)\nI don't know much, but I know this shit\nKyle's momma is a big fat bitch!\n\nKyle's momma is a big fat bitch\nKyle's momma is a big fat bitch\nKyle's momma is a big fat bitch\nShe's a three-toed, stanky-ass, cross-eyed bitch\n\nKid Rock:\n\nUh-huh, Kid Rock, check it\nMy homie named Kyle lives up the block\nHe's got a big fat mom that sucks my cock, huh\nNon-stop, she's a sight to see\nA real sloppy bitch, that does right by me\nShe might be the best suck in the mountains\nTen times a week; but shit, who's countin'?\nI'm astounded by the things she does\nShe's the suckinest, fuckinest freak there ever was\nShe ain't a slut, she's a super-groupie\nAnd I pass that bitch around like a doobie\nI don't know much, but I know this\nKyle's mom is a big fat bitch\n\nKid Rock & Joe C:\n\nKyle's momma is a big fat bitch\nKyle's momma is a big fat bitch\nKyle's momma is a big fat bitch\nShe's a three-toed, stanky-ass, cross-eyed bitch\n\nKid Rock:\n\nOh, shit\nTell em, Joe\n\nJoe C, Kid Rock, & Both:\n\nI'm Joe C, the C stands for Cool\nI might be a fuck, but I ain't no fool (Uh-uh)\nI just rolled from South Park to Boulder\nCaught Kyle's mom trippin' on X, so I bowled her\nThen I sold her, 'cause I'm like that\nLittle freak-ass pimp, but you know that (Yeah)\nI'm just mad, gold tracks, like I'm Puffy\nColorado bitches ain't shit but yuppies\nWhattup? I'm the J-O-E\nTo the motherfuckin C in the place to be (Uh, uh, yeah)\nI don't know much, but I know this\nKyle's momma is a big fat beotch!\n\nKid Rock, & Both:\nKyle's momma is a big fat bitch\nKyle's momma is a big fat bitch\nKyle's momma is a big fat bitch\nShe's a three-toed, stanky-ass, cross-eyed bitch!	[NOT AVAILABLE IN STREAMING SERVICES]
40	I Swear It (I Can Change)	2	Some people say that I'm a bad guy\nThey may be right\nThey may be wrong\nBut it's not as if I don't try\nI just mess up\nAnd I go wrong\n\nBut I can change, I can change\nI can learn to keep my promises, I swear it\nOpen up my heart and I will dare it\nAny minute now I swear I'll share it\n\nOh it's strange, yes, it's strange\nThough I guess it's quite clear\nI killed an antelope and deer\nAnd there's no home on my range\nYes, I'm a little deranged\nBut I can change\n\nIt's not my fault that I'm so evil\nIt's society, sobriety\nYou know my momma picked cotton\nAnd my daddy boll weevil\n\nIt was history, it wasn't me\n\nBut I can change, I can change\nI can learn to keep my promises I know it\nOpen up my heart and I will show it\nAny minute passed 'til I outgrow it\n\nYou'll never change\nYou'll never change\nYou'll always be a dog with me\n\nYes, but don't be such a boob\nManna from heaven shall be my food\nMy acts of past were misconstrued\nAnd God above will watch me change\nAnd while I'm changing, I'll be changing, I'm gonna CHANGE!\nSoon...\n\n[solo]\n\nI can change, I can change\nI can learn to keep my promises, I swear it\nOpen up my heart and I will dare it\nAny minute now I swear I'll share it\nI'm gonna change	[NOT AVAILABLE IN STREAMING SERVICES]
51	O Tannenbaum	3	O Tannenbaum, o Tannenbaum,\nwie treu sind deine Blätter!\nO Tannenbaum, o Tannenbaum,\nwie treu sind deine Blätter!\nDu grünst nicht nur\nzur Sommerzeit,\nNein auch im Winter, wenn es schneit.\nO Tannenbaum, o Tannenbaum,\nwie treu sind deine Blätter!	https://music.youtube.com/watch?v=qHRKLHxZ1tQ
35	Good Love	2	Chef:\n\nI'm bonafide, solidified\nAnd qualified to do\nAnything your heart can stand\nIt all depends on you\nI'll turn your world upside-down\nI'll blow your mind to pieces\nYou'll recommend me to your mother\nYour sister, your aunts and your nieces\nListed in the Yellow Pages\nAll around the world\n30 years experience\nAnd loving sweet young girls\n\n(Chorus)\n\nJust call Good Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nIt ain't how good I make it, baby\nIt's how I make it good\n\nChef:\n\nI'm the king of the woman's world\nThey tell it from town to town\nAnd when I find that deserving queen\nI'm gonna share my crown\nBut if the line is busy\nDon't freak out or get nervous\nJust keep on dialing again and again\nUntil you get some service\n\n(Chorus)\n\nCall Good Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nI'll send your temperature higher\nJust like a ball of fire\n\nChef:\n\nNow listen to me, baby\nJust let your finger do the walking\nLet Chef do the talking and the loving\nYou see I'm a backdoor man\nAnd I do the things your man fail to do\nI don't know but I've been told\nBy a, a player hater\nThat my bedroom is a disguise\nFor a freak incubator\nSo if you see a fine young woman\nThat can't be satisfied\nSend her over to my stable\nI'm a horny junction that loves to ride\n\n(Chorus)\nSo call Good Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nIt ain't how good I make it, baby\nIt's how I make it good\n\n\nGood Love 6 9 9 6 9\nCall me anytime\n(Good Love 6 9 9 6 9)\nRight now would be fine, call my number\n(Good Love 6 9 9 6 9)\nCall on me\nLove gravy train, I ride ya on into glory\n(Good Love 6 9 9 6 9)\n(Good Love 6 9 9 6 9)\nLet's get it on\n(Good Love 6 9 9 6 9)\nLet's get it on\nGood Love\n\nGood Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nGood Love 6 9 9 6 9\nGood Love 6 9 9 6 9	[NOT AVAILABLE IN STREAMING SERVICES]
39	What Would Brian Boitano Do? Pt. II	2	Fight! Skate! Fight! Skate!\nFight! Skate! Fight! Skate!\n\nWhat would Brian Boitano do if he was here right now?\nHe'd make a plan, and he'd follow through\nThat's what Brian Boitano'd do!\n\nWhen Brian Boitano was in the Olympics skating for the gold\nHe did two Salchows and a triple Lutz wearing a blindfold\nWhen Brian Boitano was in the Alps fighting grizzly bears\nHe used his magical fire breath and saved the maidens' fair\n\nFight! Skate! Fight! Skate!\n\nSo what would Brian Boitano do if he was here today?\nI'm sure he'd kick an ass or two, that's what Brian Boitano'd do!\n\nFight! Skate! Fight! Skate!\n\nWhen Brian Boitano traveled through time to the year 3010,\nHe fought the evil robot king and saved us all again\nAnd when Brian Boitano built the pyramids, he beat up Kubla Khan\n'Cause Brian Boitano doesn't take shit from anybody!\n\nNo, Brian! Those chicken wings are really spicy! Don't eat those!\nI've never seen a man eat so many chicken wings\nI've never seen a man eat so many chicken wings\nI've never seen a man eat so many chicken wings\n(Aah!) I've never seen a man eat so many chicken wings!\n(Aah!) I've never seen a man eat so many chicken wings!\n(Aah!) I've never seen a man eat so many chicken wings!\n(Aah!) I've never seen a man eat so many chicken wings!\n\nFight! Skate! Fight! Skate!\n\nBrian Boitano was born on the planet of Kryluck\nHe came to earth to save us all from war and death and such\nHi de lo de, hi de lay, Brian Boitano's here!\nSo round up all your lasses, and tell them to have no fear\n\nSay, come over here, my honey\nAnd you're gonna take off my pants\nAnd I'm gonna make dirty love to you\n'Cause that's what Brian Boitano'd do\n'Cause that's what Brian Boitano'd do!	[NOT AVAILABLE IN STREAMING SERVICES]
41	Super	2	Super bitch, super bitch\nSuper bitch, super bitch\nSuper bitch, super bitch\nSuper bitch, super bitch\n\nTouch, touch, touch, touch, touch, touch\nTouch this skin, honey\nTouch all of this skin, darling\n\nCan you handle it? Can you handle it?\nCan you handle it? Can you hurdle it?\n\nIt's super, it's for you, it's for everyone\nTell everyone, tell everyone, tell everyone\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, you gotta go and feel this now\n\nI'm super, super, super, super, super, super, super\nEveryone, tell everyone, tell everyone, tell everyone, tell\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, you gotta go and feel this now\n\nSix-foot seven inch of raw dynamite\nDynamite, dynamite, dynamite, dynamite\nDynamite, dynamite, dynamite, dynamite\n\nEveryone, tell everyone, tell everyone, tell everyone, tell\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, you gotta go and feel this now\n\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, super bitch\nSuper bitch, super bitch, super bitch, that's me\nSuper bitch, super bitch	[NOT AVAILABLE IN STREAMING SERVICES]
42	O Canada	2	O Canada!\nOur home and native land!\nTrue patriot love in all thy sons command.\nWith glowing hearts we see thee rise,\nThe True North strong and free!\nFrom far and wide,\nO Canada, we stand on guard for thee.\nGod keep our land glorious and free!\nO Canada, we stand on guard for thee.\nO Canada, we stand on guard for thee.	[NOT AVAILABLE IN STREAMING SERVICES]
45	O Holy Night	3	And, O holy night! The stars are brightly shining,\nIt is the night of our dear Savior's b-b-b-birth.\n\nO holy night! The something something distant\nIt is the night with the Christmas trees and pie.\n\nJesus was born and so I get presents.\nThank you, Jesus for being born.\n\n(Whooo-oh-oh-oh-oh)\n\nFall\n(Fa-a-a-a-alllll)\n\nOn your knees!\n(On your knees)\n\nAnd, hear\n(Can't you heaaar)\n\nThe angel's... something\n(Voices!)\n\nO night\n(O night!)\n\nDivine\n(Divine!)\n\nThe night when I get presents;\n(O-o-o)\n\nO night\n(O night!)\n\nBeeef-caaakkkeee, O night;\nO night devine!\n\nEhh.. chmm	https://music.youtube.com/watch?v=mye434WSFLQ
44	Merry Fucking Christmas	3	I heard there is no Christmas\nIn the silly Middle East\nNo trees, no snow, no Santa Claus,\nThey have different religious beliefs\n\nThey believe in Muhammad\nAnd not in our holiday,\nAnd so every December,\nI go to the Middle East and say...\n\nHey there, Mr. Muslim!\nMerry fucking Christmas!\nPut down that book the Quran,\nAnd hear some holiday wishes!\n\nIn case you haven't noticed,\nIt's Jesus' birthday!\nSo get off your heathen Muslim ass\nand fucking celebrate!\n\nThere is no holiday season\nin India, I've heard\nThey don't hang up their stockings,\nAnd that is just absurd!\n\nThey've never read a Christmas story,\nThey don't know what Rudolph is about,\nAnd that is why in December,\nI'll go to India and shout...\n\nHey there, Mr. Hinduist!\nMerry fucking Christmas!\nDrink eggnog and eat some beef,\nAnd pass it to the missus!\n\nIn case you haven't noticed,\nIt's Jesus' birthday!\nSo get off your heathen Hindu ass,\nand fucking celebrate!\n\nNow I heard that in Japan,\nEveryone just lives in sin\nThey pray to several gods,\nAnd put needles in their skin.\n\nOn December 25th,\nAll they do is eat a cake,\nAnd that is why I go to Japan,\nAnd walk around and say...\n\nHey there, Mr. Shintoist!\nMerry fucking Christmas!\nGod is gonna kick your ass,\nYou infidelic pagan scum!\n\nIn case you haven't noticed,\nThere's festive things to do!\nSo let's all rejoice for Jesus,\nAnd Merry fucking Christmas to you.\n\nOn Christmas Day,\nI travel 'round the world and say,\nTaoists, Krishnas, Buddhists, and all you atheists too\nMerry Fucking Christmas to you!\n\n(Clapping) Oh, thank you, Mr. Hat.	https://music.youtube.com/watch?v=7z3kVCiGfhk
52	Christmas Time in Hell	3	Satan:\n\nWell I'll tell you what,\nMaybe we'll have ourselves a little Christmas, right here.\nC'mon everyone, gather 'round!\n\nString up the lights and light up the tree,\nwe're gonna make some revelry,\nspirits are high, so I can tell\nit's Christmas time in hell!\n\nDemons are nicer as you pass them by,\nthere's lots of demon toys to buy,\nthe snow is falling and all is well,\nit's Christmas time in hell!\n\nThere goes Jeffrey Dahmer, with a festive Christmas ham,\nafter he has sex with it he'll eat up all he can.\nAnd there goes John F. Kennedy, caroling with his son,\n\nJFK & Son:\n\nReunited for the holidays, god bless us everyone!\n\nEveryone:\n\nEverybody has a happy glow,\nlet's dance in blood and pretend it's snow,\n\nSatan:\n\nEven Mao Tse-tung is under the spell,\nit's Christmas time in hell!\n\nAdolf, here's a present for you!\n\nHitler:\n\n(Unwraps present to find a Christmas tree)\nEin Tannenbaum!'\n\nSatan:\n\nYes, ein Tannenbaum!\n\nGod cast me down from heavens door,\nto rule in hell for ever more,\nbut now I'm kinda glad, that I fell,\n 'cause it's Christmas time in hell!\n\nHere's a rack to hang the stocking on,\nwe still have to shop for Genghis Khan,\nMichael Landon's hair looks swell,\nit's Christmas time in hell!\n\nThere's Princess Diana,\nholding burning mistletoe,\nover poor Gene Siskel's head,\njust watch his weenie grow!\n\nFor one day we all stop burning,\nand the flames are not so thick,\nall the screaming and the torture stops,\nas we wait for old St. Nick!\n\nSo, string up the lights and light up the tree,\nwe're damned for all eternity,\nbut for just one day, all is well,\nit's Christmas time in hell!\n\nGather close together,\nand make it quick,\nwe gotta make room for\nAndy Dick.\n\nWake his mother and ring the bell,\n\nIt's, Christmas time...\nChristmas time...\nIt's Christmas, time, in, hell!\n\nJimmy Stewart:\n\nMerry Christmas, movie house! 	https://music.youtube.com/watch?v=H05CZSpMTZA
53	What the Hell Child is This?	3	Baby, you know there's a lot of love between us\nSometimes that love goes bad\nBut other times it's so right!\nYeah, I know we've been through some rough waters\nBut most of the time our thing is off the hook!\nI just want to know one thing baby...\n\nWhat child is this you've laid to rest\nAt my feet this is not the time.\nI know that I'm not responsible\nIt's white so it cannot be mine.\n\nNo, this, this is Christ the King.\nWith a feeling of relief I cannot sing.\nHaste, haste to bring him laud\nThe Babe, the Son of Mary.\n\nMmmmm, Son of Mary! (Son of Mary)\nLittle bitty baby! (Mary)\n\nSo, bring Him incense, gold, and myrrh\nCome peasant king to own Him.\nThe King of Kings, salvation brings,\nLet loving hearts enthrone Him.\n\nRaise, raise the song on high\nThe Virgin sings her lullaby.\nJoy, joy, for Christ is born\nThe Babe, the Son of Mary.\n\nSon of Mary (Son of Mary)\nLittle bitty baby (Little bitty baby, yeah)\n\nI'm gonna lay you down by the yule log\nI'm gonna, gonna love you right.\nBaby, I'm gonna deck your halls\nAnd silent your night!\nYou'll hear the herald angels sing\nWhen I'm sliding off your bra.\nI just can't wait to jingle your bells\nAnd fa la la your la! (Fa la la your la)\n\nThis, this is Christmas Day\nA time for lovers to celebrate.\nI'm gonna ding dong you merrily on high\nBecause this is the season for giving! (Give it to me baby, give it to me baby)\nSeason for giving (Season for giving, give me love!)\nSeason for living (Season for living, give me love!)\nSeason for giving (Season for giving)\nGiving you love (Give me love!)\nGiving you good love (Season for good love)\nOoh la la (Give me love!)\nMaking love (Season for giving)\nBy the fire (Give me love!)\nOoh la la (Season for good love)\nBy the fire (Give me love!)\nDon't need no mistletoe (Season for giving)\nYou've got toes (Give me love!)\nWhole lotta loving (Season for good love!)\nGiving you love (Give me love!)\nJingle your bells (Season for giving, give me love!)\nFa la la your la. (Season for good love, give me love!)	https://music.youtube.com/watch?v=ouy54KdNe2c
54	Santa Claus is On His Way	3	anta Claus is on his way\nHe's loaded goodies on his sleigh\nTo drop them off on Christmas Day\nAnd I'll say 'Howdy-ho'\nFolks will gather 'round the fire\nsing a song, stroll the choir\nPretty soon they'll all retire\nAnd I'll say 'Howdy-ho'\nI hope that Santa comes real soon\nI've been waiting for some we...	https://music.youtube.com/watch?v=dUPyQ1R3ncs
61	Timmy & The Lords of The Underworld	4	Timmy!\nTimmy livin' a lie!\nDah duoah\nUgh ah daah\n\nAnd the Lords of the Underworld\nDarkness fills my heart with pain (Timmy)\nAnd when girls start to sleep with girls\nBeelzebub will rise again\n\nTimmy livin' a lie\nPah yup pa dub dub duh\nYeah doh\nTimmy\n\nAnd the Lords of the Underworld\nDarkness fills my heart with pain (Timmy)\nAnd when girls start to sleep with girls\nThe auspices will rise again\nDuh, Timmy break it down\n\n(Now, Timmy, you need to work on your study skills)\nHeah\n(Are you mocking me?)\nTimmy\n(Young man, if you don't want to be held back a grade I suggest you start cooperating)\nDoah\n(This young man definitely has Attention Deficit Disorder)\nTimmy\nI pledge allegiance to the flag\nTim-my\nThe United States, of\nTimmy\n\nTimmy\nTimmy livin' a lie\nDap pit gul hod Timmy\nHuyah, daah\n\nAnd the Lords of the Underworld\nDarkness fills my heart with pain (Timmy)\nAnd when girls start to sleep with girls\n(Timmy, Timmy) Beelzebub will rise again\n\nTimmy\nTimmy, Timmy, Timmy, Timmy\nTimmy, Timmy, Timmy\nTimmy, Timmy, Timmy, Timmy, Timmy, Timmy\nTimmy, Timmy, Timmy, Timmy\nTimmy\nTimmy\nNo tears	[NOT AVAILABLE IN STREAMING SERVICES]
62	Timmy Livin' A Lie	4	Alright, everyone\nGive it up for Timmy and The Lords Of The Underworld\n\nAll you player haters suckin' on my jimmy (Timmy)\nBet nobody knows what kind of blow to give me (Timmy)\nYou can accept that this you didn't even try (livin' a lie)\n'Cause you know that we're the baddest band alive\nSo don't be fuckin' and just let your tushy shimmy (Timmy)\nTell you a magic tip, my hat gets all swimmy (Timmy)\nWe're sick of hearin' boy band whine (livin' a lie)\nThe Lords are here to climax in your eye (wack, man)\n\nLove brings lies\n(Timmy)\n\nStyling's gonna win me an Emmy (Timmy)\nStandin' up like Bruce Willis and Demi (Timmy)\nWe're the Lords from the Land of Noise\nWe rock the hizouse and we'll never ever die\nWe'll be in the corner booth puffin' like a chimney (Timmy)\nWith all the ladies grabbin' hold of my beanie (Timmy)\nOn a power chord munch we try hard (livin' a lie)\nLords of the Underworld putting the Kool Whip on your bike\n\nLies bring hate\n(Timmy, livin' a lie, Timmy, livin' a lie)\nLove brings lies\nLies bring hate (Timmy)\nHate brings fear\nFear brings love\nLove brings lies\nLies bring hate\nHate brings fear\nAnd tear brings-\n\nThe sun is down, the ending of another day (Timmy)\nThe night has come, and it's time for all the Lords to play (Timmy)\nLet's live it up and let the teams sport a bike (livin' a lie)\nThe underworld is filled with love, it's not such a bad place\nThis is the way I like my dream because it fits me well (Timmy)\nIf it were up to me, the world would be a little bit more like hell (Timmy)\nBecause the world I see before me has far too much pain (livin' a lie)\nAnd the Lords are the only thing that keep me sane\n\nLove brings lies (Timmy)\nLies bring hate\nHate brings fear (Timmy)\nFear brings love (Timmy)\nLove brings lies (Timmy)\nLies bring hate (Timmy)\n\nHate brings fear\nFear brings love\nLove brings lies\nLies bring hate\nHate brings fear\nLies, hate, fear, love, lies\n(Timmy)	[NOT AVAILABLE IN STREAMING SERVICES]
59	We Three Kings	3	We three king of orient are\nBearing gift we traverse afar\nField and fountain, moor and mountain,\nFollowing yonder star.\n\nO-o-o-o-oh\n\nStar of wonder, star of light,\nStar of royal beauty bright,\nWestward leading, still proceeding,\nGuide us to thy perfect light.	https://music.youtube.com/watch?v=eKdc1DPoVJI
60	Have Yourself a Merry Little Christmas	3	Mr. Hankey:\n\nHave yourself a merry little Christmas,\nLet your heart be light\nFrom now on,\nour troubles will be out of sight.\n\nHave yourself a merry little Christmas,\nMake the Yule-tide gay,\nFrom now on,\nour troubles will be miles away.\n\nThe Boys and Mr. Hankey:\n\nHere we are as in olden days,\nHappy golden days of yore.\nFaithful friends who are dear to us\nGather near to us once more.\n\nThe Boys:\n\nThrough the years\nWe all will be together,\nIf the Fates allow.\n\nMr. Hankey:\n\nHang a shining star upon the highest bough!\n\nThe Boys and Mr. Hankey:\nAnd have yourself A merry little Christmas now.\n	https://music.youtube.com/watch?v=CTRh-dRhmZ0
63	San Diego	5	Singers:\n\nBaaam badam baaam baaadam, baaam badam bam.\nBaaam badam baaam baaadam, baaam badam bam.\n\nI'm gonna jack it where the sun always shines (He's gonna jack it)\nBeen spreadin' the word and now I need to ease my mind (Jackin' it, ohhh)\nBeen plantin' them apple seeds, and while the apples grow,\nI'm gonna go out jackin' it in San Diego\n\nJackin' it, jackin' it, jackety-jack\nSpankin' it, jackin' it, spankety-smack\n\nI don't need no shirt, no, gonna take them pants right off (He's about to jack it)\nOn such a bright day, who needs underwear or socks? (Jack it, jack it, ohhh)\nBeen around God's country, and there's one thing I know,\nThere's no better place for jackin' it than San Diego\n\nJack it, jack it, jackety-jack\nSpankin' it, spankin' it, smackety-smack\nJackin' it, jackin' it, jackety-jack\nJackin' it, spankin' it, smackety-smack (Jackin' for the Lord!)\n\nJerry Sanders:\n\n"Come to San Diego, there's so much to see. From the sparkling waters of Mission Bay to the warm tortillas of Old Town. And after a day of sightseeing, why not try spankin' it in one of our charming city streets? San Diego. Come, take a load off."\n\nSingers:\n\nJackin' it, jackin' it, jackety-jack\nSpankin' it, spankin' it, smackety-smack\nA-whackin' it, whackin' it, whackety-whack\nSpankin' it, jerkin' it, smackety-smack\n\nThe cars are passin' me by, they honk and say "hello" (Hey, that guy's jackin' it!)\nFrom his window, there's a guy shootin' video (Video of him jackin')\nAnd if the good Lord, Jesus, comes knockin' on my door,\nJust tell him that I'm jackin' it in San Diego\n\nJackin' it, jackin' it, jackety-jack\nSpankin' it, spankin' it, smackety-smack (He's about to jack it)\nJack it, whack it, jack it, jackin' it, jack (Whackin' it, whackin' it)\nWhack it, whack it, spank, spank, whack, whackin' it, whack (Look at me, I'm jackin' it)\nSpank it, whack it, jack it, jack it, whackin' it, whack (Whack it)\nSpank it, spank it, whack it, whack it, San Diego (He's about to jack it)\nSan Diego, jack, jack, whackin' it, wack (Whackin' it, whackin' it)\nWhack it, San Diego, whackin' it, whack (Keep on jackin' it)\nSan Diego, jack it, jack it, whackin' it, whack (San Diego)\nJack, San Diego, whack, whack, jackin' it, jack (Jack it)\nJackin' it, jackin' it, jackin' it, jack (Whackin' it, whackin' it, whackin' it, whack)\nSan Diego, jack, jack, (Wack, wack)\nWhack, jack, spank, spank, spank,\nSan Diego, ahhh...	https://music.youtube.com/watch?v=9VPxmXPFOvY
65	There's Magic Inside You (Live)	6	There's magic inside you\n\nWhat is magic?\nIts a thought, its a vision\nBut most of all magic is a feeling that you get\nDeep down inside in your balls\nOr if you're a woman, deep down in your girl balls\n\nThe magic's inside you\n\nAnd sometimes there's magic in the wonder of a little boy\n\nOh hey everybody, it's me Butters\n\nButters come on, you have to see this\n\nHey, where you going Eric?\n\nWhere the hell are we, dude?\n\nDo you believe in magic, Stan?\n\nCartman, where are you?\n\n(muffled)\n\nYeah look, Eric is up on those rocks\n\nThat's right, I'm up here guys!\nThere's magic in all of us\nGathered here tonight\nCome on!\n\nWhat are you doing Cartman?\n\nJust come on, its f*cking magic, Kyle\n\nThis way guys, you got to see!\n\nThere's magic inside you\nYou just have to find it\nIt's deep down in your balls\nOr in your girl balls\n\nLook you guys, isn't this amazing!\n\nLe'me see\nWoah!\n\nWhere are we?\n\n(muffled)\n\nWhat is this place?\n\nI don't know, but it's just so facking magical\n\nWait a minute, wait, you guys\nI know where we are\nWe're home	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
67	Montage (Live)	6	The day is approaching to give it your best\nYou've got to reach your prime!\nThat's when you need to put yourself to the test\nAnd show us the passage of time\n\nWe're gonna need a montage (Montage)\nA sports-training montage (Montage)\n\nAnd just show a lot of things happenin' at once.\nRemind everyone of what's goin' on. (What's goin' on?)\nAnd with every shot, show a little improvement\nTo show it won't take too long\n\nThat's called a montage (Montage)\nEven Rocky had a montage (Montage)\n\nIn any sport, if you want to go\nFrom just a beginner to a pro\nYou'll need a montage (Montage)\na simple little montage (Montage)\n\nAlways fade out (Montage) into a montage (Montage)\nIf you fade out it seems like a long time (Montage) has passed in a montage (Montage)\nMontage (Montage)	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
64	Here Come the Bastards (Live)	6	Here they come\nHere come the bastards\nI heard it from a confidant\nWho heard it from a confidant\nThey're definitely on their way\nThere's one with this idea\nSomething about a hammer head shark\nNose hairs and flatus\nBest keep your distance because\nHere they come\nHere come the bastards\nBury your head deep in the sand\nAnonymity is a virtue\nIn this day and age\nAmazing hand dexterity\nFlagrant misuse of security\nBetter run, run, run, run, run, run run run run, run\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they come\nHere they comeeeee	https://music.youtube.com/watch?v=z0ncs8eM8Gw
66	Uncle Fucker (Live)	6	Shut your fucking face, uncle fucka!\nYou're a cock-sucking, ass-licking uncle fucka!\nYou're an uncle fucka, yes it's true!\nNobody fucks uncles quite like you!\n\nShut YOUR fucking face, uncle fucka!\nYou're the one who fucked your uncle, uncle fucka!\nYou don't eat or sleep or mow the lawn,\nYou just fuck your uncle all day long!\n\nHmm!\n\nWhat's going on here?\n\nUncle fucka, uncle fucka, uncle fucka, uncle fucka!\n\nShut your fucking face, uncle fucka!\n(Uncle fucka!)\n\nYou're a boner biting bastard, uncle fucka!\n\nYou're an uncle fucka, I must say.\n\nWell, you fucked your uncle yesterday!\n\nUncle fucka... that's...\n\nU-N-C-L-E, fuck you! Uncle fuckaaaaaa!!!!!!!!!!!\nToo right!\n\nSuck my balls!	https://music.youtube.com/watch?v=bbaZauwdO4c
69	It's Easy MMkay (Live)	6	There are times when you get suckered in\nBy drugs and alcohol and sex with women, m'kay?\nBut it's when you do these things too much\nThat you've become an addict and must get back in touch\n\nYou can do it, it's all up to you, m'kay?\nWith a little plan, you can change your life today\nYou don't have to spend your life addicted to smack\nHomeless on the streets, giving handjobs for crack\nFollow my plan and very soon you will say\n"It's easy, m'kay?"\n\nStep one: instead of "ass," say "buns"\nLike, "Kiss my buns" or "You're a buns-hole"\nStep two: instead of "shit," say "poo"\nAs in, "Bull-poo," "Poo-head," and "This poo is cold"\nStep three: with "bitch," drop the T\n'Cause "bich" is Latin for generosity\nStep four: don't say "fuck" anymore\n'Cause "fuck" is the worst word that you can say\nSo just use the word, "m'kay"\n\nWe can do it it's all up to us, m'kay?\n\nM'kay?\n\nWith a little plan we can change our lives today\n\nYou can change today\n\nWe don't have to spend our lives shootin' up in the trash\nHomeless on the streets, giving handjobs for cash\nFollow this plan and very soon you will say\n"It's easy, m'kay?"\n\nStep one: instead of "ass," say "buns"\n\nLike, "Kiss my buns" or "You're a buns-hole"\n\nStep two: instead of "shit," say "poo"\n\nAs in, "Bull-poo," "Poo-head," and "This poo is cold"\n\nStep three: with "bitch," drop the T\n\n'Cause "bich" is Latin for generosity\n\nStep four: don't say "fuck" anymore\n\n'Cause "fuck" is the worst word that you can say\n\n"Fuck" is the worst word that you can say\nWe shouldn't say "fuck", no\nWe shouldn't say "fuck," fuck no\n\nYou're cured, you can go!\n\nWe don't have to spend our lives shootin' up in the trash\nHomeless on the streets, giving handjobs for cash\nFollow this plan and very soon you will say\n\n\n"It's easy, m'kay?"\n\n"It's easy, m'kay?"\n\n"It's easy, m'kay?"\n\n"It's easy, m'kay?"\n\n"It's easy, m'kay?"\n\n\n"It's easy, m'—," "It's easy, m'—"\n"It's easy, m'kay?"\n\nHahaha, m'kay\nHahahaha, m'kay\nHaha, m'kay	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
70	South Park Themes (Live)	6	I'm goin' down to South Park, gonna have myself a time\nFriendly faces everywhere humble folks without temptations\n\nGoing down to South Park, gonna leave my woes behind\nAmple parking day or night, people spouting: Howdy, Neighbor\n\nI'm heading down to South Park, gonna see if I can unwind\nI like girls with big vagina, I like girls with big fat titties\nSo coming down to South Park, and meet some fiends' mine	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
71	Butters Theme Song/Robot Friend (Live)	6	Who's the boy that can laugh at a storm cloud?\nTurn a frown into a smile for free?\nWho's the kid with a heart full of magic?\nEveryone knows it's Butters!\n\nButters (Voice): "That's me!"\n\nWho's the boy with eyes full of wonder?\nWho thinks being yourself is the best thing to be?\nWho's that rascal with the tweezers in his pocket?\nEveryone knows it's Butters!\n\nButters (Voice): "That's me!"\n\nJumping in puddles, skipping down the hallway,\nPetting goats at the petting zoo, he loves John Alway\n\nButters (Voice): "John Elway!"\n\nWho's the little tyke with the cutest little dimples?\nBatting his eyes at every puppy he sees?\nIf you look inside yourself you might be surprised when you find\nA little boy named Butters!\n\nButters (Voice): "Well, that's - that's me. Yeah."\n\n\nHey there, have you heard about my robot friend?\nHe's metal and small and doesn't judge me at all\nHe's a cyberwired bundle of joy,\nMy robot friend\n\nI like to dip and daddle with my robot friend\nHe's smart as can be and emotion-free,\nAnd he's computin' his way to my heart,\nMy robot friend\n\nMy robot friend,\nMy robot friend,\nMy robot ...friend\n\nI'm hangin' out in LA with my robot friend\nWe're havin' such fun in the hot hot sun\nWe're two of a kind- That's me!\nAnd my robot friend\n\nMy robot friend,\nMy robot ...friend\n\nHey there, did you know I had a robot friend?\nWe used to laugh and play, but someone took him away\nHe was my ten gigahertz old pal,\nMy robot friend...\n\nI like to dip and daddle with my robot friend\nHe's smart as can be and emotion-free,\nAnd he's computin' his way to my heart,\nMy robot friend\n\nMy robot friend,\nMy robot friend,\nMy robot ...friend	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
72	Blame Canada (Live)	6	Times have changed,\nOur kids are getting worse!\nThey won't obey their parents,\nThey just want to fart and curse!\n\nShould we blame the government?\n\nOr blame society?\n\nOr should we blame the images on TV?\n\nNo, blame Canada!\n\nBlame Canada!\n\nWith all their beady little eyes,\nAnd flapping heads so full of lies!\n\nBlame Canada!\nBlame Canada!\n\nWe need to form a full assault!\n\nIt's Canada's fault!\n\nDon't blame me,\nFor my son Stan,\nHe saw the darn cartoon,\nAnd now he's off to join the Klan!\n\nAnd my boy Eric once,\nHad my picture on his shelf,\nBut now when I see him, he tells me to fuck myself!\n\nWell, blame Canada!\n\nBlame Canada!\n\nIt seems that everything's gone wrong,\nSince Canada came along!\n\nBlame Canada!\nBlame Canada!\n\nThey're not even a real country anyway.\n\nMy son could have been a doctor or a lawyer, rich and true,\nInstead, he burned up like a piggy on a barbecue!\n\nShould we blame the matches?\nShould we blame the fire?\nOr the doctors who allowed him to expire?\n\nHeck, no!\n\nBlame Canada!\nBlame Canada!\n\nWith all their hockey hullabaloo,\n\nAnd that bitch Anne Murray too!\n\nBlame Canada!\nShame on Canada!\nFor...\nThe smut we must cut,\nThe trash we must bash,\nThe laughter and fun,\nMust all be undone,\nWe must blame them and cause a fuss,\nBefore somebody thinks of blaming us!	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
73	Closer To The Heart (Live)	6	And the men who hold high places\nMust be the ones who start\nTo mold a new reality\nCloser to the heart\nCloser to the heart\nThe blacksmith and the artist\nReflect it in their art\nThey forge their creativity\nCloser to the heart\nYes, closer to the heart\nPhilosophers and ploughmen\nEach must know his part\nTo sow a new mentality\nCloser to the heart\nYes, closer to the heart, yeah\nOh\nWhoa-whoa, you can be the captain\nAnd I will draw the chart\nSailing into destiny\nCloser to the heart\nCloser to the heart\nWell, closer to the heart, yeah\nCloser to the heart\nCloser to the heart\nI said closer to the heart\nWell, closer to the heart, yeah\nCloser to your heart\nCloser to your heart\nWhoa-oh-oh	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
80	Buckingham Green (Live)	6	\nLetras\nA child without an eye\nMade her mother cry\nWhy ask why?\nShe kept her child clean\nOn Buckingham Green\nThe children saw the eye\nAs a sign from God\nDescending from the sky\nIt was alright to dream\nOf Buckingham Green\n"Summon the queen"\nSpoke of the child of eye\nIt's time to fly\nTurning fire to steam\nOn Buckingham Green\nA child without an eye\nMade her mother cry\nWhy ask why?\nShe kept her child clean\nOn Buckingham Green	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
74	Colorado Farm (Live)	6	This ol' world is getting to me.\nThere's just no trust, no 'tegridy.\nSo I loaded up the kids, took my wife by the arm,\nAnd I moved on out to a Colorado farm.\n\nNow it's early to bed, early to rise.\nThe crops are plowed and it's no surprise\nCity folks are fightin' and I don't give a darn (darn, darn)\n'Cause I make my livin' on a Colorado farm.\n\nI gotta drive the tractor, gotta cut the grass\nChut-chut goes the baler like it's never gonna last\nThere's food in the kitchen and there's bud in the barn (barn, barn)\nThat's life livin' on a Colorado farm.\n\nIce-cold beer, pickup truck. Country music, listin' shit.\nWe got tegridy to keep us warm.\nThat's what you get on a Colorado farm.\nAnd I'm gonna stay on a Colorado farm.\n\nShit....\n\nIce-cold beer, down-home days\nCountry music and bike parades\nWe got Tegridy all around (round, round)\nThat's life livin' in our Colorado town.\n\nWe don't need nothing from big corporations\nWe don't need progress or fancy educations\nMaybe our tegridy keeps us down (down, down)\nBut that's life livin' in our Colorado town.\n\nNow we gotta learn to live without boxes every day\nWe might wake up tomorrow and wonder why they went away\nGuess you might call us a bunch of white trash hicks (hicks, hicks)\nBut at least we ain't suckin' no Bezosian dicks.	https://music.youtube.com/watch?v=6a37aaVyYUs
75	Gay Fish (Live)	6	Yo, uhh\nUhh, come on\nI've been so lonely, girl\nI've been so sad and down\nCouldn't understand why haters joked around\nI wanted to be free\nWith other creatures like me\nAnd now I got my wish\nCause I know that I'm a gay fish, gay fish\n(Gay fish, yo')\nMotherfucking gay fish, gay fish\n(I'm a fish, yo')\nGoing on a gay fish, gay fish\n(It's alright, girl)\nMakin' love to other gay fish, gay fish\n\nUhh\nOn these lonely nights at the grocery store\nIn the frozen fish aisle, feeling like a whore\nCause I wasn't bein' true, you know everyone said\nThat I had to make a switch\n(Gay fish)\nNow I know that I'm a gay fish, gay fish\n(Gay fish, yo')\nMotherfucking gay fish\n(I'm, I'm a fish, yo')\nGoing on a gay fish, gay fish\n(Yeah, now where I belong, girl)\nMakin' love to other gay fish, gay fish\n\nI used to be scared, denying who I was\nActin' straight, but then goin' out to the gay fish clubs\nDancin' with the mullets,\nMakin' out with all the snappers\nI take that salmon home and work that coddle fin for hours\n\nBut now I'm out and I'm free to love what I want\nBe it yellowfin or bass or them trout in Vermont\nI slap that Marlin ass,\nMake that grouper butt shake\nI come to your house and have an orgy\nIn your motherfucking fish tank, fish tank\nMotherfucking gay fish, gay fish\n(I'm, I'm a fish, yo')\nGoing on a gay fish, gay fish\n(Yeah, now where I belong, girl)\nMakin' love to other gay fish, gay fish\n\nI really get around\nI'm a slut of the sea\nWhen I say I got crabs, I mean it literally\nI was eating dinner and just had to go down\nOn the Mackerel on the dish\n'Cause I'm the gayest of the gay fish,\nGay fish, gay fish\nMotherfucking gay fish, gay fish\n(I'm, I'm a fish, yo')\nGoin' on a gay fish, gay fish\n(Yeah, now where I belong, girl)\n\nBut I got to settle down, I can't be a whore\nI ain't gonna' just sleep with any fish no more\nI found me a lover, a brother\nWho's a cross-dressing pike named Trish\nAnd together we are gay fish, gay fish\n(Gay fish, yo')\nMotherfucking gay fish, gay fish\n(I'm, I'm a fish, yo')\nGoing on a gay fish, gay fish\n(Yeah, now where I belong, girl)\nMakin' love to other gay fish, gay fish	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
78	Let's Fighting Love (Live)	6	素晴らしいチンチンもの\n金玉の髪ある\nそれの音　サルボボ？\nいいえ！忍者がいます\n\nHey Hey Let's Go! 喧嘩する\n大切な物を protect my balls\n僕が悪い so let's fighting\nLet's fighting love...\nLet's fighting love…\n\nこの歌ちょっと馬鹿\n訳が分からない\n英語がメチャクチャ\n大丈夫 we do it all the time \n\nHey Hey Let's Go! 喧嘩する\n大切な物を protect my balls\n僕が悪い so let's fighting\nLet's fighting love...\nLet's fighting love…\n\nたーたー狸の金玉は\n風に吹かれてぶらぶら\nたーたー狸の金玉は\n風に吹かれてぶらぶら \n\nHey Hey Let's Go! 喧嘩する\n大切な物を protect my balls\n僕が悪い so let's fighting\nLet's fighting love...\nLet's fighting love... 	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
76	The Mollusk (Live)	6	\nLetras\nHey little boy, whatcha got there?\nKind sir it's a mollusk i've found\nDid you find it in the sandy ground?\nDoes it emulate the ocean's sound?\nYes I found it on the ground\nEmulating the ocean's sound\nBring forth the mollusk cast unto me\nLet's be forever let forever be free\nHey little boy come walk with me\nAnd bring your new found mollusk along\nDoes it speaketh of the trinity\nCan it gaze at the sun with its wandering eye\nYes it speaks of the trinity\nCasting light at the sun with its wandering eye\nBring forth the mollusk, cast unto me\nLet's be forever let forever be free\nYou see there are three things that spur the mollusk from the sand\nThe waking of all creatures that live on the land\nAnd with just one faint glance, back into the sea\nThe mollusk lingers, with it's wandering eye	https://music.youtube.com/watch?v=WHlk7UEOKOw
81	The Ballad of Lemmiwinks (Live)	6	A great adventure is waiting for you ahead.\nHurry onward Lemmiwinks, or you will soon be dead.\nThe journey before you may be long and filled with woe.\nBut you must escape the gay man's ass, or your tale can't be told.\n\nLemmiwinks, Lemmiwinks, Lemmiwinks, Lemmiwinks!\n\nLemmiwink's journey is distant, far and vast!\nTo find his way out of a gay man's ass!\nThe road ahead is filled with danger and fright!\nBut push onward Lemmiwinks with all of your might!\n\nThe Sparrow Prince lies somewhere way up ahead!\nDon't look back Lemmiwinks, or you will soon be dead!\nLemmiwinks, Lemmiwinks, the time is growing late. Slow down now, and seal your fate.\n\nTake the magic helmet-torch to help you light the way,\nthere's still a lot of ground to cross inside the man so gay!\nAhead of you lies adventure, and your strength still lies within!\nFreedom from the ass of doom is the treasure you will win!\n\nLemmiwinks came to the stomach dark....\nNear the depths of the lungs and heart...\n\nCatatafish of the stomach's cove!\n\nCatatafish's riddle will soon be told!\n\nLemmiwinks has made it out, his tale is nearly through!\n\nNow that you're the Gerbil king has more adventures to go on!\nFly away to faraway lands and to the setting sun!\nSo many enemies and battles yet to fight!\nFor Lemmiwinks the Gerbil King's tale is told throughout the night!\n\nLe-Le-Lemmiwinks Lemmiwinks Lemmi-Lemmiwinks Lemmiwinks, Lemm-Le-Lemmiwinks, Gerbil King.	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
30	La Resistance	2	Gregory:\n\nGod has smiled upon you this day\nThe fate of a nation in your hands\nAnd blessed be the children we,\nWho fight with all our bravery\n'Til only the righteous stand.\nYou see the distant flames, they bellow in the night\nYou fight in all our names for what we know is right\nAnd when you all get shot, and cannot carry on\nThough you die, La Resistance lives on.\n\nGregory and the Other Children:\nYou may get stabbed in the head with a dagger or sword,\nYou may be burned to death, or skinned alive, or worse\nBut when they torture you, you will not feel the need to run\nFor though you die, La Resistance lives on.\n\nM.A.C.:\n\nBlame Canada! Blame Canada!\n\nSheila:\n\nBecause the country's gone awry, tomorrow night these freaks will fry!\n\nSoldiers:\n\nTomorrow night,\nOur lives will change!\nTomorrow night,\nWe'll be entertained!\nAn execution!\nWhat a sight!\nTomorrow night!\n\nSatan:\n\nUp there, there is so much room, where babies burp and flowers bloom\nTomorrow night, up there is doomed, and so I will be going soon!\n\nTerrance and Phillip:\n\nShut your fucking face, Uncle Fucka!\nYou're a boner-biting bastard, Uncle Fucka!\n\nTerrance:\n\nLooks like we may be out of luck!\n\nPhillip:\n\nTomorrow night, we're pretty fucked!\n\nStan and Kyle:\n\nWhy did our mothers start this war? What the fuck are they fighting for?\nWhen did this song become a marathon?\n\nSatan:\n\nI want to be up there…\n\nSheila:\n\nWhen Canada is dead and gone, there'll be no more Celine Dion!\n\nGregory:\n\nThey may cut your dick in half,\n\nSoldiers:\n\nTomorrow night,\n\nGregory:\n\nAnd serve it to a pig.\n\nSoldiers:\n\nOur lives will change!\n\nGregory:\n\nAnd though it hurts, you'll laugh.\n\nSoldiers:\n\nTomorrow night,\n\nGregory:\n\nAnd you'll dance a dickless jig.\n\nSoldiers:\n\nWe'll be entertained!\n\nGregory:\n\nBut that's the way it goes!\n\nSoldiers:\n\nAn execution!\n\nGregory:\n\nIn war, you're shat upon! Though you die...\n\nSatan:\n\nI want to be... up...\n\nGregory:\n\n...La Resistance…\n\nStan, Kyle, Cartman:\n\nTomorrow we fight, for La Resistaaance!\n\nGregory:\n\n...Lives on!!\n\nSoldiers:\n\nTomorrow night! Tomorrow night! Tomorrow night!\n\nM.A.C.:\n\nJust don't cry out, "Bring your noose!" Blame Canada! Blame Canada! Blame Canada!\n\nSatan:\n\nUp thereeeee!	[NOT AVAILABLE IN STREAMING SERVICES]
32	I Can Change	2	Saddam:\n\nSome people say that I'm a bad guy\nThey may be right, they may be right.\nBut its not as if I don't try\nI just fuck up. Try as I might.\n\nBut I can change, I can change.\nI can learn to keep my promises, I swear it.\nI'll open up my heart and I will share it.\nAny minute now I will be born again.\n\nYes I can change, I can change.\nI know I've been a dirty little bastard.\nI like to kill, I like to maim, yes, I'm insane, but it's okay 'cause I can change.\n\nIts not my fault that I'm so evil\nIt's society, society.\nYou see, my parents were sometimes abusive\nAnd it made a prick of me.\n\nBut I can change, I can change!\nI can learn to keep my promises, I know it!\nI'll open up my heart and I will show it...\nAny minute now I will be born again!\n\nSatan:\n\nBut what if you never change?\nWhat if you remain a sandy little butthole?\n\nSaddam:\n\nHey Satan! Don't be such a twit.\nMother Teresa won't have shit\n\nOn me!\nJust watch, just watch me change here I go I'm changing!!!\n\nHeeeeeeey Satan!	[NOT AVAILABLE IN STREAMING SERVICES]
79	When I Was On Top Of You (Live)	6	She'll never know, what she meant to me\nWhenever I was with her, I was always as gentle as I could be\nAnd now I don't know why, but she's gone away\nAnd I'll just have to stand on my own two legs\nYour eyes, your smile\nMade my little life worthwhile\nThere's was nothing I couldn't do\nWhen I was on top of you\nI'd pull her hair, she'd know to stop\nAnd when she'd look behind her, I'd always be there\nAnd now I don't know why, but she, she's gone\nAnd all I can do is, try to carry on\nYour eyes, your smile\nMade my little life worthwhile\nThe sky was a lot more blue\nWhen I was on top of you\nWhen I was on top of you	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
84	Boogers & Cum (Live)	6	So you're one of the Yelpers' special blessed\nYou demand a restaurants' very best\nWell, they're gonna treat you special\nI'm telling you, chum\nNow get yourself ready for some boogers and cum\n\nBoogers and cum\nBoogers and cum\n\n(Boogers and cum) That's called "The Yelper special"!\n(Boogers and cum) Say, what's that on your pretzel?\n(Ooh-ooh-ooh-ooh) Your online critiques are real useful to some\nNow have a good time eating boogers and cum\n\n(Boogers and cum) Someone farted on your salad\n(Boogers and cum) But your decor critiques are valid\n(Ooh-ooh-ooh-ooh) You think you're special like you're A-number one\nWell, there's a whole lot of special in boogers and cum\n\n(Boogers and cum) How 'bout some feces with your flounder?\n(Boogers and cum) You like that queefy quarter pounder?\n\n(Ooh-ooh-ooh-ooh) What's that spice that feels tangy on my tongue?\nWaiter:\nOh, that's the yuzu pepper, along with some boogers and cum.\n\nHere you are, sir.\n\nThank you, David, that's good service.\n\nI will bring you food every day, my friend.\n\nMmm, is that a Jalapeño cream sauce?\n\nYes, my father made it just for you.\n\nHmm, it's tart, but savory.\n\n(Boogers and cum) Being a food critic's easy!\n(Boogers and cum) Oh, you feel a little queasy?\n(Ooh-ooh-ooh-ooh) Do you need a diagnosis? Well, the doctor's got one\n\n(Boogers and cum) Piss in your potatoes\n(Boogers and cum) Some guys' shit on your tomatoes\nAlright, fancy food critics, looks like you've won\nNow please enjoy all the\nBoo-oo-oogers\nBoo-oo-oo-oo-oogers\nAnd cum (Boogers and cum)	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
85	America, Fuck Yeah/America Medley (Live)	6	America\nAmerica\nAmerica, fuck yeah!\nComing again, to save the mother fucking day yeah!\nAmerica, fuck yeah!\nFreedom is the only way yeah!\nTerrorists your game is through cause now you have to answer to\nAmerica, fuck yeah!\nSo lick my butt, and suck on my balls\nAmerica, fuck yeah!\nWhat you gonna do when we come for you now\nIt's the dream that we all share, it's the hope for tomorrow\n\nFuck yeah!\n\nMcDonalds, fuck yeah!\nWal-Mart, fuck yeah!\nThe Gap, fuck yeah!\nBaseball, fuck yeah!\nNFL, fuck, yeah!\nRock and roll, fuck yeah!\nSlavery, fuck yeah!\n\nAmerica, fuck yeah!\n\nAmerica, fuck yeah!\n\nStarbucks, fuck yeah!\nDisney World, fuck yeah!\nPorno, fuck yeah!\nFake tits, fuck yeah!\nSushi, fuck yeah!\nTaco bell, fuck yeah!\nRodeos, fuck yeah!\nChicken nuggets, fuck yeah!	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
83	What Would Brian Boitano Do? (Live)	6	Fight! Skate! Fight! Skate!\nFight! Skate! Fight! Skate!\n\nWhat would Brian Boitano do if he was here right now?\nHe'd make a plan, and he'd follow through\nThat's what Brian Boitano'd do!\n\nWhen Brian Boitano was in the Olympics skating for the gold\nHe did two Salchows and a triple Lutz wearing a blindfold\nWhen Brian Boitano was in the Alps fighting grizzly bears\nHe used his magical fire breath and saved the maidens' fair\n\nFight! Skate! Fight! Skate!\n\nSo what would Brian Boitano do if he was here today?\nI'm sure he'd kick an ass or two, that's what Brian Boitano'd do!\n\nFight! Skate! Fight! Skate!\n\nWhen Brian Boitano traveled through time to the year 3010,\nHe fought the evil robot king and saved us all again\nAnd when Brian Boitano built the pyramids, he beat up Kubla Khan\n'Cause Brian Boitano doesn't take shit from anybody!\n\nNo, Brian! Those chicken wings are really spicy! Don't eat those!\nI've never seen a man eat so many chicken wings\nI've never seen a man eat so many chicken wings\nI've never seen a man eat so many chicken wings\n(Aah!) I've never seen a man eat so many chicken wings!\n(Aah!) I've never seen a man eat so many chicken wings!\n(Aah!) I've never seen a man eat so many chicken wings!\n(Aah!) I've never seen a man eat so many chicken wings!\n\nFight! Skate! Fight! Skate!\n\nBrian Boitano was born on the planet of Kryluck\nHe came to earth to save us all from war and death and such\nHi de lo de, hi de lay, Brian Boitano's here!\nSo round up all your lasses, and tell them to have no fear\n\nSay, come over here, my honey\nAnd you're gonna take off my pants\nAnd I'm gonna make dirty love to you\n'Cause that's what Brian Boitano'd do\n'Cause that's what Brian Boitano'd do!	https://music.youtube.com/playlist?list=OLAK5uy_k-XClxCE8I4WTQ97MNO_t652ccER6d958
11	No Substitute	1	Nobody could take your place\nNo way they could match your face\nNo, you got it going on in a way so clear\nI just wanna buy you a beer\nOr maybe tonight at seven thirty or something\nI could er... come and er... pick you up in my car\n(No substitute) No substitute for you,\n(No substitute) No baby there's...\n(No substitute) for you girl\n(No substitute) for you now\nYou know that it's true\n(Not substitute) There's just no substitute for you.	https://music.youtube.com/watch?v=iNILtByf68M
26	Blame Canada	2	Sheila:\n\nTimes have changed,\nOur kids are getting worse!\nThey won't obey their parents,\nThey just want to fart and curse!\n\nSharon:\n\nShould we blame the government?\n\nLiane:\n\nOr blame society?\n\nRandy, Gerald, and Stuart:\n\nOr should we blame the images on TV?\n\nSheila:\n\nNo, blame Canada!\n\nEveryone:\n\nBlame Canada!\n\nSheila:\n\nWith all their beady little eyes,\nAnd flapping heads so full of lies!\n\nEveryone:\n\nBlame Canada!\nBlame Canada!\n\nSheila:\n\nWe need to form a full assault!\n\nEveryone:\n\nIt's Canada's fault!\n\nSharon:\n\nDon't blame me,\nFor my son Stan,\nHe saw the darn cartoon,\nAnd now he's off to join the Klan!\n\nLiane:\n\nAnd my boy Eric once,\nHad my picture on his shelf,\nBut now when I see him, he tells me to fuck myself!\n\nSheila:\n\nWell, blame Canada!\n\nEveryone:\n\nBlame Canada!\n\nSheila:\n\nIt seems that everything's gone wrong,\nSince Canada came along!\n\nEveryone:\n\nBlame Canada!\nBlame Canada!\n\nCopy Shack Employee:\n\nThey're not even a real country anyway.\n\nCarol:\n\nMy son could have been a doctor or a lawyer, rich and true,\nInstead, he burned up like a piggy on a barbecue!\n\nEveryone:\n\nShould we blame the matches?\nShould we blame the fire?\nOr the doctors who allowed him to expire?\n\nSheila:\n\nHeck, no!\n\nEveryone:\n\nBlame Canada!\nBlame Canada!\n\nSheila:\n\nWith all their hockey hullabaloo,\n\nLiane:\n\nAnd that b**** Anne Murray too!\n\nEveryone:\n\nBlame Canada!\nShame on Canada!\nFor...\nThe smut we must cut,\nThe trash we must bash,\nThe laughter and fun,\nMust all be undone,\nWe must blame them and cause a fuss,\nBefore somebody thinks of blaming us!	[NOT AVAILABLE IN STREAMING SERVICES]
29	Up There	2	Sometimes I think, when I look up real high\nThat there is such a big world up there\nI'd like to give it a try\nBut then I sink\n'Cause it is here I'm supposed to stay\nBut I get so lonely down here\nTell me why's it have to be that way?\n\nUp there\nThere is so much room\nWhere babies burp and flowers bloom\nEveryone dreams, I can dream too\n\nUp there\nUp where the skies are ocean blue\nI can be safe and live without a care\nUp there\n\nThey say I don't belong\nI must stay below alone\nBecause of my beliefs\nI'm supposed to stay where evil is sown\n\nBut what is evil anyway?\nIs there reason to the rhyme?\nWithout evil there can be no good\nSo it must be good to be evil sometimes\n\nUp there\nThere is so much room\nWhere babies burp and flowers bloom\nEveryone dreams, I can dream too\n\nUp there\nUp where the skies are ocean blue\nI can be safe and live without a care\nLive without a care\nIf only I could live up there\n\nI wanna live\nI wanna live up\nOoh baby, ooh\nI want to live up there	[NOT AVAILABLE IN STREAMING SERVICES]
33	I'm Super	2	Big Gay Al:\n\nBombs are flying\nPeople are dying\nChildren are crying\nPoliticians are lying too.\n\nCancer is killing\nTexaco's spilling\nThe whole world's gone to hell\nBut how are you?\n\nI'm super\nThanks for asking\nAll things considered\nI couldn't be better I must say\n\nI'm feeling super\nNo, nothing bugs me\nEverything is super when you're\nDon't you think I look cute in this hat\n\nI'm so sorry\nMr. C******\nBut I just can't feel too bad for you right now.\n\nBecause I'm feeling\nSo insanely super\nThat even the fact that you can't walk\nCan't bring me down.\n\nBackground singers:\n\nHe's super\nThanks for asking\nAll things considered\nHe couldn't be better he must say\n\nBig Gay Al:\n\nI'm super\nNo, nothing bugs me\nEverything is super when you're\nDon't you think I look cute in this hat\nThese little pants, this matching tie\nThat I got at Merv's\nI'm super\n\nBackground singers:\n\nIn the barracks and the trenches as well\n\nBig Gay Al:\n\nStick 'em up.\n\nBackground singers:\n\nBig Gay Al says do ask do tell\n\nBig Gay Al:\n\nSkittles\n\nBackground singers:\n\nYes he's super and he's proud to be gay\n\nBig Gay Al:\n\nOK\n\nBackground singers:\n\nEverything is super when you're gay! When you're gay!	[NOT AVAILABLE IN STREAMING SERVICES]
3	Chocolate Salty Balls	1	Two tablespoons of cinnamon,\nand two or three egg whites,\na half a stick of butter, melted.\nStick it all in a bowl baby,\nstir it with a wooden spoon,\nmix in a cup of flour.\nYou'll be in heaven soon.\n\nSay everybody have you seen my balls they're big and salty and brown.\nIf you ever need a quick pick me up, just stick my balls in your mouth.\nOOH! Suck on my chocolate salty balls, stick 'em in your mouth and suck 'em.\nSuck on my chocolate salty balls, they're packed full of vitamins,\nand good for you, so suck on my balls.\n\nPour in a cup of unsweetened chocolate,\nand a half a cup of brandy\nthen throw in a bag or two of sugar,\nand just a pinch of vanilla,\ngrease up the cookie sheet.\n'Cause I hate when my balls stick!\nthen preheat the oven to tree-fiddy, and give that spoon a lick!\n\nSay everybody have you seen my balls they're big and salty and brown.\nIf you ever need a quick pick me up, just stick my balls in your mouth.\nOh! Suck on my chocolate salty balls, put 'em in your mouth and suck 'em.\nSuck on my chocolate salty balls, they're packed full of goodness,\nand high in fiber, so suck on my balls.\n\n(sniff, sniff, sniff)\n\nHey, wait a minute, what's that smell?\nIt smells like something's burning.\nWell, that don't bother me none, as long as I get my rent paid on Friday.\nBaby, you better get back in the kitchen, cause I got a sneakn' suspicion.\nOh man baby, baby, you just burnt my balls.\nMy balls are on fire, come on, my balls are burning, gimme some water pour some water on 'em, o goodness, blow on them, do something\n\nSay everybody have you seen my balls they're big and salty and brown. (They're on fire baby)\nIf you ever need a quick pick me up, just stick my balls in your mouth.\nOOH! Suck on my chocolate salty balls, put 'em in your mouth and suck 'em. (Put 'em out, blow on 'em.)\nsuck on my balls baby,\nsuck on my balls baby,\nsuck on my red hot salty chocolate balls.\nCome on,baby, woo, woo, suck on my balls!\n\n(blow, blow, blow)	https://music.youtube.com/watch?v=7ZBLw-6JAmA
4	Brad Logan	1	California sun has sunk\nBehind the Anaheim Hills, here comes the night\nI was high on junk\nAnd the warm winds of Santa Ana feel all right\n\nWill every crimmin' hood make a bargain with the world\nSeats are successive when you're shot to the curb\nI spend my day in blindness, at night I get my vision\nDodgy, cause there are no one indecision\nCause it's wild, When it's Wild wild wild wild\n\nCalifornia sun has sunk\nBehind the Anaheim Hills, here comes the night\nI was high on junk\nAnd the warm winds of Santa Ana feel all right\n\nI get destructive outside obedience\nI am no longer respected in this new transition\nI put into effect, my long time standard\nDisastrous living, disastrous living!\n\nCause it's wild, When it's Wild wild wild wild\n\nCalifornia sun has sunk\nBehind the Anaheim Hills, here comes the night\nI was high on junk\nAnd the warm winds of Santa Ana feel all right\n\nCause it's wild, When it's Wild wild wild wild\n\nCalifornia sun has sunk\nBehind the Anaheim Hills, here comes the night\nI was high on junk\nAnd the warm winds of Santa Ana feel all right	https://music.youtube.com/watch?v=_bRSZ0m4OtU
5	Come Sail Away	1	(Kyle)\n\nI'm sailing away,\nset an open course for the virgin sea...\n\n(Cartman)\n\nI'm sailing away,\nset an open course for the virgin sea\nI've got to be free,\nfree to face the life that's ahead of me\nOn board, I'm the captain,\nso climb aboard\nWe'll search for tomorrow on every shore\nAnd I'll try, oh Lord,\nI'll try to carry on\n\nI look to the sea,\nreflections in the waves spark my memory\nSome happy, some sad\nI think of childhood friends and the dreams we had\nWe live happily forever, so the story goes\nBut somehow we missed out, on that pot of gold\nBut we'll try best that we can to carry on\n\nA gathering of angels appeared above my head\nThey sang to me this song of hope, and this is what they did\nThey said come sail away, come sail away\nCome sail away with me\nCome sail away, come sail away\nCome sail away with me\nCome sail away, come sail away\ncome sail away with me\nCome sail away, come sail away\ncome sail away with me\n\nI thought that they were angels, but to my surprise\nThey climbed aboard their starship and headed for the skies\n\nSinging come sail away, come sail away\nCome sail away with me\nCome sail away, come sail away\nCome sail away come sail with me\nCome sail away, come sail away\nCome and sail away come sail with me\nCome sail away, come sail away\nCome sail away come sail with me\n\n(Chef)\n\nMake it funky now\nCome sail away, come sail away\nCome sail away with me...\n\n(Cartman)\n\nCome sail away, come sail away\nCome sail away come sail with me\nCome sail away, come sail away\nCome sail away come sail with me\n\nCome sail away... (Cartman singing frantically)\n	https://music.youtube.com/watch?v=prPd0qMuZ3Q
7	Simultaneous	1	Baby, you know, you're the one for me\nAnd all that I want to be is...\n\nYou! And me! And her, simultaneous,\nYou, and me, and you, and you\nSimultaneous lovin', baby, two or three\nSimultaneous, ooh! Come on!\n\nHave an open mind,\nPull my trigger down\nGive me the last, cold turkey brass, make it fast,\nTake my ass to town\nHave an open mind,\nSend my cares away\nRing my bell, ya fat pig, oh well, what the hell,\nToday's your lucky day\n\nYou! And me! and her, simultaneous\nYou, and me, and Winona Ryder\nSimultaneous lovin', baby, two or three\nSimultaneous, ooh! Come on!\n\nHave an open mind,\nIt's a normal thing to do\nDon't be prude, just get nude, oh, you're being rude,\nI would do it for you\nBaby, please have an open mind,\nYou're the only one I love\nThese girls, you see, they don't mean anything,\nLet's all get in the tub!\n\nYou! And me! And her too, simultaneous\nYou, and me, and your momma, and your sister\nSimultaneous lovin', baby, two or three\nSimultaneous, ow! Come on!\n\nEverybody here in the pool!\n\nHave an open mind,\nDon't be so mean to me\nCall your sister, and your mother, and your aunt\nIt's every man's fantasy\nHave an open- Whoa, baby!\nPut that knife away\nDon't be mad, I'll take you back, just relax,\nWe can make love your way\n\nI'm talkin' about you, and me, and some flowers, and some wine, instantaneous!\nYou, and me, and Whitney Houston- On the radio, babe, on the radio!\nSome candles and some good feelings, just the two of us\nOh, fudge it\nNow, I'm talkin' about you, and me! And her, and her, and her, simultaneous!\nYou and me, all the women in the house!\nSimultaneous lovin', three on seven, make it a baker's dozen\nSay the ladies in the house, clap your hands! Woo!\n\nNow, that'd be a party, ladies	https://music.youtube.com/watch?v=3F8aF7Zietc
9	Hot Lava	1	\nMmmm\nBaby, every time that we kiss\nHot Lava!\nEvery time that we make love, hot lava\nHot Lava!\nLava so hot it makes me sweat\nLava so warm and red and wet\nLava!\nBrrrrrrrrrrrr.\nChef Aid: The South Park Album Version\n\nBaby, every time we kiss, Hot Lava\nAnd every time that we make love, that's Lava, Hot Lava\nIt's lava so hot, it makes me sweat\nAnd lava so warm, it's red and wet\n\nMountain is rumbling, We must find a safer place\nSoon half of Pele, Will fall upon your face\nGreat Nectar of the Gods spews far from Pinatabo\nMixed with a Women's Sweat, it makes the Lava we know\nBaby, every time we kiss, Hot Lava\nAnd every time that we make love, that's Lava, Hot Lava\nIt's lava so hot, it makes me sweat\nAnd lava so warm, it's red and wet\n\nBurnin' through the forest, Where Red hot lava flows\nRolls down the islands body, and into the ocean below\nWhen it meets the cool, cool water, there's a big flow of the living\nRich magma flowing into a sobiquious environment, Produces Pillow Lava\nHydrostatic pressure of sea water\nTends to inhabit the vesical size of the basalt\nBaby, every time we kiss, Hot Lava\nAnd every time that we make love, that's Lava, Hot Lava\nIt's lava so hot, it makes me sweat\nAnd lava so warm, it's red and wet\n\nAnd after the eruption, you lay dormant for a while\nLet's just hold each other and talk, For now, Pele sleeps\nBaby, every time we kiss, Hot Lava\nAnd every time that we make love, that's Lava, Hot Lava\nIt's lava so hot, it makes me sweat\nAnd lava so warm, it's red and wet\nBaby, every time we kiss, Hot Lava\nAnd every time that we make love, that's Lava, Hot Lava\nIt's lava so hot, it's red and wet\nAnd lava so warm it makes me sweat.	https://music.youtube.com/watch?v=D3kreKGXPIA
10	Bubblegoose	1	Igo by the name of Wyclef Jean\nWe are the refugee all-stars\nWe salute to soldiers around the world\n\nCartman: Hell, yeah!\n\nThis one's called "Bullet in your Bubblegoose"\n\nCartman: Mac 10!\nKyle: Cartman, this isn't Mac 10!\nCartman: Seriously! Mac 10!\n\nSit right back and hear a tale\nOf a hustler round my way\nWho used to clock around the block\nFrom where my grandma stayed\n\nA black BMW with rims to match\nWindows bullet-proof\nOne night he jumped out the car\nAnd caught a bullet in his Bubblegoose\n\nHe caught a bullet in his Bubblegoose\nHe caught a bullet in his Bubblegoose\nYou can be at a party getting loose\nBut you can catch a bullet in your goose\n \nHe caught a bullet in his Bubblegoose\nHe caught a Bullet in his Bubblegoose\nYou can be at a party getting loose\nBut you can catch a bullet in your goose\n\nSit right back and you hear a tale\nOf a young girl around my way\nWho used to dance around the way\nFrom where my homeboy stayed\n\nBlack BMW with rims to match\nWindows Bullet-proof\nOne night she jumped out the car\nAnd got a Bullet in her Bubblegoose\n\nShe got a bullet in her Bubblegoose\nShe got a bullet in her Bubblegoose\nYou can be at a party getting loose\nBut you can catch a bullet in your goose\n\nShe got a bullet in her Bubblegoose\nShe got a bullet in her Bubblegoose\nYou can be at a party getting loose\nBut you can catch a bullet in your goose\n\nCartman: Mac 10 you guys!\nKyle: This isn't Mac 10, Cartman!\nCartman: It is Mac 10!\n\nCartman: Kenny! Your family's poor, Kenny! Get up, Kenny! Kenny! Your dad's an alcoholic!\nKenny: (Fuck you, Cartman!)\n\nCartman: Yeah, Mac 10 in the big house you guys!\nKyle: Cartman, you're ruining the song.\nCartman: Fuck you guys!\n\nShe got a bullet in her Bubblegoose\nShe got a bullet in her Bubblegoose\nYou can be at a party getting loose\nBut you can catch a bullet in your goose\n\nShe got a bullet in her Bubblegoose\nShe got a bullet in her Bubblegoose\nYou can be at a party getting loose\nBut you can catch a bullet in your goose\n\nCartman: Bubblegoose you guys!\nKyle: Damn that's high, dude.\nCartman: 'Mac 10!\n\nThis one's for the People\n\nCartman: Hell yeah. 	https://music.youtube.com/watch?v=GOrKAWrL0bo
12	Wake Up Wendy	1	Got this bug-eyed girl\nCold hand on my knee\nFrozen teeth, chitter, chatter\nShe's dressed up like a cemetery\nLike a cemetery\n\nSnowbound all winter\nBlue lips on my cheek\nLittle tongues, prattlin', rattlin'\nTalkin' about them hometown geeks\nThem hometown geeks\n\nWake up Wendy, smell the coffee\nHelp me into your custom kitchen\nGimme a cup of that old black magic\nI wanna get me some of that old home cookin'\nCan you feel it, it's chilly and a freezin'\nWake up Wendy, moods a changin'\nI got a reason and you got a feelin'\nWake up Wendy, love's in season\n\nFeels like a steam clean\nWhen she washes me\nClouds a bustin', pumps a hissin'\nJust peel me off the ceiling\nOff the ceiling\n\nChill out bug-eyed-girl\nZap me into cinders\nPop the thermal mumbo jumbo\nMelt me with your little fingers\nWith little fingers\n\nWake up Wendy, smell the coffee\nHelp me into your custom kitchen\nGimme a cup of that old black magic\nI wanna get me some of that old home cookin'\nCan you feel it, it's chilly and a freezin'\nWake up Wendy, moods a changin'\nI got a reason, you got a feelin'\nWake up Wendy, love's in season\nWake up Wendy, love's in season\nWake up Wendy, love's in season	https://music.youtube.com/watch?v=T3m6Whj9qik
14	Huboon Stomp	1	Well, I'm a huboon baby\nI'm a cross between a human and an ape\nI'm all decked out\nI'm gonna hoot, I'm gonna root, I'm gonna rape\n\nPeople look at me and laugh and make fun of my face\nI laugh right back\nI don't want to be part of the human race\nI did it to myself\nNow somebody's gonna be sorry\n\nWell, I'm a huboon baby\nGonna mess around with all you fools\nI'm all pumped up, gonna romp, bone and stomp\nI'm gonna rule\n\nI had the operation\nNothing else left to do\nWell lookit here, I've been hurt\nGonna hurt you\n\nNow, somebody's gonna be sorry\nLike all you wankers and you slime\nAnd you right-wing pinheads\nWho make screwing a big crime\nYou titty-twisted up my life\nAnd pissed on all my dreams\nYou made me hate myself\nNow come on shoot me\nSet me free\n(Let's go!)\n\nHe's a Huboon Baby, he's really all fudged up! (x4)\n\nI did it to myself\nNow somebody's gonna be sorry\n\nWell, I'm a huboon baby\nI'll grow up to be the president\nI'm upside-in, I'm really tweaked\nI'm really freaked, I'm really bent\nBig town mommas better hurry\nHide your little girls\nI'll jump their bones\nI'll sniff 'em out 'round the world\n\nNow somebody’s gonna be sorry\nLike all you wankers and you slime\nAnd you right-wing pinheads\nWho make screwing a big crime\nYou titty-twisted up my life\nAnd pissed on all my dreams\nYou made me hate myself\nNow come on, shoot me, set me free\n\nI’m a huboon baby\nI’m a cross between a human and an ape\nWell, I’m all decked out\nI’m gonna hoot, I’m gonna root, I’m gonna rape\n\nPeople look at me\nAnd laugh and make fun of my face\nI laugh right back\nI don’t want to be part of the human race	https://music.youtube.com/watch?v=WYWJHeZhFd4
15	Love Gravy	1	MMmmmmmmmmmmmmm!!\nMake Love!\n\nGonna make love to you woman,\ngonna lay you down by the fire,\nand caress your womanly body make you moan and prespire,\nI'm gonna get those juices flownin,\n\nMakin love gravy\nlove gravy love gravy love love love,\n\nGonna make love to you woman,\ngonna lay you down by the fire,\nand caress your womanly body make you moan and prespire,\nI'm gonna get those juices flownin,\n\nMakin love gravy\nlove gravy love gravy love love love,\n\nOwe,\nOpen up a packet of my gravy,\nBaby it's burnin' just for you child,\nwould you like another helping of gravy,\nsay yeah, yeah, yeah, yeah\n\nWatch out, don't let it get in your eyes now!!!\n\nGonna make love to ya' woman\ngonna get a little freaky to,\nwith langeray of leather and a bottle of super glue,\nlet's make a human prezel dip it in\nlove gravy, love gravy, love love love\n\nOpen up a packet of my gravy,\nBaby it's burn in' just for you child,\nwould you like another helping of gravy,\nbaby say yeah, yeah, yeah, yeah\n\nsay yeah, say yeah, say yeah babe\n\nC'mon\n\nI like to....\n\nSay yeah, yeah, yeah, Sure yeah\n\nI'm gonna climb into your cockpit,\nI'm gonna get those rockets firing,\nBlast you into orbit,\nand burn out all your wiring,\nget our asses on the launchpad makin',\nlove gravy, love gravy love love love,\n\nYeah,\n\nOpen up a packet of my gravy,\nBaby its burnin' just for you child,\nwouldn't you like another helping of gravy,\nbaby say yeah, yeah, yeah, yeah\n\nI got a whole look a gravy left baby,\nOh, those are nice,\nwould you like some gravy on those,\nthere's enough gravy to go around for everybody,\n\nOhhhh,\nI'm gonna drown all you b****** in gravy.\n\nChef:\nOh come on Rick, you don't drown b******, dummy, that's not cool!! 	https://music.youtube.com/watch?v=0svA3wcVmBM
18	Tonight is Right for Love	1	\n\nChef:\nTonight is right for love, you know I\nWanna touch you where the lights don't go\nTonight is right for love (with Meredith Baxter-Birney)\n\nExpressing love so sweet,\nI'll keep you burning like a dog in heat\nTonight is right for love (with Meredith Baxter-Birney)\n\nWe had a love that was so magical\nWith Meredith Baxter-Birney burning, burning in my soul\nI'm not talking about Meredith Baxter-Birney today, no\nI'm talking about Meredith Baxter-Birney that was on Family Ties two years ago\n\nMeat Loaf:\nAfter the love comes a darkness in hell,\nA demon inside you like a bottomless well\nNothing is safe and everything is a lie\nLove doesn't last, no matter how hard you try\nBurnin', burnin', through your brain\nI think I'm insane...\n\nChef:\nMeat\n\nMeat Loaf:\nBut when you finally realize that it's all in vein\n\nChef:\nMeat Loaf\n\nMeat Loaf:\nSplinters of wood, they can be forced through your eyes\n\nChef:\nMeat Loaf!!!\n\nMeat Loaf:\nCheese graters of steel being rubbed in your thighs\nYour skin is comin' off and you rollin' in salt!\n\nChef:\nMeat!!! Hey Meat! Meat Loaf!!!\n\nMeat Loaf:\nWhat?\n\nChef:\nWhere are you goin' son?\n\nMeat Loaf:\nOh... gosh...\n\nChef:\nCome back to us, we're over here\n\nMeat Loaf:\nOK, oh, sorry Chef, man. Sorry.\n\nChef:\nIt's alright son, but this song is about Meredith Baxter-Birney,\nnot about splinters of wood in your eyes, you need to calm down man.\n\nMeat Loaf:\nYou're right\n\nChef:\nHere, have a taco\n\nMeat Loaf:\nTaco, great, I need a taco\n\nChef:\nYou're messing up my business with Meredith Baxter-Birney. OK?\n\nMeat Loaf:\nYeah, great\n\nChef & Meat Loaf:\nTonight is right for love\nThe rain is fallen and Jay Leno is on\nLet's turn down the lights, turn up the volume\nAnd go crazy\nI'll touch your body and soul\nAnd change the channels with remote control\n'Cause tonight is right for love with Meredith Baxter-Birney	https://music.youtube.com/watch?v=rG5KT_KOq-s
19	It's a Rockin' World	1	Well it's a rockin' world, make no mistake about it\nIt's a shockin' world, could be what's so great about it\nIt's a rockin' world, there ain't nothin' fake about it\n\nWhoa, whoa, now welcome to this Earth, bro\nWhoa, whoa, we're tryin' to find an answer\nWhoa, whoa, we got a surface module and a belly-dancer\n\nOn the sidewalk earth, a boy is tryin' to show a girl what he is worth\nBoth arms in plaster, but he's still gonna\nGo right up and ask her\n\nWhy is it barbaric, is it biological?\nWhy is it frenetic, is it asophysiological?\nIt's an epidemic, there's nothing logically logical, logical, logical\n\nNow, why do babies cry?\nI asked a crow today but all he did was fly and he took the cynic way\nThe laws of chaos, left us all in disarray\n\nNow take the bumblebee, a lousy rotten bum\nNot a shred of money just a lazy buzzin' hum\nHe takes all our honey and now the Garden of Eden has got to pay, that's who.\n\nWell we go, back to base\nCan't make no head or tale of this place\nBut home we're returnin' back to base, base\n\nCan we be notified when love comes of age\nDoes the cell divide in the initial phase\nIt's all codified in the DNA stage	https://music.youtube.com/watch?v=7NrSLcAkZyU
43	Mr. Hankey, the Christmas Poo	3	We've all heard of Rudolph and his shiny nose\nAnd we all know Frosty whose made out of snow\nBut all of those stories seem kind of... gay\nCuz we all know who brightens up our holiday\n\nMr. Hankey the Christmas Poo\nSmall and brown he comes from you\nSit on the toilet here he comes\nSqueeze him between your festive buns\n\nA present from down below\nSpreading joy with a "howdy ho"\nHe's seen the love inside of you\nCuz' he's a piece of poo\n\nSometimes he's nutty\nSometimes he's corny\nHe can be brown or greenish-brown (Mmm Mmm)\nBut if you eat fiber on Christmas Eve he might come to your town.\n\nMr. Hankey the Christmas Poo\nHe loves me I love you\nTherefore vicariously he loves you\n\nBradley:\n\nI can make a Mr Hankey too!\n(fart noise)\n\nCartman:\n\nWell Kyle where is he?\n\nKyle:\n\nHe's comin'\n\nStan:\n\nC'mon dude push!\n\nKyle:\n\nI'm trying!\n\nCartman:\n\nOh wait wait I can see his head!\n\nKyle:\n\nHERE HE COMES!!\n(fart noise)\n\nMr. Hankey:\n\nHOWDY HO!\nI'm Mr. Hankey the Christmas Poo\nSeasons greetings to all of you\n\nLet's sing songs and dance and play\nNow before I melt away\nHere's a game I like to play\nStick me in your mouth and try to say\n\nHowdy ho ho yum yum yum\nChristmas time has come!\nSometimes he's runny\nSometimes he's firm\n\nSometimes he's practically water\nSometime he hangs off the end of your ass\nand won't fall in the toilet\nCuz he's just clinging to your sphincter\n\nand he won't drop off and so you\nshake your ass around and try to get it to drop in the toilet\nand finally it does\n\nMr. Hankey the Christmas Poo\nWhen Christmas leaves he must leave too\nFlush him down but he's never gone\nHis smell and his spirit lingers on....\nHowdy ho!	https://music.youtube.com/watch?v=9SV7wNfYf-8
46	Dead, Dead, Dead	3	Juan Schwartz:\n\nDead, dead, dead.\nSomeday you'll be dead.\nDead, dead, dead.\nSomeday we'll all be dead.\n\nThe minute we're born we start dying,\nWe die a little more every day.\nYoung or old, rich or poor,\nThere's nothing we can do to stop it.\n\nSo look long at that Christmas tree,\nIt may be the last one that you see.\nDecorate your house in green and red\n'Cause someday you'll be dead.\n\nTogether:\n\nDead, dead, dead.\nSomeday you'll be dead.\nDead, dead, dead.\nSomeday we'll all be dead.\n\nJuan Schwartz:\n\nIt might happen in a couple of months\nOr fifty years from now.\nBut no matter when it happens,\nIt will seem too soon to you.\n\nSo be sure on Christmas Eve,\nWhen you snuggle into bed\nThat you thank God for your family\n'Cause someday they'll be dead.\n\nTogether:\n\nDead, dead, dead.\nSomeday they'll be dead.\nDead, dead, dead.\nSomeday we'll all be dead.\n\nJuan Schwartz:\n\nWho knows how many Christmases\nAre left in their short lives.\nNobody knows, that's my point!\nEnjoy it while you can.\n\nAnd so on Christmas morning,\nLet good tidings fill your head.\nWhat a festive season,\nSomeday you'll be dead.\n\nTogether:\n\nDead, dead, dead.\nSomeday we'll be dead.\nDead, dead, dead.\n\nJuan Schwartz:\n\nEveryone you know...\n\nTogether:\n\nDead.\n\nJuan Schwartz:\n\nA very merry Christmas to you.\n\nTogether:\n\nDead, dead, dead...\n\nSouth Park Children's Choir:\n\nMerry Christmas everybody!	https://music.youtube.com/watch?v=HlhBPVOknBI
47	Carol of the Bells	3	Uh Hark hear the Bells,\nSweet Silver Bells\nall seem to say\nDing Dong M'kay\n(Ding Dong, Ding Dong, Ding Dong)\n\nChristmas is here\nBringing good cheer\nto young and old\nmeek and the bold,\n(Ding Dong, Ding Dong)\n\nDing Dong Ding Dong\nthat is their song\nwith joyful ring\nall caroling\n(Ding Mm'kay)\n\nOne seems to hear\nwords of good cheer\nfrom everywhere\nfilling the air\n(Oh well nearly there ringing while Gaily is singing)\n\nOh how they bound\nraising the sound\nOh here and now\ntelling their tale,\n\nGaily they ring\nwhile people sing\nsongs of good cheer\nChristmas is here,\n(Merry, Merry, Merry, Merry Christmas, Merry, Merry, Merry, Merry Christmas)\n\n(Ding Dong)\nDing Dong, Ding Dong,\nthat is their song\nwith joyful ring\nall caroling'\n\nOn on they send\non without end\ntheir joyful tone\nto every home\n\nHark hear the Bells,\nSweet Silver Bells\nall seem to say\nDing Dong M'kay\n\nOn on they send\non without end\ntheir joyful tone\nto every home\n\nDing Dong Ding Dong\nM'kay M'kay M'kay M'kay M'kay.	https://music.youtube.com/watch?v=rR2MX31uwO0
48	The Lonely Jew on Christmas	3	Kyle:\n\nIt's hard to be a Jew on Christmas\nMy friends won't let me join in any games\nAnd I can't sing Christmas songs or decorate a Christmas tree\nOr leave water out for Rudolph 'cause there is something wrong with me\nMy people don't believe in Jesus Christ's divinity!\n\nI'm a Jew\nA lonely Jew\nOn Christmas.\n\nHanukkah is nice, but why is it\nThat Santa passes over my house every year?\nAnd instead of eating ham, I have to eat kosher latkes\nInstead of Silent Night, I'm singing "Huhash Dogavish"\nAnd what the fuck is up with lighting all these fucking candles? Tell me, please!\n\nI'm a Jew\nA lonely Jew\nI'd be merry\nBut I'm Hebrew\nOn Christmas.\n\nSpecial Celebrity Guest:\n\nHey, little boy, I couldn't help but hear\nYou're feeling left out of Christmas cheer\nBut I've come to see that you shouldn't be sad\nThis is the one month that you should be glad.\n\nCause it's nice to be a Jew on Christmas\nYou don't have to deal with the season at all\nDon't have to be on your best behavior or give to charity\nYou don't have to go to grandma's house with your alcoholic family.\n\nKyle:\n\nAnd I don't have to sit on some fake Santa's lap and have him breathe his stinky breath on me!\n\nSpecial Celebrity Guest:\nThat's right. You're a Jew...\n\nKyle:\n\nA stylin' Jew...\n\nTogether:\n\nIt's a good time... to be Hebrew\nOn Christmas!\n\nSpecial Celebrity Guest:\n\nOn Christmas.	https://music.youtube.com/watch?v=eJHyB4ODVuo
49	I Saw Three Ships	3	I saw three ships come sailing in\nOn Christmas Day, on Christmas Day\nI saw three ships come sailing in\nOn Christmas Day, in the morning.\n\nAnd what was in those ships, all three?\nOn Christmas Day, on Christmas Day\nAnd what - shut up turds! - was in those ships all three\nOn Christmas Day, in the morning?\n\nThe Virgin Mary and Christ were there\nOn Christmas Day, on Christmas Day\nThe Virgin Mary - shut up turds! - and Christ were there\nOn Christmas Day, in the morning.\n\nLet us all rejoice, amain,\nOn Christmas Day, on Christmas Day\nAnd - I told you to shut up! - let us all rejoice, amain,\nOn Christmas Day, in the morning.\n\nShelley is starting to get pissed\nOn Christmas Day, on Christmas Day\nShelley got up and killed those turds\nOn Christmas Day, in the MORNING!	https://music.youtube.com/watch?v=t4wgoyT9s_E
50	It Happened in Sun Valley	3	Stan:\n\nHowdy folks, let's go for a ride\nGet your favorite one to sit by your side\nCuddle up in the sleigh, giddyap Nellie Grey\nAnd away we go.\n\nWendy:\n\nWhile you listen to the sleigh bells ring\nYou're yodeling to your baby\nYou feel nice and warm\nNo matter how cold it may be.\n\nStan:\n\nTake a look at little Jack and Jill\nThey ski down a hill, there's a snow plow turn\nLook there's a spill, there's a spill on the hill\nWhen you're down it's a thrill to get up again.\n\nTogether:\n\nEverybody ought to learn to ski\n'Cause that's how we first met.\n\nWendy:\n\nWe were that Jack and Jill\nThat came down a hill.\n\nStan:\n\nWhen I looked at you my heart took a spill.\n\nWendy:\n\nTook a spill on a hill.\n\nStan:\n\nIt's a thrill...\n\nTogether:\n\nThat I can't forget.\nIt happened in Sun Valley\nNot so very long ago.\n\nStan:\n\nThere were sunbeams in the snow\nAnd a twinkle in your eye.\n\nWendy:\n\nI remember oh so clearly\nThat you nearly passed me by.\n\nTogether:\n\nThen it happened in Sun Valley\nWhen you slipped and fell and so did I.\n\n(Instrumental)\n\nWendy:\n\nCatch me Stan! (Stan vomits) Eewww!\nLook Stan, I made a snow angel! (Stan vomits) Eewww!\n\nTogether:\n\nI remember oh so clearly\nThat you nearly passed me by.\nThen it happened in Sun Valley\nWhen you tripped and fell and so did I.\n\nStan:\n\nNow every year we go back and then...\n\nWendy:\n\nWe recall that fall and that moment when...\n\nStan:\n\nWe were there on the hill...\n\nTogether:\n\nSo we both take a spill\nAnd we're Jack and Jill again.\n\nWendy:\n\nMuak! (Stan vomits) Eeewwww!!!	https://music.youtube.com/watch?v=eCW8alDQ9m8
55	Swiss Colony Beef Log	3	Stockings are hung on the chimney\nAnd the presents are under the tree.\nAnd mama's in the kitchen\nMaking some... herbal tea.\n\nWindows are covered with frost\nAnd the candles are all alight.\nBut as I wander through this quiet house\nSomething just doesn't seem right.\n\nYou see, every year the neighbors bring us\nA Swiss Colony Beef Log.\nBut the neighbors aren't around (Around, around)\nThere's no Beef Log to be found.\n\nThis year...\nNo Beef Log.\n\nChristmas, isn't Christmas\nWithout a Swiss Colony Beef Log.\nWithout those cheeses and meat\nI don't think I can get along.\n\nMother tries to comfort me\nShe says:\n"Here son, have some eggnog."\nBut I fucking hate eggnog seriously.\n\nWhat do I see?\nUnderneath the tree?\nGrandma got a Swiss Colony Beef Log\nJust for me! Aaah, aaaaah, aaaaaah, grandma!\n\nSwiss Colony Beef Log, baby\nThat's what Christmas is all about!\nA roly-poly Colony Beef Log, lady\nMakes a little boy scream and shout!\n\nDeck the halls with boughs of Swiss Colony!\nFa-la-la-la-la, laa-laa-laa-laaaa!.. sweet.	https://music.youtube.com/watch?v=JzLrbzwB5FQ
56	Hark! The Herald Angels Sing	3	All:\n\nHark! the herald angels sing:\n"Glory to the newborn King!\nPeace on earth and mercy mild\nGod and sinners reconciled"\nJoyful, all ye nations rise\nJoin the triumph of the skies\nHark! the herald angels sing\n\nStan:\n\nDude, this is pretty fucked up right here! 	https://music.youtube.com/watch?v=LlkfpvW0S98
57	Dreidel, Dreidel, Dreidel	3	Kyle:\nOkay Ike, you're my little brother, so I have to show you how to celebrate Hanukkah. This is called a dreidel. You spin it and see where it lands, and you sing this song\n\nI have a little dreidel, I made it out of clay\nAnd when it's dry and ready, with dreidel I shall play\nOh dreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\n\nNow you try it, Ike. Just spin it with your fingers, like this\n\nIke:\nH-I-J-K-L-O-P\nUm, this song, like, go all the way\nPlay, came down the rain and wash the spider out\n\nCartman: Hey, what the hell are you doing?\n\nKyle: Oh, hey, Cartman. We're playing dreidel. You wanna try?\n\nCartman: Sure.\n\nHere's a little dreidel that's small and made of clay\nBut I'm not gonna play with it, 'cause dreidel's fuckin' gay\n\nKyle: Hey, shut your mouth, fatass!\n\nCartman:\nJ*** play stupid games\nJ***, that's why they're lame\n\n\n[They singing simultaneously]\n\nCartman:\nJ*** play stupid games\nJ***, that's why they're lame\n\t \n\t\n\nKyle:\nDreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\n\n[They stop singing simultaneously]\n\nStan:\nWhat's going on? Oh, it's that Hannukah thing\n\nCartman:\nIt's so amazing. You spin this thing on the ground and it goes round and round. I could watch it all day.\n\nStan:\nLet me try.\n\nI'll try to make it spin\nIt fell, I'll try again\n\n[They singing simultaneously]\n\nStan:\nI'll try to make it spin\nIt fell, I'll try again\n\t \n\t\n\nKyle:\nOh, dreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\n\n\n[Cartman starts singing]\n\nStan:\nI'll try to make it spin\nIt fell, I'll try again\nI'll try to make it spin\nIt fell, I'll try again\n\t \n\t\n\nKyle:\nOh, dreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\nOh, dreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\n\t \n\t\n\nCartman:\nJ*** play stupid games\nJ***, that's why they're lame\nJ*** play stupid games\nJ***, that's why they're lame\n\n[They stop singing]\n\nSheila:\nHello boys!\n\n\nKyle:\nHi, mom\n\nSheila:\nOh, how precious! You boys are all playing dreidel. Now you know that dreidel is a time-honored tradition for the Hebrew people.\n\nCartman:\nYes, we know, Ms. Broflovski, it's so very interesting\n\nSheila:\nNow when you learn to make the dreidel spin\nYou'll know our people always win, keep spinning!\n\n[They singing simultaneously]\n\nSheila:\nLearn to make the dreidel spin\nYou'll know our people always win\n\t \n\t\n\nCartman:\nJ*** play stupid games\nJ***, that's why they're lame\n\n[They stop singing]\n\nKyle:\nOh, hi Dad!\n\nGerald:\nHello, everybody. Say, can I join in?\n\nKyle:\nSure!\n\nI have a little dreidel, I made it out of clay\nAnd when it's dry and ready, with dreidel I shall...everybody!\n\n[Everybody starts singing simultaneously]\n\nKyle:\nDreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\nOh dreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\n\t \n\t\n\nCartman:\nJ*** play stupid games\nJ***, that's why they're lame\nJ*** play stupid games\nJ***, that's why they're lame\n\t \n\t\n\nStan:\nI'll try to make it spin\nIt fell, I'll try again\nI'll try to make it spin\nIt fell, I'll try again\n\t \n\t\n\nSheila:\nNow when you learn to make the dreidel spin\nYou'll know our people always win, keep spinning!\nLearn to make the dreidel spin\nYou'll know our people always win, keep spinning!\n\t \n\t\n\nGerald:\nCourteney Cox, I love you!\nYou're so hot on that show!\nCourteney Cox, I love you!\nYou're so hot on that show!\n\n[Everybody stops singing except Gerald]\n\nGerald:\nCourteney Cox, I love you\nYou're so hot on that show\n\nKyle:\nDad?\n\nGerald:\nCourteney Cox...\n\nKyle:\nDad!\n\nGerald:\nI love...\n\nKyle:\nWe're singing about a dreidel\n\nGerald:\nOh, sorry\n\nSheila:\nWe'll talk about this later, Gerald\n\n[Everybody starts singing simultaneously]\n\nKyle:\nDreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\nOh dreidel, dreidel, dreidel, I made you out of clay\nDreidel, dreidel, dreidel, with dreidel I shall play\n\t \n\t\n\nCartman:\nJ*** play stupid games\nJ***, that's why they're lame\nJ*** play stupid games\nJ***, that's why they're lame\n\t \n\t\n\nStan:\nI'll try to make it spin\nIt fell, I'll try again\nI'll try to make it spin\nIt fell, I'll try again\n\t \n\t\n\nSheila:\nNow when you learn to make the dreidel spin\nYou'll know our people always win, keep spinning!\nLearn to make the dreidel spin\nYou'll know our people always win!\n\t \n\t\n\nGerald:\nCourteney Cox, I love you!\nYou're so hot on that show!\nCourteney Cox, I love you!\nYou're so hot on that show!	https://music.youtube.com/watch?v=s24OHloNhYs
58	The Most Offensive Song Ever	3	Howdy Ho.\nthe Virgin Mary was sleepin'\nWhen Angel Gabriel appeared\nHe said, "You are to be the virgin mother."\nand Mary thought that was weird.\nMary said, "I'm not a virgin.\nI blew a guy last year."\nBut then Gabriel said to Mary,\n"My child, have no fear."\ncause, you can suck all the dick you want And still be a virgin, Mary.\nYou can suck all the dick you want\nAnd still not be considered flawed.\nAlthough you went to town\nand sucked some semen down,\nYou're still a virgin in the eyes of God.\n\nThere was no room at the inn\nWhen Mary and Joseph did arrive.\nBut they were so very tired, you see,\nAnd Mary had to offer a bribe.\nSince she had no money,\nHow would she pay for a place to sleep?\nGabriel appeared to Mary\nAnd told her not to weep.\n\n'Cause you can suck all the dick you want\nAnd still be a virgin, Mary.\nYou can suck all the dick you want\nAnd still be the mother of Christ.\nIf there's no room at the inn,\nthen it's not considered a sin\nto suck some dick to get a room for the night.\n\nThen, three wise men did appear\nBearing gifts of myrrh and such\nThey said that they had followed a star\nAnd missed a woman's touch.\nMary thought she might pleasure them\nBut could not take them to bed.\nBut again, Gabriel appeared to her\nAnd this is what he said:\n\nYou can suck all the dick you want\nAnd still be a virgin, Mary.\nYou can suck all the dick you want\nEvery one that hangs in the nation.\nFellatio ain't no sin.\nGo on and blow those Three Wise Men\nAnd you'll still be a virgin 'cause there was no penetration!\n\nSo, you can suck all the dick you want\nAnd still be a virgin, Mary.\nThe donkey and the ox and the lambs\nAnd even the little drummer boy\nfolks will remember your name quick.\nThey'll say "Damn, that bitch could suck a dick!"\n'Cause sucking dick brings peace on Earth and joy.\n\n'Cause sucking dick brings peace on Earth and joy.\nMary, Mary suck that dick.	https://music.youtube.com/watch?v=DE71dr7ZZnc
68	Jackin' It In San Diego (Live)	6	Baaam badam baaam baaadam, baaam badam bam.\nBaaam badam baaam baaadam, baaam badam bam.\n\nI'm gonna jack it where the sun always shines (He's gonna jack it)\nBeen spreadin' the word and now I need to ease my mind (Jackin' it, ohhh)\nBeen plantin' them apple seeds, and while the apples grow,\nI'm gonna go out jackin' it in San Diego\n\nJackin' it, jackin' it, jackety-jack\nSpankin' it, jackin' it, spankety-smack\n\nI don't need no shirt, no, gonna take them pants right off (He's about to jack it)\nOn such a bright day, who needs underwear or socks? (Jack it, jack it, ohhh)\nBeen around God's country, and there's one thing I know,\nThere's no better place for jackin' it than San Diego\n\nJack it, jack it, jackety-jack\nSpankin' it, spankin' it, smackety-smack\nJackin' it, jackin' it, jackety-jack\nJackin' it, spankin' it, smackety-smack (Jackin' for the Lord!)\n\n"Come to San Diego, there's so much to see. From the sparkling waters of Mission Bay to the warm tortillas of Old Town. And after a day of sightseeing, why not try spankin' it in one of our charming city streets? San Diego. Come, take a load off."\n\nJackin' it, jackin' it, jackety-jack\nSpankin' it, spankin' it, smackety-smack\nA-whackin' it, whackin' it, whackety-whack\nSpankin' it, jerkin' it, smackety-smack\n\nThe cars are passin' me by, they honk and say "hello" (Hey, that guy's jackin' it!)\nFrom his window, there's a guy shootin' video (Video of him jackin')\nAnd if the good Lord, Jesus, comes knockin' on my door,\nJust tell him that I'm jackin' it in San Diego\n\nJackin' it, jackin' it, jackety-jack\nSpankin' it, spankin' it, smackety-smack (He's about to jack it)\nJack it, whack it, jack it, jackin' it, jack (Whackin' it, whackin' it)\nWhack it, whack it, spank, spank, whack, whackin' it, whack (Look at me, I'm jackin' it)\nSpank it, whack it, jack it, jack it, whackin' it, whack (Whack it)\nSpank it, spank it, whack it, whack it, San Diego (He's about to jack it)\nSan Diego, jack, jack, whackin' it, wack (Whackin' it, whackin' it)\nWhack it, San Diego, whackin' it, whack (Keep on jackin' it)\nSan Diego, jack it, jack it, whackin' it, whack (San Diego)\nJack, San Diego, whack, whack, jackin' it, jack (Jack it)\nJackin' it, jackin' it, jackin' it, jack (Whackin' it, whackin' it, whackin' it, whack)\nSan Diego, jack, jack, (Wack, wack)\nWhack, jack, spank, spank, spank,\nSan Diego, ahhh...	https://music.youtube.com/watch?v=lKgU8-ckkdI
77	Tommy (Butters) The Cat (Live)	6	Well, I remember it as though it were a meal ago\nSaid Tommy the Cat as he reeled back to clear whatever foreign matter may have nestled its way into his mighty throat\nMany a fat alley rat had met its demise while staring point blank down the cavernous barrel of this awesome prowling machine\nTruly a wonder of nature this urban predator\nTommy the cat had many a story to tell\nBut it was a rare occasion such as this that he did\n\nWell, she came sliding on down the alleyway like butter drippin' off a hot biscuit\nThe aroma, the mean scent, was enough to arouse suspicion in even the oldest of tigers that hung around the hot spot in those days\nThe sight was beyond belief\nMany a head snapped for double, even triple takes as this vivacious feline made her her way into the delta of the alleyway where the most virile of the young tabbies were known to hang out\nThey hung out in droves\nSuch a multitude of masculinity could only be found in one place and that was O'Malley's Alley\n\nThe air was thick with catcalls, no pun intended\nBut not even a muscle in her neck did twitch as she sauntered straight to behind the alleyway\nShe knew what she wanted\nShe was looking for that stud bull\nShe was looking for that He-cat\nAnd that was me\nTommy the Cat is my name and I say unto thee\n\nSay baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, baby\nSay, baby\n\nSay, baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, baby\nSay, baby\nSay, baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, b-b-b-b-b-b-b-baby\nSay, baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, baby\nSay, baby\n\nSay, baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, baby\nSay, baby\nSay, baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, baby\nSay, baby\nSay, baby, do you wanna lay down with me?\nSay, baby, do you wanna lay down by my side?\nAh, baby, do you wanna lay down with me?\nSay, baby\nSay, baby	https://music.youtube.com/watch?v=FxFozKx5kqY
82	Kyle's Mom's a Bitch (Live)	6	Cartman: Weeellll\n\nKyle: Don't do it, Cartman!\n\nCartman: Weeellll\n\nKyle: I'm warning you!\n\nCartman: Okay, okay.\n\nKyle: I'm getting pretty sick of him, call my mom...\n\nWeeellll\nKyle's mom's a bitch, she's a big fat bitch,\nShe's the biggest bitch in the whole wide world\nShe's a stupid bitch, if there ever was a bitch,\nShe's a bitch to all the boys and girls.\n\nKyle: SHUT YOUR F**KING MOUTH, CARTMAN!\n\nOn Monday she's a bitch,\nOn Tuesday she's a bitch,\nOn Wednesday through Saturday she's a bitch\nThen on Sundays, just to be different,\nShe's a super King Kamehameha biyotch!\n\nCome on! You all know the words!\n\nHave you ever met my friend Kyle's mom?\nShe's the biggest bitch in the whole wide world.\n(La-la-la-la-la-la-la)\nShe's a mean old bitch, and she has stupid hair.\nShe's a bitch-bitch-bitch-bitch-bitch-bitch-bitch.\n\nbitch-bitch-bitch-bitch-bitch-bitch-bitch-bitch (bitch, bitch, bitch, bitch)\nShe's a stupid bitch! (WHOO!)\nKyle's mom's a bitch (Stupid bitch, because...)\nAnd she's such a dirty bitch! (...she's such a dirty bitch. bitch!)\n\nTalk to kids around the world,\nIt might go a little bit something like this:\n\n(Chinese)\n凯尔妈妈是个泼妇，她是基佬秘术大师，我只想说摸了被她变泼妇。\nKǎiěr māmā shìgè pōfù, tā shì jī lǎo mìshù dàshī, wǒ zhǐ xiǎng shuō mōle bèi tā biàn pōfù,\nKyle Mom's a bitch, She's a fat gay bitch, when I touch her she becomes a big fat bitch.\n(French)\nLa mère de Kyle est une pute, est une sacrée vieille pute, la plus grande pute du monde entier.\nKyle's Mom's a bitch, a one hell of a bitch, the biggest bitch in the whole, wide world.\n(Dutch)\nKyle's moeder is een teef, ze is een grote fout te teef ze grote teef ter ver reld, teef ter ver reld.\nKyle's Mom is a bitch, she was a big mistake of a bitch, she's the biggest bitch in the world, bitch in the world.\n(Swahili)\nMama yake Kyle ni mbwa mkubwa, ndiye ni mbwa mkubwa kuliko wote duniani hii.\nKyle's Mom's a dog, a female dog, she's the biggest bitch in whole wide world.\n\nHave you ever met my friend Kyle's mom?\nShe's the biggest bitch in the whole wide world.\n(La-la-la-la-la-la-la)\n\nShe's a mean old bitch, and she has stupid hair.\nShe's a bitch-bitch-bitch-bitch-bitch-bitch-bitch\n\nbitch-bitch-bitch-bitch-bitch-bitch-bitch-bitch.\nShe's a stupid bitch! (Uh, Cartman?)\n\nKyle's mom's a bitch\nAnd she's such a dirty bitch!\n\nI really mean it!\nKyle's mom, she's a big… fat… fucking bitch!\nBig ole fat fucking bitch, Kyle's mom!\nYeah, chaaaa!\n\nCartman: What?\n\nCartman: Oh, fuck!	https://music.youtube.com/watch?v=iHhWxC6zR78
\.


--
-- Data for Name: albums; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.albums (id, name, release_date, album_cover) FROM stdin;
4	Timmy & the Lords of the Underworld	2000-09-05	img/albums/covers/Timmy_and_the_Lords_of_the_Underworld.jpg
5	San Diego	2012-08-21	img/albums/covers/San_Diego.jpg
1	Chef Aid: The South Park Album	1998-12-08	img/albums/covers/Chef_Aid_The_South_Park_Album.jpg
3	Mr. Hankey's Christmas Classics	1999-11-23	img/albums/covers/Mr_Hankey's_Christmas_Classics.jpg
6	South Park The 25th Anniversary Concert	2022-09-25	img/albums/covers/SSouth_Park_25th_Aniversary_Concert.jpg
2	South Park: Bigger, Longer & Uncut (Soundtrack)	1999-06-22	img/albums/covers/South_Park_Bigger_Longer_and_Uncut.jpg
\.


--
-- Data for Name: alter_ego; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.alter_ego (id, original_character, name, images) FROM stdin;
1	1	Mysterion	{/img/alteregos/phone_destroyer/Mysterion_PhoneDestroyer.png,/img/alteregos/serie/Mysterion.png}
2	1	Cyborg Kenny	{/img/alteregos/phone_destroyer/Cyborg_Kenny_PhoneDestroyer.png,/img/alteregos/serie/Cyborg_Kenny.png}
3	1	Inuit Kenny	{/img/alteregos/phone_destroyer/Inuit_Kenny_PhoneDestroyer.png,/img/alteregos/serie/Inuit_Kenny.png}
4	1	Hermes Kenny	{/img/alteregos/phone_destroyer/Hermes_Kenny_PhoneDestroyer.png,/img/alteregos/serie/Hermes_Kenny.png}
5	1	Princess Kenny	{/img/alteregos/phone_destroyer/Princess_Kenny_PhoneDestroyer.png,/img/alteregos/serie/Princess_Kenny.png}
1	42	Astronaut Butters	{/img/alteregos/phone_destroyer/Astronaut_Butters_PhoneDestroyer.png,/img/alteregos/serie/Astronaut_Butters.png}
2	42	Deckhand Butters	{/img/alteregos/phone_destroyer/Deckhand_Butters_PhoneDestroyer.png,/img/alteregos/serie/Deckhand_Butters.png}
3	42	Choirboy Butters	{/img/alteregos/phone_destroyer/Choirboy_Butters_PhoneDestroyer.png,/img/alteregos/serie/Choirboy_Butters.png}
4	42	Paladin Butters	{/img/alteregos/phone_destroyer/Paladin_Butters_PhoneDestroyer.png,/img/alteregos/serie/Paladin_Butters.png}
5	42	Professor Chaos	{/img/alteregos/phone_destroyer/Profesor_Chaos_PhoneDestroyer.png,/img/alteregos/serie/Professor_Chaos.png}
5	4	Poseidon Stan	{/img/alteregos/phone_destroyer/Stan_Poseidon_PhoneDestroyer.png,/img/alteregos/serie/Poseidon_Stan.png}
4	4	Tron Stan / Program Stan	{/img/alteregos/phone_destroyer/Stan_Program_PhoneDestroyer.png,/img/alteregos/serie/Tron_Stan.png}
3	4	Stan of Many Moons	{/img/alteregos/phone_destroyer/Stan_Of_Many_Moons_PhoneDestroyer.png,/img/alteregos/serie/Stan_of_Many_Moons.png}
2	4	Stan Marshwalker	{/img/alteregos/phone_destroyer/Stan_MashWalker_PhoneDestroyer.png,/img/alteregos/serie/Stan_Marshwalker.png}
1	4	Toolshed	{/img/alteregos/phone_destroyer/Toolshed_PhoneDestroyer.png,/img/alteregos/serie/Toolshed.png}
5	3	Bounty Hunter Kyle	{/img/alteregos/phone_destroyer/Bounty_Hunter_Kyle_PhoneDestroyer.png,/img/alteregos/serie/Bounty_Hunter_Kyle.png}
4	3	Gunslinger Kyle	{/img/alteregos/phone_destroyer/Gunslinger_Kyle_PhoneDestroyer.png,/img/alteregos/serie/Gunslinger_Kyle.png}
3	3	The Master Ninjew	{/img/alteregos/phone_destroyer/Master_NinJew_PhoneDestroyer.png,/img/alteregos/serie/The_Master_Ninjew.png}
2	3	High Jew Elf King	{/img/alteregos/phone_destroyer/High_Jew_Elf_King_PhoneDestroyer.png,/img/alteregos/serie/High_Jew_Elf_King.png}
1	3	The Human Kite	{/img/alteregos/phone_destroyer/HumanKite_PhoneDestroyer.png,/img/alteregos/serie/Humankite.png}
5	2	Zen Cartman	{/img/alteregos/phone_destroyer/Cartman_Zen_PhoneDestroyer.png,/img/alteregos/serie/Cartman_Zen.png}
4	2	Sheriff Cartman	{/img/alteregos/phone_destroyer/Cartman_Sheriff_PhoneDestroyer.png,/img/alteregos/serie/Sheriff_Cartman.png}
3	2	AWESOMO 4000	{/img/alteregos/phone_destroyer/AWESOMO_4000_PhoneDestroyer.png,/img/alteregos/serie/AWESOMO_4000.png}
2	2	The Grand Wizard	{/img/alteregos/phone_destroyer/Cartman_Wizard_PhoneDestroyer.png,/img/alteregos/serie/The_Grand_Wizard.png}
1	2	The Coon	{/img/alteregos/phone_destroyer/The_Coon_PhoneDestroyer.png,/img/alteregos/serie/The_Coon.png}
4	188	Ice Sniper Wendy	{/img/alteregos/phone_destroyer/Ice_Sniper_Wendy.png,/img/alteregos/serie/Ice_Sniper_Wendy.png}
3	188	Angel Wendy	{/img/alteregos/phone_destroyer/Angel_Wendy.png,/img/alteregos/serie/Angel_Wendy.png}
2	188	Shieldmaiden Wendy	{/img/alteregos/phone_destroyer/Shieldmaiden_Wendy.png,/img/alteregos/serie/Sheildmaiden_Wendy.png}
1	188	Call Girl	{/img/alteregos/phone_destroyer/Call_Girl.png,/img/alteregos/serie/Call_Girl.png}
5	199	Fastpass	{/img/alteregos/phone_destroyer/Fastpass,/img/alteregos/serie/Fastpass.png}
4	199	Le Bard Jimmy	{/img/alteregos/phone_destroyer/Le_Bard_Jimmy.png,/img/alteregos/serie/Jimmy_The_Bard.png}
3	199	Friar Jimmy	{/img/alteregos/phone_destroyer/Friar_Jimmy.png,/img/alteregos/serie/Flair_Jimmy.png}
2	199	Enforcer Jimmy	{/img/alteregos/phone_destroyer/Enforcer_Jimmy.png,/img/alteregos/serie/Enforcer_Jimmy.png}
1	199	Storyteller Jimmy	{/img/alteregos/phone_destroyer/Storyteller_Jimmy.png,/img/alteregos/serie/Storyteller_Jimmy.png}
5	78	Shaman Tolkien	{/img/alteregos/phone_destroyer/Shaman_Tolkien.png,/img/alteregos/serie/Shaman_Tolkien.png}
4	78	Space Warrior Tolkien	{/img/alteregos/phone_destroyer/Space_Warrior_Tolkien.png,/img/alteregos/serie/Space_Warrior_Tolkien.png}
3	78	Witch Doctor Tolkien	{/img/alteregos/phone_destroyer/Witch_Doctor_Tolkien.png,/img/alteregos/serie/Witch_Doctor_Tolkien.png}
2	78	Rogue Tolkien	{/img/alteregos/phone_destroyer/Rouge_Tolkien.png,/img/alteregos/serie/Rouge_Tolkien.png}
1	78	Tupperware	{/img/alteregos/phone_destroyer/Tupperware.png,/img/alteregos/serie/Tupperware.png}
5	99	Hookhand Clyde	{/img/alteregos/phone_destroyer/Hookhand_Clyde.png,/img/alteregos/serie/Hookhand_Clyde.png}
4	99	Alien Clyde	{/img/alteregos/phone_destroyer/Alien_Clyde.png,/img/alteregos/serie/Alien_Clyde.png}
3	99	Hercules Clyde	{/img/alteregos/phone_destroyer/Hercules_Clyde.png}
2	99	Dwarf King Clyde	{/img/alteregos/phone_destroyer/Dwarf_King_Clyde.png,/img/alteregos/serie/Clyde_Dwarf_King.png}
1	99	Mosquito	{/img/alteregos/phone_destroyer/Mosquito.png,/img/alteregos/serie/Mosquito.png}
5	58	Incan Craig	{/img/alteregos/phone_destroyer/Incan_Craig.png}
4	58	Marine Craig	{/img/alteregos/phone_destroyer/Marine_Craig.png,/img/alteregos/serie/Marine_Craig.png}
3	58	Youth Pastor Craig	{/img/alteregos/phone_destroyer/Young_Pastor_Craig.png,/img/alteregos/serie/Youth_Paster_Craig.png}
2	58	Dark Mage Craig	{/img/alteregos/phone_destroyer/Dark_Mage_Craig.png,/img/alteregos/serie/Dark_Mage_Craig.png}
1	58	Super Craig	{/img/alteregos/phone_destroyer/Super_Craig.png,/img/alteregos/serie/Super_Craig.png}
5	52	Outlaw Tweek	{/img/alteregos/phone_destroyer/Outlaw_Tweek.png}
4	52	Warboy Tweek	{/img/alteregos/phone_destroyer/Warboy_Tweek.png}
3	52	Imp Tweek	{/img/alteregos/phone_destroyer/Imp_Tweek.png,/img/alteregos/serie/IMP_Tweek.png}
2	52	Robin Tweek	{/img/alteregos/phone_destroyer/Robin_Tweek.png,/img/alteregos/serie/Robin_Tweek.png}
1	52	Wonder Tweek	{/img/alteregos/phone_destroyer/Wonder_Tweek.png,/img/alteregos/serie/Wonder_Tweek.png}
5	82	Pirate Ship Timmy	{/img/alteregos/phone_destroyer/Pirate_Ship_Timmy.png,/img/alteregos/serie/Pirate_Ship_Timmy.png}
4	82	Mecha Timmy	{/img/alteregos/phone_destroyer/Mecha_Timmy.png,/img/alteregos/serie/Mecha_Timmy.png}
3	82	Pope Timmy	{/img/alteregos/phone_destroyer/Pope_Timmy.png,/img/alteregos/serie/Pope_Timmy.png}
2	82	Catapult Timmy	{/img/alteregos/phone_destroyer/Catapult_Timmy.png,/img/alteregos/serie/Catapult_Timmy.png}
1	82	Doctor Timothy	{/img/alteregos/phone_destroyer/Doctor_Timothy.png,/img/alteregos/serie/Doctor_Timothy.png}
4	171	Buccaneer Bebe	{/img/alteregos/phone_destroyer/Buccaneer_Bebe.png}
3	171	Robo Bebe	{/img/alteregos/phone_destroyer/Robo_Bebe.png}
2	171	Medusa Bebe	{/img/alteregos/phone_destroyer/Medusa_Bebe.png}
1	171	Blood Elf Bebe	{/img/alteregos/phone_destroyer/Blood_Elf_Bebe.png}
5	151	Swashbuckler Red	{/img/alteregos/phone_destroyer/Swashbukler_Red.png}
4	151	Alien Queen Red	{/img/alteregos/phone_destroyer/Alien_Queen_Red.png,/img/alteregos/serie/Red_Alien_Queen.png}
3	151	Dark Angel Red	{/img/alteregos/phone_destroyer/Dark_Angel_Red.png,/img/alteregos/serie/Dark_Angel_Red.png}
2	151	Dragonslayer Red	{/img/alteregos/phone_destroyer/Dragonslayer_Red.png,/img/alteregos/serie/Red_Dragonslayer.png}
1	151	Changeling Red	{/img/alteregos/phone_destroyer/Changeling_Red.png}
1	5	Canadian Knight Ike	{/img/alteregos/phone_destroyer/Canadian_Knight_Ike.png,/img/alteregos/serie/Canadian_Knight_Ike.png}
4	5	Smuggler Ike	{/img/alteregos/phone_destroyer/Smuggler_Ike.png,/img/alteregos/serie/Smuggler_Ike.png}
3	5	Gizmo Ike	{/img/alteregos/phone_destroyer/Gizmo_Ike.png,/img/alteregos/serie/Gizmo_Ike.png}
2	5	Scout Ike	{/img/alteregos/phone_destroyer/Scout_Ike.png,/img/alteregos/serie/Scout_Ike.png}
5	65	Frontier Bradley	{/img/alteregos/phone_destroyer/Frontier_Bradley.png}
4	65	Space Pilot Bradley	{/img/alteregos/phone_destroyer/Space_Pilot_Bradley.png}
3	65	Archangel Bradley	{/img/alteregos/phone_destroyer/Archangel_Bradley.png}
2	65	Elven King Bradley	{/img/alteregos/phone_destroyer/Elven_King_Bradley.png}
1	65	Mintberry Crunch	{/img/alteregos/phone_destroyer/Mintberry_Crunch.png,/img/alteregos/serie/Mint_Berry_Crunch.png}
5	19	Pocahontas Randy	{/img/alteregos/phone_destroyer/Pocahontas_Randy.png,/img/alteregos/serie/Pocahontas_Randy.png}
4	19	Sixth Element Randy	{/img/alteregos/phone_destroyer/Sixth_Element_Randy.png,/img/alteregos/serie/Sixth_Element_Randy.png}
3	19	Sexy Nun Randy	{/img/alteregos/phone_destroyer/Sexy_Nun_Randy.png,/img/alteregos/serie/Sexy_Nun_Randy.png}
2	19	The Amazingly Randy	{/img/alteregos/phone_destroyer/The_Amazingly_Randy.png,/img/alteregos/serie/The_Amazingly_Randy.png}
1	19	Mary Jane Randy	{/img/alteregos/phone_destroyer/Mary_Jane_Randy.png,/img/alteregos/serie/Mary_Jane_Randy.png}
4	7	President Garrison	{/img/alteregos/phone_destroyer/President_Garrison.png,/img/alteregos/serie/President_Garrison.png}
3	7	Swordsman Garrison	{/img/alteregos/phone_destroyer/Swordsman_Garrison.png}
2	7	Commander Hat	{/img/alteregos/phone_destroyer/Commander_Hat.png}
1	7	Witch Garrison	{/img/alteregos/phone_destroyer/Witch_Garrison.png}
2	141	Alchemist Scott	{/img/alteregos/phone_destroyer/Alchemist_Scott.png,/img/alteregos/serie/Ranger_Scott.png}
1	141	Captain Diabetes	{/img/alteregos/phone_destroyer/Captain_Diabetes.png,/img/alteregos/serie/Captain_Diabetes.png}
5	188	Captain Wendy	{/img/alteregos/phone_destroyer/Captain_Wendy.png}
1	61	Alternate Human Kite	{/img/alteregos/phone_destroyer/Alt_Human_Kite.png,/img/alteregos/serie/Alt_Human_Kite.png}
1	194	Calamity Heidi	{/img/alteregos/phone_destroyer/Calamity_Heidi.png}
1	43	Infiltrator Kevin	{/img/alteregos/phone_destroyer/Infiltrator_Kevin.jpg,/img/alteregos/serie/Infiltrator_Kevin.png}
1	95	Nymph Nichole	{/img/alteregos/phone_destroyer/Nymph_Nichole.png}
1	17	Sharpshooter Shelley	{/img/alteregos/phone_destroyer/Sharpshooter_Shelley.png,/img/alteregos/serie/Sharpshooter_Shelley.png}
1	33	Sorceress Liane	{/img/alteregos/phone_destroyer/Sorceress_Liane.png,/img/alteregos/serie/Sorceress_Liane.png}
1	21	War Hero Ned	{/img/alteregos/phone_destroyer/War_Hero_Ned.png}
1	24	S-WOW Tittybang	{/img/alteregos/phone_destroyer/S-WOW_Tittybang.png,/img/alteregos/serie/S_Wow_Tittybang.png}
1	16	Medicine Woman Sharon	{/img/alteregos/phone_destroyer/Medicine_Woman_Sharon.png,/img/alteregos/serie/Medicine_Woman_Sharon.png}
1	39	Sizzler Stuart	{/img/alteregos/phone_destroyer/Sizzler_Stuart.png,/img/alteregos/serie/Sizzler_Stuart.png}
1	27	Full Moon Sparky	{/img/alteregos/phone_destroyer/Full_Moon_Sparky.png}
\.


--
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.characters (id, name, friend_group, family, birthday, age, religion, first_apperance, images, famious_guest) FROM stdin;
1	Kenneth "Kenny" McCormick	1	4	March 22th	9	{Christianity,"Blaintologist (Temporary)"}	1	{/img/characters/serie/Kenny_McCormick.png}	f
2	Eric Theodore Cartman	1	2	July 1st	10	{"Roman Catholicism","Blaintologistism (Temporary)","Judaism (Post-Covid)"}	1	{/img/characters/serie/Eric_Cartman.png}	f
3	Kyle Broflovski	1	1	May 26th	10	{Judaism,"Christianity (Temporary)","Blaintologist (Temporary)","Atheistism (Temporary)"}	1	{/img/characters/serie/Kyle_Broflovski.png}	f
4	Stanley "Stan" Marsh	1	3	October 19th	10	{Christian,"Atheist (Temporariry)","Mormon (Temporariry)","Scientologist (Temporariry)","Blaintologist (Temporarily)"}	1	{/img/characters/serie/Stan_Marsh.png}	f
5	Sir Ike Moisha Broflovski	\N	1	December 17th	3	{Judaism}	1	{/img/characters/serie/Ike_Broflovski.png}	f
6	Jerome McElroy "The Chef"	\N	27	\N	\N	{Christianity,"Islam (Temporary)"}	1	{/img/characters/serie/Chef.png}	f
7	Herbert Garrison	\N	16	\N	41	{"Roman Catholic","Atheist (Temporary)"}	1	{/img/characters/serie/Herbert_Garrison.png}	f
8	Kathie Lee Gifford	\N	\N	August 16th	71	{Evangelicalism}	2	{/img/characters/serie/Kathie_Lee.png}	t
9	Geraldo Rivera	\N	\N	July 4th	82	{"Reform Judaism"}	2	{/img/characters/serie/Geraldo_Rivera.png}	t
10	Jimbo Kern	\N	3	\N	\N	{"Roman Catholic"}	2	{/img/characters/serie/Jimbo_Kern.png}	\N
11	Mr. Hat	\N	16	\N	\N	\N	1	{/img/characters/serie/Mr_Hat.png}	\N
12	Great-Great-Grandpa Marsh	\N	3	\N	\N	\N	6	{/img/characters/serie/Great_Great_Grandpa_Marsh.png}	\N
13	Flo Kimble	\N	3	\N	\N	\N	28	{/img/characters/serie/Flo_Kimble.png}	\N
14	Marvin Marsh	\N	3	\N	102	{"Roman Catholic"}	6	{/img/characters/serie/Marvin_Marsh.png}	\N
15	Roy	\N	3	\N	\N	\N	25	{/img/characters/serie/Roy.png}	\N
16	Sharon Marsh	\N	3	December 16th	\N	{Christian,"Atheist (Temporariry)","Mormon (Temporariry)"}	5	{/img/characters/serie/Sharon_Marsh.png}	\N
17	Shelley Marsh	\N	3	November 24th	13	{Christian,"Atheist (Temporariry)","Mormon (Temporariry)"}	5	{/img/characters/serie/Shelley_Marsh.png}	\N
18	Fluffy	\N	2	\N	\N	\N	5	{/img/characters/serie/Fluffy.png}	\N
19	Randy Marsh	\N	3	March 1st	45	{Christian,"Atheist (Temporariry)","Mormon (Temporariry)"}	3	{/img/characters/serie/Randy_Marsh.png}	\N
20	Patrick Duffy	\N	\N	March 17th	76	{Buddhism}	3	{/img/characters/serie/Patrick_Duffy.png}	t
21	Ned Gerblanski	\N	\N	\N	\N	{"Roman Catholic"}	3	{/img/characters/serie/Ned_Gerblanski.png}	\N
22	Scuzzlebutt	\N	\N	\N	\N	\N	3	{/img/characters/serie/Scuzzlebutt.png}	\N
23	Murrey Broflovski	\N	1	\N	\N	{Judaism}	16	{/img/characters/serie/Murrey_Broflovski.png}	\N
24	Sheila Broflovski	\N	1	\N	\N	{Judaism}	6	{/img/characters/serie/Sheila_Broflovski.png}	\N
25	Gerald Broflovski	\N	1	\N	\N	{Judaism}	9	{/img/characters/serie/Gerald_Broflovski.png}	\N
26	Clone Stan Marsh	\N	3	\N	0	\N	5	{/img/characters/serie/Clone_Stan_Marsh.png}	\N
27	Sparky	\N	3	\N	\N	\N	4	{/img/characters/serie/Sparky.png}	\N
28	Howard Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Howard_Cartman.png}	\N
29	"Eric's Unnamed Uncle"	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Uncle_Cartman.png}	\N
30	Stinky Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Stinky_Cartman.png}	\N
31	Mabel Louise Cartman	\N	2	\N	\N	{"Roman Catholic"}	24	{/img/characters/serie/Mabel_Cartman.png}	\N
32	Harold Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Harold_Cartman.png}	\N
33	Liane Cartman	\N	2	\N	\N	{"Roman Catholic"}	1	{/img/characters/serie/Liane_Cartman.png}	\N
34	Fred Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Fred_Cartman.png}	\N
35	Elvin Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Elvin_Cartman.png}	\N
36	Alexandra Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Alexandra_Cartman.png}	\N
37	Eric's Unnamed Aunt	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Aunt_Cartman.png}	\N
38	Lisa Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Lisa_Cartman.png}	\N
39	Stuart McCormick	\N	4	\N	\N	{"Roman Catholic","Cult of Cthulhu (Formerly)"}	8	{/img/characters/serie/Stuart_McCormick.png}	\N
40	Mr. Kitty	\N	2	\N	\N	\N	1	{/img/characters/serie/Mr_Kitty.png}	\N
41	Florence Cartman	\N	2	\N	\N	{"Roman Catholic"}	29	{/img/characters/serie/Florence_Cartman.png}	\N
42	Leopold "Butters" Stotch	\N	34	September 11th	9	{"Roman Catholic","Blaintology (Temporarily)"}	25	{/img/characters/serie/Butters_Stotch.png}	\N
43	Kevin McCormick	\N	4	\N	\N	{"Roman Catholic"}	8	{/img/characters/serie/Kevin_McCormick.png}	\N
96	Mrs. Daniels	\N	13	\N	\N	\N	230	{/img/characters/serie/Mrs_Daniels.png}	\N
44	Carol McCormick	\N	4	\N	\N	{"Roman Catholic","Cult of Cthulhu (Formerly)"}	8	{/img/characters/serie/Carol_McCormick.png}	\N
45	Nellie Stotch	\N	34	\N	\N	\N	116	{/img/characters/serie/Nellie_Stotch.png}	\N
46	Bud Stotch	\N	34	\N	\N	\N	116	{/img/characters/serie/Bud_Stotch.png}	\N
47	Grandma Stotch	\N	34	\N	\N	\N	228	{/img/characters/serie/Grandma_Stotch.png}	\N
48	Linda Stotch	\N	34	\N	\N	{"Roman Catholic"}	64	{/img/characters/serie/Linda_Stotch.png}	\N
49	Stephen Willis Stotch	\N	34	\N	\N	{"Roman Catholic"}	17	{/img/characters/serie/Stephen_Stotch.png}	\N
50	Karen McCormick	\N	4	\N	6	{"Roman Catholic"}	129	{/img/characters/serie/Karol_McCormick.png}	\N
51	Richard Tweak	\N	48	\N	\N	{Buddhist,"Roman Catholic (Formerly)","Atheist (Formerly)"}	30	{/img/characters/serie/Richard_Tweak.png}	\N
52	Tweek Tweak	\N	48	\N	10	{Buddhist,"Roman Catholic (Formerly)","Atheist (Formerly)"}	30	{/img/characters/serie/Tweek_Tweak.png}	\N
53	Stripe	\N	43	\N	\N	\N	36	{/img/characters/serie/Stripe.png}	\N
54	Tricia Tucker	\N	43	\N	\N	{"Roman Catholic"}	36	{/img/characters/serie/Tricia_Tucker.png}	\N
55	Laura Tucker	\N	43	\N	\N	{"Roman Catholic"}	36	{/img/characters/serie/Laura_Tucker.png}	\N
56	Thomas Tucker	\N	43	\N	\N	{"Roman Catholic"}	36	{/img/characters/serie/Thomas_Tucker.png}	\N
57	Grandma Tucker	\N	43	\N	\N	\N	178	{/img/characters/serie/Grandma_Tucker.png}	\N
58	Craig Tucker	\N	43	Octuber 23	10	{"Roman Catholic"}	9	{/img/characters/serie/Craig_Tucker.png}	\N
59	Manuela Tweak	\N	48	\N	\N	{Buddhist,"Roman Catholic (Formerly)","Atheist (Formerly)"}	30	{/img/characters/serie/Manuela_Tweak.png}	\N
60	Grandma Tweak	\N	48	\N	\N	\N	312	{/img/characters/serie/Grandma_Tweak.png}	\N
61	Kyle Schwartz	\N	1	\N	10	{Judaism}	76	{/img/characters/serie/Kyle_Schwartz.png}	\N
62	Kyle's Elephant	\N	1	\N	\N	\N	5	{/img/characters/serie/Kyle_Elephant.png}	\N
63	Spookyfish	\N	3	\N	\N	\N	28	{/img/characters/serie/Spookyfish.png}	\N
64	Grandpa McCormick	\N	4	\N	\N	\N	63	{/img/characters/serie/Grandpa_McCormick.png}	\N
65	Bradley Biggle	\N	8	\N	10	\N	46	{/img/characters/serie/Bradley_Biggle.png}	\N
66	Harriet Biggle	\N	8	\N	\N	\N	110	{/img/characters/serie/Mrs_Biggle.png}	\N
67	Mr. Biggle	\N	8	\N	\N	\N	241	{/img/characters/serie/Mr_Biggle.png}	\N
68	Barney	\N	7	\N	\N	\N	264	{/img/characters/serie/Barney.png}	\N
69	Mrs. Barbrady	\N	7	\N	\N	\N	264	{/img/characters/serie/Mrs_Barbrady.png}	\N
70	Officer Barbrady	\N	7	\N	\N	{"Roman Catholic"}	1	{/img/characters/serie/Officer_Barbrady.png}	\N
71	Mike Makowski	\N	5	\N	11	\N	181	{/img/characters/serie/Mike_Makowski.png}	\N
72	Mr. Adams	\N	5	\N	\N	\N	223	{/img/characters/serie/Mr_Adams.png}	\N
73	Henrietta Biggle	\N	8	\N	11	{Satanism,"Cult of Cthulhu (Formerly)"}	110	{/img/characters/serie/Henrietta_Biggle.png}	\N
74	Rosie O'Donnell	\N	6	March 21th	63	{"Roman Catholic"}	60	{/img/characters/serie/Rosie_Odonnell.png}	t
75	Filmore Anderson	\N	6	\N	\N	\N	60	{/img/characters/serie/Filmore_Anderson.png}	\N
76	Mrs. Anderson	\N	6	\N	\N	\N	64	{/img/characters/serie/Mrs_Anderson.png}	\N
77	Millard Anderson	\N	6	\N	\N	\N	90	{/img/characters/serie/Millard_Anderson.png}	\N
78	Tolkien Black	\N	9	\N	10	{"Roman Catholic"}	36	{/img/characters/serie/Tolkien_Black.png}	\N
79	Linda Black	\N	9	\N	\N	{"Roman Catholic"}	50	{/img/characters/serie/Linda_Black.png}	\N
80	Steve Black	\N	9	\N	\N	{"Roman Catholic"}	50	{/img/characters/serie/Steve_Black.png}	\N
81	Gobbles	\N	10	\N	\N	\N	61	{/img/characters/serie/Gobbles.png}	\N
82	Timothy "Timmy" Burch	\N	10	\N	10	\N	49	{/img/characters/serie/Timmy_Burch.png}	\N
83	Helen Burch	\N	10	\N	\N	\N	51	{/img/characters/serie/Helen_Burch.png}	\N
84	Richard Burch	\N	10	\N	\N	\N	51	{/img/characters/serie/Richard_Burch.png}	\N
85	Charlotte's Grandmother	\N	11	\N	\N	\N	259	{/img/characters/serie/Charlottes_Grandma.png}	\N
86	Charlotte's Siste	\N	11	\N	\N	\N	259	{/img/characters/serie/Charlottes_Sister.png}	\N
87	Charlotte's Brother	\N	11	\N	\N	\N	259	{/img/characters/serie/Charlottes_Brother.png}	\N
88	Charlotte	\N	11	\N	10	\N	259	{/img/characters/serie/Charlotte.png}	\N
89	Charlotte's Mother	\N	11	\N	\N	\N	259	{/img/characters/serie/Charlottes_Mother.png}	\N
90	Thomas (Charlotte's Father)	\N	11	\N	\N	\N	259	{/img/characters/serie/Charlottes_Father.png}	\N
91	Rebecca Cotswolds	\N	12	\N	9	\N	43	{/img/characters/serie/Rebecca_Cotswolds.png}	\N
92	Mark Cotswolds	\N	12	\N	10	\N	43	{/img/characters/serie/Mark_Cotswolds.png}	\N
93	Mrs. Cotswolds	\N	12	\N	\N	\N	43	{/img/characters/serie/Mrs_Cotswolds.png}	\N
94	Mr. Cotswolds	\N	12	\N	\N	\N	43	{/img/characters/serie/Mr_Cotswolds.png}	\N
95	Nichole Daniels	\N	13	\N	10	{"Roman Catholic"}	230	{/img/characters/serie/Nichole_Daniels.png}	\N
97	William Daniels	\N	13	\N	\N	\N	230	{/img/characters/serie/William_Daniels.png}	\N
98	Rex	\N	14	\N	\N	\N	4	{/img/characters/serie/Rex.png}	\N
99	Clyde Donovan	\N	14	April 10th	10	{"Roman Catholic"}	2	{/img/characters/serie/Clyde_Donovan.png}	\N
100	Betsy Donovan	\N	14	\N	\N	{"Roman Catholic"}	136	{/img/characters/serie/Betsy_Donovan.png}	\N
101	Roger Donovan	\N	14	\N	\N	{"Roman Catholic"}	87	{/img/characters/serie/Roger_Donovan.png}	\N
102	Larry Feegan	\N	15	\N	13	\N	220	{/img/characters/serie/Larry_Feegan.png}	\N
103	Mrs. Feegan	\N	15	\N	\N	\N	220	{/img/characters/serie/Mrs_Feegan.png}	\N
104	Mr. Feegan	\N	15	\N	\N	\N	220	{/img/characters/serie/Mr_Feegan.png}	\N
105	Mrs. Garrison Senior	\N	16	\N	\N	\N	48	{/img/characters/serie/Mrs_Garrison.png}	\N
106	Mr. Garrison Senior	\N	16	\N	\N	\N	48	{/img/characters/serie/Mr_Garrison.png}	\N
107	Sophie Gray	\N	17	\N	10	\N	306	{/img/characters/serie/Sophie_Gray.png}	\N
108	Mrs. Gray	\N	17	\N	\N	\N	306	{/img/characters/serie/Mrs_Gray.png}	\N
109	Mr. Hakeem	\N	50	\N	\N	{Islam}	157	{/img/characters/serie/Mr_Hakeem.png}	\N
110	Bridon Gueermo	\N	18	\N	9	\N	180	{/img/characters/serie/Bridon_Gueermo.png}	\N
111	Mrs. Gueermo	\N	18	\N	\N	\N	180	{/img/characters/serie/Mrs_Gueermo.png}	\N
112	Mr. Gueermo	\N	18	\N	\N	\N	180	{/img/characters/serie/Mr_Gueermo.png}	\N
113	Baahir Hassan Abdul Hakeem	\N	50	\N	8	{Islam}	157	{/img/characters/serie/Baahir.png}	\N
114	Mrs. Hakeem	\N	50	\N	\N	{Islam}	157	{/img/characters/serie/Mrs_Hakeem.png}	\N
115	Simon Hankey	\N	19	\N	\N	\N	65	{/img/characters/serie/Simon_Hankey.png}	\N
116	Amber Hankey	\N	19	\N	\N	\N	65	{/img/characters/serie/Amber_Hankey.png}	\N
117	Cornwallis Hankey	\N	19	\N	\N	\N	65	{/img/characters/serie/Cornwallis_Hankey.png}	\N
118	Autumn Hankey	\N	19	\N	\N	\N	65	{/img/characters/serie/Autumn_Hankey.png}	\N
119	Mr. Hankey	\N	19	\N	\N	\N	9	{/img/characters/serie/Mr_Hankey.png}	\N
120	Chad Handler	\N	21	\N	10	{Judaism}	113	{/img/characters/serie/Chad_Harrison.png}	\N
121	Louis Handler	\N	21	\N	10	{Judaism}	42	{/img/characters/serie/Louse_Handler.png}	\N
122	Mrs. Handler	\N	21	\N	\N	{Judaism}	22	{/img/characters/serie/Mrs_Handler.png}	\N
123	Mr. Handler	\N	21	\N	\N	{Judaism}	66	{/img/characters/serie/Mr_Handler.png}	\N
124	Amanda Harrison	\N	20	\N	\N	{Mormon}	108	{/img/characters/serie/Amanda_Harrison.png}	\N
125	Dave Harrison	\N	20	\N	\N	{Mormon}	108	{/img/characters/serie/Dave_Harrison.png}	\N
126	Jenny Harrison	\N	20	\N	\N	{Mormon}	108	{/img/characters/serie/Jenny_Harrison.png}	\N
127	Gary Harrison	\N	20	\N	10	{Mormon}	108	{/img/characters/serie/Gary_Harrison.png}	\N
128	Mark Harrison	\N	20	\N	\N	{Mormon}	108	{/img/characters/serie/Mark_Harrison.png}	\N
129	Mrs. Harrison	\N	20	\N	\N	{Mormon}	108	{/img/characters/serie/Mrs_Harrison.png}	\N
130	Mr. Harrison	\N	20	\N	\N	{Mormon}	108	{/img/characters/serie/Mr_Harrison.png}	\N
131	Mrs. Larsen	\N	26	\N	\N	{"Roman Catholic"}	77	{/img/characters/serie/Mrs_Larsen.png}	\N
132	Flora Larsen	\N	26	\N	5	{"Roman Catholic"}	60	{/img/characters/serie/Flora_Larsen.png}	\N
133	Millie Larsen	\N	26	\N	10	{"Roman Catholic"}	77	{/img/characters/serie/Millie_Larsen.png}	\N
134	Mrs. Knitts	\N	22	\N	\N	{"Roman Catholic"}	123	{/img/characters/serie/Mrs_Knitts.png}	\N
135	Annie Knitts	\N	22	\N	10	{"Roman Catholic"}	36	{/img/characters/serie/Annie_Knitts.png}	\N
136	Mr. Mackey Senior	\N	25	\N	\N	\N	313	{/img/characters/serie/Mrs_Mackey_Senior.png}	\N
137	Mrs. Mackey Senior	\N	25	\N	\N	\N	90	{/img/characters/serie/Mr_Mackey_Senior.png}	\N
138	Mr. Mackey	\N	25	\N	50	{"Roman Catholic"}	9	{/img/characters/serie/Mr_Mackey.png}	\N
139	Clark Malkinson	\N	24	\N	\N	\N	306	{/img/characters/serie/Clark_Malkinson.png}	\N
140	Ellen Malkinson	\N	24	\N	\N	\N	306	{/img/characters/serie/Ellen_Malkinson.png}	\N
141	Scott Malkinson	\N	24	\N	10	\N	117	{/img/characters/serie/Scott_Malkinson.png}	\N
142	Michael's Mom	\N	29	\N	\N	\N	241	{/img/characters/serie/Michael_Dad.png}	\N
143	Michael	\N	29	\N	11	{Unconfirmed,"Cult of Cthulhu (Formerly)"}	110	{/img/characters/serie/Michael.png}	\N
144	Dr. Alphonse Mephesto	\N	30	\N	\N	\N	5	{/img/characters/serie/Dr_Mephesto.png}	\N
145	Kevin Mephesto	\N	30	\N	\N	\N	5	{/img/characters/serie/Kevin_Mephesto.png}	\N
146	Terrance Mephesto	\N	30	\N	9	\N	5	{/img/characters/serie/Terrance_Mephesto.png}	\N
147	Thomas McElroy	\N	27	\N	\N	\N	34	{/img/characters/serie/Thomas_McElroy.png}	\N
148	Nellie McElroy	\N	27	\N	\N	\N	34	{/img/characters/serie/Nellie_McElroy.png}	\N
149	Mr. McArthur	\N	23	\N	\N	{"Roman Catholic"}	184	{/img/characters/serie/Mr_McArthur.png}	\N
150	Moira McArthur	\N	23	\N	\N	{"Roman Catholic"}	177	{/img/characters/serie/Moira_McArthur.png}	\N
151	Red McArthur	\N	23	\N	10	{"Roman Catholic"}	10	{/img/characters/serie/Red_McArthur.png}	\N
152	Nelly's Mom	\N	28	\N	\N	{"Roman Catholic"}	240	{/img/characters/serie/Nelly_Dad.png}	\N
153	Nelly	\N	28	\N	10	{"Roman Catholic"}	167	{/img/characters/serie/Nelly.png}	\N
154	Michael's Dad	\N	29	\N	\N	\N	241	{/img/characters/serie/Michael_Mom.png}	\N
155	Margaret Nelson	\N	32	June 18th	35	{"Roman Catholic"}	260	{/img/characters/serie/Liza_Nelson.png}	\N
156	Liza Nelson	\N	32	\N	10	{"Roman Catholic"}	260	{/img/characters/serie/Margaret_Nelson.png}	\N
157	Matt	\N	28	\N	\N	{"Roman Catholic"}	215	{/img/characters/serie/Nelly_Mom.png}	\N
158	Riley	\N	31	\N	0	\N	290	{/img/characters/serie/Riley.png}	\N
159	Bailey	\N	31	\N	0	\N	290	{/img/characters/serie/Bailey.png}	\N
160	Harper	\N	31	\N	0	\N	290	{/img/characters/serie/Harper.png}	\N
161	Emory	\N	31	\N	0	\N	290	{/img/characters/serie/Emory.png}	\N
162	River	\N	31	\N	0	\N	290	{/img/characters/serie/River.png}	\N
163	Strong Woman	\N	31	\N	\N	\N	286	{/img/characters/serie/Strong_Woman.png}	\N
164	Peter "PC Principal" Charles	\N	31	\N	\N	{Christian}	258	{/img/characters/serie/PC_Principal.png}	\N
165	DogPoo Petuski	\N	38	\N	10	\N	85	{/img/characters/serie/Dog_Poo.png}	\N
166	Mrs. Petuski	\N	38	\N	\N	\N	33	{/img/characters/serie/Mrs_Petuski.png}	\N
167	Mr. Petuski	\N	38	\N	\N	\N	9	{/img/characters/serie/Mr_Petuski.png}	\N
168	David Rodriguez	\N	37	\N	10	\N	261	{/img/characters/serie/David_Rodriguez.png}	\N
169	Mrs. Rodriguez	\N	37	\N	\N	\N	261	{/img/characters/serie/Mrs_Rodriguez.png}	\N
170	Mr. Rodriguez	\N	37	\N	\N	\N	261	{/img/characters/serie/Mr_Rodriguez.png}	\N
171	Bebe Stevens	\N	38	August 13th	10	{"Roman Catholic"}	2	{/img/characters/serie/Bebe_Stevens.png}	\N
172	Thumper	\N	38	\N	\N	\N	170	{/img/characters/serie/Thumper.png}	\N
173	Mrs. Stevens	\N	38	\N	\N	{"Roman Catholic"}	16	{/img/characters/serie/Mrs_Stevens.png}	\N
174	Mr. Stevens	\N	38	\N	\N	{"Roman Catholic"}	123	{/img/characters/serie/Mr_Stevens.png}	\N
175	Kevin Stoley	\N	35	\N	10	{"Roman Catholic"}	18	{/img/characters/serie/Kevin_Stoley.png}	\N
176	Mrs. Stoley	\N	35	\N	\N	{"Roman Catholic"}	95	{/img/characters/serie/Mrs_Stoley.png}	\N
177	Mr. Stoley	\N	35	\N	\N	{"Roman Catholic"}	95	{/img/characters/serie/Mr_Stoley.png}	\N
178	Chaos Hamsters	\N	34	\N	\N	\N	85	{/img/characters/serie/Chaos_Hamsters.png}	\N
179	Terrance Henry Stoot	\N	33	Octuber 20th	54	\N	6	{/img/characters/serie/Terrance.png}	\N
180	Sally Dion	\N	33	\N	\N	\N	14	{/img/characters/serie/Sally_Dion.png}	\N
181	Katie Queef	\N	33	\N	\N	\N	185	{/img/characters/serie/Katie_Queef.png}	\N
182	Streibel Daughters	\N	39	\N	\N	\N	99	{/img/characters/serie/Streibel_Daughters.png}	\N
183	Mrs. Streibel	\N	39	\N	\N	\N	99	{/img/characters/serie/Mrs_Streibel.png}	\N
184	Mr. Streibel	\N	39	\N	\N	\N	99	{/img/characters/serie/Mr_Streibel.png}	\N
185	Scott Tenorman	\N	40	\N	15	\N	69	{/img/characters/serie/Scott_Tenorman.png}	\N
186	Mrs. Tenorman	\N	40	\N	41	\N	69	{/img/characters/serie/Mrs_Tenorman.png}	\N
187	Jack Tenorman	\N	40	\N	43	\N	69	{/img/characters/serie/Jack_Tenorman.png}	\N
188	Wendy Testaburger	\N	41	\N	10	\N	1	{/img/characters/serie/Wendy_Testaburger.png}	\N
189	Grandma Testaburger	\N	41	\N	\N	\N	176	{/img/characters/serie/Grandma_Testaburger.png}	\N
190	Alexis Testaburger	\N	41	\N	\N	\N	89	{/img/characters/serie/Alexis_Testaburger.png}	\N
191	Mr. Testaburger	\N	41	\N	\N	\N	123	{/img/characters/serie/Mr_Testaburger.png}	\N
192	Damien Thorn	\N	42	\N	9	{Satanism}	10	{/img/characters/serie/Damien_Thorn.png}	\N
193	Satan	\N	42	\N	\N	{Satanism}	10	{/img/characters/serie/Satan.png}	t
194	Heidi Turner	\N	44	\N	10	{Christian}	32	{/img/characters/serie/Heidi_Turner.png}	\N
195	Robby	\N	44	\N	\N	{Christian}	61	{/img/characters/serie/Robby.png}	\N
196	Nancy Turner	\N	44	\N	\N	{"Roman Catholic"}	58	{/img/characters/serie/Nancy_Turner.png}	\N
197	Thomas Turner	\N	44	\N	\N	{Christian}	58	{/img/characters/serie/Thomas_Turner.png}	\N
198	Ryan Valmer	\N	47	\N	\N	\N	98	{/img/characters/serie/Ryan_Valmer.png}	\N
199	Jimmy Valmer	\N	47	\N	10	\N	67	{/img/characters/serie/Jimmy_Valmer.png}	\N
200	Sarah Valmer	\N	47	\N	\N	\N	98	{/img/characters/serie/Sarah_Valmer.png}	\N
201	Larry Zewiski	\N	45	\N	10	\N	296	{/img/characters/serie/Larry_Zewiski.png}	\N
202	Mrs. Zewiski	\N	45	\N	\N	\N	297	{/img/characters/serie/Mrs_Zewiski.png}	\N
203	Mr. Zewiski	\N	45	\N	\N	\N	296	{/img/characters/serie/Mr_Zewiski.png}	\N
204	Panamanian Padengo Pequeño	\N	46	\N	4	\N	303	{/img/characters/serie/Panamanian_Padengo_Pequeño.png}	\N
205	Alejandro	\N	46	\N	\N	\N	303	{/img/characters/serie/Alejandro_White.png}	\N
206	Crystal White	\N	46	\N	5	\N	287	{/img/characters/serie/Crystal_White.png}	\N
207	Jason White	\N	46	\N	10	\N	5	{/img/characters/serie/Jason_White.png}	\N
208	Mrs. White	\N	46	\N	\N	\N	287	{/img/characters/serie/Mrs_White.png}	\N
209	Bob White	\N	46	\N	\N	\N	287	{/img/characters/serie/Bob_White.png}	\N
210	Carlos	\N	\N	\N	\N	\N	95	{/img/characters/serie/Carlos.png}	\N
213	Aaron Hagen	\N	51	\N	7	\N	239	{/img/characters/serie/Aaron_Hagen.png}	f
214	Abraham Lincoln	\N	\N	February 12th	56	\N	135	{/img/characters/serie/Abraham_Lincoln.png}	t
217	Adams County Pee-Wee Hockey Team	\N	\N	\N	6	\N	153	{/img/characters/serie/Adams_County_Pee_Wee_Hockey_Team.png}	f
218	Adolf Hitler	\N	52	April 20th	56	\N	7	{/img/characters/serie/Adolf_Hitler.png}	t
220	Agent Connelly	\N	\N	\N	\N	\N	44	{/img/characters/serie/Agent_Connelly.png}	f
221	Agent Fields	\N	\N	\N	\N	\N	44	{/img/characters/serie/Agent_Fields.png}	f
222	"Agent" Tucker	\N	\N	\N	\N	\N	102	{/img/characters/serie/Agent_Tucker.png}	f
223	Aging Hippie Liberal Douche	\N	\N	\N	\N	\N	118	{/img/characters/serie/AGING_HIPPIE_LIBERAL_DOUCHE.png}	f
228	Al Pacino	\N	\N	April 25th	85	{Catholic}	257	{/img/characters/serie/Al_Pacino.png}	t
229	Albert Lincoln Roker Jr	\N	\N	August 20th	71	\N	197	{/img/characters/serie/Al_Roker.png}	t
231	Alan the Security Guard	\N	\N	\N	\N	\N	41	{/img/characters/serie/Alan_The_Security_Guard.png}	f
232	Alana "Honey Boo Boo" Thompson	\N	\N	August 28th	7	{Christian}	232	{/img/characters/serie/Honey_Boo_Boo.png}	t
233	Alanis Morissette	\N	\N	June 1st	51	{Buddhist}	27	{/img/characters/serie/Alanis_Morissette.png}	t
234	Alcoholics Anonymous Boy	\N	\N	\N	\N	\N	139	{/img/characters/serie/Alcoholics_Anonymous_Boy.png}	f
236	Alex Glick	\N	\N	\N	\N	\N	103	{/img/characters/serie/Alex_Glick.png}	t
237	Alex Hart	\N	\N	\N	\N	\N	166	{/img/characters/serie/Alex_Hart.png}	\N
238	Alexa	\N	\N	\N	\N	\N	278	{/img/characters/serie/Alexa.png}	t
239	Ali Khamenei	\N	\N	July 16th	86	{"Shia Islam"}	243	{/img/characters/serie/Ali_Khamenei.png}	\N
240	Alice	\N	53	\N	\N	\N	63	{/img/characters/serie/Alice.png}	\N
241	Alice's Parents	\N	53	\N	\N	\N	63	{/img/characters/serie/Alice's_Parents.png}	\N
242	Alinicia	\N	\N	\N	\N	\N	61	{/img/characters/serie/Alinicia.png}	\N
243	Allen Ginsberg	\N	\N	June 23th	70	{Buddhist}	57	{/img/characters/serie/Allen_Ginsberg.png}	\N
244	Allen Varcas	\N	54	\N	10	\N	130	{/img/characters/serie/Allen_Varcas.png}	\N
245	Allie Nelson	\N	\N	\N	10	\N	167	{/img/characters/serie/Allie_Nelson.png}	\N
246	Allied Atheist Alliance (AAA)	\N	\N	\N	\N	\N	151	{/img/characters/serie/Allied_Atheist_Alliance.png}	\N
247	Allison	\N	\N	\N	\N	\N	159	{/img/characters/serie/Allison.png}	\N
248	Allison Mertz	\N	\N	\N	6	\N	181	{/img/characters/serie/Allison_Mertz.png}	\N
249	Alois and Klara Hitler	\N	\N	\N	\N	\N	46	{/img/characters/serie/Hitler_Parents.png}	t
250	Alton Crawford Brown Jr	\N	\N	July 30th	63	\N	209	{/img/characters/serie/Alton_Brown.png}	t
251	Amanda	\N	\N	\N	\N	\N	49	{/img/characters/serie/Amanda.png}	\N
252	Ambassador of Humans	\N	\N	\N	\N	\N	226	{/img/characters/serie/Ambassador_of_Humans.png}	\N
253	America's Most Wanted Actors	\N	\N	\N	\N	\N	15	{/img/characters/serie/America's_Most_Wanted.png}	\N
254	American Association of Retired Persons	\N	\N	\N	\N	\N	106	{/img/characters/serie/American_Association_of_Retired_Persons.png}	\N
255	Amir	\N	\N	\N	13	\N	173	{/img/characters/serie/Amir.png}	\N
256	Anchorman	\N	\N	\N	\N	\N	46	{/img/characters/serie/Anchorman.png}	\N
257	Anderson Cooper	\N	\N	June 3th	58	\N	243	{/img/characters/serie/Anderson_Cooper.png}	t
258	Andrew Sutherland	\N	\N	\N	\N	\N	176	{/img/characters/serie/Andrew_Sutherland.png}	\N
219	Afro Ninja	\N	\N	\N	\N	\N	171	{/img/characters/serie/Afro_Ninja.png}	t
215	Adam Borque	\N	\N	\N	\N	\N	281	{/img/characters/serie/Adam_Borque.png}	f
224	Airport Security Guard	\N	\N	\N	\N	\N	76	{/img/characters/serie/Airport_Security_Guard.png}	f
211	A 34-Year-Old Asian Man Who Looks Strikingly Similar to Ricardo Montalbán	\N	\N	\N	34	\N	24	{/img/characters/serie/23_Year_Asian_Reporter.png}	f
306	Beth (Dawg's Bitch)	\N	\N	\N	\N	\N	149	{/img/characters/serie/Beth_Bitch.png}	f
307	Betsy ("D-Yikes!")	\N	\N	\N	\N	\N	159	{/img/characters/serie/Betsy_D_Yikes.png}	f
308	Betsy MacIntosh	\N	\N	\N	\N	\N	214	{/img/characters/serie/Betsy_MacIntosh.png}	f
309	Betsy	\N	\N	\N	10	\N	309	{/img/characters/serie/Betsy_Labubu_Girl.png}	f
310	Big Black Scary Monster	\N	\N	\N	\N	\N	20	{/img/characters/serie/The_Big_Black_Scary_Monster.png}	f
311	Big Gay Al	\N	49	\N	\N	\N	4	{/img/characters/serie/Big_Gay_Al.png}	f
312	Big Mesquite Murph	\N	\N	\N	\N	\N	309	{/img/characters/serie/Big_Mesquite_Murph.png}	f
313	Biggest Douche in the Universe Committee	\N	\N	\N	\N	\N	94	{/img/characters/serie/Biggest_Douche_Judges.png}	f
259	Angela Merkel	\N	\N	July 17th	71	{Lutheran}	187	{/img/characters/serie/Angela_Merkel.png}	t
260	Angelina Jolie	\N	\N	June 4th	50	{"Former Roman Catholic"}	156	{/img/characters/serie/Angelina_Jolie_Voight.png}	t
261	Angus T. Jones	\N	\N	October 8th	31	{Adventist}	203	{/img/characters/serie/Angus_T_Jones.png}	t
262	Animal Liberation Front	\N	\N	\N	\N	\N	138	{/img/characters/serie/ALF_Members.png}	\N
263	Ann Curry	\N	\N	November 19th	68	\N	197	{/img/characters/serie/Ann_Curry.png}	t
264	Annie Bartlett	\N	\N	\N	11	\N	181	{/img/characters/serie/Annie_Bartlett.png}	\N
265	Anonymous821	\N	\N	\N	\N	\N	271	{/img/characters/serie/Anonymous821.png}	\N
266	Anthony Fauci	\N	\N	December 24th	84	\N	308	{/img/characters/serie/Anthony_Fauci.png}	\N
267	Anthony Webster	\N	\N	\N	\N	\N	271	{/img/characters/serie/Anthony_Webster.png}	\N
268	Anthropologist	\N	\N	\N	\N	\N	12	{/img/characters/serie/Anthropologist.png}	\N
269	Anti-Christ	\N	\N	\N	\N	{Satanism}	125	{/img/characters/serie/Anti_Christ.png}	\N
270	Apple Replacement Friend	\N	\N	\N	\N	\N	210	{/img/characters/serie/Apple_Replacement_Friend.png}	\N
271	Dr. Apu Nahasapeemapetilon, Ph.D. Jr.	\N	\N	\N	38	{Hinduism}	290	{/img/characters/serie/Apu.png}	\N
272	Archangel Michael	\N	\N	\N	\N	\N	129	{/img/characters/serie/Archangel_Michael.png}	f
273	Arnold Schwarzenegger	\N	\N	July 30th	78	{"Roman Catholic"}	204	{/img/characters/serie/Arnold_Schwarzenegger.png}	t
274	"Ash Ketchum"	\N	\N	\N	10	\N	42	{/img/characters/serie/Ash_Ketchum.png}	\N
275	Ashley	\N	\N	\N	10	\N	190	{/img/characters/serie/Ashley.png}	\N
276	Aslan the Lion	\N	\N	\N	\N	\N	77	{/img/characters/serie/Aslan.png}	\N
277	Aunt Jemima	\N	\N	\N	\N	\N	249	{/img/characters/serie/Aunt_Jemima.png}	\N
212	Aaron Brown	\N	\N	November 10th	76	\N	118	{/img/characters/serie/Aaron_brown.png}	t
216	Adam Sandler	\N	\N	September 9th	58	{Judaism}	211	{/img/characters/serie/Adam_Sandler.png}	t
225	Airsoft Armory Salesman	\N	\N	\N	\N	\N	314	{/img/characters/serie/Airsoft_Armory_Salesman.png}	\N
226	Al Gore	\N	\N	March 31th	77	{Baptist}	45	{/img/characters/serie/Al_Gore.png}	t
227	Al-Qaeda	\N	\N	\N	\N	\N	74	{/img/characters/serie/Al_Qaeda.png}	t
230	Alan Jackson	\N	\N	Octuber 17th	66	{Christian}	91	{/img/characters/serie/Al_Jackson.png}	t
235	Alec Vaughn	\N	\N	\N	\N	\N	294	{/img/characters/serie/Alec_Vaughn.png}	\N
278	Baby Cows	\N	\N	\N	\N	\N	83	{/img/characters/serie/Baby_Cows.png}	f
279	Kevern Zaksor (Baby Fark McGee-zax)	\N	\N	\N	\N	\N	187	{/img/characters/serie/Kevern_Zaksor.png}	f
280	Grogu (Baby Yoda)	\N	\N	\N	\N	\N	306	{/img/characters/serie/Grogu.png}	t
281	Babylonians	\N	\N	\N	\N	\N	15	{/img/characters/serie/Babylonians.png}	f
282	Bakery Napoleon Bakers	\N	\N	\N	\N	\N	150	{/img/characters/serie/Bakery_Napoleon_Bakers.png}	f
283	Barack Hussein Obama II	\N	55	August 4	64	{Protestant}	169	{/img/characters/serie/Barack_Obama.png}	t
284	Barbara Garthunk	\N	\N	\N	\N	\N	75	{/img/characters/serie/Barbara_Garthunk.png}	f
285	Barbra Streisand	\N	\N	April 24	83	{Judaism}	12	{/img/characters/serie/Barbra_Streisand.png}	t
286	Barkley	\N	\N	\N	\N	\N	226	{/img/characters/serie/Barkley.png}	f
287	Barky	\N	\N	\N	\N	\N	14	{/img/characters/serie/Barky.png}	f
288	Barry Bonds	\N	\N	July 24	61	\N	113	{/img/characters/serie/Barry_Bonds.png}	t
289	Bartholomew "Bart" JoJo Simpson	\N	56	April 1 or February 23	10	{Christian}	143	{/img/characters/serie/Bart_Simpson.png}	t
290	Bartender	\N	\N	\N	\N	\N	4	{/img/characters/serie/Bartender.png}	f
291	Bartles	\N	\N	\N	\N	\N	25	{/img/characters/serie/Bartles.png}	f
292	Basketball Coach	\N	\N	\N	\N	\N	126	{/img/characters/serie/Basketball_Coach.png}	f
293	Beatrice Arthur	\N	\N	May 13	86	{Judaism}	189	{/img/characters/serie/Beatrice_Arthur.png}	t
294	Beach Family ("Insecurity")	\N	\N	\N	\N	\N	233	{/img/characters/serie/Beach_Family.png}	f
295	Beast	\N	\N	\N	\N	\N	299	{/img/characters/serie/Beast.png}	t
296	Beatrice McGullicutty	\N	\N	\N	\N	{"Roman Catholic"}	282	{/img/characters/serie/Beatrice_McGullicutty.png}	f
297	Belarusian Farmers	\N	\N	\N	\N	\N	236	{/img/characters/serie/Belarusian_Farmers.png}	f
298	Ben ("Blizzard" Staff)	\N	\N	\N	\N	\N	147	{/img/characters/serie/Ben_Blizzard.png}	f
299	Benjamin Géza Affleck-Boldt	\N	57	August 15	53	{Methodist}	75	{/img/characters/serie/Ben_Affleck.png}	t
300	Ben Roethlisberger	\N	\N	March 2	43	{Methodist}	196	{/img/characters/serie/Ben_Roethlisberger.png}	t
301	Benjamin Franklin	\N	\N	January 17	84	{Deist}	100	{/img/characters/serie/Benjamin_Franklin.png}	t
302	Benny	\N	\N	\N	\N	\N	184	{/img/characters/serie/Benny.png}	f
303	Benny Hill	\N	\N	January 21	68	\N	78	{/img/characters/serie/Benny_Hill.png}	t
304	Best Buy President	\N	\N	\N	\N	\N	210	{/img/characters/serie/Best_Buy_President.png}	f
305	Beth	\N	\N	\N	10	\N	123	{/img/characters/serie/Beth.png}	f
314	Bill Allen	\N	\N	\N	10	\N	4	{/img/characters/serie/Bill_Allen.png}	f
315	William Jefferson "Bill" Clinton	\N	58	August 19	79	{Baptist}	15	{/img/characters/serie/Bill_Clinton.png}	t
316	Bill Cosby	\N	\N	July 12	88	{Protestant}	77	{/img/characters/serie/Bill_Cosby.png}	t
317	Bill Cosby (BSM-471)	\N	\N	\N	\N	\N	60	{/img/characters/serie/Bill_Cosby_BSM_471.png}	f
318	Bill Denkins	\N	\N	\N	\N	\N	1	{/img/characters/serie/Bill_Denkins.png}	f
319	Bill Donohue	\N	\N	July 18	78	{"Roman Catholic"}	158	{/img/characters/serie/Bill_Donahue.png}	t
320	Bill Gates	\N	\N	October 28	69	{"Roman Catholic"}	76	{/img/characters/serie/Bill_Gates.png}	t
321	Bill Norman	\N	\N	\N	\N	\N	264	{/img/characters/serie/Bill_Norman.png}	f
322	Bill O'Reilly	\N	\N	September 10	76	{"Roman Catholic"}	118	{/img/characters/serie/Bill_Oreilly.png}	t
323	William Forrester Owens	\N	\N	October 22	74	\N	88	{/img/characters/serie/Bill_Owens.png}	t
324	Bill Stewart	\N	\N	\N	\N	\N	106	{/img/characters/serie/Bill_Stewart.png}	f
325	Bill Yellow Hawk	\N	\N	\N	\N	\N	280	{/img/characters/serie/Bill_Yellow_Hawk.png}	f
326	Billy (Kindergartner)	\N	\N	\N	\N	\N	60	{/img/characters/serie/Kindergartener_Billy.png}	f
327	Billy ("Sons A Witches")	\N	\N	\N	10	\N	283	{/img/characters/serie/Billy_Sons_A_Witches.png}	f
328	Billy Bob Thornton	\N	\N	August 4	70	{Agnostic}	196	{/img/characters/serie/Billy_Bob_Thornton.png}	t
329	Billy Circlovich	\N	\N	\N	\N	\N	49	{/img/characters/serie/Billy_Circlovich.png}	f
330	Billy Harris	\N	\N	\N	\N	\N	60	{/img/characters/serie/Billy_Harris.png}	f
331	Billy Martin	\N	\N	\N	10	\N	122	{/img/characters/serie/Billy_Martin.png}	f
332	William Darrell "Billy" Mays Jr	\N	\N	July 20	50	{Christian}	189	{/img/characters/serie/Billy_Mays.png}	t
333	Billy Miller	\N	\N	\N	\N	\N	198	{/img/characters/serie/Billy_Miller.png}	f
334	Billy Thompson	\N	\N	\N	10	\N	205	{/img/characters/serie/Billy_Thompson.png}	f
335	Billy Turner	\N	\N	\N	9	\N	132	{/img/characters/serie/Billy_Turner.png}	f
336	Birthday Party Parents	\N	\N	\N	\N	\N	255	{/img/characters/serie/Birthday_Party_Parents.png}	f
337	Bishop of Banff	\N	\N	\N	\N	\N	212	{/img/characters/serie/Bishop_Of_Banff.png}	f
338	Black-Haired Scientist	\N	\N	\N	\N	\N	164	{/img/characters/serie/Black_Haired_Scientist.png}	f
339	Black Panther	\N	\N	\N	\N	\N	299	{/img/characters/serie/Black_Panther.png}	t
340	Blanket Jackson	\N	59	February 21	2	\N	117	{/img/characters/serie/Blanket_Jackson.png}	t
341	Blaze	\N	\N	\N	\N	\N	102	{/img/characters/serie/Blaze.png}	f
342	Blink-182	\N	\N	\N	\N	\N	105	{/img/characters/serie/Blink_182.png}	t
343	Blinky's Airsoft Referee	\N	\N	\N	\N	\N	314	{/img/characters/serie/Blinky's_Airsoft_Referee.png}	f
344	Blockbuster Employee's Ghost	\N	\N	\N	\N	\N	235	{/img/characters/serie/Blockbuster_Employee's_Ghost.png}	f
345	Blonde-Haired Girl ("Erection Day")	\N	\N	\N	\N	\N	132	{/img/characters/serie/Blonde-Haired_Girl.png}	f
346	Bloods (Gang)	\N	\N	\N	\N	\N	98	{/img/characters/serie/Blonde-The_Bloods.png}	f
347	Bloody Sunday: The Dangers of Memeing narrator	\N	\N	\N	\N	\N	226	{/img/characters/serie/Bloody_Sunday_The_Dangers_of_Memeing_narrator.png}	f
348	Bob Denver	\N	\N	January 9	70	\N	19	{/img/characters/serie/Bob_Denver.png}	t
349	Bob Dole	\N	\N	July 22	98	{Methodist}	33	{/img/characters/serie/Bob_Dole.jpg}	t
350	Bob Ferrin	\N	\N	\N	\N	\N	78	{/img/characters/serie/Bob_Ferrin.png}	f
351	Bob Johnson	\N	\N	\N	\N	\N	2	{/img/characters/serie/Bob_Johnson.png}	f
352	Bob Saget	\N	\N	January 9	65	{Judaism}	13	{/img/characters/serie/Bob_Saget.png}	f
353	Bob Summers	\N	\N	\N	\N	\N	169	{/img/characters/serie/Bob_Summers.png}	f
354	Bob Thomas	\N	\N	\N	\N	\N	18	{/img/characters/serie/Bob_Thomas.png}	f
355	Bobby	\N	\N	\N	\N	\N	226	{/img/characters/serie/Bobby.png}	f
356	Bobby ("Cartman Joins NAMBLA")	\N	\N	\N	\N	\N	53	{/img/characters/serie/Bobby_Nambla.png}	f
357	Robert William Flay	\N	\N	December 10	60	{Catholic}	209	{/img/characters/serie/Bobby_Flay.png}	t
358	Bobby Palmer	\N	60	\N	\N	\N	176	{/img/characters/serie/Bobby_Palmer.png}	f
359	Bono	\N	\N	May 10	65	{Christian}	162	{/img/characters/serie/Bono.png}	t
360	Bono's Butler	\N	\N	\N	\N	\N	162	{/img/characters/serie/Bono's_Butler.png}	f
361	Book Mobile Driver	\N	\N	\N	\N	\N	17	{/img/characters/serie/Booktastic_Bus_Driver.png}	f
362	Boom Microphone Operator	\N	\N	\N	\N	\N	2	{/img/characters/serie/Boom_Microphone_Operator.png}	f
363	Boris Johnson	\N	\N	June 19	61	{"'Church of England'"}	275	{/img/characters/serie/Boris_Johnson.png}	t
364	Boston	\N	\N	\N	\N	\N	269	{/img/characters/serie/Boston.png}	t
365	Boy in Finn Costume	\N	\N	\N	\N	\N	235	{/img/characters/serie/Boy_in_Finn_Costume.png}	f
366	Quest for Ratings	\N	\N	\N	\N	\N	122	{/img/characters/serie/Boy_with_Blond_Hair.png}	f
367	Boy with Brown Hair	\N	\N	\N	\N	\N	223	{/img/characters/serie/Boy_with_Brown_Hair.png}	f
368	Boy with Brown Hair and Red Shirt	\N	\N	\N	\N	\N	122	{/img/characters/serie/Boy_with_Brown_Hair_and_Red_Shirt.png}	f
369	Boy with C Cap	\N	\N	\N	\N	\N	34	{/img/characters/serie/Boy_with_C_Cap.png}	f
370	Boy with Dark Green Shirt and Glasses	\N	\N	\N	\N	\N	36	{/img/characters/serie/Boy_with_Dark_Green_Shirt_and_Glasses.png}	f
371	Boy with Earmuffs	\N	\N	\N	\N	\N	36	{/img/characters/serie/Boy_with_Earmuffs.png}	f
372	Boy with Green Shirt	\N	\N	\N	\N	\N	226	{/img/characters/serie/Boy_with_Green_Shirt.png}	f
373	Boy with Huge Glasses	\N	\N	\N	\N	\N	58	{/img/characters/serie/Boy_with_Huge_Glasses.png}	f
374	Boy with Olive Shirt and Black Pants	\N	\N	\N	\N	\N	9	{/img/characters/serie/Boy_with_olive_shirt_andb_lack_pants.png}	f
375	Boy with Orange Shirt	\N	\N	\N	\N	\N	122	{/img/characters/serie/Boy_with_orange_shirt.png}	f
376	Boy with Red Shirt	\N	\N	\N	\N	\N	20	{/img/characters/serie/Boy_with_red_shirt.png}	f
377	Boy with Red Shirt and Blue Pants	\N	\N	\N	\N	\N	136	{/img/characters/serie/Boy_with_red_shirt_blue_pants.png}	f
378	Brad	\N	\N	\N	\N	\N	258	{/img/characters/serie/Brad.png}	f
379	Brad Davis	\N	\N	July 20	\N	\N	179	{/img/characters/serie/Brad_Davis.png}	t
380	Brad Morgan	\N	\N	\N	\N	\N	118	{/img/characters/serie/Brad_Morgan.png}	\N
381	Brad Paisley	\N	\N	October 28	52	\N	230	{/img/characters/serie/Brad_Paisley.png}	t
382	Bradley	\N	\N	\N	\N	\N	155	{/img/characters/serie/Bradley.png}	f
383	Brandon Carlile	\N	\N	\N	\N	\N	250	{/img/characters/serie/Brandon_Carlile.png}	f
384	Brett	\N	\N	\N	\N	\N	166	{/img/characters/serie/Brett.png}	f
385	Brett Favre	\N	\N	\N	\N	\N	21	{/img/characters/serie/Brett_Favre.png}	f
386	Brian	\N	\N	\N	\N	\N	143	{/img/characters/serie/Brian.png}	f
387	Brian ("Free Willzyx")	\N	\N	\N	\N	\N	138	{/img/characters/serie/Brian_Willzyx.png}	f
388	Brian ("The Losing Edge")	\N	\N	\N	\N	\N	130	{/img/characters/serie/Brian_The_Losing_Edge.png}	f
389	Brian Boitano	\N	\N	October 22	61	\N	4	{/img/characters/serie/Brian_Boitano.png}	t
390	Brian Boyant	\N	\N	\N	\N	\N	265	{/img/characters/serie/Brian_Boyant.png}	f
391	Brian Dennehy	\N	\N	July 9	81	{"Roman Catholic"}	200	{/img/characters/serie/Brian_Dennehy.png}	t
392	Brian Griffin	\N	\N	\N	8	\N	142	{/img/characters/serie/Brian_Griffin.png}	t
393	Brian Jeffries	\N	\N	\N	\N	\N	157	{/img/characters/serie/Brian_Jeffries.png}	f
394	Brian Thompson-Jarvis	\N	\N	\N	\N	\N	141	{/img/characters/serie/Brian_Thompson-Jarvis.png}	f
395	Brimmy	\N	\N	\N	10	\N	1	{/img/characters/serie/Brimmy.png}	f
396	Britney Spears	\N	\N	December 2	43	{Baptist}	34	{/img/characters/serie/Britney_Spears.png}	t
397	Brooke Shields	\N	\N	May 31	60	{"Roman Catholic"}	200	{/img/characters/serie/Brooke_Shields.png}	t
398	Brobee	\N	\N	\N	\N	\N	242	{/img/characters/serie/Brobee.png}	f
399	Bruce	\N	\N	\N	\N	\N	65	{/img/characters/serie/Bruce.png}	f
400	Brunette Nurse	\N	\N	\N	\N	\N	89	{/img/characters/serie/Brunette_Nurse.png}	f
401	Bryan Adams	\N	\N	November 5	65	\N	212	{/img/characters/serie/Bryan_Adams.png}	t
402	Bubb Rubb	\N	\N	\N	47	\N	171	{/img/characters/serie/Bubb_Rubb.jpg}	t
403	Buck	\N	61	\N	\N	\N	31	{/img/characters/serie/Buck.png}	f
404	Buck Jr	\N	\N	\N	13	\N	31	{/img/characters/serie/Buck_Jr.png}	f
405	Bucky Bailey	\N	\N	\N	\N	\N	228	{/img/characters/serie/Bucky_Bailey.png}	f
406	Buddha	\N	\N	\N	2574	\N	68	{/img/characters/serie/Buddha.png}	t
407	Buddy Ebsen	\N	\N	April 2	95	\N	24	{/img/characters/serie/Buddy_Ebsen.png}	t
408	Busy Beaver Truck Driver	\N	\N	\N	\N	\N	79	{/img/characters/serie/Busy_Beaver_Truck_Driver.png}	f
409	Butt Out!	\N	\N	\N	\N	\N	109	{/img/characters/serie/Butt_Out.png}	f
410	Buzz Lightyear	\N	\N	\N	\N	\N	299	{/img/characters/serie/Buzz_Lightyear.png}	t
411	Benjamin Netanyahu	\N	\N	October 21th	75	{Judaism}	326	{/img/characters/serie/Benjamin_Netanyahu.png}	t
412	Brendan Carr	\N	\N	January 5th	46	\N	326	{/img/characters/serie/Brendan_Carr.png}	t
\.


--
-- Data for Name: chinpokomon; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.chinpokomon (id, name, image) FROM stdin;
27	Stegmata	img/chinpokomon/Stegmata.png
26	Sna-kat	img/chinpokomon/Sna-kat.png
25	Shoe	img/chinpokomon/Shoe.png
24	Roo-stor	img/chinpokomon/Roo-stor.png
23	Roidrat	img/chinpokomon/Roidrat.png
22	Rabbitech	img/chinpokomon/Rabbitech.png
21	Pterdaken	img/chinpokomon/Pterdaken.png
20	Poodlesaurus Rex	img/chinpokomon/Poodlesaurus_Rex.png
19	Pengin	img/chinpokomon/Pengin.png
18	Mouse-tik	img/chinpokomon/Mouse-tik.png
17	Monkay	img/chinpokomon/Monkay.png
16	Lambtron	img/chinpokomon/Lambtron.png
15	Gunrilla	img/chinpokomon/Gunrilla.png
14	Gophermon	img/chinpokomon/Gophermon.png
13	Gerbitoad	img/chinpokomon/Gerbitoad.png
12	Furrycat	img/chinpokomon/Furrycat.png
11	Flowerpotamus	img/chinpokomon/Flowerpotamus.png
10	Fetuswami	img/chinpokomon/Fetuswami.png
9	Ferasnarf	img/chinpokomon/Ferasnarf.png
8	Fatdactyl	img/chinpokomon/Fatdactyl.png
7	Donkeytron	img/chinpokomon/Donkeytron.png
6	Cosmonewt	img/chinpokomon/Cosmonewt.png
5	Chu-Chu Nezumi	img/chinpokomon/Chu-Chu_Nezumi.png
4	Brocorii	img/chinpokomon/Brocorii.png
3	Biebersaurus	img/chinpokomon/Biebersaurus.png
2	Beetlebot	img/chinpokomon/Beetlebot.png
1	Accountafish	img/chinpokomon/Accountafish.png
30	Velocirapstar	img/chinpokomon/Velocirapstar.png
29	Vamporko	img/chinpokomon/Vamporko.png
28	Terribovine	img/chinpokomon/Terribovine.png
\.


--
-- Data for Name: episodes; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.episodes (id, name, season, episode, realese_date, description, view_on_website, censured, paramount_plus_exclusive) FROM stdin;
20	City on the Edge of Forever (Flashbacks)	2	7	1998-06-17	A freak accident leaves the South Park Elementary School Bus teetering precariously on the edge of a cliff.	https://www.southparkstudios.com/episodes/k5278s/south-park-city-on-the-edge-of-forever-season-2-ep-7	f	f
21	Summer Sucks	2	8	1998-06-24	The entire town is gearing up for the annual 4 July celebration when a ban on fireworks is imposed.	https://www.southparkstudios.com/episodes/3wdzae/south-park-summer-sucks-season-2-ep-8	f	f
22	Chef's Chocolate Salty Balls	2	9	1998-08-19	South Park's first film festival attracts crowds of pretentious, tofu-eating movie lovers to the quiet mountain town.	https://www.southparkstudios.com/episodes/5ftz8k/south-park-chef-s-chocolate-salty-balls-season-2-ep-9	f	f
23	Chickenpox	2	10	1998-08-26	The kids' parents only have their best interests at heart when they arrange for Stan, Kyle, and Cartman to be exposed to the chickenpox virus.	https://www.southparkstudios.com/episodes/ewsl9y/south-park-chickenpox-season-2-ep-10	f	f
24	Roger Ebert Should Lay off the Fatty Foods	2	11	1998-09-02	Is the new planetarium a harmless place to learn about the solar system, or the scene of a diabolical plot to control the minds of South Park's citizens?	https://www.southparkstudios.com/episodes/2ixlzj/south-park-roger-ebert-should-lay-off-the-fatty-foods-season-2-ep-11	f	f
25	Clubhouses	2	12	1998-09-23	Stan and Kyle are psyched to have Wendy and Bebe visit their clubhouse for a game of Truth or Dare, but first they have to build one.	https://www.southparkstudios.com/episodes/k58rq5/south-park-clubhouses-season-2-ep-12	f	f
26	Cow Days	2	13	1998-09-30	South Park's 14th Annual "Cow Days" rodeo and carnival is here and the boys are determined to win Terrance and Phillip dolls.	https://www.southparkstudios.com/episodes/4xxqgo/south-park-cow-days-season-2-ep-13	f	f
17	Chickenlover	2	4	1998-05-27	When Barbrady resigns, anarchy ensues and the boys pitch in to help.	https://www.southparkstudios.com/episodes/c1m717/south-park-chickenlover-season-2-ep-4	f	f
27	Chef Aid	2	14	1998-10-07	After a huge loss in court, Chef is left penniless, but he has some very famous and talented friends in the music business who want to help their old mentor.	https://www.southparkstudios.com/episodes/23818m/south-park-chef-aid-season-2-ep-14	f	f
28	Spookyfish	2	15	1998-10-28	When Sharon Marsh's aunt makes a monthly visit, she brings a mysterious pet fish for Stan.	https://www.southparkstudios.com/episodes/973coq/south-park-spookyfish-season-2-ep-15	f	f
29	Merry Christmas Charlie Manson!	2	16	1998-12-09	Dinner with Cartman's family takes a bizarre twist when Uncle Howard shows up after breaking out of prison with the help of his cellmate, Charlie Manson.	https://www.southparkstudios.com/episodes/q52xqu/south-park-merry-christmas-charlie-manson-season-2-ep-16	f	f
30	Gnomes	2	17	1998-12-16	Cartman, Stan, Kyle and Kenny are assigned to write a report with Tweek, the very nervous and highly caffeinated boy who insists gnomes are stealing his underpants.	https://www.southparkstudios.com/episodes/13y790/south-park-gnomes-season-2-ep-17	f	f
32	Rainforest Shmainforest	3	1	1999-04-07	The boys travel to the Costa Rica as a part of the "Getting Gay with Kids" choir tour.	https://www.southparkstudios.com/episodes/hv0a9m/south-park-rainforest-shmainforest-season-3-ep-1	f	f
33	Spontaneous Combustion	3	2	1999-04-14	When the citizens of South Park start exploding randomly, the mayor enlists Stan's dad, the resident geologist, to find a solution to the problem.	https://www.southparkstudios.com/episodes/iizk09/south-park-spontaneous-combustion-season-3-ep-2	f	f
34	Succubus	3	3	1999-04-21	Chef's parents arrive in South Park from Scotland fresh from an encounter with the Loch Ness Monster to attend Chef's wedding.	https://www.southparkstudios.com/episodes/97d61n/south-park-succubus-season-3-ep-3	f	f
35	Jakovasaurs	3	4	1999-06-16	The boys discover a prehistoric creature called a Jackovasaur while camping at Stark's Pond.	https://www.southparkstudios.com/episodes/f1j0t8/south-park-jakovasaurs-season-3-ep-4	f	f
36	Tweek Vs. Craig	3	5	1999-06-23	The boys instigate a fight between Tweek and Craig in shop class. Meanwhile, Mr. Adler, the shop teacher, is haunted by a recurring dream of his lost love.	https://www.southparkstudios.com/episodes/7efemk/south-park-tweek-vs-craig-season-3-ep-5	f	f
37	Sexual Harassment Panda	3	6	1999-07-07	After Sexual Harassment Panda "educates" the children, Cartman sues Stan for sexual harassment, and a flurry of other lawsuits follow.	https://www.southparkstudios.com/episodes/zcplyz/south-park-sexual-harassment-panda-season-3-ep-6	f	f
38	Cat Orgy	3	7	1999-07-14	While all the adults are gathering at Mr. Mackey's house to watch a meteor shower Shelley Marsh is left babysit Cartman.	https://www.southparkstudios.com/episodes/9h0qbg/south-park-cat-orgy-season-3-ep-7	f	f
39	Two Guys Naked in a Hot Tub	3	8	1999-07-21	Stan's parents drag him along to Mr. Mackey's meteor shower party, where he is sent down into the basement to play with Pip, Butters and Dougie.	https://www.southparkstudios.com/episodes/noc1s7/south-park-two-guys-naked-in-a-hot-tub-season-3-ep-8	f	f
40	Jewbilee	3	9	1999-07-28	Kyle invites Kenny to join him and Ike at Jewbilee, a camp for Jewish kids.	https://www.southparkstudios.com/episodes/wq9n30/south-park-jewbilee-season-3-ep-9	f	f
41	Korn's Groovy Pirate Ghost Mystery	3	10	1999-10-27	Korn comes to South Park for a Halloween concert and helps the boys solve a spooky pirate ghost mystery.	https://www.southparkstudios.com/episodes/h7udco/south-park-korn-s-groovy-pirate-ghost-mystery-season-3-ep-10	f	f
42	Chinpokomon	3	11	1999-11-03	Stan, Kyle, Cartman and Kenny are caught up in the latest fad from Japan: Chinpoko Mon!	https://www.southparkstudios.com/episodes/mkw3sw/south-park-chinpokomon-season-3-ep-11	f	f
43	Hooked on Monkey Fonics	3	12	1999-11-10	To help Cartman win the school spelling bee, Cartman's Mom gives him the Hooked on Monkey Fonics spelling system.	https://www.southparkstudios.com/episodes/x7thqq/south-park-hooked-on-monkey-fonics-season-3-ep-12	f	f
44	Starvin' Marvin In Space	3	13	1999-11-17	Starvin' Marvin returns to South Park with an alien spaceship and enlists Cartman, Stan, Kyle and Kenny's help to seek out a new home for his starving people.	https://www.southparkstudios.com/episodes/ziuoor/south-park-starvin-marvin-in-space-season-3-ep-13	f	f
45	The Red Badge of Gayness	3	14	1999-11-24	Cartman has visions of glory as he suits up for the Confederacy in the annual reenactment of a Civil War battle, and leads the drunken rebels to defeat the union.	https://www.southparkstudios.com/episodes/d9sb5t/south-park-the-red-badge-of-gayness-season-3-ep-14	f	f
46	Mr. Hankey's Christmas Classics	3	15	1999-12-01	An extravaganza of holiday songs are performed in unique South Park style, hosted by Mr. Hankey.	https://www.southparkstudios.com/episodes/w7a0m8/south-park-mr-hankey-s-christmas-classics-season-3-ep-15	f	f
47	Are You There God? It's Me, Jesus	3	16	1999-12-29	People from all over the world start to gather outside Jesus' house waiting for a millennium miracle.	https://www.southparkstudios.com/episodes/6ci3pc/south-park-are-you-there-god-it-s-me-jesus-season-3-ep-16	f	f
48	World Wide Recorder Concert	3	17	2000-01-12	The children of South Park are invited to Arkansas for the "Four Million Child Blow 2000," the first worldwide recorder concert.	https://www.southparkstudios.com/episodes/gxlmci/south-park-world-wide-recorder-concert-season-3-ep-17	f	f
49	Tooth Fairy's Tats 2000	4	1	2000-04-05	When Cartman discovers the Tooth Fairy is paying a premium price for his lost teeth, he and the boys seize the opportunity to make some cash.	https://www.southparkstudios.com/episodes/x5kud8/south-park-tooth-fairy-s-tats-2000-season-4-ep-1	f	f
50	Cartman's Silly Hate Crime 2000	4	2	2000-04-12	Cartman is pursued by the FBI for committing a hate crime and lands in juvenile hall.	https://www.southparkstudios.com/episodes/1fr0nc/south-park-cartman-s-silly-hate-crime-2000-season-4-ep-2	f	f
51	Timmy 2000	4	3	2000-04-19	When Timmy is diagnosed with Attention Deficit Disorder, it triggers a wave of prescription drug abuse at South Park Elementary.	https://www.southparkstudios.com/episodes/ixn44n/south-park-timmy-2000-season-4-ep-3	f	f
52	Quintuplets 2000	4	4	2000-04-26	8-year-old contorting quintuplets from Romania defect to the United States and seek shelter with Stan's family.	https://www.southparkstudios.com/episodes/ib8m8u/south-park-quintuplets-2000-season-4-ep-4	f	f
53	Cartman Joins NAMBLA	4	5	2000-06-21	Cartman decides to seek friendship using the Internet, and finds an older man who is more than willing to be his friend...and more.	https://www.southparkstudios.com/episodes/vxu8qr/south-park-cartman-joins-nambla-season-4-ep-5	f	f
54	Cherokee Hair Tampons	4	6	2000-06-28	Kyle needs a kidney transplant and Cartman is discovered to be the perfect donor. Cartman gladly offers his kidney to Kyle -- for the price of $10 million dollars.	https://www.southparkstudios.com/episodes/dgwub0/south-park-cherokee-hair-tampons-season-4-ep-6	f	f
55	Chef Goes Nanners	4	7	2000-07-05	Chef's passionate protest declaring the South Park flag racist enflames the entire town.\n\n	https://www.southparkstudios.com/episodes/zplcis/south-park-chef-goes-nanners-season-4-ep-7	f	f
56	Something You Can Do With Your Finger	4	8	2000-07-12	"Fingerbang" is the newest boy band starring all the boys and it's also Cartman's latest scheme to make a million dollars.	https://www.southparkstudios.com/episodes/oien0o/south-park-something-you-can-do-with-your-finger-season-4-ep-8	f	f
57	Do The Handicapped Go To Hell?	4	9	2000-07-19	The boys learn in Sunday school that they must confess their sins, but worry about Timmy since all he can say is his own name.	https://www.southparkstudios.com/episodes/bw7g97/south-park-do-the-handicapped-go-to-hell-season-4-ep-9	f	f
58	Probably	4	10	2000-07-26	Cartman's flock begins to grow and the children begin plans to build him a Church. Meanwhile, Satan turns to God for advice.	https://www.southparkstudios.com/episodes/06brb8/south-park-probably-season-4-ep-10	f	f
59	Fourth Grade	4	11	2000-11-08	The boys devise a plan to travel back in time a full year and return to the third grade, with the help of Timmy and his electronic wheelchair.\n\n	https://www.southparkstudios.com/episodes/d9fr51/south-park-fourth-grade-season-4-ep-11	f	f
60	Trapper Keeper	4	12	2000-11-15	When Cartman finally stops bragging about his new Trapper Keeper, a stranger informs him that it will eventually take over the world and destroy humankind, if they don't destroy it first.	https://www.southparkstudios.com/episodes/5fuujn/south-park-trapper-keeper-season-4-ep-12	f	f
61	Helen Keller! The Musical	4	13	2000-11-22	When Butters informs the forth grader's that the Kindergarteners school play is a magnificent sight to behold, they go through a lot of pain to make sure they beat the tiny tots' show.	https://www.southparkstudios.com/episodes/dh0u78/south-park-helen-keller-the-musical-season-4-ep-13	f	f
62	Pip	4	14	2000-11-29	When Pip is offered the opportunity to become a gentleman he goes to London only to discover that Miss Havisham plans to break his heart.	https://www.southparkstudios.com/episodes/6bxssx/south-park-pip-season-4-ep-14	f	f
63	Fat Camp	4	15	2000-12-06	Cartman's family and friends have intervened and are forcing him to trim down. While Cartman's away, Kenny's star is on the rise when he gets his own reality TV show.	https://www.southparkstudios.com/episodes/frgptn/south-park-fat-camp-season-4-ep-15	f	f
64	The Wacky Molestation Adventure	4	16	2000-12-13	To get back at his parents for not letting him go to a concert, Kyle tells the police that his parents molested him. Soon, the whole town is free of adults and divided into two rival cities.\n\n	https://www.southparkstudios.com/episodes/fmgki1/south-park-the-wacky-molestation-adventure-season-4-ep-16	f	f
65	A Very Crappy Christmas	4	17	2000-12-20	When Mr. Hankey skips Christmas, the boys find him living with his alcoholic wife and their three little nuggets. He tells them that no one is into Christmas anymore.	https://www.southparkstudios.com/episodes/7rd3vw/south-park-a-very-crappy-christmas-season-4-ep-17	f	f
66	It Hits The Fan	5	1	2001-06-20	The you-know-what hits the fan 162 times when the citizens of South Park tune in to hear the word "shit" on a popular TV show.	https://www.southparkstudios.com/episodes/nppzdg/south-park-it-hits-the-fan-season-5-ep-1	f	f
67	Cripple Fight!	5	2	2001-06-27	Big Gay Al returns to South Park as the new scout leader. When he is fired for being gay, the boys rally to his defense with the help of the new "handi-capable" kid, Jimmy.	https://www.southparkstudios.com/episodes/jgvuoc/south-park-cripple-fight-season-5-ep-2	f	f
69	Scott Tenorman Must Die	5	4	2001-07-11	After the other boys explain to Cartman that pubes don't count unless you grow your own, Cartman realizes he's been tricked by the school bully, Scott Tenorman.	https://www.southparkstudios.com/episodes/yf32xo/south-park-scott-tenorman-must-die-season-5-ep-4	f	f
70	Terrance and Phillip: Behind the Blow	5	5	2001-07-18	When the boys discover Terrance and Philip have called it quits, they'll go to any lengths to reunite the duo and recruit them for South Park's Earth Day festivities.	https://www.southparkstudios.com/episodes/vzztv5/south-park-terrance-and-phillip-behind-the-blow-season-5-ep-5	f	f
71	Cartmanland	5	6	2001-07-25	Cartman inherits a million dollars from his grandmother and fulfills his lifelong dream of owning his own amusement park: Cartmanland!	https://www.southparkstudios.com/episodes/zm98ei/south-park-cartmanland-season-5-ep-6	f	f
72	Proper Condom Use	5	7	2001-08-01	In a time-honored tradition and right-of-passage, the boys are separated from the girls and schooled in the mysteries of sex by none other than Mr. Mackey.	https://www.southparkstudios.com/episodes/t746u2/south-park-proper-condom-use-season-5-ep-7	f	f
73	Towelie	5	8	2001-08-08	When the government steals their new Gamesphere, the boys will stop at nothing to get it back.	https://www.southparkstudios.com/episodes/l23dim/south-park-towelie-season-5-ep-8	f	f
74	Osama Bin Laden Has Farty Pants	5	9	2001-11-07	The kids of South Park have raised money to send to the children of Afghanistan, but the Government believes the Afghani children's thank you gift is contaminated with Anthrax and the boys are forced to take it back to Afghanistan.	https://www.southparkstudios.com/episodes/gef4gc/south-park-osama-bin-laden-has-farty-pants-season-5-ep-9	f	f
75	How to Eat with Your Butt	5	10	2001-11-14	Cartman gets Kenny's school picture on every "missing child" milk carton in the country.	https://www.southparkstudios.com/episodes/1jaqiq/south-park-how-to-eat-with-your-butt-season-5-ep-10	f	f
76	The Entity	5	11	2001-11-21	Mr. Garrison gets fed up with long lines, delayed flights and the airline industry in general and invents his own transportation device.	https://www.southparkstudios.com/episodes/rxb67x/south-park-the-entity-season-5-ep-11	f	f
77	Here Comes The Neighborhood	5	12	2001-11-28	Tolkien is tired of being the only rich kid in town, and succeeds in attracting several other wealthy families to South Park.	https://www.southparkstudios.com/episodes/ulcvyu/south-park-here-comes-the-neighborhood-season-5-ep-12	f	f
78	Kenny Dies	5	13	2001-12-05	In a very special episode of "South Park," Cartman fights for Kenny's life when he speaks before Congress in favor of stem-cell research.	https://www.southparkstudios.com/episodes/zb407b/south-park-kenny-dies-season-5-ep-13	f	f
79	Butters' Very Own Episode	5	14	2001-12-12	Alone and lost, Butters determinedly makes his way through porn theatres and gay bathhouses in an effort to get his dad back home in time to eat at Bennigan's for his parents' anniversary.	https://www.southparkstudios.com/episodes/8gq1cu/south-park-butters-very-own-episode-season-5-ep-14	f	f
80	Jared Has Aides	6	1	2002-03-06	As the country becomes obsessed with a popular program for losing weight, the boys see an opportunity to become sponsored by a major restaurant chain.	https://www.southparkstudios.com/episodes/vs89ol/south-park-jared-has-aides-season-6-ep-1	f	f
81	Asspen	6	2	2002-03-12	While the adults trapped at a time-share sales meeting, Stan is challenged by the best skier on the mountain.	https://www.southparkstudios.com/episodes/y0ffuc/south-park-asspen-season-6-ep-2	f	f
82	Freak Strike	6	3	2002-03-20	The boys convince Butters to appear on "The Maury Povich Show" with a fake facial deformity in order to receive the show's prizes.	https://www.southparkstudios.com/episodes/aba4sz/south-park-freak-strike-season-6-ep-3	f	f
83	Fun With Veal	6	4	2002-03-27	Stan is appalled when he realizes the veal he's been eating is, in fact, the meat from little baby calves.	https://www.southparkstudios.com/episodes/ahrfg6/south-park-fun-with-veal-season-6-ep-4	f	f
84	The New Terrance and Phillip Movie Trailer	6	5	2002-04-03	All the kids in South Park are glued to the TV, wild with anticipation to see the first trailer for the latest Terrance and Phillip movie.	https://www.southparkstudios.com/episodes/m1tz7n/south-park-the-new-terrance-and-phillip-movie-trailer-season-6-ep-5	f	f
85	Professor Chaos	6	6	2002-04-10	The boys fire Butters as their new friend. Devastation over his rejection unleashes Butters' dark side and Professor Chaos is born.	https://www.southparkstudios.com/episodes/2rl3z6/south-park-professor-chaos-season-6-ep-6	f	f
86	The Simpsons Already Did It	6	7	2002-06-26	Professor Chaos is frustrated when he realizes all of his diabolical plans to wreak havoc on South Park have already been done by "The Simpsons."	https://www.southparkstudios.com/episodes/155r7v/south-park-the-simpsons-already-did-it-season-6-ep-7	f	f
87	Red Hot Catholic Love	6	8	2002-07-03	A sexual abuse scandal involving priests hits South Park and is taken all the way to the Vatican.	https://www.southparkstudios.com/episodes/9sz0th/south-park-red-hot-catholic-love-season-6-ep-8	f	f
88	Free Hat	6	9	2002-07-10	When the boys find out that their favorite movies are being enhanced, re-released and ruined in the process, they form a club to "Save Films from their Directors."	https://www.southparkstudios.com/episodes/b4vsck/south-park-free-hat-season-6-ep-9	f	f
89	Bebe's Boobs Destroy Society	6	10	2002-07-17	Cartman gets kicked out of the gang when Bebe develops boobs and the boys lose their minds, threatening their friendships and society as we know it.	https://www.southparkstudios.com/episodes/g3404w/south-park-bebe-s-boobs-destroy-society-season-6-ep-10	f	f
90	Child Abduction is Not Funny	6	11	2002-07-24	In an effort to protect their children from kidnappers, the parents hire the owner of City Wok Restaurant to build the Great Wall of South Park.	https://www.southparkstudios.com/episodes/welysd/south-park-child-abduction-is-not-funny-season-6-ep-11	f	f
91	A Ladder to Heaven	6	12	2002-11-06	Kenny died with the winning ticket to a prize of endless candy in his pocket. The boys decide to build a ladder to Heaven where they expect to find him and get the ticket back.	https://www.southparkstudios.com/episodes/qly8oc/south-park-a-ladder-to-heaven-season-6-ep-12	f	f
92	The Return of the Fellowship of the Ring to the Two Towers	6	13	2002-11-13	The boys embark upon a mythical quest as they set out to return their copy of the "The Lord of the Rings" movie to their local video store.	https://www.southparkstudios.com/episodes/u2kecs/south-park-the-return-of-the-fellowship-of-the-ring-to-the-two-towers-season-6-ep-13	f	f
93	The Death Camp of Tolerance	6	14	2002-11-20	The boys are sentenced to the Death Camp of Tolerance where they learn how to treat minorities. Mr. Slave and Lemmiwinks make their debut in this episode.	https://www.southparkstudios.com/episodes/z0mpok/south-park-the-death-camp-of-tolerance-season-6-ep-14	f	f
94	The Biggest Douche in the Universe	6	15	2002-11-27	When a famous psychic fails to help him exorcise Kenny from his body, Cartman and Chef travel to the moors of Scotland, where Chef's mom tries a little of her voodoo magic on him.	https://www.southparkstudios.com/episodes/h70xwl/south-park-the-biggest-douche-in-the-universe-season-6-ep-15	f	f
95	My Future Self n' Me	6	16	2002-12-04	When a 32-year-old man claiming to be Stan from the future shows up in South Park, young Stan is forced to come to terms with the loser he will become.	https://www.southparkstudios.com/episodes/xfaqzg/south-park-my-future-self-n-me-season-6-ep-16	f	f
96	Red Sleigh Down	6	17	2002-12-11	With the help of Santa, Mr. Hankey and Jesus, Cartman attempts to bring Christmas to the downtrodden citizens of Iraq.	https://www.southparkstudios.com/episodes/e8zvyz/south-park-red-sleigh-down-season-6-ep-17	f	f
97	Cancelled	7	1	2003-03-19	Stan, Cartman, Kyle and Kenny find out that planet Earth is just one big intergalactic reality show and it's about to be cancelled.	https://www.southparkstudios.com/episodes/sa19zy/south-park-cancelled-season-7-ep-1	f	f
98	Krazy Kripples	7	2	2003-03-26	Jimmy and Timmy pull together a group of people like themselves and call their new club the "Crips."	https://www.southparkstudios.com/episodes/rvu68b/south-park-krazy-kripples-season-7-ep-2	f	f
99	Toilet Paper	7	3	2003-04-02	Cartman convinces the boys to "toilet paper" their teacher's house, but Kyle is overwhelmed with guilt.	https://www.southparkstudios.com/episodes/lfnim5/south-park-toilet-paper-season-7-ep-3	f	f
100	I'm a Little Bit Country	7	4	2003-04-09	The boys join some anti-war protesters because it's a free pass out of school for the day.	https://www.southparkstudios.com/episodes/zyprl7/south-park-i-m-a-little-bit-country-season-7-ep-4	f	f
101	Fat Butt and Pancake Head	7	5	2003-04-16	One of Cartman's body parts becomes famous overnight and rivals the popularity of another superstar.	https://www.southparkstudios.com/episodes/kfc77n/south-park-fat-butt-and-pancake-head-season-7-ep-5	f	f
102	Lil' Crime Stoppers	7	6	2003-04-23	After they return a missing doll to a little girl, the police department recognizes the boys' efforts and officially names them "junior deputies."	https://www.southparkstudios.com/episodes/1jbnuo/south-park-lil-crime-stoppers-season-7-ep-6	f	f
103	Red Man's Greed	7	7	2003-04-30	The citizens of South Park are being forced off their land to make way for a new super highway after owners of the Three Feathers Indian Casino acquire the town.	https://www.southparkstudios.com/episodes/fopnh6/south-park-red-man-s-greed-season-7-ep-7	f	f
104	South Park Is Gay	7	8	2003-10-22	The town of South Park celebrates the new, hip metro-sexual craze.	https://www.southparkstudios.com/episodes/fq8wbh/south-park-south-park-is-gay-season-7-ep-8	f	f
105	Christian Rock Hard	7	9	2003-10-29	When the other boys kick Cartman out of their band, he pulls his own group together to make music for Jesus.	https://www.southparkstudios.com/episodes/iccjhj/south-park-christian-rock-hard-season-7-ep-9	f	f
106	Grey Dawn	7	10	2003-11-05	With South Park's senior citizens behind the wheel, more than a few farmer's markets have been mowed down. Unwilling to surrender their driver's licenses, the elderly fight back.	https://www.southparkstudios.com/episodes/gid3ua/south-park-grey-dawn-season-7-ep-10	f	f
107	Casa Bonita	7	11	2003-11-12	Kyle chooses Stan, Kenny and Butters to celebrate his birthday at Casa Bonita. When Cartman finds out he's not invited, he arranges for Butters to conveniently go "missing."	https://www.southparkstudios.com/episodes/me0b40/south-park-casa-bonita-season-7-ep-11	f	f
108	All About Mormons	7	12	2003-11-19	A Mormon kid moves to South Park and it's up to Stan to kick his ass. But when Stan and his dad meet their new Mormon neighbors, they become fascinated with how genuinely nice they are.	https://www.southparkstudios.com/episodes/rl7pjr/south-park-all-about-mormons-season-7-ep-12	f	f
109	Butt Out	7	13	2003-12-03	After singing and dancing representatives from an anti-smoking campaign rap about the dangers of smoking, the kids at South Park Elementary realize how cool it really is and take up the habit.	https://www.southparkstudios.com/episodes/u9u3rq/south-park-butt-out-season-7-ep-13	f	f
110	Raisins	7	14	2003-12-10	After Wendy breaks up with Stan the boys take him to "Raisins," a local restaurant known for its great chicken wings and hot girls.	https://www.southparkstudios.com/episodes/tr6pou/south-park-raisins-season-7-ep-14	f	f
111	It's Christmas in Canada	7	15	2003-12-17	The town decides to cancel Christmas and take up a collection when Ike's Canadian birth parents show up unexpectedly and want their baby back.	https://www.southparkstudios.com/episodes/m91chj/south-park-it-s-christmas-in-canada-season-7-ep-15	f	f
112	Good Times With Weapons	8	1	2004-03-17	The boys are transformed into Japanese Warriors after they trick a vendor and buy martial arts weapons at a local flea market.	https://www.southparkstudios.com/episodes/2znij2/south-park-good-times-with-weapons-season-8-ep-1	f	f
113	Up the Down Steroid	8	2	2004-03-24	Jimmy is in training for the upcoming Special Olympics and he's determined to win at any cost.	https://www.southparkstudios.com/episodes/5nhida/south-park-up-the-down-steroid-season-8-ep-2	f	f
114	The Passion of the Jew	8	3	2004-03-31	Kyle finally sees the blockbuster movie "The Passion of the Christ" and admits that Cartman has been right about the Jewish people all along.	https://www.southparkstudios.com/episodes/d7grkc/south-park-the-passion-of-the-jew-season-8-ep-3	f	f
115	You Got F'd in the A	8	4	2004-04-07	Stan just got served, and now it's up to him to put together a team of South Park's best dancers to compete against a troupe from Orange County.	https://www.southparkstudios.com/episodes/d47csv/south-park-you-got-f-d-in-the-a-season-8-ep-4	f	f
116	AWESOM-O	8	5	2004-04-14	Cartman plans to learn all of Butters' innermost secrets and then use them against him, by pretending to be Butters' new best friend, a robot named AWESOM-O.	https://www.southparkstudios.com/episodes/ktqvb2/south-park-awesom-o-season-8-ep-5	f	f
117	The Jeffersons	8	6	2004-04-21	The children of South Park are attracted to "Mr. Jefferson," the new neighbor in town, and Cartman goes out of his way to get "Mr. Jefferson" to love him best.	https://www.southparkstudios.com/episodes/rd6zxu/south-park-the-jeffersons-season-8-ep-6	f	f
118	Goobacks	8	7	2004-04-28	Humans from the year 4035 are traveling to South Park through a recently opened time portal and are looking for work.	https://www.southparkstudios.com/episodes/n6dj9t/south-park-goobacks-season-8-ep-7	f	f
119	Douche and Turd	8	8	2004-10-27	A PETA protest against the use of a cow as South Park Elementary's mascot forces the student body to choose a new one.	https://www.southparkstudios.com/episodes/ndszwn/south-park-douche-and-turd-season-8-ep-8	f	f
120	Something Wall-Mart This Way Comes	8	9	2004-11-03	In order to save South Park, Stan and Kyle have to find a way to destroy the ever-expanding Wall-Mart superstore while keeping Cartman from stabbing them in the back.	https://www.southparkstudios.com/episodes/7yupl4/south-park-something-wall-mart-this-way-comes-season-8-ep-9	f	f
121	Preschool	8	10	2004-11-10	The kid who took the fall for the boys five years ago is getting out of Juvie, and his first order of business is revenge.	https://www.southparkstudios.com/episodes/z31od5/south-park-preschool-season-8-ep-10	f	f
122	Quest for Ratings	8	11	2004-11-17	The boys of South Park produce their own morning news show on the school's closed-circuit television station and are immediately caught up in an intense competition for ratings.	https://www.southparkstudios.com/episodes/8fwe5a/south-park-quest-for-ratings-season-8-ep-11	f	f
123	Stupid Spoiled Whore Video Playset	8	12	2004-12-01	Disturbed by the corruptive influence Paris Hilton has on all little girls in South Park, one of the town's favorite citizens challenges her to a "whore-off."	https://www.southparkstudios.com/episodes/uixekv/south-park-stupid-spoiled-whore-video-playset-season-8-ep-12	f	f
124	Cartman's Incredible Gift	8	13	2004-12-08	After sustaining a severe head injury, Cartman appears to have the power to see into the future. South Park detectives are quick to enlist his help in cracking unsolved murder cases.	https://www.southparkstudios.com/episodes/038jht/south-park-cartman-s-incredible-gift-season-8-ep-13	f	f
125	Woodland Critter Christmas	8	14	2004-12-15	Stan agrees to help a group of adorable woodland critters build a manger in anticipation of the birth of their Lord and Savior, only to find out that they serve Satan.	https://www.southparkstudios.com/episodes/itr2k3/south-park-woodland-critter-christmas-season-8-ep-14	f	f
126	Mr. Garrison's Fancy New Vagina	9	1	2005-03-09	As Mr. Garrison enjoys his new womanly attributes after his sex change, the rest of the town gets in touch with their inner feelings too.	https://www.southparkstudios.com/episodes/805rnc/south-park-mr-garrison-s-fancy-new-vagina-season-9-ep-1	f	f
127	Die Hippie, Die	9	2	2005-03-16	When hippie drum circles start popping up in people's attics and backyards the citizens of South Park have no choice but to turn to Eric Cartman for help.	https://www.southparkstudios.com/episodes/xahxl6/south-park-die-hippie-die-season-9-ep-2	f	f
128	Wing	9	3	2005-03-23	The boys set up a talent agency and pool all their resources and impress their first client only to have another agency steal him away.	https://www.southparkstudios.com/episodes/h9tnne/south-park-wing-season-9-ep-3	f	f
129	Best Friends Forever	9	4	2005-03-30	Kenny is the only one of his friends to get the newest, coolest portable gaming device and Cartman can't deal with it. Will they remain best friends forever?	https://www.southparkstudios.com/episodes/5gkuf7/south-park-best-friends-forever-season-9-ep-4	f	f
130	The Losing Edge	9	5	2005-04-06	The kids desperately want an end to the boring baseball season. The problem is, they keep winning.	https://www.southparkstudios.com/episodes/6q8det/south-park-the-losing-edge-season-9-ep-5	f	f
131	The Death of Eric Cartman	9	6	2005-04-13	Cartman is sure he's dead and Butters is sure that Eric Cartman's ghost is haunting him. Together they attempt to make amends to all the people Cartman has wronged over the years.	https://www.southparkstudios.com/episodes/a9w7lr/south-park-the-death-of-eric-cartman-season-9-ep-6	f	f
132	Erection Day	9	7	2005-04-20	The South Park Elementary School Talent Show is coming up and Jimmy can't wait to perform his comedy routine, but first he must find a way to gain control of his raging hormones.	https://www.southparkstudios.com/episodes/7fzi8u/south-park-erection-day-season-9-ep-7	f	f
157	The Snuke	11	4	2007-03-28	While Cartman follows a lead on a possible terrorist attack, Hillary Clinton makes a campaign stop in South Park for a big rally.	https://www.southparkstudios.com/episodes/58qtax/south-park-the-snuke-season-11-ep-4	f	f
133	Two Days Before the Day After Tomorrow	9	8	2005-10-19	A Global Warming State of Emergency is declared in South Park as the world's largest beaver dam breaks and floods the adjacent town of Beaverton.	https://www.southparkstudios.com/episodes/evqh3x/south-park-two-days-before-the-day-after-tomorrow-season-9-ep-8	f	f
134	Marjorine	9	9	2005-10-26	Butters must fake his death, dress up as a girl and infiltrate a slumber party, in order to retrieve a future telling device Cartman is convinced the girls have.	https://www.southparkstudios.com/episodes/jy6p4p/south-park-marjorine-season-9-ep-9	f	f
135	Follow That Egg	9	10	2005-11-02	In an effort to thwart her ex-lovers plans to get married, Mrs. Garrison leads the charge against gay marriage.	https://www.southparkstudios.com/episodes/uhtcfl/south-park-follow-that-egg-season-9-ep-10	f	f
136	Ginger Kids	9	11	2005-11-09	After the sudden on-set of the disease Gingervitis, Cartman rallies all other ginger kids to rise up and assume their role as the master race.	https://www.southparkstudios.com/episodes/uvp08l/south-park-ginger-kids-season-9-ep-11	f	f
137	Trapped in the Closet	9	12	2005-11-16	Scientologists converge on Stan's house after he is identified as the reincarnation of L. Ron Hubbard. One A-lister locks himself in the closet and refuses to come out after Stan criticizes his "talent."	https://www.southparkstudios.com/episodes/a3esfi/south-park-trapped-in-the-closet-season-9-ep-12	f	f
138	Free Willzyx	9	13	2005-11-30	The boys try to rescue their new friend Willzyx, a talking space whale, from the Denver Sea Park and with the help of MASA (Mexican Aeronautica y Spacia Administracion) get him home to the moon for $200.	https://www.southparkstudios.com/episodes/esubf0/south-park-free-willzyx-season-9-ep-13	f	f
139	Bloody Mary	9	14	2005-12-07	Stan is embarrassed when his dad gets pulled over for drunk driving. Randy believes that only one thing can save him from his "disease," a bleeding statue of the Virgin Mary in the next town.	https://www.southparkstudios.com/episodes/dspvu8/south-park-bloody-mary-season-9-ep-14	f	f
140	The Return of Chef	10	1	2006-03-22	Chef returns to South Park after spending time away with a group called, "The Super Adventure Club," but when his strange behavior starts getting him in trouble, the boys risk everything to save him.	https://www.southparkstudios.com/episodes/38fqq4/south-park-the-return-of-chef-season-10-ep-1	f	f
141	Smug Alert!	10	2	2006-03-29	Kyle and his family are moving to San Francisco. The only way Stan can get his best friend back is to convince everyone to start driving hybrid cars.	https://www.southparkstudios.com/episodes/o0wg88/south-park-smug-alert-season-10-ep-2	f	f
144	A Million Little Fibers	10	5	2006-04-19	Towelie gets over his drug addiction and writes his memoirs. With Oprah's support, his book becomes a best seller and his story inspires millions to turn their lives around.	https://www.southparkstudios.com/episodes/okhu48/south-park-a-million-little-fibers-season-10-ep-5	f	f
145	Manbearpig	10	6	2006-04-26	Al Gore warns the school about the threat of Manbearpig.	https://www.southparkstudios.com/episodes/diujt8/south-park-manbearpig-season-10-ep-6	f	f
146	Tsst	10	7	2006-05-03	When Cartman's mom realizes she can't control her son anymore, she gets help from an expert. The "Dog Whisperer" may have what it takes but Eric Cartman's not going down without a fight.	https://www.southparkstudios.com/episodes/h7679l/south-park-tsst-season-10-ep-7	f	f
147	Make Love, Not Warcraft	10	8	2006-10-04	The boys dedicate their lives to defeating a mad gamer and saving the World of Warcraft.	https://www.southparkstudios.com/episodes/hk2x6r/south-park-make-love-not-warcraft-season-10-ep-8	f	f
148	Mystery of the Urinal Deuce	10	9	2006-10-11	The world's biggest conspiracy of all time is finally uncovered when Eric Cartman exposes the true culprit behind the September 11th attacks.	https://www.southparkstudios.com/episodes/bvihkk/south-park-mystery-of-the-urinal-deuce-season-10-ep-9	f	f
149	Miss Teacher Bangs a Boy	10	10	2006-10-18	In his new role as School Hallway Monitor at South Park Elementary, Cartman must team up with Kyle when they discover a teacher having sex with a student.	https://www.southparkstudios.com/episodes/cd3jat/south-park-miss-teacher-bangs-a-boy-season-10-ep-10	f	f
150	Hell on Earth 2006	10	11	2006-10-25	Satan is throwing the biggest Halloween costume party ever. Just like a girl getting ready for her sweet sixteen, every detail must be perfect for the prince of darkness. The antics of the most notorious serial killers of all time threaten his fun.	https://www.southparkstudios.com/episodes/6ok1di/south-park-hell-on-earth-2006-season-10-ep-11	f	f
151	Go God Go	10	12	2006-11-01	South Park Elementary faces strong opposition to the topic of evolution. Cartman's too busy to notice as he plans to propel himself into the future on the precise release date of the newest, hottest game console.	https://www.southparkstudios.com/episodes/ekt82w/south-park-go-god-go-season-10-ep-12	f	f
152	Go God Go XII	10	13	2006-11-08	Eric Cartman has frozen himself in an attempt to make his three-week wait for a Nintendo Wii pass quickly. A freak accident landed him over 500 years in the future and now, he's stuck in a Godless world on the brink of war with no Nintendo Wii.	https://www.southparkstudios.com/episodes/rqe7bl/south-park-go-god-go-xii-season-10-ep-13	f	f
153	Stanley's Cup	10	14	2006-11-15	Stan Marsh has hit rock bottom. He's got no job, no bicycle and his only way out of a bad situation is to coach the local pee wee hockey team.	https://www.southparkstudios.com/episodes/w19jp7/south-park-stanley-s-cup-season-10-ep-14	f	f
154	With Apologies to Jesse Jackson	11	1	2007-03-07	After Randy Marsh experiences an unfortunate incident on national TV, the "N" bomb hits South Park. While Randy seeks forgiveness from Jesse Jackson, South Park Elementary invites a midget by the name of Dr. Nelson to talk about sensitivity.	https://www.southparkstudios.com/episodes/7ug7sr/south-park-with-apologies-to-jesse-jackson-season-11-ep-1	f	f
155	Cartman Sucks	11	2	2007-03-14	When his "ultimate plan" to embarrass Butters backfires, Cartman struggles to keep his classmates from seeing a compromising photograph. Meanwhile, Butters is sent to a special camp where they "Pray the Gay Away."	https://www.southparkstudios.com/episodes/pomjzh/south-park-cartman-sucks-season-11-ep-2	f	f
156	Lice Capades	11	3	2007-03-21	An infestation of head lice plagues South Park Elementary. When Mr. Garrison refuses to name names, Cartman finds a way to detect who has lice in the hopes of making fun of his unfortunate classmate.	https://www.southparkstudios.com/episodes/zjrua8/south-park-lice-capades-season-11-ep-3	f	f
158	Fantastic Easter Special	11	5	2007-04-04	Determined to get the real story behind why he has to decorate eggs for Easter, Stan falls in with an eccentric society that guards a legendary secret.	https://www.southparkstudios.com/episodes/2n6i47/south-park-fantastic-easter-special-season-11-ep-5	f	f
159	D-Yikes!	11	6	2007-04-11	Ms. Garrison gets dumped again and takes her frustration out on the fourth grade class. However, things start looking up for her when she meets a new friend at the gym and they go out for drink at a local "girl bar."	https://www.southparkstudios.com/episodes/bbubl3/south-park-d-yikes-season-11-ep-6	f	f
160	Night of the Living Homeless	11	7	2007-04-18	As an increasing number of homeless people are begging for change all over South Park, the boys work to solve the homeless problem once and for all.	https://www.southparkstudios.com/episodes/jp51b1/south-park-night-of-the-living-homeless-season-11-ep-7	f	f
161	Le Petit Tourette	11	8	2007-10-03	Cartman's Tourette's is making school even more tedious for Kyle.	https://www.southparkstudios.com/episodes/1niqj9/south-park-le-petit-tourette-season-11-ep-8	f	f
162	More Crap	11	9	2007-10-10	Stan's dad becomes South Park's home-town hero when the guys down at the local bar see the size of his most recent crap.	https://www.southparkstudios.com/episodes/d3wt0d/south-park-more-crap-season-11-ep-9	f	f
163	Imaginationland	11	10	2007-10-17	When the entire contents of the world's imagination lay open before them, Stan and Kyle step right in. Back in South Park, Cartman swears he's seen a leprechaun.	https://www.southparkstudios.com/episodes/e1yoxn/south-park-imaginationland-season-11-ep-10	f	f
164	Imaginationland Episode II	11	11	2007-10-24	Stan and Kyle are being held in the bowels of the Pentagon until they tell the government how they got into Imaginationland. Meanwhile, Cartman simply won't rest until he finds Kyle and gets him to make good on their bet to suck his balls.	https://www.southparkstudios.com/episodes/vtizvz/south-park-imaginationland-episode-ii-season-11-ep-11	f	f
165	Imaginationland, Episode III	11	12	2007-10-31	nside Imaginationland, Stan and Butters engage in the battle of their lives as they fight the army of evil imaginary forces. Meanwhile, Cartman goes all the way to the Supreme Court to get Kyle to pay up on their bet.	https://www.southparkstudios.com/episodes/yi4pad/south-park-imaginationland-episode-iii-season-11-ep-12	f	f
166	Guitar Queer-O	11	13	2007-11-07	Stan and Kyle are hooked on Guitar Hero. Unfortunately, Stan's superior skills on the video game damage his friendship with Kyle.	https://www.southparkstudios.com/episodes/xv5ktr/south-park-guitar-queer-o-season-11-ep-13	f	f
167	The List	11	14	2007-11-14	The girls in the fourth grade class have made a secret list that rates every boy's looks from cutest to ugliest. When the boys steal the list, they are completely unprepared to deal with the results.	https://www.southparkstudios.com/episodes/5uz0vg/south-park-the-list-season-11-ep-14	f	f
168	Tonsil Trouble	12	1	2008-03-12	Cartman finds himself fighting for his life after a routine tonsillectomy goes wrong. When Kyle becomes infected with Cartman's ailment, the two won't stop for anything as they search for a cure that will reverse their otherwise certain mortality.	https://www.southparkstudios.com/episodes/n9jsjf/south-park-tonsil-trouble-season-12-ep-1	f	f
169	Britney's New Look	12	2	2008-03-19	When the boys help Britney Spears get to the North Pole, they discover the shocking secret behind her popularity.	https://www.southparkstudios.com/episodes/3cgswn/south-park-britney-s-new-look-season-12-ep-2	f	f
170	Major Boobage	12	3	2008-03-26	In a South Park homage to the 1981 film, "Heavy Metal", the boys are trying to get Kenny off the latest drug craze that's captured the junior high and under set.	https://www.southparkstudios.com/episodes/4r4367/south-park-major-boobage-season-12-ep-3	f	f
171	Canada On Strike	12	4	2008-04-02	The head of the World Canadian Bureau leads the country into a long and painful strike and the responsibility of brokering a settlement rests with the boys.	https://www.southparkstudios.com/episodes/u1yv8w/south-park-canada-on-strike-season-12-ep-4	f	f
172	Eek, A Penis!	12	5	2008-04-09	While Ms. Garrison is off trying to find a way to become the man he always intended to be, Cartman is put in charge of the classroom.	https://www.southparkstudios.com/episodes/327ba3/south-park-eek-a-penis-season-12-ep-5	f	f
173	Over Logging	12	6	2008-04-16	The citizens of South Park wake up and find the internet is gone. When Randy hears there may still be some internet out in California, he packs up his family and heads west.	https://www.southparkstudios.com/episodes/u2xk6s/south-park-over-logging-season-12-ep-6	f	f
174	Super Fun Time	12	7	2008-04-23	While the kids are on an educational field trip to a living museum, Cartman makes Butters sneak away from the class to go to the amusement center located next door.	https://www.southparkstudios.com/episodes/6hs21a/south-park-super-fun-time-season-12-ep-7	f	f
175	The China Probrem	12	8	2008-10-08	With the rest of the American people haunted by the memory of a recent tragic event, only Butters will stand with Cartman as he confronts the Chinese.	https://www.southparkstudios.com/episodes/zwjhca/south-park-the-china-probrem-season-12-ep-8	f	f
176	Breast Cancer Show Ever	12	9	2008-10-15	Wendy gets in trouble when she threatens to beat up Cartman after school.	https://www.southparkstudios.com/episodes/16pd0d/south-park-breast-cancer-show-ever-season-12-ep-9	f	f
177	Pandemic	12	10	2008-10-22	While the world struggles to contain an epidemic of epic proportions, the boys find a way to make money off of it.	https://www.southparkstudios.com/episodes/hg0bib/south-park-pandemic-season-12-ep-10	f	f
178	Pandemic 2 – The Startling	12	11	2008-10-29	Giant guinea pigs are attacking cities all over the world.  The boys have the key that will save everyone from the onslaught but they're stranded in the Andes Mountains.	https://www.southparkstudios.com/episodes/akix98/south-park-pandemic-2-the-startling-season-12-ep-11	f	f
179	About Last Night…	12	12	2008-11-05	While the country celebrates the outcome of the election, the new President-elect catches everyone off guard when he arrives at the White House prematurely.	https://www.southparkstudios.com/episodes/dt5skl/south-park-about-last-night-season-12-ep-12	f	f
180	Elementary School Musical	12	13	2008-11-12	The boys must embrace the latest fad to hit South Park Elementary or risk their status as the coolest kids in school.	https://www.southparkstudios.com/episodes/x6u02r/south-park-elementary-school-musical-season-12-ep-13	f	f
181	The Ungroundable	12	14	2008-11-19	Butters is sure he's seen a Vampire at school but he can't get anyone to listen to him. Meanwhile, the Goth Kids are angry and frustrated when the other kids can't tell the difference between a Goth and a Vampire.	https://www.southparkstudios.com/episodes/tt4m8l/south-park-the-ungroundable-season-12-ep-14	f	f
182	The Ring	13	1	2009-03-12	Kenny takes his new girlfriend to a Jonas Brothers' concert where they each get purity rings.\n\n	https://www.southparkstudios.com/episodes/doonr4/south-park-the-ring-season-13-ep-1	f	f
183	The Coon	13	2	2009-03-19	"The Coon" rises from the trash and takes his place as a lone vigilante who wipes out crime in the town of South Park.	https://www.southparkstudios.com/episodes/0dx5kg/south-park-the-coon-season-13-ep-2	f	f
184	Margaritaville	13	3	2009-03-26	Randy steps forward with a solution to fix the desperate state of the economy.	https://www.southparkstudios.com/episodes/9do3gw/south-park-margaritaville-season-13-ep-3	f	f
185	Eat, Pray, Queef	13	4	2009-04-02	Someone plays an April Fool's joke on the boys and it doesn't go over well.	https://www.southparkstudios.com/episodes/vyruue/south-park-eat-pray-queef-season-13-ep-4	f	f
186	Fishsticks	13	5	2009-04-09	Cartman and Jimmy come up with the funniest joke of all time.	https://www.southparkstudios.com/episodes/bgla3i/south-park-fishsticks-season-13-ep-5	f	f
187	Pinewood Derby	13	6	2009-04-15	Randy has a plan that will assure Stan a first place trophy in this year's Pinewood Derby.	https://www.southparkstudios.com/episodes/oki0th/south-park-pinewood-derby-season-13-ep-6	f	f
188	Fatbeard	13	7	2009-04-22	Cartman's dream of living the life of a pirate will come true if he can just get to Somalia.	https://www.southparkstudios.com/episodes/8qplt2/south-park-fatbeard-season-13-ep-7	f	f
189	Dead Celebrities	13	8	2009-10-07	Ike is being tormented by paranormal forces. Kyle brings in professional ghost hunters to help save his little brother.	https://www.southparkstudios.com/episodes/k2g54a/south-park-dead-celebrities-season-13-ep-8	f	f
190	Butters' Bottom Bitch	13	9	2009-10-14	Butters is determined to get his first kiss so his friends won't make fun of him anymore.	https://www.southparkstudios.com/episodes/mphf21/south-park-butters-bottom-bitch-season-13-ep-9	f	f
191	W.T.F.	13	10	2009-10-21	After attending their first WWE match, all the boys want to be professional wrestlers.	https://www.southparkstudios.com/episodes/5h5in2/south-park-w-t-f-season-13-ep-10	f	f
192	Whale Whores	13	11	2009-10-28	Stan takes action to stop the Japanese from killing the world's whales and dolphins.	https://www.southparkstudios.com/episodes/lzz69d/south-park-whale-whores-season-13-ep-11	f	f
193	The F Word	13	12	2009-11-04	The boys fight back against the loud and obnoxious Motorcycle Riders that are disrupting everyone in South Park.	https://www.southparkstudios.com/episodes/wpmnpk/south-park-the-f-word-season-13-ep-12	f	f
194	Dances with Smurfs	13	13	2009-11-11	Cartman is chosen to do the morning announcements at South Park Elementary.	https://www.southparkstudios.com/episodes/81p0af/south-park-dances-with-smurfs-season-13-ep-13	f	f
195	Pee	13	14	2009-11-18	The boys' fun-filled day at the water park is about to turn deadly.	https://www.southparkstudios.com/episodes/xenush/south-park-pee-season-13-ep-14	f	f
196	Sexual Healing	14	1	2010-03-17	The latest in scientific testing reveals that some of the boys at South Park Elementary have a sex addiction problem.	https://www.southparkstudios.com/episodes/7k3t00/south-park-sexual-healing-season-14-ep-1	f	f
197	The Tale of Scrotie McBoogerballs	14	2	2010-03-24	The boys are given a controversial book to read in school and it inspires them to write one of their own.	https://www.southparkstudios.com/episodes/rb5qgf/south-park-the-tale-of-scrotie-mcboogerballs-season-14-ep-2	f	f
198	Medicinal Fried Chicken	14	3	2010-03-31	Cartman's favorite restaurant has been shut down and replaced by a store that sells medicinal marijuana. Randy is desperate to get a prescription card to buy pot and Cartman will do anything to get his beloved fried chicken back.	https://www.southparkstudios.com/episodes/x5mqiz/south-park-medicinal-fried-chicken-season-14-ep-3	f	f
199	You Have 0 Friends	14	4	2010-04-07	When Kyle begs Stan to "friend" him, Stan gets sucked into Facebook.	https://www.southparkstudios.com/episodes/1hc2pe/south-park-you-have-0-friends-season-14-ep-4	f	f
202	Crippled Summer	14	7	2010-04-28	Jimmy and Timmy are off to summer camp with all their handicapable friends.	https://www.southparkstudios.com/episodes/lxnxlb/south-park-crippled-summer-season-14-ep-7	f	f
203	Poor and Stupid	14	8	2010-10-06	Cartman dreams of being a NASCAR driver and he's willing to do whatever it takes to make it happen.	https://www.southparkstudios.com/episodes/hmaufp/south-park-poor-and-stupid-season-14-ep-8	f	f
204	It's A Jersey Thing	14	9	2010-10-13	New Jersey is taking over the nation one state at a time. Randy and the boys take a stand as the Jerseyites approach South Park.	https://www.southparkstudios.com/episodes/ueimun/south-park-it-s-a-jersey-thing-season-14-ep-9	f	f
205	Insheeption	14	10	2010-10-20	When Stan is sent to the school counselor because he's holding on to an obscene number of useless possessions, he realizes that Mr. Mackey has a hoarding disorder too.	https://www.southparkstudios.com/episodes/l7svnd/south-park-insheeption-season-14-ep-10	f	f
206	Coon 2: Hindsight	14	11	2010-10-27	"Coon and Friends" set out to help the victims of BP's latest catastrophic drilling accident in the Gulf. Much to the Coon's dismay, another Super Hero gets there first.	https://www.southparkstudios.com/episodes/5xx4ao/south-park-coon-2-hindsight-season-14-ep-11	f	f
207	Mysterion Rises	14	12	2010-11-03	Mysterion's true identity is revealed. Meanwhile, the Coon, scorned by his fellow Super Heroes, is out for revenge.	https://www.southparkstudios.com/episodes/2lhwyz/south-park-mysterion-rises-season-14-ep-12	f	f
208	Coon vs. Coon & Friends	14	13	2010-11-10	Coon and Friends find themselves at the mercy of Cartman who now has the dark lord, Cthulhu, doing his bidding. Kenny wrestles with the curse of his super power through his alter ego, Mysterion.	https://www.southparkstudios.com/episodes/avmdp8/south-park-coon-vs-coon-friends-season-14-ep-13	f	f
209	Crème Fraiche	14	14	2010-11-17	Randy's obsession with the Food Network forces Sharon to explore a new interest of her own.	https://www.southparkstudios.com/episodes/dsbhg9/south-park-creme-fraiche-season-14-ep-14	f	f
210	HUMANCENTiPAD	15	1	2011-04-27	Kyle is intimately involved in the development of a revolutionary new product called HumancentiPad.	https://www.southparkstudios.com/episodes/j6a6zs/south-park-humancentipad-season-15-ep-1	f	f
211	Funnybot	15	2	2011-05-04	Jimmy hosts the Special Ed Department's First Annual Comedy Awards.	https://www.southparkstudios.com/episodes/9xrwb4/south-park-funnybot-season-15-ep-2	f	f
212	Royal Pudding	15	3	2011-05-11	The Prince of Canada is about to take a Princess and Ike is obsessed with the Royal Wedding.	https://www.southparkstudios.com/episodes/96vz9g/south-park-royal-pudding-season-15-ep-3	f	f
213	T.M.I.	15	4	2011-05-18	Cartman throws a fit when the boys' penis sizes are posted on the school bulletin board, and is sent to anger management therapy.	https://www.southparkstudios.com/episodes/axbak0/south-park-t-m-i-season-15-ep-4	f	f
214	Crack Baby Athletic Association	15	5	2011-05-25	Kyle gets in on the ground floor of Cartman's latest business venture, The Crack Baby Athletic Association.	https://www.southparkstudios.com/episodes/poic89/south-park-crack-baby-athletic-association-season-15-ep-5	f	f
215	City Sushi	15	6	2011-06-01	Butters is diagnosed with multiple personality disorder.	https://www.southparkstudios.com/episodes/dhi2tb/south-park-city-sushi-season-15-ep-6	f	f
216	You're Getting Old	15	7	2011-06-08	Just after Stan's 10th birthday, his worldview starts to change and so do his friendships.	https://www.southparkstudios.com/episodes/pxvz34/south-park-you-re-getting-old-season-15-ep-7	f	f
217	Ass Burgers	15	8	2011-10-05	Cartman finds a unique way to cope with Asperger's Syndrome.	https://www.southparkstudios.com/episodes/2b4m4s/south-park-ass-burgers-season-15-ep-8	f	f
218	The Last of the Meheecans	15	9	2011-10-12	Cartman joins the U.S. Border Patrol.	https://www.southparkstudios.com/episodes/rcs4ge/south-park-the-last-of-the-meheecans-season-15-ep-9	f	f
219	Bass to Mouth	15	10	2011-10-19	The kids' most scandalous secrets are being leaked on an outrageous new gossip website.	https://www.southparkstudios.com/episodes/yhhd0f/south-park-bass-to-mouth-season-15-ep-10	f	f
220	Broadway Bro Down	15	11	2011-10-26	After Randy takes Sharon to see a hit musical, he becomes Broadway's biggest fan.	https://www.southparkstudios.com/episodes/1nq9xv/south-park-broadway-bro-down-season-15-ep-11	f	f
221	1%	15	12	2011-11-02	The 99% is ganging up on Eric Cartman.	https://www.southparkstudios.com/episodes/k5327t/south-park-1-season-15-ep-12	f	f
222	A History Channel Thanksgiving	15	13	2011-11-09	The boys are getting close to discovering the truth about the first Thanksgiving.	https://www.southparkstudios.com/episodes/ex6roo/south-park-a-history-channel-thanksgiving-season-15-ep-13	f	f
223	The Poor Kid	15	14	2011-11-16	Kenny ends up in the foster care system after his parents are arrested.	https://www.southparkstudios.com/episodes/t9jqji/south-park-the-poor-kid-season-15-ep-14	f	f
224	Reverse Cowgirl	16	1	2012-03-14	When one of the boys leaves the toilet seat up after he uses the bathroom, an unspeakable tragedy occurs.	https://www.southparkstudios.com/episodes/c98dqj/south-park-reverse-cowgirl-season-16-ep-1	f	f
225	Cash For Gold	16	2	2012-03-21	Cartman launches his own gem shopping channel.	https://www.southparkstudios.com/episodes/by1nbe/south-park-cash-for-gold-season-16-ep-2	f	f
226	Faith Hilling	16	3	2012-03-28	The kids are in danger when new trends start to evolve and shift at a rapid pace.	https://www.southparkstudios.com/episodes/g9h6mq/south-park-faith-hilling-season-16-ep-3	f	f
227	Jewpacabra	16	4	2012-04-04	The town's big Easter Egg Hunt is in jeopardy when Cartman produces video evidence of a mysterious creature lurking in the woods.	https://www.southparkstudios.com/episodes/f756rp/south-park-jewpacabra-season-16-ep-4	f	f
228	Butterballs	16	5	2012-04-11	Butters is the victim of an unlikely bully.	https://www.southparkstudios.com/episodes/0lctr4/south-park-butterballs-season-16-ep-5	f	f
229	I Should Have Never Gone Ziplining	16	6	2012-04-18	The boys' ziplining adventure becomes a terrifying test of survival.	https://www.southparkstudios.com/episodes/9vau76/south-park-i-should-have-never-gone-ziplining-season-16-ep-6	f	f
230	Cartman Finds Love	16	7	2012-04-25	The time has finally come for Cartman to let a special someone know exactly how he feels.	https://www.southparkstudios.com/episodes/iyw8ps/south-park-cartman-finds-love-season-16-ep-7	f	f
231	Sarcastaball	16	8	2012-09-26	South Park Elementary takes steps to address football's concussion crisis.	https://www.southparkstudios.com/episodes/x8uh1a/south-park-sarcastaball-season-16-ep-8	f	f
232	Raising The Bar	16	9	2012-10-03	Cartman finally admits he's fat and immediately gets a mobility scooter.	https://www.southparkstudios.com/episodes/egyait/south-park-raising-the-bar-season-16-ep-9	f	f
233	Insecurity	16	10	2012-10-10	Cartman signs up for a home security system.	https://www.southparkstudios.com/episodes/tyqohz/south-park-insecurity-season-16-ep-10	f	f
234	Going Native	16	11	2012-10-17	It is time for Butters to begin a journey where he will follow in the path of his Hawaiian ancestors.	https://www.southparkstudios.com/episodes/hrno4n/south-park-going-native-season-16-ep-11	f	f
235	A Nightmare On FaceTime	16	12	2012-10-24	Randy's big plans for Halloween night keep Stan from trick or treating with his friends.	https://www.southparkstudios.com/episodes/bghu33/south-park-a-nightmare-on-facetime-season-16-ep-12	f	f
236	A Scause For Applause	16	13	2012-10-31	A serious doping scandal shakes everyone's faith in a beloved icon. Everyone who once supported the fallen hero is now cutting off their symbolic yellow wristbands.	https://www.southparkstudios.com/episodes/1se5q4/south-park-a-scause-for-applause-season-16-ep-13	f	f
237	Obama Wins!	16	14	2012-11-07	Eric Cartman is hiding something in his bedroom that could change the entire outcome of the Presidential election.	https://www.southparkstudios.com/episodes/1oyb2s/south-park-obama-wins-season-16-ep-14	f	f
238	Let Go, Let Gov	17	1	2013-09-25	Cartman infiltrates the NSA and doesn't like what he finds in his personal file.	https://www.southparkstudios.com/episodes/8motqv/south-park-let-go-let-gov-season-17-ep-1	f	f
239	Informative Murder Porn	17	2	2013-10-02	The boys use the game of "Minecraft" as a distraction tokeep their parents from hurting each other.	https://www.southparkstudios.com/episodes/4sa1hk/south-park-informative-murder-porn-season-17-ep-2	f	f
240	World War Zimmerman	17	3	2013-10-09	Cartman sees Tolkien as a threat to all humanity.	https://www.southparkstudios.com/episodes/mbk94a/south-park-world-war-zimmerman-season-17-ep-3	f	f
241	Goth Kids 3: Dawn of the Posers	17	4	2013-10-23	The Goth kids are being sent away to a camp for troubled children.	https://www.southparkstudios.com/episodes/ski9r6/south-park-goth-kids-3-dawn-of-the-posers-season-17-ep-4	f	f
242	Taming Strange	17	5	2013-10-30	When Ike hits puberty, he and Kyle start to grow apart. To save their relationship, Kyle takes Ike to see a live performance of Yo Gabba Gabba.	https://www.southparkstudios.com/episodes/dpkd3j/south-park-taming-strange-season-17-ep-5	f	f
243	Ginger Cow	17	6	2013-11-06	Cartman's latest prank brings peace to the world.	https://www.southparkstudios.com/episodes/1uyt33/south-park-ginger-cow-season-17-ep-6	f	f
244	Black Friday	17	7	2013-11-13	The boys prepare to battle the crowds already lining up for the first official day of holiday shopping.	https://www.southparkstudios.com/episodes/g3ceb7/south-park-black-friday-season-17-ep-7	f	f
245	A Song of Ass and Fire	17	8	2013-11-20	Black Friday is almost here and the battle for the new gaming devices is heating up. Princess Kenny's betrayal has left Cartman out for revenge.	https://www.southparkstudios.com/episodes/tz6dfn/south-park-a-song-of-ass-and-fire-season-17-ep-8	f	f
246	Titties and Dragons	17	9	2013-12-04	The doors to the mall will finally open for the biggest Black Friday sale in history. The boys are divided over which gaming device to buy and a bloody battle will determine whether Xbox or Sony will be the winner.	https://www.southparkstudios.com/episodes/eimjio/south-park-titties-and-dragons-season-17-ep-9	f	f
247	The Hobbit	17	10	2013-12-11	When Wendy tries to fix one of her girlfriends up with Butters, she ends up in the counselor's office.	https://www.southparkstudios.com/episodes/pp7udu/south-park-the-hobbit-season-17-ep-10	f	f
248	Go Fund Yourself	18	1	2014-09-24	The boys name their new start-up company, The Washington Redskins.	https://www.southparkstudios.com/episodes/q743k3/south-park-go-fund-yourself-season-18-ep-1	f	f
249	Gluten Free Ebola	18	2	2014-10-01	South Park goes gluten free.	https://www.southparkstudios.com/episodes/7lho6r/south-park-gluten-free-ebola-season-18-ep-2	f	f
250	The Cissy	18	3	2014-10-08	Randy is harboring a giant secret and the pressure is getting to him. Meanwhile, Cartman calls Stan a cissy.	https://www.southparkstudios.com/episodes/2opbg6/south-park-the-cissy-season-18-ep-3	f	f
251	Handicar	18	4	2014-10-15	Timmy's successful new car service makes him a lot of enemies.	https://www.southparkstudios.com/episodes/muya48/south-park-handicar-season-18-ep-4	f	f
252	The Magic Bush	18	5	2014-10-29	Graphic video from an unknown drone is uploaded on the internet.	https://www.southparkstudios.com/episodes/vb9a1j/south-park-the-magic-bush-season-18-ep-5	f	f
253	Freemium Isn't Free	18	6	2014-11-05	Stan is addicted to the new Terrance and Phillip mobile game.	https://www.southparkstudios.com/episodes/jy5lbq/south-park-freemium-isn-t-free-season-18-ep-6	f	f
254	Grounded Vindaloop	18	7	2014-11-12	Butters is convinced he's living in a virtual reality.	https://www.southparkstudios.com/episodes/y3uvvc/south-park-grounded-vindaloop-season-18-ep-7	f	f
255	Cock Magic	18	8	2014-11-19	There are illegal goings-on in the basement of City Wok.	https://www.southparkstudios.com/episodes/p9i8uw/south-park-cock-magic-season-18-ep-8	f	f
256	#REHASH	18	9	2014-12-03	Kyle just wants to play video games with his little brother. But, when Ike doesn't want to play with him anymore, Kyle is afraid that the next generation is passing him by.	https://www.southparkstudios.com/episodes/2bf9a5/south-park-rehash-season-18-ep-9	f	f
257	#HappyHolograms	18	10	2014-12-10	Cartmaan Bra is trending as the country prepares to watch the biggest Holiday Spectacular ever.	https://www.southparkstudios.com/episodes/ndr2at/south-park-happyholograms-season-18-ep-10	f	f
258	Stunning and Brave	19	1	2015-09-16	The boys express their utmost respect for Caitlyn Jenner in the most stunning and brave South Park ever.	https://www.southparkstudios.com/episodes/h4o269/south-park-stunning-and-brave-season-19-ep-1	f	f
259	Where My Country Gone?	19	2	2015-09-23	Garrison wants to build a wall to keep out all of the undocumented immigrants.	https://www.southparkstudios.com/episodes/dfdwfl/south-park-where-my-country-gone-season-19-ep-2	f	f
260	The City Part of Town	19	3	2015-09-30	The town of South Park is gentrifying and Kenny thinks it's time to get a job.	https://www.southparkstudios.com/episodes/v9t3m6/south-park-the-city-part-of-town-season-19-ep-3	f	f
261	You're Not Yelping	19	4	2015-10-14	Cartman considers himself the top on-line restaurant reviewer in South Park.\n\n	https://www.southparkstudios.com/episodes/en0srq/south-park-you-re-not-yelping-season-19-ep-4	f	f
262	Safe Space	19	5	2015-10-21	Cartman is the latest victim of body shaming.	https://www.southparkstudios.com/episodes/oeajfq/south-park-safe-space-season-19-ep-5	f	f
263	Tweek x Craig	19	6	2015-10-28	The Asian girls in school are drawing dreamy pictures of Tweek and Craig.	https://www.southparkstudios.com/episodes/x4lqr3/south-park-tweek-x-craig-season-19-ep-6	f	f
264	Naughty Ninjas	19	7	2015-11-11	The citizens of South Park decide they no longer need a police force in town.	https://www.southparkstudios.com/episodes/pxhhxe/south-park-naughty-ninjas-season-19-ep-7	f	f
265	Sponsored Content	19	8	2015-11-18	Jimmy's integrity as a newsman runs smack into PC Principal's ideology. 	https://www.southparkstudios.com/episodes/pzzs15/south-park-sponsored-content-season-19-ep-8	f	f
266	Truth and Advertising	19	9	2015-12-02	PC Principal disappears with two of the 4th grade students.	https://www.southparkstudios.com/episodes/ppnf3g/south-park-truth-and-advertising-season-19-ep-9	f	f
267	PC Principal Final Justice	19	10	2015-12-09	Kyle has chosen a dangerous alliance over his friendship with Stan.	https://www.southparkstudios.com/episodes/exg4nv/south-park-pc-principal-final-justice-season-19-ep-10	f	f
268	Member Berries	20	1	2016-09-14	Garrison is still hot on the campaign trail.	https://www.southparkstudios.com/episodes/oq0xia/south-park-member-berries-season-20-ep-1	f	f
269	Skank Hunt	20	2	2016-09-21	Kyle's dad manages to keep his identity as a troll a secret while he takes his on-line abuse global.	https://www.southparkstudios.com/episodes/wrlyv5/south-park-skank-hunt-season-20-ep-2	f	f
270	The Damned	20	3	2016-09-28	Gerald is thrilled with the media attention as he continues to troll everyone and anyone.	https://www.southparkstudios.com/episodes/fpihop/south-park-the-damned-season-20-ep-3	f	f
271	Wieners Out	20	4	2016-10-12	The boys band together to stand up for their rights.	https://www.southparkstudios.com/episodes/gmluc5/south-park-wieners-out-season-20-ep-4	f	f
272	Douche and a Danish	20	5	2016-10-19	Giant Douche wants out of the Presidential race.	https://www.southparkstudios.com/episodes/zi1v0u/south-park-douche-and-a-danish-season-20-ep-5	f	f
273	Fort Collins	20	6	2016-10-26	An entire city in Colorado gets hacked. Gerald and Cartman may lose everything when their complete history of internet activity becomes public.	https://www.southparkstudios.com/episodes/mr5c13/south-park-fort-collins-season-20-ep-6	f	f
274	Oh, Jeez	20	7	2016-11-09	Gerald comes face-to-face with the Troll Hunter.	https://www.southparkstudios.com/episodes/9gzguw/south-park-oh-jeez-season-20-ep-7	f	f
275	Members Only	20	8	2016-11-16	The new President-elect pays a visit to his hometown.	https://www.southparkstudios.com/episodes/s0b5rt/south-park-members-only-season-20-ep-8	f	f
276	Not Funny	20	9	2016-11-30	Cartman is certain that Butters is trying to steal his girlfriend.	https://www.southparkstudios.com/episodes/8avhur/south-park-not-funny-season-20-ep-9	f	f
277	The End of Serialization As We Know It	20	10	2016-12-07	Cartman finally understands why Heidi wants to get him to Mars.	https://www.southparkstudios.com/episodes/rqcgz5/south-park-the-end-of-serialization-as-we-know-it-season-20-ep-10	f	f
278	White People Renovating Houses	21	1	2017-09-13	Protestors armed with tiki torches and confederate flags take to the streets of South Park. Randy comes to grips with what it means to be white in today's society.	https://www.southparkstudios.com/episodes/p4ucy0/south-park-white-people-renovating-houses-season-21-ep-1	f	f
279	Put It Down	21	2	2017-09-20	When Tweek is caught in the middle of a petty conflict, it drives his relationship with Craig to the brink.	https://www.southparkstudios.com/episodes/46s8wh/south-park-put-it-down-season-21-ep-2	f	f
280	Holiday Special	21	3	2017-09-27	In a return to form, a forbidden love story between a white man and a Native American man unfolds. However, the boys' story exploits people's misery for laughs. 4 ½ out of 5 stars. A-	https://www.southparkstudios.com/episodes/hswgo6/south-park-holiday-special-season-21-ep-3	f	f
281	Franchise Prequel	21	4	2017-10-11	Professor Chaos has found the perfect tool to spread lies and misinformation about Coon and Friends. In trying to save their reputation, the boys come face to face with Mark Zuckerberg.	https://www.southparkstudios.com/episodes/5tj3ff/south-park-franchise-prequel-season-21-ep-4	f	f
282	Hummels & Heroin	21	5	2017-10-18	Drugs are flowing into South Park. A passionate young health advocate has traced the source of these illegal meds and is about to expose Stan Marsh.	https://www.southparkstudios.com/episodes/wrnwv5/south-park-hummels-heroin-season-21-ep-5	f	f
283	Sons a Witches	21	6	2017-10-25	This year at the traditional Halloween get together, a witch casts a spell that terrorizes the town and ruins Halloween for the boys. Cartman sees a way to use the witch's power to his advantage.	https://www.southparkstudios.com/episodes/zrbq13/south-park-sons-a-witches-season-21-ep-6	f	f
284	Doubling Down	21	7	2017-11-08	Kyle doesn't understand why Heidi won't break up with Cartman. He's playing with fire when he gets in the middle of the school's most talked about couple.	https://www.southparkstudios.com/episodes/1f66wc/south-park-doubling-down-season-21-ep-7	f	f
285	Moss Piglets	21	8	2017-11-15	Jimmy and Timmy's project has caught the attention of some very important people. Their experiment could have far reaching implications that could save the world… and they might even win first prize in this year's science fair.	https://www.southparkstudios.com/episodes/b67nke/south-park-moss-piglets-season-21-ep-8	f	f
286	SUPER HARD PCness	21	9	2017-11-29	PC Principal is wrestling with some unfamiliar feelings. Meanwhile, boys will be boys except for Kyle who, for the first time, seems to see things differently from the rest of his friends.	https://www.southparkstudios.com/episodes/9wx0zg/south-park-super-hard-pcness-season-21-ep-9	f	f
287	Splatty Tomato	21	10	2017-12-06	The children of South Park claim to have seen Mr. Garrison lurking around town and they're frightened. The town comes together to make the President go away.	https://www.southparkstudios.com/episodes/l1xpyg/south-park-splatty-tomato-season-21-ep-10	f	f
288	Dead Kids	22	1	2018-09-26	Sharon is abnormally emotional and it's really getting Randy down.	https://www.southparkstudios.com/episodes/ykf57h/south-park-dead-kids-season-22-ep-1	f	f
289	A Boy and a Priest	22	2	2018-10-03	A Boy and a Priest - The town finds the church doors locked and there's no sign of Butters or the Pastor.	https://www.southparkstudios.com/episodes/hjfzgc/south-park-a-boy-and-a-priest-season-22-ep-2	f	f
290	The Problem with a Poo	22	3	2018-10-10	The Problem with a Poo - Mr. Hankey's offensive behavior puts him in jeopardy of being fired as the Director of the Annual Christmas Pageant.	https://www.southparkstudios.com/episodes/38exov/south-park-the-problem-with-a-poo-season-22-ep-3	f	f
291	Tegridy Farms	22	4	2018-10-17	Tegridy Farms - Randy moves the family to the country and he takes up farming.	https://www.southparkstudios.com/episodes/5b6ld6/south-park-tegridy-farms-season-22-ep-4	f	f
292	The Scoots	22	5	2018-10-31	The Scoots - The kids plan to use the latest revolution in mobility to get more candy on Halloween than they have ever gotten before.	https://www.southparkstudios.com/episodes/c5x1x5/south-park-the-scoots-season-22-ep-5	f	f
293	Time to Get Cereal	22	6	2018-11-07	Time to Get Cereal - South Park Citizens are in danger and the boys realize that only Al Gore can help.	https://www.southparkstudios.com/episodes/ngow57/south-park-time-to-get-cereal-season-22-ep-6	f	f
295	Buddha Box	22	8	2018-11-26	Cartman has been diagnosed with anxiety.	https://www.southparkstudios.com/episodes/xj9ctz/south-park-buddha-box-season-22-ep-8	f	f
296	Unfulfilled	22	9	2018-12-05	South Park is chosen to be the home for Amazon's newest Fulfillment Center.	https://www.southparkstudios.com/episodes/o7l8co/south-park-unfulfilled-season-22-ep-9	f	f
297	Bike Parade	22	10	2018-12-12	The boys' chance of winning the Bike Parade is in jeopardy when Kenny quits.	https://www.southparkstudios.com/episodes/82j5ue/south-park-bike-parade-season-22-ep-10	f	f
298	Mexican Joker	23	1	2019-09-25	Randy fights against home-grown. Meanwhile, Kyle goes to camp.	https://www.southparkstudios.com/episodes/fi4nmu/south-park-mexican-joker-season-23-ep-1	f	f
299	Band in China	23	2	2019-10-02	Randy sees an opportunity for Tegridy in China.	https://www.southparkstudios.com/episodes/4yl119/south-park-band-in-china-season-23-ep-2	f	f
300	SHOTS!!!	23	3	2019-10-09	Randy celebrates the success of Tegridy Farms while Cartman refuses to get a shot.	https://www.southparkstudios.com/episodes/o2ma0w/south-park-shots-season-23-ep-3	f	f
301	Let Them Eat Goo	23	4	2019-10-16	Cartman is sure the new plant-based diet in the school cafeteria gave him a heart attack.	https://www.southparkstudios.com/episodes/wnbonm/south-park-let-them-eat-goo-season-23-ep-4	f	f
302	Tegridy Farms Halloween Special	23	5	2019-10-30	It's Halloween and Randy is dealing with his daughter's marijuana problem.	https://www.southparkstudios.com/episodes/mrtmad/south-park-tegridy-farms-halloween-special-season-23-ep-5	f	f
303	Season Finale	23	6	2019-11-06	The citizens of South Park have had enough of Randy and Tegridy Farms and they just want to lock him up.	https://www.southparkstudios.com/episodes/0ltms9/south-park-season-finale-season-23-ep-6	f	f
304	Board Girls	23	7	2019-11-13	The annual Strong Woman competition pushes everyone to their limits.	https://www.southparkstudios.com/episodes/5xm5ws/south-park-board-girls-season-23-ep-7	f	f
305	Turd Burglars	23	8	2019-11-27	Kyle's mom has a fecal transplant and the boys are on a quest for the best microbiome.	https://www.southparkstudios.com/episodes/49wi25/south-park-turd-burglars-season-23-ep-8	f	f
306	Basic Cable	23	9	2019-12-04	Scott Malkinson's desperate to impress the new girl in his class.	https://www.southparkstudios.com/episodes/jiru42/south-park-basic-cable-season-23-ep-9	f	f
307	Christmas Snow	23	10	2019-12-11	Santa is stealing all the joy from the town's Holiday Season.	https://www.southparkstudios.com/episodes/z4ipl3/south-park-christmas-snow-season-23-ep-10	f	f
308	The Pandemic Special	24	1	2020-09-30	With the school on lock-down, Butters flips out knowing that things may never go back to normal.	https://www.southparkstudios.com/episodes/yy0vjs/south-park-the-pandemic-special-season-24-ep-1	f	f
309	South ParQ Vaccination Special	24	2	2021-03-10	The citizens of South ParQ are clamoring for the COVID-19 vaccine. A hilarious new militant group tries to stop the boys from getting their teacher vaccinated.	https://www.southparkstudios.com/episodes/0ncw71/south-park-south-parq-vaccination-special-season-24-ep-2	f	f
310	Pajama day	25	1	2022-02-02	After failing to show respect for their teacher, PC Principal revokes Pajama Day privileges for the entire 4th grade class. Cartman is distraught. The kids aren't going to stand for it but PC Principal refuses to back down.	https://www.southparkstudios.com/episodes/vrwkb7/south-park-pajama-day-season-25-ep-1	f	f
311	The Big Fix	25	2	2022-02-09	Stan's horrified to realize he's misinterpreted some of the greatest writing of all time.	https://www.southparkstudios.com/episodes/m339tu/south-park-the-big-fix-season-25-ep-2	f	f
312	City People	25	3	2022-02-16	Cartman is not happy when his mom gets a new job.	https://www.southparkstudios.com/episodes/pnkrck/south-park-city-people-season-25-ep-3	f	f
313	Back to the Cold War	25	4	2022-03-02	A lot is riding on Butter's ability to crush the competition in the all-important dressage championship.	https://www.southparkstudios.com/episodes/ohj8pg/south-park-back-to-the-cold-war-season-25-ep-4	f	f
314	Help, My Teenager Hates Me!	25	5	2022-03-09	The boys find out that the joys of playing Airsoft come with the challenges of dealing with teenagers.	https://www.southparkstudios.com/episodes/b6uh34/south-park-help-my-teenager-hates-me-season-25-ep-5	f	f
315	Credigree Weed St. Patrick's Day Special	25	6	2022-03-16	Butters is shocked to learn that people in South Park don’t understand what St. Patrick’s Day is really about.	https://www.southparkstudios.com/episodes/l3rtf5/south-park-credigree-weed-st-patrick-s-day-special-season-25-ep-6	f	f
316	Cupid Ye	26	1	2023-02-08	Kyle explains what he learned about Hollywood and stereotypes.	https://www.southparkstudios.com/episodes/2dhgcd/south-park-cupid-ye-season-26-ep-1	f	f
317	The World-Wide Privacy Tour	26	2	2023-02-15	The prince of Canada and his wife try to find privacy and seclusion in a small mountain town.	https://www.southparkstudios.com/episodes/3ne660/south-park-the-world-wide-privacy-tour-season-26-ep-2	f	f
318	Japanese Toilet	26	3	2023-03-01	South Park learns about the wonders of Japanese toilets.	https://www.southparkstudios.com/episodes/9niic5/south-park-japanese-toilet-season-26-ep-3	f	f
319	Deep Learning	26	4	2023-03-08	Stan is reeling when a cheating scandal hits the school.	https://www.southparkstudios.com/episodes/8byci4/south-park-deep-learning-season-26-ep-4	f	f
320	DikinBaus Hot Dogs	26	5	2023-03-22	Cartman and Kenny come up with the best name for their new restaurant. Meanwhile, Butters wants to know when he will see a return on his investment.	https://www.southparkstudios.com/episodes/2iz7sf/south-park-dikinbaus-hot-dogs-season-26-ep-5	f	f
1	Cartman Gets an Anal Probe	1	1	1997-08-13	While the boys are waiting for the school bus, Cartman explains the odd nightmare he had the previous night involving alien visitors.	https://www.southparkstudios.com/episodes/940f8z/south-park-cartman-gets-an-anal-probe-season-1-ep-1	f	f
2	Weight Gain 4000	1	2	1997-08-27	When Cartman's environmental essay wins a national contest, America's sweetheart, Kathie Lee Gifford, comes to South Park to present the award.	https://www.southparkstudios.com/episodes/er4a32/south-park-weight-gain-4000-season-1-ep-2	f	f
3	Volcano	1	3	1997-08-20	A weekend trip to experience the finer points of camping, fishing and blowing animals to smithereens is threatened by an erupting volcano.	https://www.southparkstudios.com/episodes/iuifco/south-park-volcano-season-1-ep-3	f	f
4	Big Gay Al's Big Gay Boat Ride	1	4	1997-09-03	When Stan discovers his new dog Sparky is gay, he becomes so confused he loses his will to play in the big Homecoming Football game against Middle Park.	https://www.southparkstudios.com/episodes/4rcpa5/south-park-big-gay-al-s-gay-boat-ride-season-1-ep-4	f	f
5	An Elephant Makes Love to a Pig	1	5	1997-09-10	Kyle's mom will not let him keep his new pet, an elephant because it is so huge. So the boys turn to Dr. Mephesto to genetically engineer a smaller elephant.	https://www.southparkstudios.com/episodes/2ly7rt/south-park-an-elephant-makes-love-to-a-pig-season-1-ep-5	f	f
6	Death	1	6	1997-09-17	Grandpa's sole birthday wish is for Stan to take part in his assisted suicide. Meanwhile, Mrs. Broflovski has organized a protest against the boys' favorite TV show, "Terrance and Phillip".	https://www.southparkstudios.com/episodes/u9aiib/south-park-death-season-1-ep-6	f	f
7	Pinkeye	1	7	1997-10-29	A mishap at the morgue transforms the residents of South Park into brain-eating zombies and threatens the boys' night of Trick-or-Treating.	https://www.southparkstudios.com/episodes/weqe2a/south-park-pinkeye-season-1-ep-7	f	f
8	Starvin' Marvin	1	8	1997-11-19	Mistaking Cartman for a starving African child, government authorities send him to Ethiopia where he runs into Sally Struthers.	https://www.southparkstudios.com/episodes/scexjh/south-park-starvin-marvin-season-1-ep-8	f	f
9	Mr. Hankey, the Christmas Poo	1	9	1997-12-17	While South Park Elementary is attempting to stage a non-denominational holiday play that will not offend (or entertain) anyone, Kyle checks himself into the South Park mental asylum.	https://www.southparkstudios.com/episodes/rmf3o8/south-park-mr-hankey-the-christmas-poo-season-1-ep-9	f	f
10	Damien	1	10	1998-02-04	After being shunned by the others kids, Damien, the Son of Satan, calls upon his father to fight Jesus in the ultimate Pay-Per-View Boxing Match between good and evil.	https://www.southparkstudios.com/episodes/mfcnvu/south-park-damien-season-1-ep-10	f	f
11	Tom's Rhinoplasty	1	11	1998-02-11	While Mr. Garrison deserts the class for a visit to Tom's Rhinoplasty, Stan, Kyle, Kenny, and Cartman all compete for the attention of Ms. Ellen, the new substitute teacher.	https://www.southparkstudios.com/episodes/44i3y3/south-park-tom-s-rhinoplasty-season-1-ep-11	f	f
12	Mecha-Streisand	1	12	1998-02-18	The boys' discovery of a prehistoric relic spawns a monster that threatens to destroy South Park and the world.	https://www.southparkstudios.com/episodes/negd7t/south-park-mecha-streisand-season-1-ep-12	f	f
321	Spring Break	26	6	2023-03-29	Spring Break is an excuse for Garrison to jump back into his former depraved lifestyle.	https://www.southparkstudios.com/episodes/7ux3j6/south-park-spring-break-season-26-ep-6	f	f
322	Sermon on the ‘Mount	27	1	2025-07-23	When the residents of South Park face their possible demise, Jesus returns to give them an important message.	https://www.southparkstudios.com/episodes/bfn06o/south-park-sermon-on-the-mount-season-27-ep-1	f	t
323	Got A Nut	27	2	2025-08-06	When Mr. Mackey loses his job, he desperately tries to find a new way to make a living.	https://www.southparkstudios.com/episodes/9756cz/south-park-got-a-nut-season-27-ep-2	f	t
324	Sickofancy	27	3	2025-08-20	Sharon helps Randy come down from his Ketamine bender and the Marsh family sells Tegridy Farms.	https://www.southparkstudios.com/episodes/bdoemj/south-park-sickofancy-season-27-ep-3	f	t
13	Cartman's Mom is a Dirty S***	1	13	1998-02-25	Who is Eric Cartman's father? It could be anyone who attended South Park's 12th Annual Drunken Barn Dance.	https://www.southparkstudios.com/episodes/dumjvr/south-park-cartman-s-mom-is-a-dirty-slut-season-1-ep-13	f	f
14	Terrance and Phillip in Not Without My Anus	2	1	1998-04-01	Terrance and Phillip must save Terrance's little daughter, Sally, and all of Canada from an evil dictator.	https://www.southparkstudios.com/episodes/utrgmi/south-park-terrance-and-phillip-in-not-without-my-anus-season-2-ep-1	f	f
15	Cartman's Mom Is Still a Dirty S	2	2	1998-04-22	The boys wait for Dr. Mephesto to regain consciousness and reveal the identity of Cartman's father.	https://www.southparkstudios.com/episodes/vhjxun/south-park-cartman-s-mom-is-still-a-dirty-slut-season-2-ep-2	f	f
16	Ike's Wee Wee	2	3	1998-05-20	Mr. Mackey, the school counselor, is fired and turns to drugs and alcohol. Meanwhile, when the boys find out what it means to be circumcised they try to save Ike from his bris.	https://www.southparkstudios.com/episodes/i3ry4k/south-park-ike-s-wee-wee-season-2-ep-3	f	f
18	Conjoined Fetus Lady	2	5	1998-06-03	With Pip as their star player, the South Park dodgeball team is off to the championships.	https://www.southparkstudios.com/episodes/wl2v8q/south-park-conjoined-fetus-lady-season-2-ep-5	f	f
19	The Mexican Staring Frog of Southern Sri Lanka	2	6	1998-06-10	Jimbo and Ned's efforts to drive up the ratings for their new hunting show on the cable access channel threatens to edge out an old favorite, Jesus and Pals.	https://www.southparkstudios.com/episodes/q9v4qf/south-park-the-mexican-staring-frog-of-southern-sri-lanka-season-2-ep-6	f	f
31	Prehistoric Ice Man	2	18	1999-01-20	The boys' discovery of a man encased in ice threatens Stan and Kyle's friendship.	https://www.southparkstudios.com/episodes/19f06j/south-park-prehistoric-ice-man-season-2-ep-18	t	f
68	Super Best Friends	5	3	2001-07-04	A magician performs in South Park, convincing Kenny, Cartman and Kyle to join his cult-like following, leaving Stan & Jesus to save them.	https://www.southparkstudios.com/episodes/b1846v/south-park-super-best-friends-season-5-ep-3	t	f
142	Cartoon Wars Part I	10	3	2006-04-05	Cartman and Kyle are at war over the popular cartoon "Family Guy."	https://www.southparkstudios.com/episodes/m6ohvr/south-park-cartoon-wars-part-i-season-10-ep-3	t	f
143	Cartoon Wars Part II	10	4	2006-04-12	After leaving Kyle injured on the side of the road, Cartman races to the headquarters of "Family Guy" determined to put an end to the show once and for all.	https://www.southparkstudios.com/episodes/ov0kz8/south-park-cartoon-wars-part-ii-season-10-ep-4	t	f
200	200	14	5	2010-04-14	The town of South Park faces a class action lawsuit as every celebrity they've ever ridiculed is out for revenge.	https://www.southparkstudios.com/episodes/uxg9g7/south-park-200-season-14-ep-5	t	f
201	201	14	6	2010-04-21	Angry celebrities, violent ginger kids and Mecha Streisand are about to destroy South Park and all anyone wants to know is, "Who is Eric Cartman's father?"	https://www.southparkstudios.com/episodes/wrosbx/south-park-201-season-14-ep-6	t	f
294	Nobody Got Cereal?	22	7	2018-11-14	The boys break out of jail and are on the run from the police and ManBearPig.	https://www.southparkstudios.com/episodes/sagwyy/south-park-nobody-got-cereal-season-22-ep-7	t	f
325	Wok is Dead	27	4	2025-09-03	Butters experiences the reality of tariffs when he has to buy a Labubu doll for his girlfriend’s birthday.	https://www.southparkstudios.com/episodes/7kgkzb/south-park-wok-is-dead-season-27-ep-4	f	t
326	Conflict of Interest	27	5	2025-09-24	Kyle and Cartman are at odds when a prediction markets app gets popular with their fellow students.	\N	f	t
\.


--
-- Data for Name: families; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.families (id, name, images) FROM stdin;
1	The Broflovskis	\N
2	The Cartmans	\N
3	The Marshs	\N
4	The McCormicks	\N
5	The Adams-Makowskis	\N
6	The Andersons / O'Donnells	\N
7	The Barbradys	\N
8	The Biggles	\N
9	The Blacks	\N
10	The Burchs	\N
11	The Charlotte's Family	\N
12	The Cotswolds	\N
13	The Daniels	\N
14	The Donovans	\N
15	The Feegan	\N
16	The Garrisons	\N
17	The Grays	\N
18	The Gueermos	\N
19	The Hankeys	\N
20	The Harrisons	\N
21	The Handlers	\N
22	The Knitts	\N
23	The McArthurs	\N
24	The Malkinsons	\N
25	The Mackeys	\N
26	The Larsens	\N
27	The McElroys	\N
28	The Nelly's Family	\N
29	The Michael's Family	\N
30	The Mephestos	\N
31	The PC Family	\N
32	The Nelsons	\N
33	The Stoots	\N
34	The Stotchs	\N
35	The Stoleys	\N
36	The Stevens	\N
37	The Rodriguezes	\N
38	The Petuskis	\N
39	The Streibels	\N
40	The Tenormans	\N
41	The Testaburgers	\N
42	The Thorns	\N
43	The Tuckers	\N
44	The Turners	\N
45	The Zewiskis	\N
46	The Whites	\N
47	The Valmers	\N
48	The Tweaks	\N
49	The Slave/Big Gay Al Familiy	\N
50	The Hakeems	\N
51	The Hagens	\N
52	The Hitlers	\N
53	Alice's Family	\N
54	The Varcas	\N
55	The Obamas	\N
56	The Simpsons	\N
57	The Thompsns	\N
58	The Clintons	\N
59	The Jacksons	\N
60	The Palmers	\N
61	Buck's Family	\N
\.


--
-- Data for Name: games; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.games (id, name, developer, platforms, realese_date, images) FROM stdin;
1	South Park Imaginationland	Mr. Goodliving	{IOS}	2008-07-10	\N
2	South Park (Videogame)	Appaloosa Interactive	{PS1}	1999-09-30	\N
3	South Park Mega Millionaire	GameHouse	{IOS,"Blackberry OS"}	2010-01-26	\N
4	South Park Let's Go Tower Defense Play!	South Park Digital Studios	{X360}	2009-10-07	\N
5	South Park Mega Millionaire	GameHouse	{Android}	2012-07-02	\N
6	South Park: Tenorman's Revenge	South Park Digital Studios	{X360}	2012-03-30	\N
7	South Park: Phone Destroyer	RedLynx	{IOS,Android}	2017-11-09	\N
8	South Park: The Stick of Truth	Obsidian Entertainment	{Switch}	2018-09-25	\N
9	South Park: The Stick of Truth	Obsidian Entertainment	{PS4,XOne}	2018-02-13	\N
10	South Park: The Stick of Truth	Obsidian Entertainment	{PC,X360,PS3}	2014-03-04	\N
11	South Park (Videogame)	Iguana Entertainment	{N64}	1998-12-21	\N
12	South Park Pinball (Original Realese)	Zen Studios	{PS3,PSVita,PS4}	2014-10-14	\N
13	South Park (Videogame)	Crawfish Interactive	{GBC}	\N	\N
14	South Park (Videogame)	Iguana Entertainment	{PC}	1999-03-01	\N
15	South Park (Pinball Machine)	Software: Neil Falconer, Orin Day. Hardware: Joe Balcer, Rob Hurtado	{"Pinball Machine"}	1999-02-01	\N
16	South Park: Chef's Luv Shack	Acclaim	{PC}	1999-12-01	\N
17	South Park: Chef's Luv Shack	Acclaim	{PS1,N64}	1999-11-16	\N
18	South Park: Chef's Luv Shack	Acclaim	{Dreamcast}	1999-09-09	\N
19	South Park Rally	Tantalus Interactive	{PS1}	2000-01-05	\N
20	South Park Rally	Tantalus Interactive	{N64}	2000-02-28	\N
21	South Park Rally	Tantalus Interactive	{PC}	2000-01-24	\N
22	South Park Rally	Tantalus Interactive	{Dreamcast}	2000-07-07	\N
23	South Park: Big Wheel Death Rally	South Park Digital Studios	{Web}	2006-01-01	\N
24	South Park Double Bunny	South Park Digital Studios	{Web}	\N	\N
25	South Park Pinball (Original Realese)	Zen Studios	{XOne}	2014-10-16	\N
26	South Park Pinball (Original Realese)	Zen Studios	{PC,X360}	2014-10-15	\N
27	South Park: The Fractured but Whole	Ubisoft San Francisco	{PC,PS4,XOne}	2017-10-17	\N
28	South Park Pinball (Re-realese)	Zen Studios	{PC,PS4,XOne,PS5,XSeries,Switch}	2023-10-12	\N
29	South Park: The Fractured but Whole	Ubisoft San Francisco	{Switch}	2018-04-24	\N
30	Cartman's Escape Room (Virtual Game)	South Park Studios & Escape the Room	{Web}	2021-01-01	\N
31	Cartman's Escape Room (Chichago)	South Park Studios & Escape the Room	{"Escape Room"}	2019-05-15	\N
32	Cartman's Escape Room (San Diego Comic Con)	South Park Studios & Escape the Room	{"Escape Room"}	2018-07-20	\N
33	South Park: Snow Day!	Question LLC	{XSeries,PS5,PC,Switch}	2024-03-26	\N
\.


--
-- Data for Name: specials; Type: TABLE DATA; Schema: public; Owner: southpark
--

COPY public.specials (id, title, release_date, link, description) FROM stdin;
1	South Park: Post Covid	2021-11-25	https://www.paramountplus.com/movies/video/Ga_vaU8r4h3Ax7aJnrCWG9EV8h0uugvO/	In SOUTH PARK: POST COVID, we’ll find out the answer to the question: what happened to the children who lived through the pandemic? Stan, Kyle, Cartman and Kenny survived, but will never be the same post COVID.
2	South Park: Post Covid: The Return of Covid	2021-12-16	https://www.paramountplus.com/movies/video/Wnj6RyDK_sWCjm81KIBBZOk_PwsfWnii/	If Stan, Kyle and Cartman could just work together, they could go back in time to make sure Covid never happened and save Kenny's life. In SOUTH PARK: POST COVID: THE RETURN OF COVID, traveling back to the past seems to be the easy answer until they meet Victor Chaos.
3	South Park: The Streaming Wars	2022-06-01	https://www.paramountplus.com/movies/video/Rc4DHb2MiyJbgO2lJuibS9RigcEfyHc9/	In South Park: The Streaming Wars, Cartman locks horns with his mom in a battle of wills while an epic conflict unfolds that threatens South Park's very existence.
4	South Park: The Streaming Wars Part 2	2022-07-13	https://www.paramountplus.com/movies/video/QwiZqWlp0ZW9krpI4h8lyeAn_hLZhNBp/	In South Park: The Streaming Wars Part 2, a drought has brought the town of South Park to the brink of disaster.
5	South Park: Joining the Panderverse	2023-10-27	https://www.paramountplus.com/movies/video/ke8wS05iuRiq2rYCVU9vgag2de2Ay4_S/	In South Park: Joining the Panderverse, Cartman's deeply disturbing dreams portend the end of the life he knows and loves. The adults in South Park are also wrestling with their own life decisions as the advent of AI is turning their world upside down.
6	South Park (Not Suitable For Children)	2023-12-20	https://www.paramountplus.com/movies/video/0glSpjhJpLkp2ZiiJOkXO029GaSLgN_b/	After it's discovered that a teacher at South Park Elementary has an OnlyFans page, Randy is compelled to take a closer look at the seedy underbelly of the world of on-line influencers.
7	South Park: The End Of Obesity	2024-05-24	https://www.paramountplus.com/movies/video/Cd3Fse6Xve3v7e69nMKZmNchXwEHGvll/	The advent of new weight loss drugs has a huge impact on everyone in South Park. When Cartman is denied access to the life-changing medicine, the kids jump into action.
\.


--
-- Name: album_songs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: southpark
--

SELECT pg_catalog.setval('public.album_songs_id_seq', 84, true);


--
-- Name: albums_id_seq; Type: SEQUENCE SET; Schema: public; Owner: southpark
--

SELECT pg_catalog.setval('public.albums_id_seq', 6, true);


--
-- Name: characters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: southpark
--

SELECT pg_catalog.setval('public.characters_id_seq', 266, true);


--
-- Name: episodes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: southpark
--

SELECT pg_catalog.setval('public.episodes_id_seq', 13, true);


--
-- Name: family_id_seq; Type: SEQUENCE SET; Schema: public; Owner: southpark
--

SELECT pg_catalog.setval('public.family_id_seq', 49, true);


--
-- Name: games_id_seq; Type: SEQUENCE SET; Schema: public; Owner: southpark
--

SELECT pg_catalog.setval('public.games_id_seq', 50, true);


--
-- Name: albums albums_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_pkey PRIMARY KEY (id);


--
-- Name: alter_ego alter_ego_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.alter_ego
    ADD CONSTRAINT alter_ego_pkey PRIMARY KEY (id, original_character);


--
-- Name: characters characters_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_pkey PRIMARY KEY (id);


--
-- Name: chinpokomon chinpokomon_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.chinpokomon
    ADD CONSTRAINT chinpokomon_pkey PRIMARY KEY (id);


--
-- Name: episodes episodes_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.episodes
    ADD CONSTRAINT episodes_pkey PRIMARY KEY (id);


--
-- Name: families family_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.families
    ADD CONSTRAINT family_pkey PRIMARY KEY (id);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (id);


--
-- Name: album_songs id; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.album_songs
    ADD CONSTRAINT id PRIMARY KEY (id);


--
-- Name: specials specials_pkey; Type: CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.specials
    ADD CONSTRAINT specials_pkey PRIMARY KEY (id);


--
-- Name: characters episode_debut_fkey; Type: FK CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT episode_debut_fkey FOREIGN KEY (first_apperance) REFERENCES public.episodes(id) NOT VALID;


--
-- Name: characters family_fkey; Type: FK CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT family_fkey FOREIGN KEY (family) REFERENCES public.families(id) NOT VALID;


--
-- Name: album_songs fk_album; Type: FK CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.album_songs
    ADD CONSTRAINT fk_album FOREIGN KEY (album) REFERENCES public.albums(id) NOT VALID;


--
-- Name: alter_ego original_character_fkey; Type: FK CONSTRAINT; Schema: public; Owner: southpark
--

ALTER TABLE ONLY public.alter_ego
    ADD CONSTRAINT original_character_fkey FOREIGN KEY (original_character) REFERENCES public.characters(id);


--
-- PostgreSQL database dump complete
--

\unrestrict BaARXfcJBQUZEenuhCvvKECSW6Icg5YtVJjLADJfSOCHRVWWSln2Jgi0yQPc9Q2


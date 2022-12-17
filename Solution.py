from typing import List, Tuple, Any

from psycopg2 import sql

import Utility.DBConnector as Connector
import Utility.ReturnValue
from Business.Actor import Actor
from Business.Critic import Critic
from Business.Movie import Movie
from Business.Studio import Studio
from Utility.Exceptions import DatabaseException
from Utility.ReturnValue import ReturnValue


# ---------------------------------- CRUD API: ----------------------------------
def createCritics() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("CREATE TABLE Critics("
                     "id INTEGER PRIMARY KEY,"
                     "name TEXT NOT NULL)"
                     )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createMovies() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("CREATE TABLE Movies("
                     "movie_name TEXT,"
                     "year INTEGER CHECK(year >= 1895),"
                     "genre TEXT CHECK(genre IN ('Drama', 'Action', 'Comedy', 'Horror')) NOT NULL,"
                     "PRIMARY KEY (movie_name, year))"
                     )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createActors() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("CREATE TABLE Actors("
                     "id INTEGER PRIMARY KEY CHECK(id > 0),"
                     "name TEXT NOT NULL,"
                     "age INTEGER NOT NULL CHECK(age > 0),"
                     "height INTEGER NOT NULL CHECK(height > 0))"
                     )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createStudios() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("CREATE TABLE Studios("
                     "id INTEGER PRIMARY KEY,"
                     "name TEXT NOT NULL)"
                     )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createCriticsMovie() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            "CREATE TABLE CriticsMovie("
            "critic_id INTEGER ,"
            "movie_name TEXT NOT NULL,"
            "movie_year INTEGER,"
            "rating INTEGER NOT NULL CHECK(1 <= rating AND rating <= 5),"
            "UNIQUE (movie_name, movie_year, critic_id),"
            "FOREIGN KEY (critic_id) REFERENCES Critics(id) ON DELETE CASCADE,"
            "FOREIGN KEY (movie_name, movie_year) REFERENCES Movies(movie_name, year) ON DELETE CASCADE)"
        )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createStudiosMovie() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            "CREATE TABLE StudiosMovie("
            "studio_id INTEGER,"
            "movie_name TEXT NOT NULL,"
            "movie_year INTEGER,"
            "budget INTEGER NOT NULL CHECK(budget >= 0),"
            "revenue INTEGER NOT NULL CHECK(revenue >= 0),"
            "UNIQUE(movie_name, movie_year) ,"
            "FOREIGN KEY (studio_id) REFERENCES Studios(id) ON DELETE CASCADE,"
            "FOREIGN KEY (movie_name, movie_year) REFERENCES Movies(movie_name, year) ON DELETE CASCADE )"
        )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createActorsMovie() -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            "CREATE TABLE ActorsMovie("
            "actor_id INTEGER,"
            "movie_name TEXT NOT NULL,"
            "movie_year INTEGER,"
            "salary INTEGER NOT NULL CHECK(salary > 0),"
            "roles TEXT[],"
            "UNIQUE (actor_id, movie_name, movie_year),"
            "FOREIGN KEY (actor_id) REFERENCES Actors(id) ON DELETE CASCADE,"
            "FOREIGN KEY (movie_name, movie_year) REFERENCES Movies(movie_name, year) ON DELETE CASCADE)"
        )
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
        return ReturnValue.OK


def createTables():
    createCritics()
    createMovies()
    createActors()
    createStudios()
    createActorsMovie()
    createCriticsMovie()
    createStudiosMovie()


def clearCritics():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DELETE FROM Critics")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def clearActors():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DELETE FROM Actors")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def clearMovies():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DELETE FROM Movies")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def clearStudios():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DELETE FROM Studios")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def clearTables():
    clearCritics()
    clearMovies()
    clearActors()
    clearStudios()


def dropAvOnAv():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP VIEW IF EXISTS av_on_av")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()

def dropCritics():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS Critics CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropActors():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS Actors CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropMovies():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS Movies CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropStudios():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS Studios CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropCriticsMovie():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS CriticsMovie CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropActorsMovie():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS ActorsMovie CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropStudiosMovie():
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute("DROP TABLE IF EXISTS StudiosMovie CASCADE")
    except Exception as e:
        catchException(e, conn)
    if conn is not None:
        conn.close()


def dropTables():
    dropCritics()
    dropMovies()
    dropActors()
    dropStudios()
    dropStudiosMovie()
    dropActorsMovie()
    dropCriticsMovie()

def dropViews():
    dropAvOnAv()


def addCritic(critic: Critic) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL("INSERT INTO Critics(id, name) VALUES({id}, {username})").format(
                id=sql.Literal(critic.getCriticID()), username=sql.Literal(critic.getName())))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def addActor(actor: Actor) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL("INSERT INTO Actors(id, name, age, height) VALUES("
                    "{id}, {name}, {age}, {height})").format(
                id=sql.Literal(actor.getActorID()),
                name=sql.Literal(actor.getActorName()),
                age=sql.Literal(actor.getAge()),
                height=sql.Literal(actor.getHeight())))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def addStudio(studio: Studio) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL("INSERT INTO Studios(id, name) VALUES({id}, {name})").format(
                id=sql.Literal(studio.getStudioID()),
                name=sql.Literal(studio.getStudioName())))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def deleteCritic(critic_id: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(sql.SQL("DELETE FROM Critics WHERE id={c_id}".format(c_id=critic_id)))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def getCriticProfile(critic_id: int) -> Critic:
    conn = None
    try:
        conn = Connector.DBConnector()
        _, r = conn.execute(sql.SQL(f"SELECT name FROM Critics WHERE id={critic_id}"))
        return Critic(critic_id=critic_id, critic_name=r.rows[0][0])
    except Exception as e:
        catchException(e, conn)
        return Critic.badCritic()


def deleteActor(actor_id: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(sql.SQL(f"DELETE FROM Actors WHERE id={actor_id}"))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def getActorProfile(actor_id: int) -> Actor:
    conn = None
    try:
        conn = Connector.DBConnector()
        _, r = conn.execute(sql.SQL(f"SELECT name, age, height FROM Actors WHERE id={actor_id}"))
        name, age, height = r.rows[0]
        return Actor(actor_id, name, age, height)
    except Exception as e:
        catchException(e, conn)
        return Actor.badActor()


def addMovie(movie: Movie) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL("INSERT INTO Movies(movie_name, year, genre) VALUES({name}, {year}, {genre})").format(
                name=sql.Literal(movie.getMovieName()), year=sql.Literal(movie.getYear()),
                genre=sql.Literal(movie.getGenre())))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def catchException(e: Exception, conn: Any) -> ReturnValue:
    try:
        raise e
    except DatabaseException.ConnectionInvalid:
        return ReturnValue.ERROR
    except DatabaseException.NOT_NULL_VIOLATION:
        return ReturnValue.BAD_PARAMS
    except DatabaseException.CHECK_VIOLATION:
        return ReturnValue.BAD_PARAMS
    except DatabaseException.UNIQUE_VIOLATION:
        return ReturnValue.ALREADY_EXISTS
    except DatabaseException.FOREIGN_KEY_VIOLATION:
        return ReturnValue.NOT_EXISTS
    except Exception:
        return ReturnValue.ERROR
    finally:
        conn.close()


def deleteMovie(movieName: str, year: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(
            sql.SQL("DELETE FROM Movies WHERE movie_name={name} AND year={year}").format(name=sql.Literal(movieName),
                                                                                         year=sql.Literal(year)))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def getMovieProfile(movieName: str, year: int) -> Movie:
    conn = None
    try:
        conn = Connector.DBConnector()
        _, r = conn.execute(sql.SQL(
            "SELECT genre FROM Movies WHERE movie_name={name} AND year={year}").format(name=sql.Literal(movieName),
                                                                                       year=sql.Literal(year)))
        return Movie(movie_name=movieName, year=year, genre=r.rows[0][0])
    except Exception as e:
        catchException(e, conn)
        return Movie.badMovie()


def deleteStudio(studio_id: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(
            sql.SQL(f"DELETE FROM Studios WHERE id={studio_id}"))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def getStudioProfile(studio_id: int) -> Studio:
    conn = None
    try:
        conn = Connector.DBConnector()
        _, r = conn.execute(sql.SQL(f"SELECT name FROM Studios WHERE id={studio_id}"))
        return Studio(studio_id=studio_id, studio_name=r.rows[0][0])
    except Exception as e:
        catchException(e, conn)
        return Studio.badStudio()


def criticRatedMovie(movieName: str, movieYear: int, criticID: int, rating: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL(
                "INSERT INTO CriticsMovie(critic_id, movie_name, movie_year, rating) VALUES({c_id}, {m_n}, {m_y}, {rate})").format(
                c_id=sql.Literal(criticID), m_n=sql.Literal(movieName),
                m_y=sql.Literal(movieYear), rate=sql.Literal(rating)))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def criticDidntRateMovie(movieName: str, movieYear: int, criticID: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(
            sql.SQL("DELETE FROM CriticsMovie WHERE movie_name={name} AND movie_year={year} AND critic_id={id}").format(
                name=sql.Literal(movieName),
                year=sql.Literal(movieYear), id=sql.Literal(criticID)))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def actorPlayedInMovie(movieName: str, movieYear: int, actorID: int, salary: int, roles: List[str]) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL(
                "INSERT INTO ActorsMovie(actor_id, movie_name, movie_year, salary, roles) VALUES({a_id}, {m_n}, {m_y}, {salar}, {role})").format(
                a_id=sql.Literal(actorID), m_n=sql.Literal(movieName),
                m_y=sql.Literal(movieYear), salar=sql.Literal(salary), role=sql.Literal(roles)))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def actorDidntPlayInMovie(movieName: str, movieYear: int, actorID: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(
            sql.SQL("DELETE FROM ActorsMovie WHERE movie_name={name} AND movie_year={year} AND actor_id={id}").format(
                name=sql.Literal(movieName),
                year=sql.Literal(movieYear), id=sql.Literal(actorID)))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def studioProducedMovie(studioID: int, movieName: str, movieYear: int, budget: int, revenue: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        conn.execute(
            sql.SQL("INSERT INTO StudiosMovie(studio_id, movie_name, movie_year, budget, revenue) VALUES("
                    "{id}, {name}, {year}, {budget}, {revenue})").format(
                id=sql.Literal(studioID), name=sql.Literal(movieName), year=sql.Literal(movieYear),
                budget=sql.Literal(budget), revenue=sql.Literal(revenue)))
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def studioDidntProduceMovie(studioID: int, movieName: str, movieYear: int) -> ReturnValue:
    conn = None
    try:
        conn = Connector.DBConnector()
        rows, _ = conn.execute(
            sql.SQL("DELETE FROM StudiosMovie WHERE movie_name={name} AND movie_year={year} AND studio_id={id}").format(
                name=sql.Literal(movieName),
                year=sql.Literal(movieYear), id=sql.Literal(studioID)))
        if rows == 0:
            conn.close()
            conn = None
            return ReturnValue.NOT_EXISTS
    except Exception as e:
        res = catchException(e, conn)
        conn = None
        return res
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


# ---------------------------------- BASIC API: ----------------------------------
def averageRating(movieName: str, movieYear: int) -> float:
    conn = None
    try:
        conn = Connector.DBConnector()
        _, r = conn.execute(
            sql.SQL("SELECT AVG(rating) FROM criticsmovie WHERE movie_name='{m_name}' AND movie_year={m_year}" \
                    .format(m_name=movieName, m_year=movieYear)))

        return r[0]['avg'] if r[0]['avg'] else 0
    except Exception as e:
        catchException(e, conn)
        return 0.0


def createAvOnAvView(actorID: int):
    conn = None
    try:
        conn = Connector.DBConnector()
    # quer_on_view = "select avg(avg_actor) avg_actor, movie_name, movie_year from av_on_av GROUP BY movie_name, movie_year"
        view_quer = "CREATE VIEW av_on_av AS " \
                    "SELECT AVG(rating) avg_actor, criticsmovie.movie_year, criticsmovie.movie_name from actorsmovie INNER JOIN criticsmovie " \
                    "ON (actorsmovie.movie_year=criticsmovie.movie_year " \
                    "AND actorsmovie.movie_name=criticsmovie.movie_name) " \
                    "GROUP BY criticsmovie.movie_year, criticsmovie.movie_name, actor_id " \
                    "HAVING actor_id={a_id}" \
            .format(a_id=actorID)
        conn.execute(sql.SQL(view_quer))  # create the view
    # _, (aver) = conn.execute(sql.SQL(quer_on_view))  # execute on the view
    except Exception as e:
        catchException(e, conn)
        return 0.0



def averageActorRating(actorID: int) -> float:
    createAvOnAvView(actorID)
    conn = None
    try:
        conn = Connector.DBConnector()
        quer_on_view = "select avg(avg_actor) avg_actor from av_on_av"
        _, (aver) = conn.execute(sql.SQL(quer_on_view))# execute on the view
        return aver.rows[0][0] if aver.rows[0][0] is not None else 0
    except Exception as e:
        catchException(e, conn)
        return 0.0
    finally:
        dropAvOnAv()

def bestPerformance(actor_id: int) -> Movie:
    createAvOnAvView(actor_id)
    conn = None
    try:
        conn = Connector.DBConnector()
        quer_on_view = "select movie_name, movie_year from av_on_av"
        _, (aver) = conn.execute(sql.SQL(quer_on_view))  # execute on the view

        all_movies = sorted(aver.rows,key=lambda x: (x[0],x[1]))
        # print(getMovieProfile(all_movies[0], all_movies[1]))

        return Movie.badMovie() if not aver.rows else getMovieProfile(all_movies[0][0], all_movies[0][1])
    except Exception as e:
        catchException(e, conn)
        return 0.0
    finally:
        dropAvOnAv()


def stageCrewBudget(movieName: str, movieYear: int) -> int:
    # TODO: implement
    pass


def overlyInvestedInMovie(movie_name: str, movie_year: int, actor_id: int) -> bool:
    # TODO: implement
    pass


# ---------------------------------- ADVANCED API: ----------------------------------


def franchiseRevenue() -> List[Tuple[str, int]]:
    # TODO: implement
    pass


def studioRevenueByYear() -> List[Tuple[str, int]]:
    # TODO: implement
    pass


def getFanCritics() -> List[Tuple[int, int]]:
    # TODO: implement
    pass


def averageAgeByGenre() -> List[Tuple[str, float]]:
    # TODO: implement
    pass


def getExclusiveActors() -> List[Tuple[int, int]]:
    # TODO: implement
    pass


def getMovies(printSchema: bool = False) -> ReturnValue:
    conn = None
    Connector.ResultSet()
    try:
        conn = Connector.DBConnector()
        conn.execute("SELECT * FROM Movies", printSchema=printSchema)
    except Exception as e:
        return catchException(e, conn)
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def getActors(printSchema: bool = False) -> ReturnValue:
    conn = None
    Connector.ResultSet()
    try:
        conn = Connector.DBConnector()
        conn.execute("SELECT * FROM Actors", printSchema=printSchema)
    except Exception as e:
        return catchException(e, conn)
    if conn is not None:
        conn.close()
    return ReturnValue.OK


def getStudios(printSchema: bool = False) -> ReturnValue:
    conn = None
    Connector.ResultSet()
    try:
        conn = Connector.DBConnector()
        conn.execute("SELECT * FROM Studios", printSchema=printSchema)
    except Exception as e:
        return catchException(e, conn)
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


def getCritics(printSchema: bool = False) -> ReturnValue:
    conn = None
    Connector.ResultSet()
    try:
        conn = Connector.DBConnector()
        conn.execute("SELECT * FROM Critics", printSchema=printSchema)
    except Exception as e:
        return catchException(e, conn)
    finally:
        if conn is not None:
            conn.close()
            return ReturnValue.OK


# GOOD LUCK!
if __name__ == '__main__':
    dropTables()
    # dropViews()
    createTables()

    addCritic(Critic(1, "Moshe"))
    addCritic(Critic(2, "Yagel"))
    addCritic(Critic(3, "Avigail"))
    deleteCritic(1)
    addCritic(Critic(1, "new_Moshe"))

    addMovie(Movie("Best Movie", 2000, 'Action'))
    addMovie(Movie("Worst Movie", 1990, 'Horror'))
    addMovie(Movie("Ok Movie", 2005, 'Comedy'))

    addActor(Actor(1, "Hilbert", 4, 8))
    addActor(Actor(8, "So-Yang", 16, 5))
    addActor(Actor(45, "Luna", 70, 6))
    addActor(Actor(13, "Miley", 13, 9))
    addActor(Actor(2, "Gon", 34, 1))

    addStudio(Studio(1, "Yag"))
    addStudio(Studio(5, "Baloo"))
    addStudio(Studio(6, "Shick"))

    studioProducedMovie(5, "Best Movie", 2000, 100, 2000)
    studioDidntProduceMovie(5, "Best Movie", 2000)
    studioProducedMovie(1, "Best Movie", 2000, 100, 2000)
    studioProducedMovie(6, "Ok Movie", 2005, 500, 10)

    print('critics:')
    getCritics(printSchema=True)
    print('movies:')
    getMovies(printSchema=True)
    print('actors:')
    getActors(printSchema=True)
    print('studios:')
    getStudios(printSchema=True)
    criticRatedMovie("Best Movie", 2000, 1, 5)
    criticRatedMovie("Best Movie", 2000, 2, 8)
    criticRatedMovie("Ok Movie", 2005, 1, 5)
    criticRatedMovie("Worst Movie", 1990, 3, 5)
    criticRatedMovie("Worst Movie", 1990, 2, 10)
    print("***********************************************************************")
    print(str(getCriticProfile(2)))
    deleteCritic(2)
    # print(getCriticProfile(2))
    critic = getCriticProfile(1)
    print(critic.getName())
    av = averageRating("Best Movie", 2000)
    print(av)
    av2 = averageActorRating(8)
    print(av2)
    print("***********************************************************************")

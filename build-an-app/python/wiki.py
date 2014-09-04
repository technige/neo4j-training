#!/usr/bin/env python

from bottle import abort, get, run, template
from py2neo.neo4j import GraphDatabaseService, CypherQuery


# Set up a link to the local graph database.
graph = GraphDatabaseService()


@get('/')
def get_index():
    """ Show the index page.
    """
    return template("index")


@get('/movie/')
def get_movie_list():
    """ Fetch a list of all movies, ordered by title and render
    them within the 'movie_list' template.
    """
    results = CypherQuery(graph, "MATCH (m:Movie) "
                                 "RETURN m.title, m.released "
                                 "ORDER BY m.title").execute()
    return template("movie_list", movies=results)


@get('/movie/<title>')
def get_movie(title):
    """ Display details of a particular movie.
    """
    results = CypherQuery(graph, "MATCH (m:Movie) "
                                 "WHERE m.title = {title} "
                                 "RETURN m").execute(title=title)
    if results:
        movie = results[0][0]
        return template("movie", movie=movie.get_cached_properties())
    else:
        abort(404, "Movie not found")


if __name__ == "__main__":
    run(port=8080)


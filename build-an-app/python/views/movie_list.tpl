<!doctype html>
<html>

  <head>
    <title>Movie List</title>
  </head>

  <body>

    <h1>Movies</h1>

    <ul>
    %for title, released in movies:
      <li><a href="/movie/{{title}}">{{title}} ({{released}})</a></li>
    %end
    </ul>

  </body>

</html>


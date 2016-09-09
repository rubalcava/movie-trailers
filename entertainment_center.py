# The next two lines import other python files so we can
# use their functionality
import fresh_tomatoes
import media

# The next six statements are instantiations of the Movie class
toy_story = media.Movie(
    'Toy Story',
    'A story of a boy and his toys that come to life',
    'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',  # noqa
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',  # noqa
    'https://www.youtube.com/watch?v=aVdO-cx-McA')

lion_king = media.Movie(
    'The Lion King',
    'Embark on an extraordinary coming-of-age adventure'
    ' as Simba, a lion cub who cannot wait to be king',
    'https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg',  # noqa
    'https://www.youtube.com/watch?v=GaJWzJfoXlE')

aladdin = media.Movie(
    'Aladdin',
    'When street rat Aladdin frees a genie from a lamp,'
    ' he finds his wishes granted.',
    'https://upload.wikimedia.org/wikipedia/en/5/58/Aladdinposter.jpg',
    'https://www.youtube.com/watch?v=QapaqcDucmg')

beauty_beast = media.Movie(
    'Beauty and the Beast',
    "An arrogant young prince and his castle's servants"
    " fall under the spell of a wicked enchantress, who"
    "turns him into the hideous Beast until he learns to"
    "love and be loved in return.",
    'https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg',  # noqa
    'https://www.youtube.com/watch?v=tRlzmyveDHE')

little_mermaid = media.Movie(
    'The Little Mermaid',
    "A rebellious 16-year-old mermaid Ariel is"
    " fascinated with life on land",
    'https://upload.wikimedia.org/wikipedia/en/7/75/Movie_poster_the_little_mermaid.jpg',  # noqa
    'https://www.youtube.com/watch?v=ZGZX5-PAwR8')

# This puts the objects in a list
movies = [toy_story, avatar, lion_king, aladdin, beauty_beast, little_mermaid]

# This calls a function from the imported fresh_tomatoes file and
# passes movies as an argument.This is what will render the page.
fresh_tomatoes.open_movies_page(movies)

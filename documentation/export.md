# Code for current uml diagram on Mermaid Chart for later updating

classDiagram
    class Collection {
        +String name
        +String poster_path
        +String backdrop_path
    }

    class Genre {
        +String name
    }

    class ProductionCompany {
        +String name
    }

    class ProductionCountry {
        +String iso_3166_1
        +String name
    }

    class SpokenLanguage {
        +String iso_639_1
        +String name
    }

    class Movie {
        +String title
        +String original_title
        +String overview
        +Date release_date
        +Float runtime
        +BigInteger budget
        +BigInteger revenue
        +Float vote_average
        +Integer vote_count
        +Float popularity
        +String poster_path
        +String homepage
        +String status
        +String tagline
        +Boolean adult
        +Boolean video
        +String imdb_id
        +Integer tmdb_id
        +String original_language
    }

    class Keyword {
        +BigInteger id
        +String name
    }

    class Rating {
        +User user
        +Movie movie
        +Float rating
        +DateTime timestamp
    }

    class Person {
        +BigInteger id
        +String name
        +Integer gender
        +String profile_path
    }

    class Cast {
        +Movie movie
        +Person person
        +String character
        +Integer order
    }

    class Crew {
        +Movie movie
        +Person person
        +String job
        +String department
    }

    %% Correcting relationships to avoid syntax errors
    Movie --|> Collection : belongs_to_collection
    Movie --|> Genre : genres
    Movie --|> ProductionCompany : production_companies
    Movie --|> ProductionCountry : production_countries
    Movie --|> SpokenLanguage : spoken_languages
    Movie --|> Keyword : keywords
    Movie --|> Rating : ratings
    Rating --|> User : user
    Rating --|> Movie : movie
    Movie --|> Cast : cast
    Cast --|> Person : person
    Movie --|> Crew : crew
    Crew --|> Person : person

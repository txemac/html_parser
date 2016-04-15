# HTML Parser

There are four files included - two fixtures containing html snippets to be parsed,
one test file and the parser file:

    fixtures/fixture1.html
    fixtures/fixture2.html
    src/parser.py
    tests/test.py


The HTML_parser is a method takes a string containing html content as a parameter, and returns `address`, `suite`, `postcode`, `description` and `images`.

# Run
To run unit test suite, install 'nose', eg. using 'pip': 

    pip install -r ./requirements.txt
    
Run tests:

    nosetests -v

# Author
Jose Bermudez

[www.josebermudez.co.uk](http://www.josebermudez.co.uk)

[info@josebermudez.co.uk](mailto: info@josebermudez.co.uk)

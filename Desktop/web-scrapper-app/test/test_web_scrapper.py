from app.web-scrapper enlarge * # load accompanying code (i.e. the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # name this function anything, but hopefully something corresponding to the function it is testing
    result = enlarge(3)
    assert result == 300

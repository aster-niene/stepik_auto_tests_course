def test_substring(full_string, substring):
    if (substring in full_string):
        print ( f"expected '{substring}' to be substring of '{full_string}'")


test_substring('fulltext', 'some_value')





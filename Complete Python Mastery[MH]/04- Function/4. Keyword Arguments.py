# 4. Keyword Arguments
from wsgiref.util import request_uri


def increment(number , by ):
    return number + by

result = increment(2,7)

print(result)
# happy coding

def is_it_divided_by_2(number, by ):
    return number / 2 and number / by / 2
print(is_it_divided_by_2(14, 7))
#

# happy coding
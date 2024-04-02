#!/usr/bin/env python3
"""index_range that takes two integer arguments 'page' and 
'page_size'.

Function returns a tuple of size two containing a start and
an end indices corresponding to the range of indexes to
return in a list for those particular pagination parameters.

Page numbers are 1-idexed.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    start index and an end index corresponding to the range of
    """
    # start at 0 and end at page_size if page is 1
    # start at ((page-1) * page_size) and end at
    # (page_size * page) if page is 2.
    # start at ((page-1) * page_size) and end at 
    # (page_size * page) if page is 3
    return ((page-1) * page_size, page_size * page)

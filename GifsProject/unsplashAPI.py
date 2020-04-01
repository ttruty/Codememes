import logging
from pyunsplash import PyUnsplash
api_key = 'XXe2XzeIzsPKmTuh-nltG1dMyI7RjDkUeBkHSMG9X5k'

# instantiate PyUnsplash object
py_un = PyUnsplash(api_key=api_key)

# pyunsplash logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger("pyunsplash").setLevel(logging.DEBUG)

# Start with the generic collection, maximize number of items
# note: this will run until all photos of all collections have
#       been visited, unless a connection error occurs.
#       Typically the API hourly limit gets hit during this
#
collections = py_un.collections(per_page=20)
while collections.has_next:
    for collection in collections.entries:
        photos = collection.photos()
        for photo in photos.entries:
            print(photo.link_download)

    # no need to specify per_page: will take from original object
    collections = collections.get_next_page()
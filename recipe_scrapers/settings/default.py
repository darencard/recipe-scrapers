from recipe_scrapers.plugins import (  # SchemaOrgPrioriotyPlugin,; Bcp47ValidatePlugin,
    ExceptionHandlingPlugin,
    HTMLTagStripperPlugin,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFillPlugin,
)

# Plugins to be attached.
# The upper most plugin is the "outer most" executed.
# Check recipe_scrapers.settings.template.py for ways to extend.
PLUGINS = (
    ExceptionHandlingPlugin,
    HTMLTagStripperPlugin,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFillPlugin,
    # Bcp47ValidatePlugin,
    # SchemaOrgPrioriotyPlugin,
)

META_HTTP_EQUIV = False


EXCEPTION_HANDLING = False
# Applicable only if EXCEPTION_HANDLING is True, otherwise ignored
# silence <anyScraper>.[method]() exception and return the value
# as listed in the config here.
ON_EXCEPTION_RETURN_VALUES = {
    "title": None,
    "total_time": None,
    "yields": None,
    "image": None,
    "ingredients": None,
    "instructions": None,
    "ratings": None,
    "reviews": None,
    "links": None,
    "language": None,
    "nutrients": None,
}
# LEGACY VALUES: (before v13) it used to be like this:
# ON_EXCEPTION_RETURN_VALUES = {
#     "title": "",
#     "total_time": 0,
#     "yields": "",
#     "image": "",
#     "ingredients": [],
#     "instructions": "",
#     "ratings": -1,
#     "reviews": None,
#     "links": [],
#     "language": "en",
#     "nutrients": {},
# }

TEST_MODE = False


# logging.DEBUG     # 10
# logging.INFO      # 20
# logging.WARNING   # 30
# logging.ERROR     # 40
# logging.CRITICAL  # 50
# https://docs.python.org/3/howto/logging.html
LOG_LEVEL = 30

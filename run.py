from app import app
from config import HOST, PORT, DEBUG

__author__ = "Zuri Pabon"
__credits__ = ["Zuri Pabon"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Zuri Pabon"
__email__ = "zpabon@itrsgroup.com"
__status__ = "beta"

# @TODO Read host and port from cli
app.run(host=HOST, port=PORT, debug=DEBUG)

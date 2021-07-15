import bjoern
import threading
from urllib.parse import urlparse
from typing import Callable


HOST = "http://127.0.0.1:9999"


class ServerThread(threading.Thread):
    """Run WSGI server on a background thread.
    """

    def __init__(self, host: str = HOST):
        threading.Thread.__init__(self)
        self.host = host
        self.daemon = True
        self.app = None

    def start(self, app):
        self.app = app
        super().start()

    def run(self):
        """WSGI server."""
        parts = urlparse(self.hostbase)
        host, port = parts.netloc.split(":")

        try:
            bjoern.run(self.app, host, int(port))
        except Exception as e:
            import traceback
            traceback.print_exc()

    def stop(self):
        self.app = None

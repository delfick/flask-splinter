from werkzeug.serving import make_server
import flask

class App(object):
    def __init__(self, port=3000, host='localhost'):
        self.port = port
        self.host = host
        self.app = self.setup_app()

    def setup_app(self):
        app = flask.Flask(__name__)
        app.route('/')(self.root)
        app.route('/lol')(self.lol)
        app.route('/some_javascript')(self.some_javascript)
        return app

    def lol(self):
        return "lol{}".format(flask.request.args.get("num"))

    def root(self):
        return 'root'

    def some_javascript(self):
        return """
        <html>
            <head>
                <script type="text/javascript">
                    function clicked() {
                        var thing = document.createElement("p")
                          , text = document.createTextNode("clicked")
                          ;
                        thing.appendChild(text);
                        document.body.appendChild(div);
                    }
                </script>
            </head>
            <body>
                <button id="clicker" onclick="clicked()">Click ME!</button>
            </body>
        </html>
        """

    def start(self):
        self.server = make_server(self.host, self.port, self.app)
        self.server.serve_forever()

    def stop(self):
        if hasattr(self, 'server'):
            self.server.shutdown()

import web
import json

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        dzejson = open('data.json')
        return dzejson.read()
        # return "Hello world"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
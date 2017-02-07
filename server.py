import web
import json

urls = (
    '/', 'index',
    '/2', 'index2'
)

class index:
    def GET(self):
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        dzejson = open('data.json')
        return dzejson.read()
        # return "Hello world"
class index2:
    def GET(self):
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        dzejson = open('data1.json')
        return dzejson.read()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
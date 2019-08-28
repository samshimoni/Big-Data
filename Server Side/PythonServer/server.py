from http.server import HTTPServer, BaseHTTPRequestHandler
from hdfsPySpark import collectDataFromHDFS

COMMANDS_PORT = 4012

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.address_string())
        self.send_response(200)
        self.end_headers()
        collectDataFromHDFS()
        #str1 = ''.join(map(str, ls))
        #self.wfile.write(str.encode(str1))
        self.wfile.write(b'File Uploaded')
        #self.wfile.write(str.encode(text_to_return))

    # def do_POST(self):
    #     content_length = int(self.headers['Content-Length'])
    #     body = self.rfile.read(content_length)
    #     self.send_response(200)
    #     self.end_headers()
    #     response = BytesIO()
    #     response.write(b'This is POST request. ')
    #     response.write(b'Received: ')
    #     # main_function(self.path)
    #     json_query_results = query_function(body)
    #     response.write(json_query_results)
    #     response.write(body)mapa= sorted_list_df.toJSON().map(lambda j: json.loads(j)).collect()
    #     self.wfile.write(response.getvalue())
    #     union(list[0][['item_name', 'date', 'price_for_UNIT/KG']])

print('Listening on port', COMMANDS_PORT)

httpd = HTTPServer(('localhost', COMMANDS_PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
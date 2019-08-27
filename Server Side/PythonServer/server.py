from http.server import HTTPServer, BaseHTTPRequestHandler
from hdfsPySpark import collectDataFromHDFS


COMMANDS_PORT = 4012

...
...

'''
def upload_file(path):
    if not path == '/':  # if url is like '/query?filename='
        filename = path.replace('/query?filename=', "", 1)
        print(filename)
        # wait for file to be uploaded
        time.sleep(1)

        # Check whether or not the file has been already uploaded
        if filename not in hdfs_files:
'''






class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        print(self.address_string())
        self.send_response(200)
        self.end_headers()
        #text_to_return = helloWorld()
        collectDataFromHDFS()

        #str1 = ''.join(map(str, ls))
        #self.wfile.write(str.encode(str1))

        #text_to_return = upload_file(self.path)
        # my_path =  self.path
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
    #     response.write(body)
    #     self.wfile.write(response.getvalue())        union(list[0][['item_name', 'date', 'price_for_UNIT/KG']])

print('Listening on port', COMMANDS_PORT)

httpd = HTTPServer(('localhost', COMMANDS_PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
'''
Created on Mar 12, 2014

@author: Onur
'''

import os
import random
import cgi
from base64 import decodestring
from SimpleHTTPServer import SimpleHTTPRequestHandler

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    '''
    classdocs
    '''
    
    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.

        """
        path = self.translate_path(self.path)
        
        newFile = path.split('/')        
        if newFile[-1] == "getid" and newFile[-2] == "com":
            #write to getid
            newId = random.randint(10000,99999)
            f = open(path, "w")
            f.write('{}'.format(newId))
            f.close
            
            #create the new file            
            newFile[-1] = '{}'.format(newId)
            newFile = '/'.join(newFile)
            f = open(newFile, "w")
            f.write("1\ninit")
            f.close() 
            
        else:
            f = None
            if os.path.isdir(path):
                if not self.path.endswith('/'):                
                    # redirect browser - doing basically what apache does
                    self.send_response(301)
                    self.send_header("Location", self.path + "/")
                    self.end_headers()
                    return None
                for index in "index.html", "index.htm":
                    index = os.path.join(path, index)
                    if os.path.exists(index):
                        path = index
                        break
                else:
                    return self.list_directory(path)
        ctype = self.guess_type(path)
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content
            # transmitted *less* than the content-length!
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f
    

    def do_POST(self):
        # Use cgi module to retrieve data from POST as a form
        form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                         })
        # We can get value from the form key like we did in dictionary class
        encode = form['result'].value
        # Decide the value from base64 string
        decode = decodestring(encode)
        self.wfile.write('Ok')
        print
        print decode
        
    def log_message(self, format, *args):
        return


        
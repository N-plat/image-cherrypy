import cherrypy

from root import Root


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 443}) #port 443 for https or port 80 for http
#    cherrypy.config.update({'server.socket_port': 80})
    cherrypy.config.update({'server.socket_host': 'ec2-52-40-206-104.us-west-2.compute.amazonaws.com'})

    #cherrypy.tree.mount(Root())
    cherrypy.tree.mount(Root(),'/',

{ 

    '/robots.txt': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/robots.txt'  },
    '/image1.jpeg': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/1584054812933.JPEG'  }
    
}

 )

    cherrypy.server.ssl_module = 'builtin'
    cherrypy.server.ssl_certificate = "/etc/letsencrypt/live/image.n-plat.com/fullchain.pem"
    cherrypy.server.ssl_private_key = "/etc/letsencrypt/live/image.n-plat.com/privkey.pem"
    cherrypy.server.ssl_certificate_chain = "/etc/letsencrypt/live/image.n-plat.com/fullchain.pem"
    cherrypy.server.thread_pool = 50


    cherrypy.engine.start()
    cherrypy.engine.block()


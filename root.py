import MySQLdb
import cherrypy

from cherrypy.lib import static

class Root(object):

    _cp_config = {
        'tools.sessions.on': True,
        'tools.sessions.locking': 'explicit' #this and the acquire_lock and the release_lock statements in the login and logout functions are necessary so that multiple ajax requests can be processed in parallel in a single session
    }

    @cherrypy.expose
    def index(self,filename):
        return static.serve_file("/efs/ec2-user/images/"+filename)

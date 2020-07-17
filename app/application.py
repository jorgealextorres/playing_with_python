import app.config.config as config
import app.config.connection_pool as connectionPool

class App():
  configuration = None
  connectionPool = None

  @staticmethod
  def init():
    App.configuration = config.getConfig()
    App.connectionPool = connectionPool.ConnectionPool.init(host = App.configuration.get('DATABASE', 'HOST'), 
                                                            port = App.configuration.get('DATABASE', 'PORT'), 
                                                            databaseName = App.configuration.get('DATABASE', 'DB_NAME'), 
                                                            user = App.configuration.get('DATABASE', 'USERNAME'), 
                                                            password = App.configuration.get('DATABASE', 'PASSWORD'))
    print("Application initialized successfully.")

  @staticmethod
  def finish():
    App.configuration = None
    connectionPool.ConnectionPool.finish()
    App.connectionPool = None
    
    print("Application finalized successfully.")

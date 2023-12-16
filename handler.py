from serverless_wsgi import handle_request
from API.time_api import app  # Importa el objeto Flask

# Lambda de verificación del usuario 
def lambda_handler(event, context):
    return handle_request(app, event, context)
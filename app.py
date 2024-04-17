from vetiver import VetiverModel, VetiverAPI
from dotenv import load_dotenv, find_dotenv
import vetiver
import pins

load_dotenv(find_dotenv())

b = pins.board_folder('data/model', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240415T174558Z-a6f9b')

#vetiver_api = vetiver.VetiverAPI(v)
#api = vetiver_api.app

app = VetiverAPI(v, check_prototype = True)
app.run(port = 8080)


# ======================= Imports ============================
from flask import *

# ======================= Setup ============================
app = Flask(__name__)


# ======================= Flask ============================
@app.route("/")
def index():
    # do stuff here, ie:
    # dis = distance.sensor.readout
    # atm = atmosphere.sensor.readout
    # etc

    # index.html has to be in "templates" folder
    # update based on "Water level detection with flask webpage" video on youtube
    # eg, dis will be the tag of h1
    return render_template('index.html', dis=dis)


@app.route("/temperature")
def temperature():
    
    return render_template('temperature.html', atm=atm)
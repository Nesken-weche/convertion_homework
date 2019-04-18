from flask import Flask

app = Flask(__name__)

@app.route('/')
def initial_page():
    return 'convert foot to meter'

@app.route('/ft/<int:ft>')
def ft_to_meter(ft):
    meter = ft * 0.3048
    return f"{ft} feet equal to {meter} meters."

@app.route('/meter/<int:meter>')
def meter_to_ft(meter):
    ft = meter/ 0.3048
    return f"{meter} meters equals to {ft} feets."


if __name__=="__main__":
    app.run()
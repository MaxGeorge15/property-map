from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Route for the home page (index)
@app.route('/')
def home():
    # You can add any logic here to pass data to the template (e.g., categories for pins)
    categories = [
        {'category': 'Properties', 'latitude': 37.7749, 'longitude': -122.4194},  # Example: San Francisco
        {'category': 'Commercial', 'latitude': 34.0522, 'longitude': -118.2437},  # Example: Los Angeles
        {'category': 'Residential', 'latitude': 40.7128, 'longitude': -74.0060},  # Example: New York
        {'category': 'Hotels and Resorts', 'latitude': 25.7617, 'longitude': -80.1918},  # Example: Miami
        {'category': 'Upcoming projects', 'latitude': 41.8781, 'longitude': -87.6298},  # Example: Chicago
        {'category': 'Completed', 'latitude': 51.5074, 'longitude': -0.1278}  # Example: London
    ]
    return render_template('index.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)

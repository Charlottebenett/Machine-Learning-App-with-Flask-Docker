from flask import Flask , jsonify, request
from utilities import predict_pipline

app = Flask(__name__)


@app.post('/predict')
def predict():
    data = request.get_json()
    try:    
        sample = data['text']
    except KeyError:
       return jsonify({'error':'No text sent'})
    
    sample = [sample]
    predicitions = predict_pipline(sample)
    try:    
        result =jsonify(predicitions[0])
    except TypeError as e:
       result = jsonify({'error': str(e) })
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
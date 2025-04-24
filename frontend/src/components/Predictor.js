import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Predictor = () => {
    const [input, setInput] = useState('');
    const [result, setResult] = useState('');
    const [apiStatus, setApiStatus] = useState('⏳ Checking backend...');

    // ✅ Check if backend is reachable
    useEffect(() => {
        axios.get('http://localhost:5000/')
            .then((res) => {
                setApiStatus(`✅ ${res.data.message}`);
            })
            .catch((err) => {
                console.error(err);
                setApiStatus('❌ Backend not reachable');
            });
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setResult('⏳ Predicting...');
        try {
            const res = await axios.post('http://localhost:5000/predict', { symptoms: input });
            setResult(res.data.prediction);
        } catch (err) {
            console.error(err);
            setResult('❌ Error predicting disease');
        }
    };

    return (
        <div>
            <h2>Disease Predictor</h2>
            <p style={{ fontWeight: 'bold', color: apiStatus.includes('❌') ? 'red' : 'green' }}>{apiStatus}</p>
            <form onSubmit={handleSubmit}>
                <textarea
                    rows="4"
                    cols="50"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Enter symptoms like headache fever body_pain"
                />
                <br />
                <button type="submit">Predict</button>
            </form>
            {result && <h3>Prediction: {result}</h3>}
        </div>
    );
};

export default Predictor;

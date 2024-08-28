import React, { useState } from 'react';
import axios from 'axios';
import '../index.css';

const TextInputForm = () => {
    const [text, setText] = useState('');
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        try {
            const response = await axios.post('http://localhost:8000/predict', { text });
            setResult(response.data);
        } catch (error) {
            setError('An error occurred while making the prediction. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container">
            <h1>Mental Health Classifier</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    rows="4"
                    cols="50"
                    placeholder="Enter text to classify..."
                />
                <button type="submit">Classify Text</button>
            </form>
            {loading && <p className="loading">Loading...</p>}
            {error && <p className="error">{error}</p>}
            {result && (
                <div className="result">
                    <h3>Prediction Results:</h3>
                    <p><strong>Predicted Class:</strong> {result.predicted_class}</p>
                    <p><strong>Confidence:</strong> {result.confidence.toFixed(2)}</p>
                    <h4>Confidence Scores:</h4>
                    <ul>
                        {Object.keys(result.confidence_scores).map((label, index) => (
                            <li key={index}>
                                {label}: {result.confidence_scores[label].toFixed(2)}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default TextInputForm;

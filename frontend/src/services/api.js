import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const predictDisease = async (symptoms) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/predict`, { symptoms });
        return response.data.prediction;
    } catch (error) {
        console.error('Prediction error:', error);
        throw error;
    }
};

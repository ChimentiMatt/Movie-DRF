import axios from "axios";

const API_BASE_URL = import.meta.env.VUE_APP_API_BASE_URL || "http://localhost:8000"; // Default to local if not set

export const personService = {

  async getPerson(personName) {
    try {
      const response = await axios.get(`${API_BASE_URL}/person/${personName}/`);  // Adjust URL to match Django's route
      return response.data;  // Return actor data
    } catch (error) {
      console.error(`Error fetching actor ID ${personId}:`, error);
      throw error;
    }
  },

  async getPersonsMovies(personName) {
    console.log(personName)
    try {
      const response = await axios.get(`${API_BASE_URL}/persons-movies/${personName}/`);  // Adjust URL to match Django's route
      console.log('in', response)
      return response.data;  // Return actor data
    } catch (error) {
      console.error(`Error fetching actor ${personName}:`, error);
      throw error;
    }
  },

};

export default personService;
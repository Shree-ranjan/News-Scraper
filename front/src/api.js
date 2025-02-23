import axios from "axios";
import { baseUri } from "./components/Config";


export const fetchNewsArticles = async () => {
  try {
    const response = await axios.get(`${baseUri}/api/news`);
    return response.data;
  } catch (error) {
    console.error("Error fetching news articles:", error);
    return [];
  }
};
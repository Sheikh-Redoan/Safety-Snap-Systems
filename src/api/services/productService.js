import axiosInstance from '../config';
import { API_ENDPOINTS } from '../endpoints';

export const productService = {
  getAllProducts: async (params = {}) => {
    try {
      const response = await axiosInstance.get(API_ENDPOINTS.PRODUCTS, {
        params,
      });
      return response.data;
    } catch (error) {
      throw error.response?.data?.message || error.message;
    }
  },

  getProductById: async (id) => {
    try {
      const response = await axiosInstance.get(
        `${API_ENDPOINTS.PRODUCTS}/${id}`
      );
      return response.data;
    } catch (error) {
      throw error.response?.data?.message || error.message;
    }
  },

  searchProducts: async (query) => {
    try {
      const response = await axiosInstance.get(API_ENDPOINTS.SEARCH, {
        params: { q: query },
      });
      return response.data;
    } catch (error) {
      throw error.response?.data?.message || error.message;
    }
  },

  getProductsByCategory: async (categoryId, params = {}) => {
    try {
      const response = await axiosInstance.get(
        `${API_ENDPOINTS.CATEGORIES}/${categoryId}/products`,
        { params }
      );
      return response.data;
    } catch (error) {
      throw error.response?.data?.message || error.message;
    }
  },

  filterProducts: async (filters) => {
    try {
      const response = await axiosInstance.post(
        API_ENDPOINTS.FILTER,
        filters
      );
      return response.data;
    } catch (error) {
      throw error.response?.data?.message || error.message;
    }
  },
};
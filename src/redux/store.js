import { configureStore } from '@reduxjs/toolkit';
import productSlice from './slices/productSlice';
import categorySlice from './slices/categorySlice';
import filterSlice from './slices/filterSlice';
import enquirySlice from './slices/enquirySlice';
import uiSlice from './slices/uiSlice';
import seoSlice from './slices/seoSlice';

export const store = configureStore({
  reducer: {
    products: productSlice,
    categories: categorySlice,
    filters: filterSlice,
    enquiry: enquirySlice,
    ui: uiSlice,
    seo: seoSlice,
  },
});

export default store;

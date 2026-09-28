import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchProducts, fetchProductById } from '../redux/slices/productSlice';

export const useProducts = (id = null, params = {}) => {
  const dispatch = useDispatch();
  const { products, selectedProduct, loading, error, pagination } = useSelector(
    (state) => state.products
  );

  useEffect(() => {
    if (id) {
      dispatch(fetchProductById(id));
    } else {
      dispatch(fetchProducts(params));
    }
  }, [dispatch, id, params]);

  return {
    products,
    selectedProduct,
    loading,
    error,
    pagination,
  };
};

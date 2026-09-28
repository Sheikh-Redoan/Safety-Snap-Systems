import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  search: '',
  category: null,
  sortBy: 'newest',
  priceRange: [0, 10000],
  tags: [],
};

const filterSlice = createSlice({
  name: 'filters',
  initialState,
  reducers: {
    setSearch: (state, action) => {
      state.search = action.payload;
    },
    setCategory: (state, action) => {
      state.category = action.payload;
    },
    setSortBy: (state, action) => {
      state.sortBy = action.payload;
    },
    setPriceRange: (state, action) => {
      state.priceRange = action.payload;
    },
    setTags: (state, action) => {
      state.tags = action.payload;
    },
    resetFilters: (state) => {
      return initialState;
    },
  },
});

export const {
  setSearch,
  setCategory,
  setSortBy,
  setPriceRange,
  setTags,
  resetFilters,
} = filterSlice.actions;

export default filterSlice.reducer;

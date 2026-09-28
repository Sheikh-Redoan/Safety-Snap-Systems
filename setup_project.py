import os

project_dir = r"c:\Users\ssrab\Desktop\Projects\Safety Snap Systems"

directories = [
    "public",
    "src/api/services",
    "src/redux/slices",
    "src/redux/thunks",
    "src/components/Layout",
    "src/components/Common",
    "src/components/Hero",
    "src/components/Products",
    "src/components/Category",
    "src/components/Forms",
    "src/components/Sections",
    "src/components/Video",
    "src/components/Animation",
    "src/pages/home/sections",
    "src/pages/products/sections",
    "src/pages/categories/sections",
    "src/pages/contact/sections",
    "src/pages/about/sections",
    "src/pages/error",
    "src/hooks",
    "src/utils",
    "src/styles",
    "src/config",
    "src/assets/images/hero",
    "src/assets/images/products",
    "src/assets/images/categories",
    "src/assets/images/other",
    "src/assets/icons/svg",
    "src/assets/icons/sprites",
    "src/assets/fonts/font-files",
    "src/assets/videos/background-videos",
    "src/data",
    "src/context",
    "src/middleware",
    "src/SEO",
]

for d in directories:
    os.makedirs(os.path.join(project_dir, d), exist_ok=True)

files = {
    "src/redux/store.js": """import { configureStore } from '@reduxjs/toolkit';
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
""",
    "src/redux/slices/productSlice.js": """import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { productService } from '../../api/services/productService';

export const fetchProducts = createAsyncThunk(
  'products/fetchProducts',
  async (params, { rejectWithValue }) => {
    try {
      const response = await productService.getAllProducts(params);
      return response;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const fetchProductById = createAsyncThunk(
  'products/fetchProductById',
  async (id, { rejectWithValue }) => {
    try {
      const response = await productService.getProductById(id);
      return response;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const initialState = {
  products: [],
  selectedProduct: null,
  loading: false,
  error: null,
  pagination: {
    page: 1,
    limit: 12,
    total: 0,
  },
};

const productSlice = createSlice({
  name: 'products',
  initialState,
  reducers: {
    resetProducts: (state) => {
      state.products = [];
    },
    setPagination: (state, action) => {
      state.pagination = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchProducts.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchProducts.fulfilled, (state, action) => {
        state.loading = false;
        state.products = action.payload?.data || [];
        state.pagination = action.payload?.pagination || state.pagination;
      })
      .addCase(fetchProducts.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(fetchProductById.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchProductById.fulfilled, (state, action) => {
        state.loading = false;
        state.selectedProduct = action.payload;
      })
      .addCase(fetchProductById.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const { resetProducts, setPagination } = productSlice.actions;
export default productSlice.reducer;
""",
    "src/redux/slices/filterSlice.js": """import { createSlice } from '@reduxjs/toolkit';

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
""",
    "src/redux/slices/categorySlice.js": """import { createSlice } from '@reduxjs/toolkit';
export default createSlice({ name: 'category', initialState: {}, reducers: {} }).reducer;""",
    "src/redux/slices/enquirySlice.js": """import { createSlice } from '@reduxjs/toolkit';
export default createSlice({ name: 'enquiry', initialState: {}, reducers: {} }).reducer;""",
    "src/redux/slices/uiSlice.js": """import { createSlice } from '@reduxjs/toolkit';
export default createSlice({ name: 'ui', initialState: {}, reducers: {} }).reducer;""",
    "src/redux/slices/seoSlice.js": """import { createSlice } from '@reduxjs/toolkit';
export default createSlice({ name: 'seo', initialState: {}, reducers: {} }).reducer;""",

    "src/api/endpoints.js": """export const API_ENDPOINTS = {
  PRODUCTS: '/products',
  CATEGORIES: '/categories',
  SEARCH: '/search',
  FILTER: '/products/filter'
};""",
    "src/api/config.js": """import axios from 'axios';
const axiosInstance = axios.create({ baseURL: process.env.REACT_APP_API_BASE_URL || '/api' });
export default axiosInstance;""",
    "src/api/services/productService.js": """import axiosInstance from '../config';
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
""",
    "src/api/services/contactService.js": """export const contactService = {
  sendEnquiry: async (data) => {
    return new Promise((resolve) => setTimeout(() => resolve({ success: true }), 1000));
  }
};""",
    
    "src/hooks/useProducts.js": """import { useEffect } from 'react';
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
""",
    "src/hooks/useDebounce.js": """import { useState, useEffect } from 'react';
export function useDebounce(value, delay) {
  const [debouncedValue, setDebouncedValue] = useState(value);
  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    return () => clearTimeout(handler);
  }, [value, delay]);
  return debouncedValue;
}""",
    "src/hooks/useSearch.js": """import { useState, useCallback } from 'react';
import { useDebounce } from './useDebounce';
import { productService } from '../api/services/productService';

export const useSearch = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const debouncedQuery = useDebounce(searchQuery, 300);

  const handleSearch = useCallback(async (query) => {
    if (!query.trim()) {
      setSearchResults([]);
      return;
    }

    setIsSearching(true);
    try {
      const results = await productService.searchProducts(query);
      setSearchResults(results);
    } catch (error) {
      console.error('Search error:', error);
    } finally {
      setIsSearching(false);
    }
  }, []);

  return {
    searchQuery,
    setSearchQuery,
    searchResults,
    isSearching,
    handleSearch,
  };
};""",

    "src/utils/animations.js": """import { useInView } from 'react-intersection-observer';
import { useAnimation } from 'framer-motion';
import { useEffect } from 'react';

// Framer Motion Variants
export const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.6, ease: 'easeOut' },
  },
};

export const fadeInLeft = {
  hidden: { opacity: 0, x: -30 },
  visible: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.6, ease: 'easeOut' },
  },
};

export const fadeInRight = {
  hidden: { opacity: 0, x: 30 },
  visible: {
    opacity: 1,
    x: 0,
    transition: { duration: 0.6, ease: 'easeOut' },
  },
};

export const scaleIn = {
  hidden: { opacity: 0, scale: 0.8 },
  visible: {
    opacity: 1,
    scale: 1,
    transition: { duration: 0.5, ease: 'easeOut' },
  },
};

export const slideInDown = {
  hidden: { opacity: 0, y: -40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: 'easeOut' },
  },
};

// Stagger Container
export const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.2,
    },
  },
};

// Scroll Animation Hook
export const useScrollAnimation = () => {
  const { ref, inView } = useInView({
    threshold: 0.1,
    triggerOnce: true,
  });
  const controls = useAnimation();

  useEffect(() => {
    if (inView) {
      controls.start('visible');
    }
  }, [inView, controls]);

  return { ref, controls, inView };
};
""",

    "src/SEO/SEOHelmet.jsx": """import { Helmet } from 'react-helmet-async';

const SEOHelmet = ({
  title = 'Safety Snap Systems',
  description = 'Professional safety barrier systems, reels, signage and stanchions',
  keywords = 'safety systems, barrier systems, safety signage',
  image = '/images/og-image.jpg',
  url = window?.location?.href || '',
  author = 'Safety Snap Systems',
  type = 'website',
}) => {
  return (
    <Helmet>
      <title>{title} | Safety Snap Systems</title>
      <meta name="description" content={description} />
      <meta name="keywords" content={keywords} />
      <meta name="author" content={author} />
      
      {/* Open Graph */}
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:image" content={image} />
      <meta property="og:url" content={url} />
      <meta property="og:type" content={type} />
      <meta property="og:site_name" content="Safety Snap Systems" />
      
      {/* Twitter Card */}
      <meta name="twitter:card" content="summary_large_image" />
      <meta name="twitter:title" content={title} />
      <meta name="twitter:description" content={description} />
      <meta name="twitter:image" content={image} />
      
      {/* Canonical */}
      <link rel="canonical" href={url} />
      
      {/* Robots */}
      <meta name="robots" content="index, follow" />
      <meta name="googlebot" content="index, follow" />
    </Helmet>
  );
};

export default SEOHelmet;
""",
    "src/SEO/StructuredData.jsx": """import { Helmet } from 'react-helmet-async';

export const ProductSchema = ({ product }) => {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.title,
    description: product.description,
    image: product.images,
    brand: {
      '@type': 'Brand',
      name: 'Safety Snap Systems',
    },
    manufacturer: {
      '@type': 'Organization',
      name: 'Safety Snap Systems Pty Ltd',
    },
  };

  return (
    <Helmet>
      <script type="application/ld+json">{JSON.stringify(schema)}</script>
    </Helmet>
  );
};

export const OrganizationSchema = () => {
  const schema = {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Safety Snap Systems Pty Ltd',
    url: 'https://safetysnapsystems.com',
    logo: '/images/logo.png',
    description: 'Professional safety barrier systems, reels, signage and stanchions',
    telephone: '+61-466-864-814',
    email: 'info@safetysnapsystems.com',
    address: {
      '@type': 'PostalAddress',
      addressCountry: 'AU',
    },
  };

  return (
    <Helmet>
      <script type="application/ld+json">{JSON.stringify(schema)}</script>
    </Helmet>
  );
};
""",

    "src/components/Common/Button.jsx": """import React from 'react';
import { motion } from 'framer-motion';
import clsx from 'clsx';
import styles from './Button.module.css';

const Button = ({
  children,
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  onClick,
  className,
  icon: Icon,
  animate = true,
  ...props
}) => {
  return (
    <motion.button
      className={clsx(
        styles.button,
        styles[variant],
        styles[size],
        disabled && styles.disabled,
        className
      )}
      disabled={disabled || loading}
      onClick={onClick}
      whileHover={animate ? { scale: 1.05 } : {}}
      whileTap={animate ? { scale: 0.95 } : {}}
      {...props}
    >
      {loading ? (
        <span className={styles.loader} />
      ) : (
        <>
          {Icon && <Icon className={styles.icon} />}
          {children}
        </>
      )}
    </motion.button>
  );
};

export default Button;
""",
    "src/components/Common/Button.module.css": """
.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
}
.primary { background: #00D4FF; color: #0a0e27; }
.secondary { background: #004A6F; color: white; }
.md { padding: 0.5rem 1rem; font-size: 1rem; }
.lg { padding: 0.75rem 1.5rem; font-size: 1.125rem; }
.sm { padding: 0.25rem 0.5rem; font-size: 0.875rem; }
.disabled { opacity: 0.6; cursor: not-allowed; }
""",

    "src/components/Common/Input.jsx": """import React, { forwardRef } from 'react';
import clsx from 'clsx';
import styles from './Input.module.css';

const Input = forwardRef(({ label, error, as: Component = 'input', className, ...props }, ref) => {
  return (
    <div className={clsx(styles.wrapper, className)}>
      {label && <label className={styles.label}>{label}</label>}
      <Component ref={ref} className={clsx(styles.input, error && styles.errorInput)} {...props} />
      {error && <span className={styles.error}>{error}</span>}
    </div>
  );
});

export default Input;
""",
    "src/components/Common/Input.module.css": """
.wrapper { display: flex; flex-direction: column; margin-bottom: 1rem; }
.label { margin-bottom: 0.5rem; font-weight: 500; }
.input { padding: 0.5rem; border: 1px solid #ccc; border-radius: 4px; }
.errorInput { border-color: red; }
.error { color: red; font-size: 0.875rem; margin-top: 0.25rem; }
""",

    "src/components/Products/ProductCard.jsx": """import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { LazyLoadImage } from 'react-lazy-load-image-component';
import 'react-lazy-load-image-component/src/effects/blur.css';
import Button from '../Common/Button';
import styles from './ProductCard.module.css';

const ProductCard = ({ product, index }) => {
  return (
    <motion.div
      className={styles.card}
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.1 }}
      viewport={{ once: true }}
      whileHover={{ y: -5 }}
    >
      <div className={styles.imageWrapper}>
        <LazyLoadImage
          src={product.image}
          alt={product.title}
          effect="blur"
          className={styles.image}
        />
        {product.badge && <span className={styles.badge}>{product.badge}</span>}
      </div>

      <div className={styles.content}>
        <h3 className={styles.title}>{product.title}</h3>
        <p className={styles.description}>{product.description}</p>

        <div className={styles.footer}>
          <Link to={`/products/${product.id}`}>
            <Button variant="secondary" size="sm">
              View Product →
            </Button>
          </Link>
        </div>
      </div>
    </motion.div>
  );
};

export default ProductCard;
""",
    "src/components/Products/ProductCard.module.css": """
.card { border: 1px solid #eaeaea; border-radius: 8px; overflow: hidden; background: white; }
.imageWrapper { position: relative; width: 100%; height: 200px; }
.image { width: 100%; height: 100%; object-fit: cover; }
.badge { position: absolute; top: 10px; right: 10px; background: #FFB000; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
.content { padding: 1rem; }
.title { font-size: 1.125rem; font-weight: bold; margin-bottom: 0.5rem; }
.description { color: #666; font-size: 0.875rem; margin-bottom: 1rem; }
.footer { display: flex; justify-content: flex-end; }
""",

    "src/components/Hero/HeroSection.jsx": """import React from 'react';
import { motion } from 'framer-motion';
import Button from '../Common/Button';
import { fadeInUp } from '../../utils/animations';
import styles from './HeroSection.module.css';

const HeroSection = ({
  title,
  subtitle,
  description,
  buttons = [],
  backgroundImage,
  darkOverlay = true,
}) => {
  return (
    <section
      className={styles.hero}
      style={
        backgroundImage
          ? { backgroundImage: `url(${backgroundImage})` }
          : {}
      }
    >
      {darkOverlay && <div className={styles.overlay} />}

      <div className={styles.container}>
        <motion.div
          className={styles.content}
          initial="hidden"
          animate="visible"
          variants={{
            hidden: { opacity: 0 },
            visible: {
              opacity: 1,
              transition: {
                staggerChildren: 0.2,
                delayChildren: 0.3,
              },
            },
          }}
        >
          {title && (
            <motion.h1 className={styles.title} variants={fadeInUp}>
              {title}
            </motion.h1>
          )}

          {subtitle && (
            <motion.h2 className={styles.subtitle} variants={fadeInUp}>
              {subtitle}
            </motion.h2>
          )}

          {description && (
            <motion.p className={styles.description} variants={fadeInUp}>
              {description}
            </motion.p>
          )}

          {buttons.length > 0 && (
            <motion.div className={styles.buttons} variants={fadeInUp}>
              {buttons.map((button, index) => (
                <Button
                  key={index}
                  variant={button.variant || 'primary'}
                  onClick={button.onClick}
                >
                  {button.label}
                </Button>
              ))}
            </motion.div>
          )}
        </motion.div>
      </div>
    </section>
  );
};

export default HeroSection;
""",
    "src/components/Hero/HeroSection.module.css": """
.hero { position: relative; min-height: 60vh; display: flex; align-items: center; background-size: cover; background-position: center; }
.overlay { position: absolute; inset: 0; background: rgba(0,0,0,0.5); }
.container { position: relative; z-index: 10; max-width: 1200px; margin: 0 auto; padding: 2rem; color: white; }
.title { font-size: 3rem; font-weight: bold; margin-bottom: 1rem; }
.subtitle { font-size: 1.5rem; margin-bottom: 1rem; }
.description { font-size: 1.125rem; margin-bottom: 2rem; max-width: 600px; }
.buttons { display: flex; gap: 1rem; }
""",

    "src/components/Forms/EnquiryForm.jsx": """import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import { motion } from 'framer-motion';
import { contactService } from '../../api/services/contactService';
import Button from '../Common/Button';
import Input from '../Common/Input';
import toast from 'react-hot-toast';
import styles from './EnquiryForm.module.css';

const validationSchema = yup.object().shape({
  name: yup.string().required('Name is required').min(2, 'Too short'),
  company: yup.string().optional(),
  email: yup.string().required('Email is required').email('Invalid email'),
  phone: yup.string().optional(),
  enquiry: yup.string().required('Enquiry is required').min(10, 'Too short'),
});

const EnquiryForm = ({ onSuccess }) => {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm({
    resolver: yupResolver(validationSchema),
  });

  const onSubmit = async (data) => {
    try {
      await contactService.sendEnquiry(data);
      toast.success('Enquiry sent successfully!');
      reset();
      onSuccess?.();
    } catch (error) {
      toast.error(error.message || 'Failed to send enquiry');
    }
  };

  return (
    <motion.form
      className={styles.form}
      onSubmit={handleSubmit(onSubmit)}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
    >
      <div className={styles.row}>
        <Input
          label="Name"
          type="text"
          placeholder="Your Name"
          {...register('name')}
          error={errors.name?.message}
        />
        <Input
          label="Company"
          type="text"
          placeholder="Company Name"
          {...register('company')}
          error={errors.company?.message}
        />
      </div>

      <div className={styles.row}>
        <Input
          label="Email"
          type="email"
          placeholder="your@email.com"
          {...register('email')}
          error={errors.email?.message}
        />
        <Input
          label="Phone"
          type="tel"
          placeholder="Phone Number"
          {...register('phone')}
          error={errors.phone?.message}
        />
      </div>

      <div className={styles.full}>
        <Input
          label="Enquiry"
          as="textarea"
          placeholder="Describe your enquiry"
          rows="5"
          {...register('enquiry')}
          error={errors.enquiry?.message}
        />
      </div>

      <Button
        type="submit"
        variant="primary"
        size="lg"
        loading={isSubmitting}
        disabled={isSubmitting}
        className={styles.submit}
      >
        Send Enquiry
      </Button>
    </motion.form>
  );
};

export default EnquiryForm;
""",
    "src/components/Forms/EnquiryForm.module.css": """
.form { display: flex; flex-direction: column; gap: 1rem; }
.row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.full { grid-column: 1 / -1; }
.submit { margin-top: 1rem; align-self: flex-start; }
@media (max-width: 600px) { .row { grid-template-columns: 1fr; } }
""",

    "tailwind.config.js": """export default {
  content: [
    './index.html',
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#00D4FF',
        secondary: '#004A6F',
        dark: '#0a0e27',
        light: '#f8f9fa',
        accent: '#FFB000',
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#fff',
          },
        },
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in',
        'slide-in': 'slideIn 0.5s ease-out',
        'pulse-glow': 'pulseGlow 2s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideIn: {
          '0%': { transform: 'translateX(-10px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        pulseGlow: {
          '0%, 100%': { boxShadow: '0 0 0 0 rgba(0, 212, 255, 0.7)' },
          '50%': { boxShadow: '0 0 0 10px rgba(0, 212, 255, 0)' },
        },
      },
    },
  },
  plugins: [],
};
""",

    ".env.example": """# API Configuration
REACT_APP_API_BASE_URL=http://localhost:3001/api
REACT_APP_API_TIMEOUT=10000

# Site Configuration
REACT_APP_SITE_NAME=Safety Snap Systems
REACT_APP_SITE_URL=https://safetysnapsystems.com
REACT_APP_CONTACT_EMAIL=info@safetysnapsystems.com
REACT_APP_CONTACT_PHONE=+61-466-864-814

# SEO Configuration
REACT_APP_SEO_ENABLED=true
REACT_APP_GA_ID=G-XXXXXXXXXX

# Feature Flags
REACT_APP_ENABLE_ANALYTICS=true
REACT_APP_ENABLE_CHAT=true
REACT_APP_ENABLE_TESTIMONIALS=true

# Environment
NODE_ENV=development
""",

    "src/config/routes.js": """export const ROUTES = {
  // Public
  HOME: '/',
  PRODUCTS: '/products',
  PRODUCT_DETAIL: '/products/:id',
  
  // Categories
  SYSTEMS: '/products/systems',
  REELS: '/products/reels',
  SIGNAGE: '/products/signage',
  STANCHIONS: '/products/stanchions',
  
  // Info
  CATALOG: '/catalog',
  CONTACT: '/contact',
  ABOUT: '/about',
  
  // Other
  NOT_FOUND: '/404',
};

export const NAVIGATION = [
  { label: 'Home', path: ROUTES.HOME },
  { label: 'Systems', path: ROUTES.SYSTEMS },
  { label: 'Reels', path: ROUTES.REELS },
  { label: 'Signage', path: ROUTES.SIGNAGE },
  { label: 'Stanchions', path: ROUTES.STANCHIONS },
  { label: 'Catalog', path: ROUTES.CATALOG },
  { label: 'Contact', path: ROUTES.CONTACT },
];
""",

    "src/App.jsx": """import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { Toaster } from 'react-hot-toast';
import AOS from 'aos';
import 'aos/dist/aos.css';

// Pages
import HomePage from './pages/home/HomePage';
import SystemsPage from './pages/categories/SystemsPage';
import ReelsPage from './pages/categories/ReelsPage';
import SignagePage from './pages/categories/SignagePage';
import StanchionsPage from './pages/categories/StanchionsPage';
import CatalogPage from './pages/categories/CatalogPage';
import ProductDetailPage from './pages/products/ProductDetailPage';
import ContactPage from './pages/contact/ContactPage';
import NotFoundPage from './pages/error/NotFoundPage';

// Styles
import './styles/globals.css';
import './styles/animations.css';

// Initialize AOS
AOS.init({
  duration: 1000,
  once: true,
  offset: 100,
});

function App() {
  return (
    <HelmetProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/products/systems" element={<SystemsPage />} />
          <Route path="/products/reels" element={<ReelsPage />} />
          <Route path="/products/signage" element={<SignagePage />} />
          <Route path="/products/stanchions" element={<StanchionsPage />} />
          <Route path="/catalog" element={<CatalogPage />} />
          <Route path="/products/:id" element={<ProductDetailPage />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </Router>
      <Toaster position="top-right" />
    </HelmetProvider>
  );
}

export default App;
""",

    "src/pages/home/HomePage.jsx": """import React from 'react';
import SEOHelmet from '../../SEO/SEOHelmet';

const HomePage = () => {
  return (
    <div>
      <SEOHelmet title="Home" />
      <h1>Home Page</h1>
    </div>
  );
};
export default HomePage;
""",
    "src/pages/categories/SystemsPage.jsx": """import React from 'react';
const SystemsPage = () => <div>Systems Page</div>;
export default SystemsPage;""",
    "src/pages/categories/ReelsPage.jsx": """import React from 'react';
const ReelsPage = () => <div>Reels Page</div>;
export default ReelsPage;""",
    "src/pages/categories/SignagePage.jsx": """import React from 'react';
const SignagePage = () => <div>Signage Page</div>;
export default SignagePage;""",
    "src/pages/categories/StanchionsPage.jsx": """import React from 'react';
const StanchionsPage = () => <div>Stanchions Page</div>;
export default StanchionsPage;""",
    "src/pages/categories/CatalogPage.jsx": """import React from 'react';
const CatalogPage = () => <div>Catalog Page</div>;
export default CatalogPage;""",
    "src/pages/products/ProductDetailPage.jsx": """import React from 'react';
const ProductDetailPage = () => <div>Product Detail Page</div>;
export default ProductDetailPage;""",
    "src/pages/contact/ContactPage.jsx": """import React from 'react';
const ContactPage = () => <div>Contact Page</div>;
export default ContactPage;""",
    "src/pages/error/NotFoundPage.jsx": """import React from 'react';
const NotFoundPage = () => <div>404 Not Found</div>;
export default NotFoundPage;""",
    "src/styles/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;
""",
    "src/styles/animations.css": """/* Animations */""",
    "src/main.jsx": """import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { store } from './redux/store';
import App from './App';
import './styles/globals.css';

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>
);""",
}

for filepath, content in files.items():
    full_path = os.path.join(project_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")

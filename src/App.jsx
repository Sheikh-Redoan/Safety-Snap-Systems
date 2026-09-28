import React from 'react';
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
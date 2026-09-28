export const ROUTES = {
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

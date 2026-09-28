import { Helmet } from 'react-helmet-async';

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
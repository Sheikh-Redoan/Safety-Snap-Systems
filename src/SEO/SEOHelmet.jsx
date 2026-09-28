import { Helmet } from 'react-helmet-async';

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
import React from 'react';
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

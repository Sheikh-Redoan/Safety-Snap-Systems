import React from 'react';
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
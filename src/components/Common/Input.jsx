import React, { forwardRef } from 'react';
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

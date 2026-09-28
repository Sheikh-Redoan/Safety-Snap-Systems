import React from 'react';
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

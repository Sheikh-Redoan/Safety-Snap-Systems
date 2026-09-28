import React from 'react';
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
export const contactService = {
  sendEnquiry: async (data) => {
    return new Promise((resolve) => setTimeout(() => resolve({ success: true }), 1000));
  }
};
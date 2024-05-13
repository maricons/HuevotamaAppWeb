/** @type {import('tailwindcss').Config} */

// tailwind.config.js

module.exports = {
  theme: {
    extend: {
      screens: {
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
      },
    },
    maxWidth: {
      'xs': '20rem',
      'sm': '24rem',
      'md': '28rem',
      'lg': '32rem',
      'xl': '36rem',
      '2xl': '42rem',
    },
    extend: {
      colors: {
        'body-tertiary': '#212121',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

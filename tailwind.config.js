/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./ui/**/*.{html,js,jsx,jinja}"],
  theme: {
    extend: {
      colors: {
        primary: "#EDF5F8",
        "primary-light": "#EDF5F5",
        secondary: "#FCC802",
        dark: "#023850",
        accent: "#E04541",
      },

      fontFamily: {
        JostLight: ["Jost-Light"],
        JostRegular: ["Jost-Regular"],
        JostMedium: ["Jost-Medium"],
        JostBold: ["Jost-Bold"],
      },

      screens: {
        "2xl": "1440px",
      },

      borderRadius: {
        normal: "0.28571429rem",
        "40px": "40px",
        "60px": "60px",
      },

      fontSize: {
        "8px": "0.5rem",
        "9px": "0.5625rem",
        "10px": "0.625rem",
        "11px": "0.6875rem",
        "12px": "0.75rem",
        "13px": "0.8125rem",
        "14px": "0.875rem",
        "15px": "0.9375rem",
        "16px": "1.0rem",
        "17px": "1.0625rem",
        "18px": "1.125rem",
        "19px": "1.1875rem",
        "20px": "1.25rem",
        "21px": "1.3125rem",
        "22px": "1.375rem",
        "23px": "1.4375rem",
        "24px": "1.5rem",
        "25px": "1.5625rem",
        "26px": "1.625rem",
        "27px": "1.6875rem",
        "28px": "1.75rem",
        "29px": "1.8125rem",
        "30px": "1.875rem",
        "31px": "1.9375rem",
        "32px": "2.0rem",
        "33px": "2.0625rem",
        "34px": "2.125rem",
        "35px": "2.1875rem",
        "36px": "2.25rem",
        "37px": "2.3125rem",
        "38px": "2.375rem",
        "39px": "2.4375rem",
        "40px": "2.5rem",
        "41px": "2.5625rem",
        "42px": "2.625rem",
        "43px": "2.6875rem",
        "44px": "2.75rem",
        "45px": "2.8125rem",
        "46px": "2.875rem",
        "47px": "2.9375rem",
        "48px": "3.0rem",
        "49px": "3.0625rem",
        "50px": "3.125rem",
        "51px": "3.1875rem",
        "52px": "3.25rem",
        "53px": "3.3125rem",
        "54px": "3.375rem",
        "55px": "3.4375rem",
        "56px": "3.5rem",
        "57px": "3.5625rem",
        "58px": "3.625rem",
        "59px": "3.6875rem",
        "60px": "3.75rem",
        "61px": "3.8125rem",
        "62px": "3.875rem",
        "63px": "3.9375rem",
        "64px": "4.0rem",
        "65px": "4.0625rem",
        "66px": "4.125rem",
        "67px": "4.1875rem",
        "68px": "4.25rem",
        "69px": "4.3125rem",
        "70px": "4.375rem",
        "71px": "4.4375rem",
        "72px": "4.5rem",
        "73px": "4.5625rem",
        "74px": "4.625rem",
        "75px": "4.6875rem",
        "76px": "4.75rem",
        "77px": "4.8125rem",
        "78px": "4.875rem",
        "79px": "4.9375rem",
        "80px": "5.0rem",
        "81px": "5.0625rem",
        "82px": "5.125rem",
        "83px": "5.1875rem",
        "84px": "5.25rem",
        "85px": "5.3125rem",
        "86px": "5.375rem",
        "87px": "5.4375rem",
        "88px": "5.5rem",
        "89px": "5.5625rem",
        "90px": "5.625rem",
        "91px": "5.6875rem",
        "92px": "5.75rem",
        "93px": "5.8125rem",
        "94px": "5.875rem",
        "95px": "5.9375rem",
        "96px": "6.0rem",
        "97px": "6.0625rem",
        "98px": "6.125rem",
        "99px": "6.1875rem",
        "100px": "6.25rem",
        "140px": "8.75rem",
        "150px": "9.375rem",
      },

      width: {
        "300px": "300px",
        "350px": "350px",
        "400px": "400px",
      },

      gridTemplateColumns: {
        "2col": "repeat(2, 316px);",
        "3col": "repeat(3, 316px)",
        "4col": "repeat(4, 316px)",
        "2colMethod": "repeat(2, 400px);",
        "3colMethod": "repeat(3, 400px)",
      },
    },
  },
  plugins: [],
};

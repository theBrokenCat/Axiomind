/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#09090b", // Obsidian
        surface: "rgba(255, 255, 255, 0.05)", // Glass base
        "surface-hover": "rgba(255, 255, 255, 0.1)",
        axiom: "#00f0ff", // Neon Cyan
        source: "#ffae00", // Amber
        moltbook: "#00ff9d", // Mint Green for validation
        text: {
          primary: "#ffffff",
          secondary: "#a1a1aa",
          muted: "#52525b",
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        // Add a mono font for code/data?
      },
      backdropBlur: {
        xs: '2px',
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
      },
      keyframes: {
        glow: {
          '0%': { boxShadow: '0 0 5px rgba(0, 240, 255, 0.2)' },
          '100%': { boxShadow: '0 0 20px rgba(0, 240, 255, 0.6)' },
        }
      }
    },
  },
  plugins: [],
}

module.exports = {
    mode: "jit",
    future: {
        purgeLayersByDefault: true,
        removeDeprecatedGapUtilities: true,
    },
    content: ["./src/**/*.svelte", "./src/**/*.html"],
    theme: {},
    daisyui: {
        themes: [
            {
                mocha: {
                    primary: "#f5e0dc",
                    secondary: "#cba6f7",
                    accent: "#fab387",
                    neutral: "#f9e2af",
                    "base-100": "#1e1e2e",
                    info: "#b4befe",
                    success: "#a6e3a1",
                    warning: "#f2cdcd",
                    error: "#f38ba8",
                },
            },
        ],
    },
    plugins: [require("@tailwindcss/typography"), require("daisyui")],
};

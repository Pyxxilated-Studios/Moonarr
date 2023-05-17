const tailwindcss = require("tailwindcss");
const autoprefixer = require("autoprefixer");
const purgecss = require("@fullhuman/postcss-purgecss");
const csso = require("postcss-csso");

module.exports = {
    plugins: [
        tailwindcss,
        autoprefixer,
        purgecss({
            content: ["./**/*.html", "./**/*.svelte", "./**/*.ts"],
            defaultExtractor: (content) => content.match(/[A-Za-z0-9-_:/]+/g) || [],
            safelist: {
                greedy: [/^svelte-announcer/],
            },
        }),
        csso(),
    ],
};

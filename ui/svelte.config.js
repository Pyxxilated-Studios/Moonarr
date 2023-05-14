import adapter from "svelte-adapter-bun";
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://github.com/sveltejs/svelte-preprocess
    // for more information about preprocessors
    preprocess: preprocess(),

    kit: {
        adapter: adapter({
            out: "build",
            precompress: {
                brotli: true,
                gzip: true,
                files: ["htm", "html"],
            },
        }),
    },
};

export default config;

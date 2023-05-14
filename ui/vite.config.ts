import { sveltekit } from "@sveltejs/kit/vite";
import type { UserConfig } from "vite";

const config: UserConfig = {
    plugins: [sveltekit()],
    optimizeDeps: {
        esbuildOptions: {
            minify: true,
        },
    },
    build: {
        reportCompressedSize: false,
        rollupOptions: {
            output: {
                generatedCode: {
                    objectShorthand: true,
                },
            },
            treeshake: "recommended",
        },
    },
};

export default config;

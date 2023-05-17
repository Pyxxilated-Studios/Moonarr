<nav class="navbar bg-base-300 px-4 sticky top-0 z-30">
	<div>
		<a
			href="/"
			class="text-primary text-xl hover:text-secondary transition-colors duration-300 text-lg md:text-3xl"
		>
			Moonarr
		</a>
	</div>
</nav>

<main class="prose md:prose-lg lg:prose-xl min-w-full">
	<slot />
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>

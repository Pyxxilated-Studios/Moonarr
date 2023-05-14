<script lang="ts">
	interface Artist {
		id: string;
		name: string;
		picture: string;
	}

	let item = '';
	let items: Artist[] = [];

	const lookup = () => {
		fetch(`/api/search/${item}`).then((resp) =>
			resp.json().then((resp) => {
				items = resp;
			})
		);
	};

	const download = async (item: Artist) => {
		await fetch(`/api/download/${item.id}`, { method: 'POST' });
	};
</script>

<h1>Welcome to SvelteKit</h1>

<input bind:value={item} />

<button on:click={lookup}>Search</button>

{#each items as item}
	<p>{JSON.stringify(item)}</p>
	<button on:click={() => download(item)}>Download</button>
{/each}

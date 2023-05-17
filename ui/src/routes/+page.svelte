<script lang="ts">
	interface Artist {
		id: number;
		name: string;
		picture: string;
	}

	let item = '';
	let items: Artist[] = [];

	const lookup = async () => {
		try {
			const response = await fetch(`/api/search/${item}`);
			if (response.ok) {
				const json = await response.json();
				items = json;
			}
		} catch (exception: unknown) {
			console.debug('Exception', exception);
		}
	};

	const download = async (item: Artist) => {
		await fetch(`/api/download/${item.id}`, { method: 'POST' });
	};
</script>

<form class="flex m-4">
	<input
		type="text"
		placeholder="Enter Search Term"
		class="input input-bordered w-full flex-1 mr-4"
		bind:value={item}
	/>

	<button class="btn" on:click={lookup}>Search</button>
</form>

{#each items as item (item.id)}
	<div class="flex m-4 p-4 shadow rounded">
		<p class="flex-1">{item.name}</p>
		<button class="btn" on:click={() => download(item)}>Download</button>
	</div>
{/each}

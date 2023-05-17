<script lang="ts">
	import { onMount } from 'svelte';

	interface Settings {
		albumFolderFormat: string;
		apiKeyIndex: number;
		audioQuality: string;
		checkExist: boolean;
		downloadDelay: boolean;
		downloadPath: string;
		includeEP: boolean;
		language: number;
		lyricFile: boolean;
		multiThread: boolean;
		playlistFolderFormat: string;
		saveAlbumInfo: boolean;
		saveCovers: boolean;
		showProgress: boolean;
		showTrackInfo: boolean;
		trackFileFormat: string;
		usePlaylistFolder: boolean;
		videoFileFormat: string;
		videoQuality: string;
	}

	let settings: Settings | undefined;

	onMount(async () => {
		settings = await retrieveSettings();
	});

	const retrieveSettings = async (): Promise<Settings> => {
		return await (await fetch('/api/settings')).json();
	};

	const updateSettings = async () => {
		if (settings === undefined) {
			return;
		}

		const toBoolean = (val: string): boolean => {
			return val.toLowerCase() === 'true';
		};

		settings.checkExist = toBoolean(settings.checkExist.toString());
		settings.downloadDelay = toBoolean(settings.downloadDelay.toString());
		settings.includeEP = toBoolean(settings.includeEP.toString());
		settings.lyricFile = toBoolean(settings.lyricFile.toString());
		settings.multiThread = toBoolean(settings.multiThread.toString());
		settings.saveAlbumInfo = toBoolean(settings.saveAlbumInfo.toString());
		settings.saveCovers = toBoolean(settings.saveCovers.toString());
		settings.showProgress = toBoolean(settings.showProgress.toString());
		settings.showTrackInfo = toBoolean(settings.showTrackInfo.toString());
		settings.usePlaylistFolder = toBoolean(settings.usePlaylistFolder.toString());

		await fetch('/api/settings', {
			method: 'POST',
			body: JSON.stringify(settings),
			headers: {
				'Content-Type': 'application/json'
			}
		});
	};
</script>

<h1 class="m-4">Settings</h1>

{#if settings}
	<form class="m-4 p-4">
		<button class="btn" on:click={updateSettings}>Save</button>
		<div class="flex shadow rounded">
			<p class="flex-1">Album Folder Format</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.albumFolderFormat}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Api Key Index</p>
			<input
				type="number"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.apiKeyIndex}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Audio Quality</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.audioQuality}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Check Exist</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.checkExist}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Download Delay</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.downloadDelay}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Download Path</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4 min-w-max"
				bind:value={settings.downloadPath}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Include EP</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.includeEP}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Language</p>
			<input
				type="number"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.language}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Lyric File</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.lyricFile}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Multi Thread</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.multiThread}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Playlist Folder Format</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.playlistFolderFormat}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Save Album Info</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.saveAlbumInfo}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Save Covers</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.saveCovers}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Show Progress</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.showProgress}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Show Track Info</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.showTrackInfo}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Track File Format</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.trackFileFormat}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Use Playlist Folder</p>
			<input
				type="checkbox"
				placeholder=""
				class="input input-bordered mr-4 checkbox"
				bind:checked={settings.usePlaylistFolder}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Video File Format</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.videoFileFormat}
			/>
		</div>
		<div class="flex shadow rounded">
			<p class="flex-1">Video Quality</p>
			<input
				type="text"
				placeholder=""
				class="input input-bordered mr-4"
				bind:value={settings.videoQuality}
			/>
		</div>
	</form>
{/if}

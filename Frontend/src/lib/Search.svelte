<script lang="ts">
	import { onMount } from 'svelte';
	import { writable } from 'svelte/store';

	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	let searchQuery = '';
	let isFocused = false;
	const searchQueryStore = writable('');

	onMount(() => {
		searchQueryStore.subscribe((value) => {
			searchQuery = value;
		});
	});

	function handleInput(event: Event) {
		let target = event.target as HTMLTextAreaElement;
		searchQueryStore.set(target.value);
	}

	function handleFocus() {
		isFocused = true;
	}
</script>

<div class="w-3/4 mx-auto">
	<div
		class="relative h-12 rounded-full border border-gray-300 focus-within:h-24 focus-within:rounded-md search-box"
	>
		<textarea
			class="w-full h-full py-2 pr-8 pl-3 rounded-full border-none focus:outline-none"
			placeholder="Search"
			value={searchQuery}
			on:input={handleInput}
			on:focus={handleFocus}
			style="resize: none;"
		/>
		<div class="flex justify-end mt-2">
			<button class="px-4 py-2 rounded-full bg-blue-500 text-white font-bold" type="submit"
				>Submit</button
			>
		</div>
	</div>
</div>

<style>
	.search-box {
		height: 3rem;
		border-radius: 1.5rem;
		transition: height 0.3s ease-in-out;
	}

	.search-box:focus-within {
		height: 6rem;
	}
</style>
